from bs4 import BeautifulSoup
import urllib.request

laddername = input("Enter ladder to scrape (eg. anythinggoes, ou, 1v1, vgc2018, ...): ")
print("")
url = "https://pokemonshowdown.com/ladder/gen7" + str(laddername)
ps = "https://pokemonshowdown.com"

showdown = urllib.request.Request(url, data=None, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
        )

ladder = urllib.request.urlopen(showdown)
parsed = BeautifulSoup(ladder.read(), "lxml")

filename = "logs\gen7" + str(laddername)+'.txt'
output = open(filename, "w")

counter = 0
for link in parsed.find_all("a",  class_="subtle"):
    truser = link.get('href')
    user = ps + truser
    counter += 1
    agent = urllib.request.Request(user, data=None, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        })
    print("Scanning " + str(counter) + "/500 users...",  end= "\r")
    try:
        userpage = urllib.request.urlopen(agent)

    except urllib.error.HTTPError:
        rank = "Rank " + str(counter) + ": " + user
        print(rank)
        output.write(rank + "\n")

    if counter == 500:
        print("Scanned entire " + laddername + " ladder.        ",  end="\r")


output.close()
print("\n")
input("Press enter to exit...")
