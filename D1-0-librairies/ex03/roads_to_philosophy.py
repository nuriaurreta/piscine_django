#!/usr/bin/env python3

import requests, sys
from bs4 import BeautifulSoup


def search_wiki(article):
    visited_articles = set()
    count = 0
    while article.lower() != "philosophy":
        if article.lower() in visited_articles:
            print("It leads to an infinite loop!!")
            return
        visited_articles.add(article.lower())

        to_search = article.replace(" ", "_")
        r = requests.get(f'https://en.wikipedia.org/wiki/{to_search}')
        soup = BeautifulSoup(r.text, 'html.parser')
        
        title = soup.select_one(".mw-page-title-main")
        if title is None:
            print("Article not found.")
            return
        title_text = title.get_text()
        print(title_text)
        
        if title_text.lower() == "philosophy":
            print("Philosophy")
            print(f'{count} roads from 42 (number) to Philosophy')
            return

        paragraphs = soup.find_all("p")
        
        next_link = None
        for p in paragraphs:
            a = p.find("a")
            
            while a:
                href = a.get('href')
                if href and href.startswith('/wiki/') and not href.startswith('/wiki/Help:'): 
                    next_link = href
                    break
                a = a.find_next('a')

            if next_link:
                break

        if not next_link:
            print("It doesn't found any valid link.")
            return

        article = next_link.split('/wiki/')[-1]
        count += 1
    print("Philosophy")
    print(f'{count} roads from 42 (number) to Philosophy')


def main():
    if len(sys.argv) != 2:
        return print("Error: one string is needed as an argument")
    search_wiki(sys.argv[1])


if __name__ == '__main__':
    main()