from func import selenium_init,scrolling,requesting_init,saving_files,drop_duplicate,saving_path_csv,simple_scroll
from bs4 import BeautifulSoup
from datetime import datetime
from lxml import html
import time
import pandas as pd



def betano_func():
    path = f'{saving_path_csv}/BETANO.csv'
    
    todays_name = datetime.now().strftime('%A')
    driver,wait,EC,By = selenium_init()
    driver.get(f'https://www.betano.ng/upcomingcoupon/?sid=FOOT&day={todays_name}')

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#app > div > div > section.main-content-wrapper > div.grid__row.main-content-wrapper__content > div.grid__column.grid__column--fluid.grid__column__main-content > section > div.events-list__wrapper > div.events-list__grid > div:nth-child(3) > div.events-list__grid__info.tw-truncate > a > div > div.events-list__grid__info__main__participants > div:nth-child(2) > span')))
    
    simple_scroll(driver=driver,speed=1000,t_runs=10,sleep_time=2,scroll_up='yes')

    matches = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#app > div > div > section.main-content-wrapper > div.grid__row.main-content-wrapper__content > div.grid__column.grid__column--fluid.grid__column__main-content > section > div.events-list__wrapper')))
    matches = matches.text.replace('\n','!').split('!')
    print(matches)

    int_vals = [str(x) for x in range(1,3000)]
    other_vals = ['Match Result','O 1.5','U 1.5','O 2.5','U 2.5','O 3.5','U 3.5','O 4.5','U 4.5','Both Teams to Score', 'Yes','No']
    int_vals = int_vals + other_vals


    new_matches = []
    for x in matches:
        x = x.strip()
        if '/' in x  or x in int_vals:
            pass
        else:
            new_matches.append(x)


    time_value = []
    time_index = []
    for i,x in enumerate(new_matches):
        if ':' in x:
            indx = new_matches.index(x,i,len(new_matches))
            time_index.append(indx)
            time_value.append(x)

    # print(new_matches)
    # print(time_index)
    # print(time_value)

    for x in time_index:
        try:
            f_elem_indx = time_index.index(x)
            s_elem_indx = time_index.index(x) + 1

            if (time_index[s_elem_indx] - time_index[f_elem_indx]) == 8 or (time_index[s_elem_indx] - time_index[f_elem_indx]) == 10:
                all_info = new_matches[ time_index[f_elem_indx]:time_index[s_elem_indx] ]
                match_time = all_info[0]
                home_team = all_info[1]
                away_team = all_info[2]

                home_odd = float(all_info[3])
                draw_odd = float(all_info[4])
                away_odd = float(all_info[5])
                bookmaker = 'BETANO'

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