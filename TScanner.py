# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 18:09:28 2021

@author: Rhita
"""

from TLexer import TLexer

mylex = TLexer()
lexeur = mylex.lexer


path = input('Enter file path : ')

file = open(path,'r')


data = file.read()

lexeur.input(data)

#for token in lexer:
#    pass



def main():
    args = sys.argv
    input_file=args[1]
    data = open(input_file).read()
    parser = yacc.yacc()
    result = parser.parse(data)
    if result is not None:
        for r in result:
            if r == None:
                continue;
            else:
                print(r)

if __name__ == '__main__':
    main()
    
