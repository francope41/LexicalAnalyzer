import re

class DecafTokenizer:
    def __init__(self) -> None:
        self.Keywords = "void|int|double|bool|string|null|for|while|if|else|return|break|Print|ReadInteger|ReadLine|true|false"
        self.Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(<=)|(>=)|[||]{2}"
        self.Numerals = "^(\d+)$"
        self.Special_Char = "[\[@&~!#$\^\{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
        self.Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"

    def tokenize(self,line):
        self.tokens = []
        paternKeywords = re.compile(self.Keywords)
        paternOperators = re.compile(self.Operators)
        paternNumerals = re.compile(self.Numerals)
        paternSpecialChar = re.compile(self.Special_Char)
        paternIdentifiers = re.compile(self.Identifiers)

        if paternKeywords.search(line):
            self.tokens.append((re.search(paternKeywords,line).group(0)))        
        elif paternOperators.search(line):
            self.tokens.append((re.search(paternOperators,line).group(0)))        
        elif paternNumerals.search(line):
            self.tokens.append((re.search(paternNumerals,line).group(0)))
        elif paternSpecialChar.search(line):
            self.tokens.append((re.search(paternSpecialChar,line).group(0)))
        elif paternIdentifiers.search(line):
            self.tokens.append((re.search(paternIdentifiers,line).group(0)))       
        else:
            self.tokens.append("Unidentified Token")

        if self.tokens:
            return self.tokens
        #return [tok for tok in pattern.split(line) if tok]

    def get_RegEx(self):
        Keywords = self.Keywords
        Operators = self.Operators
        Numerals = self.Numerals
        Special_Characters = self.Special_Char
        Identifiers = self.Identifiers
        return Keywords, Operators, Numerals, Special_Characters, Identifiers

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