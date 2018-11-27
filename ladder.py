from bs4 import BeautifulSoup
import urllib.request

ladder_name = input("Enter ladder to scrape (eg. anythinggoes, ou, 1v1, vgc2018, ...): ")
url = "https://pokemonshowdown.com/ladder/gen7" + str(ladder_name)
ps = "https://pokemonshowdown.com"
user_agent ="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) " \
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
showdown = urllib.request.Request(url, data=None, headers= {'User-Agent': user_agent})
ladder = urllib.request.urlopen(showdown)
parsed = BeautifulSoup(ladder.read(), "lxml")
filename = "logs\gen7" + str(ladder_name)+'.txt'
output = open(filename, "w")

for i, link in enumerate(parsed.find_all("a",  class_="subtle"), 1):
    truser = link.get('href')
    user = ps + truser
    agent = urllib.request.Request(user, data=None, headers={'User-Agent': user_agent})
    print("Scanning " + str(i) + "/500 users...",  end= "\r")
    try:
        userpage = urllib.request.urlopen(agent)
    except urllib.error.HTTPError:
        rank = "Rank " + str(i) + ": " + user
        print(rank)
        output.write(rank + "\n")

    if i == 500:
        print("Scanned entire " + ladder_name + " ladder.        ",  end="\r")

output.close()
print("\n")
input("Press enter to exit...")
