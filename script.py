#!/usr/bin/env python3
# -*- coding: utf-8 -*-


##########
# IMPORT #
##########
import os
import time


############
#  SET UP  #
############
# Path to watch : this is where the script looks for new file/folder
PATH_TO_WATCH = "./test-vsh/"

# Refresh every X seconds
REFRESH = 1

# Time between comparaison of PATH_TO_WATCH
TIME_BETWEEN = 1


#########
# PATHS #
#########
PATHS = {
    '/152x102/glossy/fill': 'C:\\Users\\Public\\0000 - Hot Folder\\10x15hotfolder\\glossy\\fill',
    '/152x102/glossy/fit': 'C:\\Users\\Public\\0000 - Hot Folder\\10x15hotfolder\\glossy\\fit',
    '/152x102/matte/fill': 'C:\\Users\\Public\\0000 - Hot Folder\\10x15hotfolder\\luster\\fill',
    '/152x102/matte/fit': 'C:\\Users\\Public\\0000 - Hot Folder\\10x15hotfolder\\luster\\fit',

    '/152x114/glossy/fill': 'C:\\Users\\Public\\0000 - Hot Folder\\11x15hotfolder\\glossy\\fill',
    '/152x114/glossy/fit': 'C:\\Users\\Public\\0000 - Hot Folder\\11x15hotfolder\\glossy\\fit',
    '/152x114/matte/fill': 'C:\\Users\\Public\\0000 - Hot Folder\\11x15hotfolder\\luster\\fill',
    '/152x114/matte/fit': 'C:\\Users\\Public\\0000 - Hot Folder\\11x15hotfolder\\luster\\fit',

    '/178x127/glossy/fill': 'C:\\Users\\Public\\0000 - Hot Folder\\13x18hotfolder\\glossy\\fill',
    '/178x127/glossy/fit': 'C:\\Users\\Public\\0000 - Hot Folder\\13x18hotfolder\\glossy\\fit',
    '/178x127/matte/fill': 'C:\\Users\\Public\\0000 - Hot Folder\\13x18hotfolder\\luster\\fill',
    '/178x127/matte/fit': 'C:\\Users\\Public\\0000 - Hot Folder\\13x18hotfolder\\luster\\fit',

    '/230x152/glossy/fill': 'C:\\Users\\Public\\0000 - Hot Folder\\15x23hotfolder\\glossy\\fill',
    '/230x152/glossy/fit': 'C:\\Users\\Public\\0000 - Hot Folder\\15x23hotfolder\\glossy\\fit',
    '/230x152/matte/fill': 'C:\\Users\\Public\\0000 - Hot Folder\\15x23hotfolder\\luster\\fill',
    '/230x152/matte/fit': 'C:\\Users\\Public\\0000 - Hot Folder\\15x23hotfolder\\luster\\fit',

    '/305x203/glossy/fill': 'C:\\Users\\Public\\0000 - Hot Folder\\20x30hotfolder\\glossy\\fill',
    '/305x203/glossy/fit': 'C:\\Users\\Public\\0000 - Hot Folder\\20x30hotfolder\\glossy\\fit',
    '/305x203/matte/fill': 'C:\\Users\\Public\\0000 - Hot Folder\\20x30hotfolder\\luster\\fill',
    '/305x203/matte/fit': 'C:\\Users\\Public\\0000 - Hot Folder\\20x30hotfolder\\luster\\fit',
}


#############
# FUNCTIONS #
#############

# Watch path and compare os.dir(path) with itself TIME_BETWEEN seconds later.
# Return new file(s) and folder(s).
def watcher(PATH_TO_WATCH):
    before = os.listdir(PATH_TO_WATCH)
    while 1:
        time.sleep(REFRESH)
        after = os.listdir(PATH_TO_WATCH)
        if before != after:
            #print("Il y a du nouveau :")
            time.sleep(TIME_BETWEEN)
            new_files = []
            for afile in after:
                exist = 0
                for bfile in before:
                    if bfile == afile:
                        exist = 1
                if exist == 0:
                    new_files.append(afile)
            # for afile in new_files:
                # print afile
            return new_files
        before = after

# Check if new_files contain an unique folder name composed by 6 digits.
# return 0 or 1
def is_it_id(new_files):
    if len(new_files) != 1:
        return 0
    if len(new_files[0]) != 6:
        return 0
    return 1

# Search searched_name in path
# return 0 or 1
def search_in_folder(searched_name, path):
    for file in os.listdir(path):
        if file == searched_name:
            return 1
    return 0


########
# MAIN #
########
def main():
    # Test if new client folder is created
    new_files = watcher(PATH_TO_WATCH)

    # List all new dir in paths_found[]
    for new_file in new_files:
        paths_found = []
        for key in PATHS:
            if os.path.isdir(PATH_TO_WATCH + new_file + key):
                paths_found.append(PATH_TO_WATCH + new_file + key)

    # Copy all content of newdir
    for path_found in paths_found:
        path_found = path_found.split('/')
        crop_path_found = ''
        for i in range(3, len(path_found)):
            crop_path_found += '/' + path_found[i]
        if crop_path_found in PATHS.keys():
            print 'Copie de ' + crop_path_found + ' vers ' + \
                  PATHS[crop_path_found]

try:
    main()
except KeyboardInterrupt:
    print "Arrêt..."
