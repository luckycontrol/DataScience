from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

def run():

    columns = ['title', 'category', 'content_text']
    df = pd.DataFrame(columns=columns)

    source_url = "https://namu.wiki/w/K.K."

    req = requests.get(source_url)
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    content_table = soup.find(name='article')
    title = content_table.find_all('h1')[0]
    category = content_table.find_all('ul')[0]
    content_paragraphs = content_table.find_all(name='div', attrs={'class':'wiki-paragraph'})
    content_corpus_list = []

    title = title.text.replace('\n', '')

    for paragraph in content_paragraphs:
        if paragraph is not None:
            content_corpus_list.append(paragraph.text.replace('\n', ''))

    category = category.text.replace('\n', '')

    row = [title, category, "".join(content_corpus_list)]
    series = pd.Series(row, index=df.colums)
    df = df.append(series, ignore_index=True)

if __name__ == '__main__':
    run()