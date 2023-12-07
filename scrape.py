import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup_obj = BeautifulSoup(res.text , 'html.parser')

links = soup_obj.find_all(rel='noreferrer')
subline = soup_obj.select('.subline')


def sort_stories(hacker_news):
    return sorted(hacker_news , key=lambda x: x['votes'] , reverse=True)

def create_costum_hacker_news(links, subline):
    hacker_news = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href' , None)
        vote = subline[index].select('.score')

        if len(vote) != 0:
            points = int(vote[0].getText().split(" ")[0])
            if points >= 100:
                hacker_news.append({'title' : title , 'link' : href ,'votes' : points} )

    return sort_stories(hacker_news)


pprint.pprint(create_costum_hacker_news(links,subline))


# print(scores[0].get('id'))
# print(soup_obj.find_all(rel='noreferrer')[0])
# print(soup_obj.find_all(rel='noreferrer')[1])
# print(soup_obj.find_all(rel='noreferrer')[2])
# print(soup_obj.find_all(rel='noreferrer')[3])
# print(soup_obj.select('.score')[0])
# print(soup_obj.select('.score')[1])
# print(soup_obj.select('.score')[2])
# print(soup_obj.select('.score')[3])