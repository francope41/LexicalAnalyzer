from utils import DecafTokenizer

tokenizer = DecafTokenizer()

file = open("samples/badstring.frag")

a = file.read()

count = 0

program = a.split("\n")
for line in program:
    count += 1
    #print("line#", count, "\n", line)
    # tokens = line.split(' ')
    #tokens = tokenizer.tokenize(line)

    tokens = tokenizer.tokenize(line)

    print (tokens)