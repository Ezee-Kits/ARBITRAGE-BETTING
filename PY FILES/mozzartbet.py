from func import saving_files,drop_duplicate,main_date,headless_selenium_init,saving_path_csv,selenium_init
from bs4 import BeautifulSoup
import time



def mozzartbet_func():
    path = f'{saving_path_csv}/MOZZARTBET.csv'
    driver,wait,EC,By = headless_selenium_init()
    driver.get('https://www.mozzartbet.ng/en#/date/'+str(main_date(0))+"?sid=1")

    time.sleep(2)
    try:
        agree = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#gdpr-wrapper > div > div.accept-button')))
        agree.click()
    except:
        pass

    try:
        for v in range(100):
            load20 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#focus > section.betting-matches.view.one.dark > div > div.paginator.dark > div.loadMore > div:nth-child(2)')))
            js_script = "arguments[0].scrollIntoView();"
            driver.execute_script(js_script,load20)
            
            print('Clicks/Loading = ',v)
            try:
                source1 = driver.page_source
                soup = BeautifulSoup(source1,'html.parser')
                remain = int(soup.find('div',class_='remaining').text.split()[-1])
                print(remain)
                if remain < 25:
                    break
                else:
                    load20.click()
            except:
                pass
            time.sleep(2)
    except:
        pass

    time.sleep(3)


    matches = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="focus"]/section[1]/div/div[2]')))
    matches = matches.text.replace('\n','!').split('!')
    print(matches)


    int_vals = [str(x) for x in range(1,3)]
    int_vals.append('X')

    new_matches = []

    for x in matches:
        x = x.strip()
        if x in int_vals or '-' in x:
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
    
            if (time_index[s_elem_indx] - time_index[f_elem_indx]) == 6 or (time_index[s_elem_indx] - time_index[f_elem_indx]) == 7:
            
                    all_info = new_matches[ time_index[f_elem_indx]:time_index[s_elem_indx] ]
                    match_time = all_info[0].split()[-1]
                    home_team = all_info[1]
                    away_team = all_info[2]

                    home_odd = float(all_info[3])
                    draw_odd = float(all_info[4])
                    away_odd = float(all_info[5])
                    bookmaker = 'MOZZARTBET'

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
