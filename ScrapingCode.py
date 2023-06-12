
from serpapi import GoogleSearch
import os, json

image_results = []

for query in ["Ash, Beech, Birch, Cherry, Maple, Oak, Pine, Teak, Walnut"]:
    params = {
        "engine": "google",               # search engine. Google, Bing, Yahoo, Naver, Baidu...
        "q": query,                       # search query
        "tbm": "isch",                    # image results
        "num": "1000",                     # number of images per page
        "ijn": 0,                         # page number: 0 -> first page, 1 -> second...
        "api_key": "82e81fec9f38460602533a3df932e12ef5d4883fc8e9255be702ccae1220a3ed"   # your serpapi api key
    }

    search = GoogleSearch(params)         # where data extraction happens

    images_is_present = True
    while images_is_present:
        results = search.get_dict()       # JSON -> Python dictionary

        # checks for "Google hasn't returned any results for this query."
        if "error" not in results:
            for image in results["images_results"]:
                if image["original"] not in image_results:
                    print(image["original"])
                    image_results.append(image["original"])
            
            # update to the next page
            params["ijn"] += 1
        else:
            images_is_present = False
            print(results["error"])

print(json.dumps(image_results, indent=2))
print(len(image_results))