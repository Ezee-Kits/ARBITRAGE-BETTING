from bangbet import bangbet_func
from bet9ja import bet9ja_func
from betano import betano_func
from betking import betking_func
from betpawa import betpawa_func
from betbonanza import betbonanza_func
from easywin import easywin_func
# from frapapa import frapapa_func
from mozzartbet import mozzartbet_func
from msport import msport_func
from nairabet import nairabet_func
from parimatch import parimatch_func
from sportybet import sportybet_func

import time
import multiprocessing
from compile_files import compile_files_func
from deleting_files import deleting_files_func



# start = time.time()

# bangbet_func()
# bet9ja_func()
# betano_func()
# betbonanza_func()
# betking_func()
# betpawa_func()
# easywin_func()
# mozzartbet_func()
# msport_func()
# nairabet_func()
# parimatch_func()
# sportybet_func()

# end = time.time()
# print('\n TIME SPENT RUNNING THR SCRIPT',end-start)




# multi_sleeptime = 5
def first_thread():
    if __name__ == '__main__':
        thread1 = multiprocessing.Process(target=bet9ja_func)
        thread2 = multiprocessing.Process(target=bangbet_func)
        thread3 = multiprocessing.Process(target=betking_func)
        thread4 = multiprocessing.Process(target=easywin_func)

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()

        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()


def second_thread():
    if __name__ == '__main__':
        thread1 = multiprocessing.Process(target=betano_func)
        thread2 = multiprocessing.Process(target=mozzartbet_func)
        thread3 = multiprocessing.Process(target=msport_func)
        thread4 = multiprocessing.Process(target=nairabet_func)     

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()

        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()

def third_thread():
    if __name__ == '__main__':
        thread1 = multiprocessing.Process(target=betpawa_func)
        thread2 = multiprocessing.Process(target=betbonanza_func)
        thread3 = multiprocessing.Process(target=parimatch_func)
        thread4 = multiprocessing.Process(target=sportybet_func)

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()

        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()

def run_py_files():
    first_thread()
    second_thread()
    third_thread()


run_py_files()



# def all_files_func():
#     run_py_files()
#     # compile_files_func()
#     # deleting_files_func()

    