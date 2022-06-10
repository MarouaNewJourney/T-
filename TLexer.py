    # -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 18:08:41 2021

TLexer => Le Lexeur de T++ 

@author: Rhita
"""

import ply.lex as lex


class TLexer :
    
    def __init__(self):
        self.lexer = lex.lex(module=(self))
        
#REMINDING MYSELF how to add /n et /t stuff like that : DONE
#do #INCLUDE <LIBRARY> : I DONT THINK WE NEED THIS
#do PRIVATE PUBLIC ETC : DONE
#do MAIN() IF needed
#do TABLEAU MAYBE IDK POUR STRING :  STRING DONE BUT ILL THINK ABOUT TAB

#Nos Tokens
        
    tokens = ['ID', 'INT', 'FLOAT', 'STRING', 'BOOLEAN', 'TRUE', 'FALSE', 
              'EQ', 'EQEQ', 'NOTEQ', 'GREATER', 'LESS', 'GREATEREQ', 'LESSEQ',
              'PLUSEQ', 'MINUSEQ', 'MULTEQ', 'DIVEQ', 'PERCENTEQ',
              'INC', 'DEC',
              'FINLIGNE',
              'LET','IF', 'ELSE', 'ELIF','WHILE','DO','FOR',
              'FCT', 'RETURN', 
              'AND', 'OR',
              'TYPEINT', 'TYPEFLOAT', 'TYPEBOOL','TYPESTRING',
              'CONTINUE', 'BREAK',
              'CLASS',
              'VOID', 'EXTENDS',
              'PUBLIC', 'PRIVATE',
              'PRINT', 'SCAN',
              'PLUS', 'MINUS', 'MULT', 'POW',
              'DIVIDE','LPAREN', 'RPAREN', 'LACCOL',
              'RACCOL', 'LCROCHET', 'RCROCHET', 'PIPE', 'ESPERLUETTE',
              'PERCENT', 'ACCENTCIRCON', 'EXCLAM', 'INTERRO', 'TWOPOINTS',
              'POINT', 'VIRGULE',
              'backslashed',
              'CONCAT', 'IN', 'RANGE'
              
]
    
    

#Nos Literals

#    literals = ['=', '+', '-', '/', '*',
#               '(', ')', '{', '}', '[', ']', 
#                '|', '&', '%', '^', '!', '?', ':',
#                '.', ',']
    
    t_backslashed = r'\\'
    t_EQ = r'='
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_MULT = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LACCOL = r'{'
    t_RACCOL = r'\}'
    t_LCROCHET = r'\['
    t_RCROCHET = r'\]'
    t_PIPE = r'\|'
    t_PERCENT = r'%'
    t_ACCENTCIRCON = r'\^'
    t_ESPERLUETTE = r'&'
    t_EXCLAM = r'!'
    t_INTERRO = r'\?'
    t_TWOPOINTS = r'\:'
    t_POINT = r'.'
    t_VIRGULE = r'\,'
    t_POW = r'\*\*'
 

#NOS REGEX
    

    t_EQEQ = r'=='
    t_NOTEQ = r'!='
    t_GREATER = r'>'
    t_LESS = r'<'
    t_GREATEREQ = r'>='
    t_LESSEQ = r'<='
    t_PLUSEQ = r'\+='
    t_MINUSEQ = r'-='
    t_MULTEQ = r'\*='
    t_DIVEQ = r'/='
    t_PERCENTEQ = r'%='
    
    t_INC = r'\+\+'
    t_DEC = r'--'
    
    t_FINLIGNE = r';'
   

    t_ignore = ' \t'

    

#Les Definitions de certains Token

    def t_BOOLEAN(self,t):
        r'(is7a|ours7i)'
        t.value = True if t.value == "is7a" else False
        return t
        
           
    def t_FLOAT(self, t):
        r'[-+]?\d+\.\d+'
        t.value = float(t.value)
        return t
    
        #-----------INT--------------
        #---------------------------------------------
    def t_INT(self, t):
        r'\d+'
        t.value = int(t.value)    
        return t
        

    def t_STRING(self, t):
        #need regex
        r'"(.*?)"|\'(.*?)\''
        #r'\"(\\.|[^"\\])*\"'
        #or r'"(.*\)"
        t.value = t.value[1:-1]
        t.value = t.value.replace(r"\n", "\n")
        t.value = t.value.replace(r"\t", "\t")
        return t
        
    def t_TRUE(self,t):
        r'is7a'
        return t
        
    def t_FALSE(self,t):
        r'ours7i'
        return t

   
    def t_RANGE(self, t):
        r'rala'
        return t
    
    def t_LET(self,t):
        r'atcht'
        return t
    
    
    def t_IF(self,t):
        r'ig'
        return t
    
 
    def t_ELSE(self,t):
        r'imata'
        return t
    
    def t_ELIF(self, t):
        r'imataig'
    
    def t_WHILE(self,t):
        r'magdisoul';
        return t
    
    def t_DO(self, t):
        r'skr'
        return t
    
    def t_OR(self,t):
        r'nghta'
        return t
    
    def t_FOR(self,t):
        r'n'
        return t
        
     
    def t_FCT(self,t):
        r'daala'
        return t
    
     
    def t_RETURN(self,t):
        r'rarid' 
        return t
        
   
    def t_AND(self,t):
        r'iy'
        return t
    
        

        

    def t_TYPEINT(self,t):
        r'tss7a'
        return t
        
    def t_TYPEFLOAT(self,t):
        r'youdr'
        return t
    
    def t_TYPEBOOL(self,t):
        r'tlawrtli'
        return t
    
    def t_TYPESTRING(self,t):
        r'iwaliwn'
        return t
        
    def t_CONTINUE(self,t):
        r'zayd'
        return t
    
    def t_BREAK(self,t):
        r'rzgh'
        return t
        
    def t_CLASS(self,t):
        r'tawant'
        return t
        
    def t_EXTENDS(self,t):
        r'iwrtn'
        return t
        
    def t_VOID(self,t):
        r'ourtli'
        return t
        
    def t_PUBLIC(self,t):
        r'ysntkoulshi'
        return t
    
         
    def t_PRIVATE(self,t):
        r'snkhtiwlinou'
        return t
        
      
    def t_PRINT(self,t):
        r'fgh'
        return t
    
    def t_IN(self, t):
       r'f'
       return t
    
    def t_SCAN(self,t):
        r'ini'
        return t
    
    def t_CONCAT(self, t):
        r'jm3ta'
        return t
    
    def t_ID(self, t):
        r'[a-z_][a-zA-Z_0-9]*'
        #token.type = self.basic_reserved.get(token.value, 'ID') ne marche pas quand on a utiliser reserved words
        return t
    

        


# /* */ works but // doesnt work  
# update, // marche aussi !

    def t_COMMENT(self,t):
        r'/\*.*?\*/|//.*?'
        pass
    
    # Ignore rule for single line comments
    t_ignore_SINGLE_LINE_COMMENT = r"\-\-[^\n]*"
        
#    def t_COMMENT(t):
#         r'\#.*'
#         pass
#COMMENTAIRE PYTHON #  I guess pas la peine on a déjà commentaire /* */
                
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)
            
            
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        
        
    # EOF handling rule
    # A TRAITER P
    
    #def t_eof(t):
    # Get more input (Example)
    #    more = raw_input('... ')
    #    if more:
    #        self.lexer.input(more)
    #        return self.lexer.token()
    #    return None
    
