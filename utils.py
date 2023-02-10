import re

class DecafTokenizer:
    def __init__(self) -> None:
        self.Keywords = "void|int|double|bool|string|null|for|while|if|else|return|break|Print|ReadInteger|ReadLine|true|false"
        self.Operators = "(\++)|(-)|(\*)|(/)|(%)|(<=)|(>=)|[||]{2}|[==]{2}|[=]"
        # self.Numerals = "^\d*\.?\d*$"
        self.Int = '^[-+]?[0-9]+$'
        self.Float = '^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$'
        self.Special_Char = "[\[@&~!#$\^\{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|;|:"
        self.Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"

    def tokenize(self,line):
        self.tokens = []
        paternKeywords = re.compile(self.Keywords)
        paternOperators = re.compile(self.Operators)
        paternInt = re.compile(self.Int)
        paterFloat = re.compile(self.Float)
        paternSpecialChar = re.compile(self.Special_Char)
        paternIdentifiers = re.compile(self.Identifiers)

        try:
            if line[0] == "\"" and line[-1] == "\"" or line == "" or line == " " :
                self.tokens.append(line)
        except:
            pass
        if paternKeywords.search(line):
            self.tokens.append((re.search(paternKeywords,line).group(0)))    
        elif paternOperators.search(line):
            self.tokens.append((re.search(paternOperators,line).group(0)))        
        elif paternInt.search(line):
            self.tokens.append((re.search(paternInt,line).group(0)))
        elif paterFloat.search(line):
            self.tokens.append((re.search(paterFloat,line).group(0)))
        elif paternSpecialChar.search(line):        
            self.tokens.append((re.search(paternSpecialChar,line).group(0)))
        elif paternIdentifiers.search(line):
            self.tokens.append((re.search(paternIdentifiers,line).group(0)))
        elif line == "":
            self.tokens.append(line)    
        else:
            self.tokens.append("Unidentified Token")

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
        return Keywords,Operators,Int,Float,Special_Characters,Identifiers

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
