import sys
import re
from utils import DecafTokenizer

class Lex_Analyzer:
    def __init__(self, file_path) -> None:
        file_path = file_path
    
        tokenizer = DecafTokenizer()

        file = open(file_path)

        a = file.read()

        Keywords,Operators,Int,Float,Special_Characters,Identifiers, String = tokenizer.get_RegEx()
        operators_key, data_type_key, punctuation_key, keyword_key, empty_key = tokenizer.get_dictionaries()

        count = 0

        no_comments_a = tokenizer.remove_Comments(a)

        program = no_comments_a.split("\n")
        for line in program:
            count += 1
            tokens = tokenizer.tokenize(line)
            for token in tokens:
                str_token = False
                float_token = False

                if token == 'Unidentified Token':
                    break
                if token == '':
                    break

                if re.search(String,token):
                    match = re.search(String,token)
                    print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), 'is T_StringConstant (value = {})'.format(token))
                    str_token = True
                
                elif re.search(Keywords,token) and not str_token:
                    match = re.search(Keywords,token)
                    print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), keyword_key[token])

                elif re.search(Int,token) and not str_token:
                    match = re.search(Int,token)
                    print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), 'is T_IntConstant (value = {})'.format(int(token)))
                
                elif re.search(Float,token) and not str_token:
                    match = re.search(Float,token)
                    print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), 'is T_DoubleConstant (value = {})'.format(float(token)))
                    float_token = True

                elif re.search(Operators,token) and not str_token and not float_token:
                    match = re.search(Operators,token)
                    print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), operators_key[token])

                

                elif re.search(Special_Characters, token) and not str_token:
                    match = re.search(Special_Characters,token)
                    print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), punctuation_key[token])

                elif re.search(Identifiers,token) and not str_token:
                    match = re.search(Identifiers,token)
                    print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start())+'-'+ str(match.end()), 'is T_Identifier')

                elif re.search('Unidentified Token',token):
                    pass

                else:
                    print('else')


Lex_Analyzer(sys.argv[1])