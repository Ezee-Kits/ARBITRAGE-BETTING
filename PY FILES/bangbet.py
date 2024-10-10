from func import scrolling,requesting_init,saving_files,drop_duplicate,headless_selenium_init,saving_path_csv
from bs4 import BeautifulSoup
from lxml import html
import time
import pandas as pd


def loading_files(tree,path):
    error = []
    for x in range(1,200):
        try:
            match_time = tree.xpath('//*[@id="app"]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div['+str(x)+']/div[1]/div[3]/text()')[0].split()[1]
            
            home_team = tree.xpath('//*[@id="app"]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div['+str(x)+']/div[1]/div[2]/text()')[0].split('vs.')[0]
            away_team = tree.xpath('//*[@id="app"]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div['+str(x)+']/div[1]/div[2]/text()')[0].split('vs.')[1]
            
            home_odd = tree.xpath('//*[@id="app"]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div['+str(x)+']/div[2]/div[1]/div[1]/div/div/div[2]/text()')[0]
            draw_odd = tree.xpath('//*[@id="app"]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div['+str(x)+']/div[2]/div[1]/div[2]/div/div/div[2]/text()')[0]
            away_odd = tree.xpath('//*[@id="app"]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div['+str(x)+']/div[2]/div[1]/div[3]/div/div/div[2]/text()')[0]
            bookmaker = 'BANGBET'
            print(match_time,home_team,away_team,home_odd,draw_odd,away_odd)
            data = {
            'TIME':match_time,
            'HOME TEAM':home_team,
            'AWAY TEAM':away_team,

            'HOME ODD': home_odd,
            'DRAW ODD':draw_odd,
            'AWAY ODD':away_odd,
            'BOOKMAKER':bookmaker
        }
            saving_files(data=[data],path=path)
            error.append(0)
        except:
            error.append(1)
        print('\n LAST 7 ERROR ARE OF ',error[-7:])
        if len(error) > 7 and error[-7] == 1 and error[-6] == 1 and error[-5] == 1 and error[-4] == 1 and error[-3] == 1 and error[-2] == 1 and error[-1] == 1:
            break




def  bangbet_func():
    path = f'{saving_path_csv}/BANGBET.csv'
    driver,wait,EC,By = headless_selenium_init()
    driver.get('https://www.bangbet.com/pc/list/sports?country=ng')

    time.sleep(10)
    today = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/span[1]')))
    today.click()
    time.sleep(10)


    for x in range(1,7):
        try:
            source = driver.page_source
            tree = html.fromstring(source)
            loading_files(tree=tree,path=path)

            more = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[3]/button[2]/i')))
            more.click()
            time.sleep(5)
        except:
            break

    drop_duplicate(path=path)
