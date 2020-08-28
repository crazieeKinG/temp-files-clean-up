# Dependencies
import os
from tqdm import tqdm
import temp_modules as tm


def main(temp_path: str):
    # LOG file
    log = list()
    # Start
    print("\nStarting to look in " + temp_path)
    temp_file_list = list()
    tm.get_dir(temp_path, temp_file_list)
    # print(temp_file_list)
    deleted_list = list()
    total = len(temp_file_list)
    # Get all sub-directories and files
    for val in temp_file_list:
        if os.path.isdir(f"{val}"):
            tm.get_dir(val, temp_file_list)
    total = len(temp_file_list)
    print(f"\nTOTAL FOUND:: {total}\n")
    # Deleting files
    for i in tqdm(
        iterable=range(len(temp_file_list)), desc="DELETING FILES (excluding folder)"
    ):
        val = temp_file_list[i]
        if os.path.isfile(f"{val}"):
            if tm.remove_file(val, log):
                deleted_list.append(val)
    tm.delete_items(deleted_list, temp_file_list)
    deleted_list = []
    print(f"\nLEFT:: {len(temp_file_list)}\n")
    # Deleting directories
    for i in tqdm(iterable=range(len(temp_file_list)), desc="DELETING DIRECTORIES"):
        val = temp_file_list[i]
        if os.path.isdir(f"{val}"):
            if tm.remove_dir(val, log):
                deleted_list.append(val)
    tm.delete_items(deleted_list, temp_file_list)
    # # Deleting files
    # for i in tqdm(iterable=range(len(temp_file_list)),desc='DELETING'):
    #     val = temp_file_list[i]
    #     if os.path.isdir(f"{val}"):
    #         if tm.remove_items(val,log):
    #             deleted_list.append(val)
    # tm.delete_items(deleted_list,temp_file_list)
    rem = len(temp_file_list)
    print(f"\nDELETED::{total-rem} / {total}")
    print(f"FAILED::{rem} / {total}\n")
    # Creating LOG FILE
    with open("records.log", "a") as tf:
        for i in tqdm(range(len(log)), desc="Updating LOG file"):
            tf.write("{}\n".format(log[i]))
        tf.close()
    # END