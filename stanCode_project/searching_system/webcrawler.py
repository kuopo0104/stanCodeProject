"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        # ----- Write your code below this line ----- #

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        tags = soup.find_all('table', {'class': 't-stripe'})
        male_num = 0
        female_num = 0
        j = 0
        for tag in tags:
            data = tag.tbody.text
            data_lst = data.split('\n')
            for i in range(200):
                target = data_lst[j+2]
                target = target.split(' ')
                male_num += only_digit(target[1])
                female_num += only_digit(target[3])
                j += 2
        print('Male number: ', male_num)
        print('Female number: ', female_num)


def only_digit(string):
    new_string = ''
    for i in range(len(string)):
        if string[i].isdigit():
            new_string += string[i]
    return int(new_string)


if __name__ == '__main__':
    main()
