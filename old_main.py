#By Eulises Franco
#UTSA ID: btz670

from nltk.tokenize import RegexpTokenizer, WordPunctTokenizer
tokenizer = WordPunctTokenizer()


# To open File
file = open("samples/badstring.frag")
operators = {'=': "'='",'+' : "'+'",  '-':"'-'", '*':"'*'",  '/':"'/'", '%':"'%'", '<':"'<'", '<=':'T_LessEqual', '>':"'>'", '>=':'T_GreaterEqual','==':'T_Equal', '||':'T_Or'}
operators_key = operators.keys()

data_type = {'void':'T_Void', 'int' : 'T_Int', 'double': 'T_Double', 'string':'T_String'}
data_type_key = data_type.keys()

punctuation = {';':"';'", ',':"','", '.':"'.'", '(':"'('", ')':"')'", '{':"'{'", '}':"'}'", '!':"'!'"}
punctuation_key = punctuation.keys()

keyword = {'while':'T_While', 'if':'T_If', 'else':'T_Else', 'return':'T_Return', 'break':'T_Break', 'true':'T_BoolConstant (value = true)', 'false':'T_BoolConstant (value = false)'}
keyword_key = keyword.keys()

empty = {'':''}
empty_key = empty.keys()

unrecognized_key = {'$':'*** Unrecognized char: \'$\'' , '@':'*** Unrecognized char: \'@\'' , '^':'*** Unrecognized char: \'^\'' , '&':'*** Unrecognized char: \'&\''  , '~':'*** Unrecognized char: \'~\'' , '`':'*** Unrecognized char: \'`\'' , '?':'*** Unrecognized char: \'?\''}

a = file.read()

count = 0

program = a.split("\n")

for line in program:
    count += 1
    #print("line#", count, "\n", line)
    # tokens = line.split(' ')
    print(line)
    tokens = tokenizer.tokenize(line)

    #print("Line#", count, "Properties \n")
    for token in tokens:
        val_isint = False
        val_isfloat = False
        val_isstring = False

        if token in empty_key:
            break

        if token[0]== "\"" and token[-1]=="\"":
            val_isstring = True

        try:
            num_token = int(token)
            if isinstance(num_token,int):
                print(token, (11-len(token))*" ", "line", count, 'cols', '1-'+str(len(token)), 'is T_IntConstant (value = {})'.format(token))
                val_isint = True
        except:
            try:
                num_token = float(token)
                if isinstance(token,float):
                    print(token, (11-len(token))*" ", "line", count, 'cols', '1-'+str(len(token)), 'is T_IntConstant (value = {})'.format(token))
                    val_isfloat = True
            except:
                pass
        
        if not val_isint and not val_isfloat and not val_isstring: 

            if token in operators_key:
                #print("operator", operators[token])
                print(token, (11-len(token))*" ", "line", count, 'cols', '1-'+str(len(token)), operators[token])

            elif token in data_type_key:
                #print("data_type", operators[token])
                print(token, (11-len(token))*" ", "line", count, 'cols', '1-'+str(len(token)), data_type[token])

            elif token in punctuation_key:
                #print("punctuation", operators[token])
                print(token, (11-len(token))*" ", "line", count, 'cols', '1-'+str(len(token)), punctuation[token])

            elif token in keyword_key:
                #print("keyword", operators[token])
                print(token, (11-len(token))*" ", "line", count, 'cols', '1-'+str(len(token)), keyword[token])
            elif token in unrecognized_key:
                print('*** Error line {}.'.format(count))
                print('*** Unrecognized char: \'{}\''.format(token))
                print('\n')
            else:
                print(token, (11-len(token))*" ", "line", count, 'cols', '1-'+str(len(token)), 'is T_Identifier')
        
        else:
            pass