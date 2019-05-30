#! python3
# PhoneAndEmail.py - This is small program which is searching for Phone and Mail in a String.

import pyperclip, re

PhoneRegex = re.compile(r'''( 
    (\d{3}|\(\d{3}\))?                      #AreaCode
    (\s|-|\.)?                             #Separator
    (\d{3})                                  #First 3 dIgits
    (\s|-|\.)                               #separator
    (\d{4})                                 #Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?         # Extension
    )''', re.VERBOSE)

EmailRegex = re.compile(r'''( 
    [a-zA-Z0-9._%+-]+           #Username
    @                           #@ symbol
    [a-zA-Z0-9.-]+              #domain name
    (\.[a-zA-Z]{2,4})           #dot-something
    )''', re.VERBOSE)

text=str(pyperclip.paste())
matches=[]
for groups in PhoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in EmailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email adresses found.')
