from func import saving_files,main_date,saving_path_csv,outcome_path_csv
from thefuzz import fuzz
import pandas as pd
import winsound
import os
import time




def compile_files_func():
    all_files_path = f'{saving_path_csv}'
    h,m = time.localtime()[3:5]
    saving_path = f'{outcome_path_csv}/{str(main_date(0))} {h}hr {os.getpid()}_OS FILE.csv'


    all_paths = [] 
    for x in os.listdir(all_files_path):
        if x == 'NAIRABET.csv':
            pass
        else:
            all_paths.append(x)

    nairabet_path = pd.read_csv(f'{all_files_path}/NAIRABET.csv')
    # print(nairabet_path)



    percent = 70
    for x in range(len(nairabet_path['HOME TEAM'])):
        print('\n X = ',x)
        data = {
            'TIME':[],

            'HOME TEAM': [],
            'AWAY TEAM': [],
            
            'HOME ODD': [],
            'DRAW ODD': [],
            'AWAY ODD':[],

            'BOOKMAKER':[]
            }
        
        data['TIME'].append(nairabet_path['TIME'][x])
        data['HOME TEAM'].append(nairabet_path['HOME TEAM'][x])
        data['AWAY TEAM'].append(nairabet_path['AWAY TEAM'][x])

        data['HOME ODD'].append(nairabet_path['HOME ODD'][x])
        data['DRAW ODD'].append(nairabet_path['DRAW ODD'][x])
        data['AWAY ODD'].append(nairabet_path['AWAY ODD'][x])

        data['BOOKMAKER'].append(nairabet_path['BOOKMAKER'][x])


            # ============================= HANDLING ALL PATHS ============================
        for paths in all_paths:
            path_df = pd.read_csv(f'{all_files_path}/{paths}')

            for y in range(len(path_df['HOME TEAM'])):
                if fuzz.token_set_ratio(nairabet_path['HOME TEAM'][x],path_df['HOME TEAM'][y]) >= percent and fuzz.token_set_ratio(nairabet_path['AWAY TEAM'][x],path_df['AWAY TEAM'][y]) >= percent and nairabet_path['TIME'].astype(str)[x].strip() == path_df['TIME'].astype(str)[y].strip():
                    
                    data['TIME'].append(path_df['TIME'][y])
                    data['HOME TEAM'].append(path_df['HOME TEAM'][y])
                    data['AWAY TEAM'].append(path_df['AWAY TEAM'][y])

                    data['HOME ODD'].append(path_df['HOME ODD'][y])
                    data['DRAW ODD'].append(path_df['DRAW ODD'][y])
                    data['AWAY ODD'].append(path_df['AWAY ODD'][y])

                    data['BOOKMAKER'].append(path_df['BOOKMAKER'][y])
                    break
        print('\n')



        max_home_odd = max(data['HOME ODD'])
        max_draw_odd = max(data['DRAW ODD'])
        max_away_odd = max(data['AWAY ODD'])
        match_coef = round((1/max_home_odd + 1/max_draw_odd + 1/max_away_odd)*100)

        if match_coef < 100:
            print(winsound.Beep(440, 1000))

            match_time = data['TIME'][0]
            h_team = data['HOME TEAM'][0]
            a_team = data['AWAY TEAM'][0]        
            h_bookmaker = data['BOOKMAKER'][data['HOME ODD'].index(max_home_odd)]
            d_bookmaker = data['BOOKMAKER'][data['DRAW ODD'].index(max_draw_odd)]
            a_bookmaker = data['BOOKMAKER'][data['AWAY ODD'].index(max_away_odd)]
            amt = 1000
            h = round(((amt * 1 / max_home_odd) / match_coef) * 100)
            d = round(((amt * 1 / max_draw_odd) / match_coef) * 100)
            a = round(((amt * 1 / max_away_odd) / match_coef) * 100)       
                 
            data = {
                    'TIME':match_time,

                    'HOME TEAM': h_team,
                    'AWAY TEAM': a_team,
                    
                    'HOME ODD': max_home_odd,
                    'DRAW ODD': max_draw_odd,
                    'AWAY ODD':max_away_odd,

                    'HOME BOOKMAKER':h_bookmaker,
                    'DRAW BOOKMAKER':d_bookmaker,
                    'AWAY BOOKMAKER':a_bookmaker,

                    'HOME STAKE':h,
                    'DRAW STAKE':d,
                    'AWAY STAKE':a,

                    'MATCH COEF':match_coef,
                    'STAKING AMOUNT':amt,

                    'HOME PROFIT':round(h * max_home_odd) - amt,
                    'DRAW PROFIT':round(d * max_draw_odd) - amt,
                    'AWAY PROFIT':round(a * max_away_odd) - amt
                    }
            # df = pd.DataFrame([data])
            # print(df.to_string())
            saving_files(data=[data],path=saving_path)

