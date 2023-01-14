import os

token_files = []
count = 0
tokens_summ = []
def main():

    for filename in os.listdir('./'):
        if filename.startswith('token'):
            token_files.append(filename)
    for token_file in token_files:
        with open(token_file, 'r') as tokens:
            for token_line in tokens:
                tokens_summ.append(token_line+'\n')
    return len(tokens_summ)

print(main())