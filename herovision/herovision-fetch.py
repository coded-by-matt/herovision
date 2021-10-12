#seperate module for api implementation
import requests
import liquipediapy
import dota from liquipediapy

#def gethero(heroname):
    #hero = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Pet_door&rvslots=*&rvprop=content&formatversion=2&format=json")
#    hero = requests.get(r'https://liquipedia.net/w/api.php?action=query&prop=revisions&titles=Sniper&rvslots=*&rvprop=content&formatversion=2&format=json&UserAgent="Herovision (http://www.github.com/coded-by-matt/herovision; matthew.harrison@2itesting.com)"')

                        #https://liquipedia.net/dota2/Sniper
    #hero = requests.get("http://lovecraft.wikia.com/api.php?action=query&prop=images&titles=Cthulhu&format=json")
#    print(hero.status_code)
#    print(hero.text)

#    return hero

#gethero("sniper")
#print(gethero("sniper").status_code())
#test scenario - sniper is found in image, find the bio info for sniper using the api.


liq = dota('herovision')
print(type(liq.get_heros()))
