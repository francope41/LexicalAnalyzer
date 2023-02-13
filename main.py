import sys
import re
from utils import DecafTokenizer

class Lex_Analyzer:
    def __init__(self, file_path):
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
            if tokens is not None:
                for token in tokens:
                    str_token = False
                    float_token = False


                    if token == '':
                        pass

                    if re.search(String,token):
                        match = re.search(String,token)
                        print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start()+1)+'-'+ str(match.end()), 'is T_StringConstant (value = {})'.format(token))

                    else:
                    
                        if re.search(Keywords,token) :
                            match = re.search(Keywords,token)
                            print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start()+1)+'-'+ str(match.end()), keyword_key[token])
                        
                        if re.search(Float,token) :
                            if "." in token:
                                match = re.search(Float,token)
                                print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start()+1)+'-'+ str(match.end()), 'is T_DoubleConstant (value = {})'.format(float(token)))
                                float_token = True
                            else:
                                pass

                        if re.search(Int,token) :
                            try:
                                match = re.search(Int,token)
                                print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start()+1)+'-'+ str(match.end()), 'is T_IntConstant (value = {})'.format(int(token)))
                            except:
                                pass
                        
                        elif re.search(Operators,token)  and not float_token:
                            match = re.search(Operators,token)
                            print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start()+1)+'-'+ str(match.end()), operators_key[token])

                        elif re.search(Special_Characters, token) :
                            match = re.search(Special_Characters,token)
                            try:
                                print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start()+1)+'-'+ str(match.end()), punctuation_key[token])
                            except:
                                print('\n*** Error line {}.\n'.format(count), ' *** Unrecognized char: \'{}\'\n'.format((token)))

                        elif re.search(Identifiers,token) :
                            match = re.search(Identifiers,token)
                            truncated = False
                            if len(token) > 31:
                                print('\n*** Error line {}.\n'.format(count), ' *** Identifier too long: \"{}\"\n'.format((token)))
                                trunc_token = token[0:31]
 
                                print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start()+1)+'-'+ str(match.end()), 'is T_Identifier (truncated to {})'.format(trunc_token))
                            else:
                                print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start()+1)+'-'+ str(match.end()), 'is T_Identifier')


                        elif re.search('Unidentified Token',token):
                            pass


Lex_Analyzer(sys.argv[1])