import re

NameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = NameRegex.search('First Name: Pawel Last Name: Primus')

print(mo.group(1))
print(mo.group(2))
