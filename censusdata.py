#! python3
# censusdata.py - This program is tracking population and number of census tracts for each county.

import openpyxl, pprint, xlrd
print('Opening workbook...')
wb = xlrd.open_workbook('censuspopdata.xlsx')
sheet = wb.sheet_by_name('Population by Census Tract')
countyData = {}

#TODO: Fill in countyData with each county`s population and tracts.
print('Reading rows')
print('Number of Rows', sheet.nrows)

for row in range(2, sheet.nrows + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    countyData.setdefault(state, {})
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

print('Writing results...')
resultFile = open('census.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
