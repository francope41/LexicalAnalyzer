import re

class DecafTokenizer:
    def __init__(self) -> None:
        self.RE_Keywords = "void|int|double|bool|string|null|for|while|if|else|return|break|Print|ReadInteger|ReadLine"
        self.RE_Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(<=)|(>=)"
        self.RE_Numerals = "^(\d+)$"
        self.RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
        self.RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
        tokens = []




    def tokenize(self,line):
        paternKeywords = re.compile(self.RE_Keywords)
        paternOperators = re.compile(self.RE_Operators)
        paternNumerals = re.compile(self.RE_Numerals)
        paternSpecialChar = re.compile(self.RE_Special_Characters)
        paternIdentifiers = re.compile(self.RE_Identifiers)

        for i in line:
            print (i)


        #return [tok for tok in pattern.split(line) if tok]