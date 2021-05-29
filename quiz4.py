# Movie.ge - SCRAPING/PARSING

import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

ind = 1
file = open('movie.csv', 'w', encoding='UTF-8_sig', newline='\n')
csv_file = csv.writer(file)
csv_file.writerow(['სახელი', 'წელი', 'რეიტინგი'])

url = f'https://movie.ge/filter-movies?type=movie&page={ind}'
for i in range(6):

    r = requests.get(url)
    # print(r.status_code)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    section_content = soup.find('section', {'class': 'content'})
    mlist_section = section_content.find('div', {'class': 'mlist section'})
    container = mlist_section.find('div', {'class': 'container'})
    row = container.find('div', class_='row')
    columns = row.find_all('div', {'class': 'col-md-3'})
    for each in columns:
        popular_card = each.find('div', class_='popular-card')
        pop_card_title = popular_card.find('div', class_='popular-card__title')
        title = pop_card_title.h2.a.p.text
        pop_card_img = popular_card.find('div', class_='popular-card__img')
        rates = pop_card_img.find('div', class_='rates')
        imdb_div = rates.find('div', class_='imdb')
        imdb = imdb_div.span.text
        year_div = rates.find('div', class_='year')
        year = year_div.text
        csv_file.writerow([title, year, imdb])
        ind += 1
        print(year)
    sleep(randint(15,20))

file.close()

