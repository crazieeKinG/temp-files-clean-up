# Dependencies
import os
import ctypes
import shutil
import datetime
# Function to check ADMIN Privilege
def is_root():
    return ctypes.windll.shell32.IsUserAnAdmin() != 0
# Function to get sub-directory and files
def get_dir(path:str,temp_file_list:list):
    dir_list = os.listdir(path)
    for val in dir_list:
        temp_file_list.append(os.path.join(path, val))
# Function to remove files
def remove_file(path:str,log:list)->bool:
    try:
        dt = datetime.datetime.now()
        os.remove(path)        
        log.append("SUCCESS: {} {} DELETED {}".format(dt.date(), dt.strftime("%H:%M:%S"), path))
        return True
    except Exception as e:
        log.append("FAILED: {} {} {}".format(dt.date(), dt.strftime("%H:%M:%S"), e))
        return False
# Function to remove empty directory
def remove_dir(path:str,log:list)->bool:
    try:        
        dt = datetime.datetime.now()
        os.rmdir(path)
        log.append("SUCCESS: {} {} DELETED {}".format(dt.date(), dt.strftime("%H:%M:%S"), path))
        return True
    except Exception as e:
        log.append("FAILED: {} {} {}".format(dt.date(), dt.strftime("%H:%M:%S"), e))
        return False
# Function to remove items
# def remove_items(path:str,log:list)->bool:
#     try:
#         dt = datetime.datetime.now()
#         if os.path.isfile(path):
#             os.remove(path)   
#         elif os.path.isdir(path):
#             shutil.rmtree(path)
#         log.append("SUCCESS: {} {} DELETED {}".format(dt.date(), dt.strftime("%H:%M:%S"), path))
#         return True
#     except Exception as e:
#         log.append("FAILED: {} {} {}".format(dt.date(), dt.strftime("%H:%M:%S"), e))
#         return False
# Function to delete items in list
def delete_items(delete_item_list:list,temp_file_list:list):
    for item in delete_item_list:
        temp_file_list.remove(item)