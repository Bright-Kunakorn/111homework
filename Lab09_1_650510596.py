from cgitb import text


def main():
    code_table =  "aceiklmr-"
    text = '''
3
5 3 4 2
3 1 2 8 1 7 2 0 86
    '''
    decode(code_table, text)

def decode(code_table, text):
    a = text.split(' ')

    print(a)

if __name__ == '__main__':
    main()