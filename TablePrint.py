fillchar = ' '
# print right justified string


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

leni=len(tableData[0])                   #how many rows we want to have
lenj=len(tableData)                      #how many columns we want
long=max(tableData[1], key=len)          #Longest string in

def printTable():
    for j in range(leni):
        print()
        for i in range(lenj):
            long=len(max(tableData[i], key=len))
            print(tableData[i][j].rjust(long,fillchar), end=" ")

printTable()
