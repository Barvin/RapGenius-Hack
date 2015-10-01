import requests
import json
import urllib

def suggest(query):
    lang = "en"

    url = "http://suggestqueries.google.com/complete/search?output=firefox&client=firefox&hl=" + lang + "&q=" + urllib.quote_plus(query)

    data = requests.get(url)

    content = data.content
    j = json.loads(content)

    jParsed = json.dumps(j[1][0], sort_keys=True, indent=4)
    #TODO add exception if JSON returns j[1][empty list]
    result = jParsed.strip('"')
    return result
