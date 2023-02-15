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
            tokens = tokenizer.tokenize(line, count)
            if tokens is not None:
                for token in tokens:
                    float_token = False
                    kewrd_token = False
                    punc_token = False
                    ident_token = False
                    if token == '':
                        pass

                    if token =="\"":
                        print('\n*** Error line {}.\n*** Unterminated string constant: \"\n'.format(count))

                    if token.startswith("\"") and not token.endswith("\""):
                        print('\n*** Error line {}.\n*** Unterminated string constant: {}\n'.format(count,token))
                        break

                    if re.search(String,token):
                        match = re.search(String,token)
                        print(token, (11-len(token))*" ", "line", count, 'cols', str(match.start()+1)+'-'+ str(match.end()), 'is T_StringConstant (value = {})'.format(token))

                    else:
                        if re.search(Keywords,token) :
                            col_start = line.find(token)
                            col_end = col_start+len(token)
                            print(token, (11-len(token))*" ", "line", count, 'cols', str(col_start+1)+'-'+ str(col_end), keyword_key[token])
                            kewrd_token = True

                        elif re.search(Identifiers,token) and not kewrd_token or re.search(Identifiers,token):
                            col_start = line.find(token)
                            col_end = col_start+len(token)
                            iden_col_start = col_start
                            iden_col_end = col_end
                            if re.search(Float,token):
                                pass
                            else:
                                if len(token) > 31:
                                    print('\n*** Error line {}.'.format(count), '\n*** Identifier too long: \"{}\"\n'.format((token)))
                                    trunc_token = token[0:31]
    
                                    print(token, (11-len(token))*" ", "line", count, 'cols', str(col_start+1)+'-'+ str(col_end), 'is T_Identifier (truncated to {})'.format(trunc_token))
                                else:
                                    print(token, (11-len(token))*" ", "line", count, 'cols', str(col_start+1)+'-'+ str(col_end), 'is T_Identifier')
                        
                        if re.search(Float,token):
                            if "." in token:
                                col_start = line.find(token)
                                col_end = col_start+len(token)
                                
                                print(token, (11-len(token))*" ", "line", count, 'cols', str(col_start+1)+'-'+ str(col_end), 'is T_DoubleConstant (value = {})'.format(float(token)))
                                float_token = True
                            else:
                                pass

                        elif re.search(Int,token):
                            #print(token, line)
                            col_start = line.find(token)
                            col_end = col_start+len(token)
                            if token != line:
                                if iden_col_start <= col_start <= iden_col_end:
                                    pass
                                else:
                                    if "+" in token or "-" in token:
                                        token = token[1:]
                                        print(token, (11-len(token))*" ", "line", count, 'cols', str(col_start+1)+'-'+ str(col_end), 'is T_IntConstant (value = {})'.format(int(token)))
                                    else:
                                        print(token, (11-len(token))*" ", "line", count, 'cols', str(col_start+1)+'-'+ str(col_end), 'is T_IntConstant (value = {})'.format(int(token)))
                            else:
                                try:
                                    print(token, (11-len(token))*" ", "line", count, 'cols', str(col_start+1)+'-'+ str(col_end), 'is T_IntConstant (value = {})'.format(int(token)))
                                except:
                                    pass

                            

                        elif re.search(Operators,token)  and not float_token:
                            col_start = line.find(token)
                            col_end = col_start+len(token)
                            print(token, (11-len(token))*" ", "line", count, 'cols', str(col_start+1)+'-'+ str(col_end), operators_key[token])

                        elif re.search(Special_Characters, token):
                            col_start = line.find(token)
                            col_end = col_start+len(token)
                            try:
                                print(token, (11-len(token))*" ", "line", count, 'cols', str(col_start+1)+'-'+ str(col_end), punctuation_key[token])
                            except:
                                print('\n*** Error line {}.'.format(count), '\n*** Unrecognized char: \'{}\'\n'.format((token)))


                        elif re.search('Unidentified Token',token):
                            pass

                        else:
                            pass#print(token)
        #print("")
                            
                            


Lex_Analyzer(sys.argv[1])