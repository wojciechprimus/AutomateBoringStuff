import re

panda = "The ADJ panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."

adje=input("Tell me the ADJECTIVE word: ")
noun=input("Tell me the NOUN word: ")
verb=input("Tell me the VERB word: ")


adjes = re.compile(r'ADJ')
panda=adjes.sub(adje,panda)

nouns = re.compile(r'NOUN')
panda=nouns.sub(noun,panda)

verbs = re.compile(r'VERB')
panda=verbs.sub(verb,panda)



print(panda)
