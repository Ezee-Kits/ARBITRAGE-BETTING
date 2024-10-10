from func import scrolling,requesting_init,saving_files,drop_duplicate,headless_selenium_init,saving_path_csv
from bs4 import BeautifulSoup
import time
import pandas as pd




def drop_row_exception(path):
    df = pd.read_csv(path)

    to_drop = []
    for x in range(len(df['HOME ODD'])):
        try:
            _ = float(df['HOME ODD'][x])
            __ = float(df["DRAW ODD"][x])
            ___ = float(df["AWAY ODD"][x])
        except:
            to_drop.append(x)
    df.drop(to_drop,axis=0,inplace = True)

    df = df.reset_index()
    df.drop(['index'], axis=1,inplace = True)
    df.to_csv(path, index=False)



def nairabet_func():
    path = f'{saving_path_csv}/NAIRABET.csv'
    driver,wait,EC,By = headless_selenium_init()
    url = 'https://www.nairabet.com/sport/football/upcoming_matches'

    driver.get(url)
    time.sleep(2)

    try:
        for x in range(1,7):
            time.sleep(3)
            view = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div.application > div.application__content > main > div > div > div > main > div.view-all-button")))
            view.click()
            print(x,'\n VIEW MORE IS CLICKED SUCCESFULLY \n',)
    except:
        pass
    time.sleep(10)

    source = driver.page_source
    soup = BeautifulSoup(source,'html.parser')


    match_time = [ x.text.split()[-1] for x in soup.find_all('span',class_='event-date-time-label')]

    teams = [ x.text for x in soup.find_all('span',class_='event-card__team-name')]
    home_team = [teams[x] for x in range(len(teams)) if x%2 == 0]
    away_team = [teams[x] for x in range(len(teams)) if x%2 == 1]

    odds = [ x.text for x in soup.find_all('button',class_='odds-button')]
    home_odd = [ odds[x] for x in range(0,len(odds),3)]
    draw_odd = [ odds[x]  for x in range(1,len(odds),3)]
    away_odd = [ odds[x]  for x in range(2,len(odds),3)]
    bookmaker = ['NAIRABET']*len(away_odd)


    data = {
        'TIME':match_time,
        'HOME TEAM':home_team,
        'AWAY TEAM':away_team,

        'HOME ODD': home_odd,
        'DRAW ODD':draw_odd,
        'AWAY ODD':away_odd,
        'BOOKMAKER':bookmaker
    }


    saving_files(data=data,path=path)
    drop_row_exception(path=path)
