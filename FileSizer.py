# Create a program which is looking for a files bigger than ' X ' in a folder
import shutil, os, re
list=[]
X=int(input('For how big files are You looking for(mb) ? '))*1000000

for folderName, subfolders, filenames in os.walk('F:\\python\\2007-07-04 Wycieczka'):         # Write path of folder from which You wanted to change files names.
    list.append(filenames)

# Loop over the files in the working directory.
m=int(0)
leng=len(list[0])
print('There is this number of files inside a MAIN folder: ', len(list[0]))
i=0            #use i for looping over photos
l = list[m]

for m in range(leng):
    size=os.path.getsize('F:\\python\\2007-07-04 Wycieczka\\'+l[m])
   # print('This file: ',l[m],          ', Is sooo big: ',          size,          'B')
    if size>X:
        print('I found a file bigger than Yours Value...')
        size=round(size/1000000, 2)
        print('This is name of file: ',l[m],', and this is size of it : ',size,'MB')
    else:
        pass

#1mb = 1000kB = 1000000B
