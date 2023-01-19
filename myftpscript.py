#!/usr/bin/python
import ftplib
import os

from ftplib import FTP  
FTP_HOST = '15.160.110.185'
FTP_USER = 'FTPUser'
FTP_PASS = 'CornerOctopus1!'
FTP_ENTRY_POINT_FOLDER = 'TEST'
FTP_WORK_FOLDER = 'OUT'

try:
    ftp = FTP(FTP_HOST)
    ftp.login(FTP_USER,FTP_PASS)

    # the structure of the FTP on the OctopusServer machine contains 3 folders: TEST, PREP, PROD.
    # In each folder you can find the IN/OUT folders.
    ftp.cwd(FTP_ENTRY_POINT_FOLDER)
    ftp.cwd(FTP_WORK_FOLDER)

    filenames = ftp.nlst()
    
    if len(filenames) != 0:
        for filename in filenames:
            local_filename = os.path.join('/Users/corey986/Desktop/testFTP', filename)
            file = open(local_filename, 'wb')
            ftp.retrbinary('RETR '+ filename, file.write)
            file.close()
        
    else:
        print('FTP FOLDER IS EMPTY')
    ftp.quit()
except ftplib.all_errors as e:
    print('FTP ERROR:', e)



