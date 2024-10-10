from func import saving_files,drop_duplicate,headless_selenium_init,saving_path_csv
from bs4 import BeautifulSoup
from lxml import html
import time
import pandas as pd



 
def betbonanza_func():
    path = f'{saving_path_csv}/BETBONANAZA.csv'
    driver,wait,EC,By = headless_selenium_init()
    driver.get('https://betbonanza.com/sport/todays_soccer')
    time.sleep(10)

    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#tb-center-container > section > div:nth-child(3) > div > div > div > div:nth-child(2) > div.wpt-table__col.wpt-table__col--fluid.event-click > div > div.wpt-event-info__wrp.wpt-event-info__wrp--primary > div.wpt-teams > div:nth-child(3) > span')))
    except:
        pass

    matches = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#tb-center-container > section')))
    matches = matches.text.replace('\n','!').split('!')
    # print(matches)

    int_vals = [str(x) for x in range(1,3)]
    int_exp = ['X','Intervals','Main Soccer','View all markets','Totals','Starts in',]

    int_vals = int_vals + int_exp

    new_matches = []
    for x in matches:
        x = x.strip()
        if '1X2' in x or '/' in x or '+' in x or '1x2' in x or '1 x 2' in x or '1 X 2' in x  or 'score' in x  or 'Score' in x or ',' in x  or 'Away' in x or 'Home' in x or 'Double' in x  or 'Fouls' in x or x in int_vals:
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
    print(time_index)

    for x in time_index:
        try:
            f_elem_indx = time_index.index(x)
            s_elem_indx = time_index.index(x) + 1

            if (time_index[s_elem_indx] - time_index[f_elem_indx]) == 8 or (time_index[s_elem_indx] - time_index[f_elem_indx]) == 9:
                all_info = new_matches[ time_index[f_elem_indx]:time_index[s_elem_indx] ]
                match_time = all_info[0]

                home_team = all_info[1]
                away_team = all_info[2]

                home_odd = float(all_info[4])
                draw_odd = float(all_info[5])
                away_odd = float(all_info[6])
                bookmaker = 'BETBONANZA'

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



