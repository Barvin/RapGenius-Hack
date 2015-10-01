from rauth import OAuth2Service
import Keys
import requests
import json

accessToken = Keys.getValue("access_token")

def jsonify(url):
    data = requests.get(url)

    content = data.content

    j = json.loads(content)

    return j

def getID(artist):
    url = "https://api.genius.com/search?access_token=" + accessToken + "&q=" + artist

    j = jsonify(url)

    artist_id = json.dumps(j["response"]["hits"][0]["result"]["primary_artist"]["id"], sort_keys=True, indent=4)

    return artist_id


def getPopularSongs(artistID):
    songList = []
    url = "https://api.genius.com/artists/" + str(artistID) + "/songs?access_token=" + accessToken + "&sort=popularity&per_page=20"

    j = jsonify(url)

    try:
        for song in range(0,20):
            jParsed = json.dumps(j["response"]["songs"][song]["title"], sort_keys=True, indent=4, ensure_ascii=False)
            songList.append(jParsed.replace('"', ''))

    except Exception, e:
        print "\nEnd of results"

    return songList
