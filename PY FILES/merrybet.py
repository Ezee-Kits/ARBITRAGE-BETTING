from func import saving_files,drop_duplicate,headless_selenium_init,saving_path_csv,main_date,simple_scroll,selenium_init
import time

 

def merrybet_func():
    path = f'{saving_path_csv}/MERRYBET.csv'
    driver,wait,EC,By = selenium_init()
    driver.get('https://www.merrybet.com/search/date/'+str(main_date(0)))
    time.sleep(10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'/html/body/div[5]/div[2]/div[1]/div[2]/div[3]/div/div/div[3]/partial[2]/div/div/div/div[2]/div[2]/div[4]')))
    simple_scroll(driver=driver,speed=1400,t_runs=10,sleep_time=.5)

    matches = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[2]/div[1]/div[2]/div[3]/div/div/div[3]/partial[2]/div/div/div/div[2]/div[2]')))
    matches = matches.text.replace('\n','!').split('!')
    print(matches)

merrybet_func()