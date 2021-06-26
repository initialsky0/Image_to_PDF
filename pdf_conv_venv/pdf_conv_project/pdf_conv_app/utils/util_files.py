from os import remove, listdir
from pathlib import Path
# import time

# def cmp_file_time(file_path):
#     ''' 
#         Return the difference between the file modified time and current time in seconds 
#     '''
#     file = Path(file_path)
#     modified_time = file.stat().st_mtime
#     return time.time() - modified_time


def clean_file(file_path):
    '''
        This function will only delete files, it will not handle any dirs associated file_path
    '''
    target_path = Path(file_path)
    if(target_path.exists() and target_path.is_file()):
        remove(file_path)


def clean_all_files(file_path):
    '''
        Pass in dir path and delete all files inside.
    '''
    file_list = listdir(file_path)
    if len(file_list) > 0:
        for filename in file_list:
            clean_file(file_path / filename)