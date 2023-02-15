import re

class DecafTokenizer:
    def __init__(self):
        self.Keywords = "^void$|^int$|^double$|^bool$|^string$|^null$|^for$|^while$|^if$|^else$|^return$|^break$|^Print$|^ReadInteger$|^ReadLine$|^true$|^false$"
        self.Operators = "(\++)|(\-)|(\*)|(/)|(%)|(<=)|(>=)|[||]{2}|[==]{2}|(=)"
        self.Int = '[0-9]+'
        self.Int_Hex = '0[xX][0-9A-Fa-f]+'
        self.Float = '[0-9]+\.[0-9]*'
        self.Float_eE = '[+-]?[0-9]+(?:\.[0-9]+)?\.?[eE][-+]?\d+?$'
        self.Special_Char = "[\[@&~!#$\^\{}\]:;<>?,\.']|\(|\)|{}|\[\]|;|:|\."
        self.Identifiers = "[a-zA-Z_]+[a-zA-Z0-9_]*"
        self.String = "\"(.*?)\""

    def tokenize(self,line, count):
        self.tokens ,StringTokens,KeywordTokens,IntTokens,FloatTokens,OperatorTokens,IdentifierTokens,SpecialCharTokens = [],[],[],[],[],[],[],[]
        disordered_Tokens, Ordered_Tokens = [],[]
        self.paterString = re.compile(self.String)
        self.paternKeywords = re.compile(self.Keywords)
        self.paternIdentifiers = re.compile(self.Identifiers)
        self.paternOperators = re.compile(self.Operators)
        self.paterFloat = re.compile(self.Float)
        self.paterFloat_eE = re.compile(self.Float_eE)
        self.paternInt = re.compile(self.Int)
        self.paternInt_Hex = re.compile(self.Int_Hex)
        self.paternSpecialChar = re.compile(self.Special_Char)

        self.line = line

        Float_token = False
        Ident_token = False

        if self.paterString.search(self.line):
            #print('1 STRING DETECTED')
            StringTokens = [tk for tk in re.findall(self.paterString,self.line)]
            for tk in StringTokens:
                self.tokens.append("\"{}\"".format(tk))
        
        else:
            if self.paternKeywords.search(self.line):
                #print('2 KEYWORD DETECTED')
                #KeywordTokens = [tk for tk in re.findall(self.paternKeywords,self.line)]
                KeywordTokens = [tk for tk in re.findall(self.paternKeywords,self.line)]                
                for tk in KeywordTokens: self.tokens.append(tk)

            if self.paterFloat.search(self.line) or self.paterFloat_eE.search(self.line):
                #print('4 FLOAT DETECTED'
                if self.paterFloat_eE.search(self.line):
                    Float_eE_Tokens = [tk for tk in re.findall(self.paterFloat_eE,self.line)]
                    for tk in Float_eE_Tokens:             
                        self.line = self.line.replace(tk,'')
                        self.tokens.append(tk)
                else:
                    FloatTokens = [tk for tk in re.findall(self.paterFloat,self.line)]
                    for tk in FloatTokens:
                        if tk.startswith('.'):
                            tk = tk[1:]
                        try:
                            self.line = self.line.replace(tk,'')
                            int_check = float(tk)
                        except:
                            int_check = None

                        if int_check is not None:
                            if "." in tk:
                                self.tokens.append(tk)
                            else:
                                pass
                        else:
                            pass

            elif self.paternInt.search(self.line) or self.paternInt_Hex.search(self.line):
                #print('5 INT DETECTED')

                IntTokens = [tk for tk in re.findall(self.paternInt,self.line)]
                for tk in IntTokens:
                    #print(tk)

                    self.tokens.append(tk)

            if self.paternIdentifiers.search(self.line):
                #print('3 IDENT DETECTED')
                IdentifierTokens = [tk for tk in re.findall(self.paternIdentifiers,self.line)]
                for tk in IdentifierTokens:
                    self.line = self.line.replace(tk,'')
                    if tk in KeywordTokens: pass 
                    else: self.tokens.append(tk)

            if self.paternOperators.search(self.line):
                #print('6 OPERATOR DETECTED')

                OperatorTokens = [tk for tk in re.findall(self.paternOperators,self.line)]
                for tk in OperatorTokens:
                    for i in tk:
                        if i == '':
                            pass
                        else:
                            self.tokens.append(i)

            if self.paternSpecialChar.search(self.line):  
                #print('7 SPechar DETECTED')

                SpecialCharTokens = [tk for tk in re.findall(self.paternSpecialChar,self.line)]
                for tk in SpecialCharTokens: self.tokens.append(tk)

        if self.tokens:
            for token in self.tokens:
                m = line.find(token)
                disordered_Tokens.append((token,m))

            Sorted_Tokens = sorted(disordered_Tokens, key=lambda item:item[1])
            for tk in Sorted_Tokens:
                Ordered_Tokens.append(tk[0])
                 
            return Ordered_Tokens

    def get_RegEx(self):
        Keywords = self.Keywords
        Operators = self.Operators
        #Numerals = self.Numerals
        Int = self.Int
        Float = self.Float
        Special_Characters = self.Special_Char
        Identifiers = self.Identifiers
        String = self.String
        return Keywords,Operators,Int,Float,Special_Characters,Identifiers, String

    def get_dictionaries(self):
        operators = {'=': "'='",'+' : "'+'",  '-':"'-'", '*':"'*'",  '/':"'/'", '%':"'%'", '<=':'T_LessEqual', '>=':'T_GreaterEqual','==':'T_Equal', '||':'T_Or'}
        operators_key = operators.keys()

        data_type = {'void':'T_Void', 'int' : 'T_Int', 'double': 'T_Double', 'string':'T_String'}
        data_type_key = data_type.keys()

        punctuation = {';':"';'", ',':"','", '.':"'.'", '(':"'('", ')':"')'", '{':"'{'", '}':"'}'", '!':"'!'",'<':"'<'",'>':"'>'"}
        punctuation_key = punctuation.keys()

        keyword = {'while':'T_While', 'if':'T_If', 'else':'T_Else', 'return':'T_Return', 'break':'T_Break', 'true':'T_BoolConstant (value = true)', 
                   'false':'T_BoolConstant (value = false)','void':'T_Void', 'int' : 'T_Int', 'double': 'T_Double', 'string':'T_String',
                   'bool':'T_Bool','null':'T_Null','for':'T_For','Print':'T_Print','ReadInteger':'T_ReadInteger','ReadLine':'T_ReadLine'}
        keyword_key = keyword.keys()


        empty = {'':''}
        empty_key = empty.keys()

        return operators, data_type, punctuation, keyword, empty

    def remove_Comments(self,program):
        program_Multi_Comments_Removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", program)
        program_Single_Comments_Removed = re.sub("//.*", "", program_Multi_Comments_Removed)
        program_Comments_removed = program_Single_Comments_Removed
        return program_Comments_removed
