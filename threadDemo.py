import threading, time
print('Start of program.')

def takeANap():                                     #1
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)       #2
threadObj.start()                                   #3

print('End of program.')
