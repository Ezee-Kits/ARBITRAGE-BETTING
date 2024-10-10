from func import saving_files,drop_duplicate,headless_selenium_init,saving_path_csv,selenium_init
import time


 

def msport_func():
    path = f'{saving_path_csv}/MSPORT.csv'
    driver,wait,EC,By = headless_selenium_init()
    driver.get('https://www.msport.com/ng/mobile/sports/list/Soccer?d=Today&sort=TIME_ASC')
    time.sleep(10)

    for scroll in range(10):
        print('scrolled :',scroll)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            match_end = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div > div.m-match-list.m-main > footer > button')))
            if match_end.text == 'Back to Top':
                print(' BREAKED')
                break
        except:
            pass
        time.sleep(2)


    matches = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div > div.m-match-list.m-main > div.m-list-view > div.skeleton')))
    matches = matches.text.replace('\n','!').split('!')
    # print(matches)


    int_vals = [str(x) for x in range(30)]
    int_vals.append('X')

    new_matches = []

    for x in matches:
        x = x.strip()
        if '/' in x or '+' in x or x in int_vals or '-' in x:
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
                    bookmaker = 'MSPORT'

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
