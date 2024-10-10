from func import saving_files,drop_duplicate,headless_selenium_init,saving_path_csv,simple_scroll
from bs4 import BeautifulSoup
from lxml import html
import time
import pandas as pd


 

def parimatch_func():
    path = f'{saving_path_csv}/PARIMATCH.csv'
    driver,wait,EC,By = headless_selenium_init()
    driver.get('https://parimatch.ng/football/today/1')
    time.sleep(10)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > main > div > div.layout__center > div:nth-child(2) > div:nth-child(3) > div > div:nth-child(1) > div.sportList__content > div:nth-child(1) > a > div')))
    time.sleep(10)
    simple_scroll(driver=driver,speed=1300,t_runs=17,sleep_time=2,scroll_up='yes')

    source = driver.page_source
    event = driver.find_elements(By.CLASS_NAME,'event-card__wrapper')

    int_vals = [str(x) for x in range(1,3)]
    int_exp = ['X']
    int_vals = int_vals + int_exp

    matches = []
    for x in event:
        x = x.text.split('\n')
        for y in x:
            if '/' in y:
                matches.append(y.split('/')[1].strip())
            else:
                matches.append(y)
    # print(matches)

    int_vals = [str(x) for x in range(1,3)]
    int_exp = ['X']
    int_vals = int_vals + int_exp

    new_matches = []
    for x in matches:
        x = x.strip()
        if x in int_vals:
            pass
        else:
            new_matches.append(x)
    # print(new_matches)

    time_value = []
    time_index = []
    for i,x in enumerate(new_matches):
        if ':' in x:
            indx = new_matches.index(x,i,len(new_matches))
            time_index.append(indx)
            time_value.append(x)
    # print(time_index)

    for x in time_index:
        try:
            f_elem_indx = time_index.index(x)
            s_elem_indx = time_index.index(x) + 1

            if (time_index[s_elem_indx] - time_index[f_elem_indx]) == 6:
                all_info = new_matches[ time_index[f_elem_indx]:time_index[s_elem_indx] ]
                match_time = all_info[0]

                home_team = all_info[1]
                away_team = all_info[2]

                home_odd = float(all_info[3])
                draw_odd = float(all_info[4])
                away_odd = float(all_info[5])
                bookmaker = 'PARIMATCH'

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
        except:
            pass
    drop_duplicate(path=path)

