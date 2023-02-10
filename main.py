import re
from utils import DecafTokenizer

tokenizer = DecafTokenizer()

file = open("samples/reserve_op.frag")

a = file.read()

Keywords, Operators, Numerals, Special_Characters, Identifiers = tokenizer.get_RegEx()
operators_key, data_type_key, punctuation_key, keyword_key, empty_key = tokenizer.get_dictionaries()

count = 0

program = a.split("\n")
for line in program:
    count += 1
    tokens = tokenizer.tokenize(line)
    for token in tokens:
        if token == 'Unidentified Token':
            break
        if token == '':
            break

        if re.search(Keywords,token):
            match = re.search(Keywords,token)
            print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), keyword_key[token])
        
        elif re.search(Operators,token):
            match = re.search(Operators,token)
            print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), operators_key[token])
        
        elif re.search(Numerals,token):
            match = re.search(Numerals,token)
            print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), match.group())
        
        elif re.search(Special_Characters, token):
            match = re.search(Special_Characters,token)
            print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), punctuation_key[token])
        
        elif re.search(Identifiers,token):
            match = re.search(Identifiers,token)
            print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), 'is T_Identifier')

        elif re.search('Unidentified Token',token):
            pass