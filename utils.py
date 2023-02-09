import re

class DecafTokenizer:
    def __init__(self) -> None:
        self.RE_Keywords = "void|int|double|bool|string|null|for|while|if|else|return|break|Print|ReadInteger|ReadLine"
        self.RE_Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(<=)|(>=)"
        self.RE_Numerals = "^(\d+)$"
        self.RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
        self.RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
        self.tokens = []




    def tokenize(self,line):
        paternKeywords = re.compile(self.RE_Keywords)
        paternOperators = re.compile(self.RE_Operators)
        paternNumerals = re.compile(self.RE_Numerals)
        paternSpecialChar = re.compile(self.RE_Special_Characters)
        paternIdentifiers = re.compile(self.RE_Identifiers)

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