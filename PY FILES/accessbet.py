from func import saving_files,drop_duplicate,headless_selenium_init,saving_path_csv,selenium_init
import time

 

def accessbet_func():
    path = f'{saving_path_csv}/ACCESSBET.csv'
    driver,wait,EC,By = selenium_init()
    driver.get('https://m.accessbet.com/en/sports/pre-match/event-view?specialSection=today-bets')
    time.sleep(10)

    # try:
    #     for v in range(100):
    #         show_more = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#root > div.layout-content-holder-bc > div.special-games-container > div > div.pm-body-bc > label > p')))
    #         js_script = "arguments[0].scrollIntoView();"
    #         driver.execute_script(js_script,show_more)
    #         print('Clicks/Loading = ',v)
    #         show_more.click()
    # except:
    #     pass

    matches = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[6]/div[2]/div/div[3]')))
    matches = matches.text.replace('\n','!').split('!')
    print(matches)

accessbet_func()