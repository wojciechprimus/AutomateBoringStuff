import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('My Number is 152-555-1243 and 496-222-0000')

print('Number Found: ', mo)
