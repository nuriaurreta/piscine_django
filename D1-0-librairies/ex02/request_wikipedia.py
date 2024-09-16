#!/usr/bin/env python3

import requests, json, sys, dewiki

URL = "https://en.wikipedia.org/w/api.php"

def search_wiki(page: str):
    PARAMS = {
        "action": "parse",
        "format": "json",
        "page": page,
        "prop": "wikitext",
        "redirects": "true"
    }
    r = requests.get(URL, PARAMS)
    if r.status_code != 200:
        return print("Error: the request has failed")
    try:
        data = json.loads(r.text)
    except json.decoder.JSONDecodeError as e:
        raise e
    if data.get("error"):
        raise Exception(data["error"]["info"])
    return dewiki.from_string(data["parse"]["wikitext"]["*"])

def main():
    if len(sys.argv) != 2:
        return print("Error: one string is needed as an argument")
    filename = (f'{sys.argv[1].replace(" ", "_")}.wiki').lower()
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(search_wiki(sys.argv[1]))
    except Exception as e:
        return print(f'Error: {e}')

if __name__ == '__main__':
    main()