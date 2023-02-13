import re

class DecafTokenizer:
    def __init__(self):
        self.Keywords = "^void$|^int$|^double$|^bool$|^string$|^null$|^for$|^while$|^if$|^else$|^return$|^break$|^Print$|^ReadInteger$|^ReadLine$|^true$|^false$"
        self.Operators = "(\++)|(\-)|(\*)|(/)|(%)|(<=)|(>=)|[||]{2}|[==]{2}|(=)"
        self.Int = '[-+]?[0-9][0-9]*'
        self.Float = '[-+]?[0-9]*\.?[0-9]+(.?[eE][-+]?[0-9]+)?'
        self.Special_Char = "[\[@&~!#$\^\{}\]:;<>?,\.']|\(|\)|{}|\[\]|;|:"
        self.Identifiers = "[a-zA-Z_]+[a-zA-Z0-9_]*"
        self.String = "\"(.*?)\""

    def tokenize(self,line):
        self.tokens ,StringTokens,KeywordTokens,IntTokens,FloatTokens,OperatorTokens,IdentifierTokens,SpecialCharTokens = [],[],[],[],[],[],[],[]
        disordered_Tokens, Ordered_Tokens = [],[]
        self.paterString = re.compile(self.String)
        self.paternKeywords = re.compile(self.Keywords)
        self.paternIdentifiers = re.compile(self.Identifiers)
        self.paternOperators = re.compile(self.Operators)
        self.paterFloat = re.compile(self.Float)
        self.paternInt = re.compile(self.Int)
        self.paternSpecialChar = re.compile(self.Special_Char)

        Float_token = False
        Ident_token = False

        if self.paterString.search(line):
            StringTokens = [tk for tk in re.findall(self.paterString,line)]
            for tk in StringTokens:
                self.tokens.append("\"{}\"".format(tk))
        
        else:
            if self.paternKeywords.search(line):
                #KeywordTokens = [tk for tk in re.findall(self.paternKeywords,line)]
                KeywordTokens = [tk for tk in re.findall(self.paternKeywords,line)]                
                for tk in KeywordTokens: self.tokens.append(tk)


            if self.paternIdentifiers.search(line):
                IdentifierTokens = [tk for tk in re.findall(self.paternIdentifiers,line)]
                for tk in IdentifierTokens:
                    if tk in KeywordTokens: pass 
                    else: self.tokens.append(tk)

            if self.paternOperators.search(line) and not Float_token:
                OperatorTokens = [tk for tk in re.findall(self.paternOperators,line)]
                for tk in OperatorTokens:
                    for i in tk:
                        if i == '':
                            pass
                        else:
                            self.tokens.append(i)

            if self.paterFloat.search(line):
                FloatTokens = [tk for tk in re.findall(self.paterFloat,line)]
                for tk in FloatTokens:
                    try:
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

            if self.paternInt.search(line) :
                        IntTokens = [tk for tk in re.findall(self.paternInt,line)]
                        for tk in IntTokens: self.tokens.append(tk)

            if self.paternSpecialChar.search(line):        
                SpecialCharTokens = [tk for tk in re.findall(self.paternSpecialChar,line)]
                for tk in SpecialCharTokens: self.tokens.append(tk)

        if self.tokens:
            #match_Str,match_Kw,match_Id,match_Op,match_Flt,match_Int,match_SpCh = self.get_matches_index(line)
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

        keyword = {'while':'T_While', 'if':'T_If', 'else':'T_Else', 'return':'T_Return', 'break':'T_Break', 'true':'T_BoolConstant (value = true)', 'false':'T_BoolConstant (value = false)','void':'T_Void', 'int' : 'T_Int', 'double': 'T_Double', 'string':'T_String'}
        keyword_key = keyword.keys()

        empty = {'':''}
        empty_key = empty.keys()

        return operators, data_type, punctuation, keyword, empty

    def get_matches_index(self, line):
        match_Str = re.search(self.paterString,line)
        match_Kw = re.search(self.paternKeywords,line)
        match_Id = re.search(self.paternIdentifiers,line)
        match_Op = re.search(self.paternOperators,line)
        match_Flt = re.search(self.paterFloat,line)
        match_Int = re.search(self.paternInt,line)
        match_SpCh = re.search(self.paternSpecialChar,line)

        if match_Str is not None:
            print(match_Str.start())
        if match_Kw is not None:
            print(match_Kw.start())
        if match_Id is not None:
            print(match_Id.start())
        if match_Op is not None:
            print(match_Op.start())
        if match_Flt is not None:
            print(match_Flt.start())

        return match_Str,match_Kw,match_Id,match_Op,match_Flt,match_Int,match_SpCh

    def remove_Comments(self,program):
        program_Multi_Comments_Removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", program)
        program_Single_Comments_Removed = re.sub("//.*", "", program_Multi_Comments_Removed)
        program_Comments_removed = program_Single_Comments_Removed
        return program_Comments_removed
