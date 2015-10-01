from rauth import OAuth2Service
#   import urllib.request
import requests
import json
import correctQuery
import Artist as artist


def setArtist(query):
    return correctQuery.suggest(query)

if __name__ == "__main__":
    global query
    query = raw_input("Enter artist: ")
    artistName = setArtist(query)

    artistID = artist.getID(artistName)

    for i in artist.getPopularSongs(artistID):
        print i
