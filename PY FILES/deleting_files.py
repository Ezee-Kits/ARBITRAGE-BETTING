import os
from func import saving_path_csv,outcome_path_csv


def deleting_files_func():
    full_files_path = f'{saving_path_csv}'
    outcome_files_path = f'{outcome_path_csv}'

    for x in os.listdir(full_files_path):
        path = f'{full_files_path}/{x}'
        os.remove(path)
    
    for x in os.listdir(outcome_files_path):
        path = f'{outcome_files_path}/{x}'
        os.remove(path)