import re

class DecafTokenizer:
    def __init__(self):
        self.Keywords = "^void$|^int$|^double$|^bool$|^string$|^null$|^for$|^while$|^if$|^else$|^return$|^break$|^Print$|^ReadInteger$|^ReadLine$|^true$|^false$"
        self.Operators = "(\++)|(\-)|(\*)|(/)|(%)|(<=)|(>=)|[||]{2}|[==]{2}|(=)"
        self.Int = '[-+]?[0-9]+'
        self.Float = '[-+]?[0-9]*\.?[0-9]+(.?[eE][-+]?[0-9]+)?'
        self.Special_Char = "[\[@&~!#$\^\{}\]:;<>?,\.']|\(|\)|{}|\[\]|;|:"
        self.Identifiers = "[a-zA-Z_]+[a-zA-Z0-9_]*"
        self.String = "\"(.*?)\""


    def tokenize(self,line):
        self.tokens, StringTokens,KeywordTokens,IntTokens,FloatTokens,OperatorTokens,IdentifierTokens,SpecialCharTokens = [],[],[],[],[],[],[],[]

        paternKeywords = re.compile(self.Keywords)
        paternOperators = re.compile(self.Operators)
        paternInt = re.compile(self.Int)
        paterFloat = re.compile(self.Float)
        paternSpecialChar = re.compile(self.Special_Char)
        paternIdentifiers = re.compile(self.Identifiers)
        paterString = re.compile(self.String)

        Float_token = False

        if paterString.search(line):
                #self.tokens = self.tokens
            StringTokens = [tk for tk in re.findall(paterString,line)]
            for tk in StringTokens:
                self.tokens.append("\"{}\"".format(tk))
        
        else:

            if paternKeywords.search(line):
                KeywordTokens = [tk for tk in re.findall(paternKeywords,line)]
                #print('2',KeywordTokens)
                for tk in KeywordTokens: self.tokens.append(tk)

            if paternIdentifiers.search(line):
                IdentifierTokens = [tk for tk in re.findall(paternIdentifiers,line)]
                #print('6',IdentifierTokens)
                for tk in IdentifierTokens: 
                    if tk in KeywordTokens: pass 
                    else: self.tokens.append(tk)

            if paternOperators.search(line) and not Float_token:
                OperatorTokens = [tk for tk in re.findall(paternOperators,line)]
                for tk in OperatorTokens:
                    for i in tk:
                        if i == '':
                            pass
                        else:
                            self.tokens.append(i)

            if paterFloat.search(line) :
                FloatTokens = [tk for tk in re.findall(paterFloat,line)]
                #print('4',FloatTokens)
                for tk in FloatTokens: self.tokens.append(tk)

            if paternInt.search(line) :
                        IntTokens = [tk for tk in re.findall(paternInt,line)]
                        #print('3',IntTokens)
                        for tk in IntTokens: self.tokens.append(tk)

            if paternSpecialChar.search(line):        
                SpecialCharTokens = [tk for tk in re.findall(paternSpecialChar,line)]
                #print('7',SpecialCharTokens)
                for tk in SpecialCharTokens: self.tokens.append(tk)

        if self.tokens:
            return self.tokens
        #return [tok for tok in pattern.split(line) if tok]

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
    
    def remove_Comments(self,program):
        program_Multi_Comments_Removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", program)
        program_Single_Comments_Removed = re.sub("//.*", "", program_Multi_Comments_Removed)
        program_Comments_removed = program_Single_Comments_Removed
        return program_Comments_removed
