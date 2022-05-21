'''
This code backs zips a folder and backs up to dropbox
'''

import os
import time
import zipfile
from datetime import datetime
from pathlib import PureWindowsPath, PurePosixPath
import sys



def zipdir(path, zipf):
    '''
    This function zips a folder
    '''
    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file))
            print('Added ' + file)
    print('Zipped ' + path)
    return None





def backup(folder_to_backup = r'G:\StarCitizen\LIVE\USER\Client\0\Controls\Mappings' , 
           folder_to_backup_into = r'L:\Dropbox\Gaming\Star Citizen\Star-Citizen-profile-for-X56-Rhino\zips'):
    '''
    This function backs up a folder to dropbox
    '''

    # Windows -> Posix
    posix_folder_to_backup = str(PurePosixPath(PureWindowsPath(folder_to_backup)))
    print('Backing up from: ' + posix_folder_to_backup)  # foo/bar/file.txt

    posix_folder_to_backup_into = str(PurePosixPath(PureWindowsPath(folder_to_backup_into)))
    print('into ' + posix_folder_to_backup_into )


    # get the folername of the folder to backup
    Folder_Name_to_backup = os.path.basename(posix_folder_to_backup)

    print('Folder name to backup : ' + Folder_Name_to_backup)
    # make a zip file of the folder with YYYY-MM-DD-HH-MM
    zip_name = posix_folder_to_backup_into + '/' + datetime.now().strftime('%Y-%m-%d-%H-%M') + '_' + Folder_Name_to_backup  + '.zip'
    zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    zipdir(posix_folder_to_backup, zipf)
    zipf.close()
    print('Backup complete')






def main():
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

    folder_to_backup = r'G:\StarCitizen\LIVE\USER\Client\0\Controls\Mappings'
    folder_to_backup_into = r'L:\Dropbox\Gaming\Star Citizen\Star-Citizen-profile-for-X56-Rhino\zips'

    # backup(str(sys.argv)[0], str(sys.argv)[1]) # run the main function with the arguments from the command line
    backup (folder_to_backup=folder_to_backup, folder_to_backup_into = folder_to_backup_into ) # run the main function with the arguments given in the notebook




# get the arguments from the command line
if __name__ == '__main__':
    main()  # run the main function
