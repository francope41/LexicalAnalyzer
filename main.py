import re
from utils import DecafTokenizer

tokenizer = DecafTokenizer()

file = open("samples/string.frag")

a = file.read()

Keywords,Operators,Int,Float,Special_Characters,Identifiers = tokenizer.get_RegEx()
operators_key, data_type_key, punctuation_key, keyword_key, empty_key = tokenizer.get_dictionaries()

count = 0

no_comments_a = tokenizer.remove_Comments(a)

program = no_comments_a.split("\n")
for line in program:
    count += 1
    tokens = tokenizer.tokenize(line)
    for token in tokens:
        if token == 'Unidentified Token':
            break
        if token == '':
            break
        if len(token) > 1:
            if token[0] == "\"" and token[-1] == "\"" or token == "" or token == " ":
                print(token, (11-len(token))*" ", "line", count, 'cols', str(0) +'-'+ str(len(token)), 'is T_StringConstant (value = {})'.format(token))
                break
        if re.search(Keywords,token):
            match = re.search(Keywords,token)
            print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), keyword_key[token])
        
        # elif re.search(String,token):
        #     match = re.search(Keywords,token)
        #     print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), 'is T_StringConstant (value = "{}")'.format(token))

        elif re.search(Operators,token):
            match = re.search(Operators,token)
            print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), operators_key[token])

        elif re.search(Int,token):
            match = re.search(Int,token)
            print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), 'is T_IntConstant (value = {})'.format(int(token)))
        
        elif re.search(Float,token):
            match = re.search(Float,token)
            print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), 'is T_DoubleConstant (value = {})'.format(float(token)))

        elif re.search(Special_Characters, token):
            match = re.search(Special_Characters,token)
            print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), punctuation_key[token])
        
        elif re.search(Identifiers,token):
            match = re.search(Identifiers,token)
            print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), 'is T_Identifier')

        elif re.search('Unidentified Token',token):
            pass