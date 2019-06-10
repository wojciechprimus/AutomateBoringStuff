import shutil, os, re
list=[]

for folderName, subfolders, filenames in os.walk('F:\\primo\\zdjecia'):         # Write path of folder from which You wanted to change files names.
    list.append(str(folderName))

# Create a regex that matches files with the PhotosNames
fotoPattern = re.compile(r"""(
    #[P]{,4}        # DSC text before the date
    #[_]
    #\d{3,8}           # 5digits 
    (.avi|AVI)         # all text after the date
    )""", re.VERBOSE)

# Loop over the files in the working directory.
m=int(0)
print("This is main folder from which we change the file names: " ,list[m])
leng=len(list)

for m in range(leng):
    i=0            #use i for looping over photos
    l = list[m]
    for fotos in os.listdir(l):
        mo = fotoPattern.search(fotos)
        # Skip files which is not a photo
        if mo == None:
            continue

        # Get the different parts of the filename.
        dscPart = mo.group(1)        #DSC group

        # Form the European-style filename.
        i = (i+1)
        j = str(i)
        newFilename = j + '.avi'

        # Get the full, absolute file paths.
        absWorkingDir = os.path.abspath(l)
        fotos = os.path.join(absWorkingDir, fotos)
        newFilename = os.path.join(absWorkingDir, newFilename)

        # Rename the files.
        print('Renaming "%s" to "%s"...' % (fotos, newFilename))
        #shutil.move(fotos, newFilename) # uncomment after testing
