# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 20:21:05 2021

@author: Rhita
"""

#Firt Tokens I made

    tokens = ['ID', 'INT', 'FLOAT', 'STRING', 'TRUE', 'FALSE', 
              'EQ', 'EQEQ', 'NOTEQ', 'GREATER', 'LESS', 'GREATEREQ', 'LESSEQ',
              'PLUSEQ', 'MINUSEQ', 'MULTEQ', 'DIVEQ', 'PERCENTEQ',
              'INC', 'DEC',
              'FINLIGNE',
              'LET','IF', 'ELSE','WHILE','FOR',
              'FCT', 'RETURN', 
              'AND', 'OR',
              'TYPEINT', 'TYPEFLOAT', 'TYPEBOOL','TYPESTRING',
              'CONTINUE', 'BREAK',
              'CLASS',
              'VOID',
              'PUBLIC', 'PRIVATE',
              'PRINT', 'SCAN']
#MOT RESERVER 
    t_TRUE = r'is7a'
    t_FALSE = r'ours7i'
    
    t_LET = r'atcht'
    t_IF = r'ig'
    t_ELSE =r'imata'
    t_WHILE = r'magdisoul'
    t_FOR = r'n'
    
    t_FCT = r'daala'
    t_RETURN = r'rarid' 
    
    t_AND = r'iy'
    t_OR = r'nghta'
    
    t_TYPEINT = r'tss7a'
    t_TYPEFLOAT = r'youdr'
    t_TYPEBOOL = r'tlawrtli'
    t_TYPESTRING = r'iwaliwn'
    
    t_CONTINUE = r'zayd'
    t_BREAK = r'rzgh'
    
    t_CLASS = r'tawant'
    
    t_VOID = r'ourtli'
    
    t_PUBLIC = r'ysntkoulshi'
    t_PRIVATE = r'snkhtiwlinou'
    
    t_PRINT = r'' 
    t_SCAN = r''
    
    
    
    
###SECOND TRY I DID

 reserved = {
     'is7a' : 'TRUE',
     'ours7i' : 'FALSE',
     'atcht' : 'LET',
     'ig' : 'IF',
     'imata' : 'ELSE',
     'magdisoul' : 'WHILE',
     'n' : 'FOR',
     'daala' : 'FCT',
     'rarid' : 'RETURN', 
     'iy' : 'AND',
     'nghta' : 'OR',
     'tss7a' : 'TYPEINT',
     'youdr' : 'TYPEFLOAT',
     'tlawrtli' : 'TYPEBOOL',
     'iwaliwn' : 'TYPESTRING',
     'zayd' : 'CONTINUE',
     'rzgh' : 'BREAK',
     'tawant' : 'CLASS',
     'ourtli' : 'VOID',    
     'ysntkoulshi' : 'PUBLIC',
     'snkhtiwlinou' : 'PRIVATE',
     #'' : 'PRINT',
     #'' : 'SCAN',
     }
 
 tokens += reserved.values()
 
 def t_ID(self,t):
     r'[a-zA-Z_][a-zA-Z0-9_]*'
     if t.value in reserved:
         t.type = reserved[t.value]
     return t
 
    
 ###smh IT DIDNT WORK
 