# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 20:29:54 2022

@author: Rhita
"""

import ply.yacc as yacc
from TLexer import TLexer
import sys

tokens = TLexer.tokens

####ID Storage######
variables = {}

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIVIDE'),
    ('left', 'AND', 'OR'),
    ('nonassoc', 'LPAREN', 'RPAREN'),
    ('nonassoc', 'LACCOL', 'RACCOL'),
    ('nonassoc', 'GREATER', 'LESS', 'GREATEREQ', 'LESSEQ', 'EQEQ'),
)

#########USEFUL DEF###########    
def p_statements(p):
    ''' statements : statements statement
                   | statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]



# def p_statement_expression(p):
#     'statement : expression'
#     p[0] = p[1]    
    
def p_expression(p):
    '''expression : INT 
                | FLOAT
                | varval
                | expr_print_id
                | expr_print
                | expr_print_exp

        
    '''
    p[0] = p[1]


def p_statement_assign(p):
    'statement : ID EQ expression'
    variables[p[1]] = p[3]
    #print(variables[p[1]])


def p_factor_ID(p):
    'factor : ID'
    p[0] = variables[p[1]]
    #print(variables[p[1]])
    
    
def p_factor_NUMBER(p):
    '''factor : INT 
              | FLOAT'''
    p[0] = p[1]
    
def p_term_NUMBER(p):
    '''term : INT 
            | FLOAT'''    
    p[0] = p[1]

def p_expression_STRING(p):
    'expression : STRING'
    p[0] = p[1]
    
def p_expression_BOOLEAN(p):
    'expression : BOOLEAN'
    p[0] = p[1]
        


##########OPERATION ENTRE ID, DIFFERENT TYPES, ETC ###############

def p_expression_plus(p):
     '''expression : expression PLUS term  
     '''
     p[0] = p[1] + p[3]
     #print(p[0])
     
def p_expression_plus_id(p):
     '''expression : ID PLUS term  
     '''
     p[0] = variables[p[1]] + p[3]
     #print(p[0])
     
def p_expression_plus_ids(p):
     '''expression : ID PLUS ID 
     '''
     p[0] = variables[p[1]] + variables[p[3]]
     #print(p[0])
 
def p_expression_minus(p):
     'expression : expression MINUS term'
     p[0] = p[1] - p[3]
     
     
def p_expression_minus_id(p):
     '''expression : ID MINUS term  
     '''
     p[0] = variables[p[1]] - p[3]
     #print(p[0])
     
def p_expression_minus_ids(p):
     '''expression : ID MINUS ID 
     '''
     p[0] = variables[p[1]] - variables[p[3]]
     #print(p[0])
 

def p_expression_mult(p):
     'expression : expression MULT term'
     p[0] = p[1] * p[3]
     
     
def p_expression_mult_id(p):
     '''expression : ID MULT term  
     '''
     p[0] = variables[p[1]] * p[3]
     #print(p[0])
     
def p_expression_mult_ids(p):
     '''expression : ID MULT ID 
     '''
     p[0] = variables[p[1]] * variables[p[3]]
     #print(p[0])
 
def p_expression_div(p):
     'expression : expression DIVIDE term'
     if p[3]==0:
         print("Error : 9issma 3la 0 mamnou3a !") 
         ###EN TAMAZIGHT , nevermind tamazight is kinda hard      
     p[0] = p[1] / p[3]
     #print(p[0])
     
def p_expression_div_id(p):
     '''expression : ID DIVIDE term  
     '''
     if p[3]==0:
         print("Error : 9issma 3la 0 mamnou3a !") 
     p[0] = variables[p[1]] / p[3]
     #print(p[0])]
     
def p_expression_div_ids(p):
     '''expression : ID DIVIDE ID 
     '''
     if variables[p[3]]==0:
         print("Error : 9issma 3la 0 mamnou3a !") 
         ###EN TAMAZIGHT , nevermind tamazight is kinda hard      
     p[0] = variables[p[1]] / variables[p[3]]
     #print(p[0])

def p_expression_modulo(p):
    'expression : expression PERCENT term'
    p[0] = p[1] % p[3]
    #print(p[0])
    
     
def p_expression_modulo_id(p):
     '''expression : ID PERCENT term  
     '''
     p[0] = variables[p[1]] % p[3]
     print(p[0])
     
def p_expression_modulo_ids(p):
     '''expression : ID PERCENT ID 
     '''
     p[0] = variables[p[1]] % variables[p[3]]
     #print(p[0])
    
def p_expression_pow(p):
    'expression : expression POW term'
    p[0] = p[1] ** p[3]
    #print(p[0])
    
     
def p_expression_pow_id(p):
     '''expression : ID POW term  
     '''
     p[0] = variables[p[1]] ** p[3]
     #print(p[0])
     
def p_expression_pow_ids(p):
     '''expression : ID POW ID 
     '''
     p[0] = variables[p[1]] ** variables[p[3]]
     #print(p[0])

#####CONCATENATION DE STRINGS################


    
def p_expression_concat(p):
    '''expression : ID EQ CONCAT LPAREN STRING VIRGULE STRING RPAREN
                  | ID EQ CONCAT LPAREN STRING VIRGULE INT RPAREN
                  | ID EQ CONCAT LPAREN INT VIRGULE STRING RPAREN
                  | ID EQ CONCAT LPAREN STRING VIRGULE FLOAT RPAREN
                  | ID EQ CONCAT LPAREN FLOAT VIRGULE STRING RPAREN
                  | ID EQ CONCAT LPAREN ID VIRGULE STRING RPAREN
                  | ID EQ CONCAT LPAREN STRING VIRGULE ID RPAREN

    '''
      
    variables[p[1]] = str(p[5]) + str(p[7])

    #print(p[1])   
    

##########ASSIGNEMENT ID = SOMETHING ##############
   
def p_assign_num(p):
    '''
    expression : int_assign
               | float_assign
    '''
    p[0] = p[1]


def p_assign_INT(p):
    'int_assign : ID EQ INT'
    p[1] = p[3]

def p_assign_FLOAT(p):
    'float_assign : ID EQ FLOAT'
    p[1] = p[3]
    
def p_assign_STRING(p):
    'expression : ID EQ STRING'
    p[1] = p[3]
    #print(p[1])

def p_assign_BOOL(p):
    'expression : ID EQ BOOLEAN'
    p[1] = p[3]
    #print(p[1])
    
    
def p_assign_id(p):
    'expression : ID EQ ID'
    variables[p[1]] = variables[p[3]]
    
 

##############Statements pour comparaison##########


##############STATEMENTS########################


def p_statement(p):
     '''
      statement : compare_statement
                | compare_ids_statement
                | compare_idvalue_statement
                | compare_bool_statement
                | and_statement
                | or_statement 
                | and_statement_for_ids
                | or_statement_for_ids
                | if_statement
                | if_else_statement
                | while_statement
                | doWhile_statement
                | for_statement
                | inc_statement
                | inc_assign_statement
                | dec_statement
                | dec_assign_statement
                | input_statement
                | fonction
                | appel_fonction
                | return
                | return_id
                | fonction_return_id
                | while_fake_statement
                | expression
     '''
     p[0] = p[1]
     
     
def p_assign_compare_bool(p):
    '''expression : ID EQ booleans
      
    '''
    variables[p[1]] = p[3]

def p_booleans(p):
    '''booleans : compare_statement
                | compare_ids_statement
                | compare_idvalue_statement
                | compare_bool_statement
                | and_statement
                | and_statement_for_ids
                | or_statement_for_ids
                | or_statement
                | BOOLEAN
    '''
   
    p[0]=p[1]            

################DECLARATION TYPE ID##################

def p_declare_INT(p):
    'expression : TYPEINT ID'
    p[2] = None
    
def p_declare_FLOAT(p):
    'expression : TYPEFLOAT ID'
    p[2] = None

def p_declare_BOOL(p):
    'expression : TYPEBOOL ID'
    p[2] = None

def p_declare_STRING(p):
    'expression : TYPESTRING ID'
    p[2] = None


    
    
###############DECLARATION AVEC AFFECTATION################

def p_declareaffect_INT(p):
    'expression : TYPEINT ID EQ factor'
    if isinstance(p[4], int) :
        variables[p[2]] = p[4]
        print('eyoo')
    else :
        print("Error : mashi tss7a")
    
    
    ###STRING AND FLOAT AND BOOLEAN"""
def p_declareaffect_FLOAT(p):
    'expression : TYPEFLOAT ID EQ factor'
    if isinstance(p[4], float) :
        variables[p[2]] = p[4]
    else :
        print("Error : mashi youdr")

def p_declareaffect_BOOL(p):
    'expression : TYPEBOOL ID EQ expression'
    if p[4] == True or p[4] == False :
        variables[p[2]] = p[4]
    else :
        print('Error : mashi tlawrtli')

def p_declareaffect_STRING(p):
    'expression : TYPESTRING ID EQ expression'
    if isinstance(p[4], str) :
        variables[p[2]] = p[4]
    else :
        print("Error : mashi iwaliwn")

    

    

########################PRINT######################

def p_print_ID(p):
    '''
    expr_print_id : PRINT LPAREN ID RPAREN                  
    '''
    p[0] = variables[p[3]]
    #print(p[0])

    
def p_print(p):
    'expr_print : PRINT LPAREN STRING RPAREN'
    p[0]=p[3]
    
    
def p_print_expression(p):
    'expr_print_exp : PRINT LPAREN expression RPAREN'
    #print(p[3])    
    
     
    

#############STATEMENTS COMPARAISON################

def p_expression_compare(p):

     '''
     compare_statement : expression EQEQ expression
                       | expression NOTEQ expression
                       | expression GREATER expression
                       | expression GREATEREQ expression
                       | expression LESS expression
                       | expression LESSEQ expression
     '''
                 
     
     if p[2] == '==':
         if p[1] == p[3]:
             p[0] = True
         else:
             p[0] = False
             

     elif p[2] == '!=' :
         if p[1] != p[3]:
             p[0] = True
         else:
             p[0] = False

     elif p[2] == '>':
         if p[1] > p[3]:
             p[0] = True
         else:
             p[0] = False

     elif p[2] == '>=':
         if p[1] >= p[3]:
             p[0] = True
         else:
             p[0] = False

     elif p[2] == '<':
         if p[1] < p[3]:
             p[0] = True
         else:
             p[0] = False

     elif p[2] == '<=':
         if p[1] <= p[3]:
             p[0] = True
         else:
             p[0] = False    
             
def p_expression_compareIDs(p):

     '''
     compare_ids_statement : ID EQEQ ID
                       | ID NOTEQ ID
                       | ID GREATER ID
                       | ID GREATEREQ ID
                       | ID LESS ID
                       | ID LESSEQ ID
     '''
                 
     
     if p[2] == '==':
         if p[1] == p[3]:
             p[0] = True
         else:
             p[0] = False

     elif p[2] == '!=':
         if variables[p[1]] != variables[p[3]] : 
             p[0] = True
         else:
             p[0] = False

     elif p[2] == '>':
         if variables[p[1]] > variables[p[3]]:
             p[0] = True
         else:
             p[0] = False

     elif p[2] == '>=':
         if variables[p[1]] >= variables[p[3]]:
             p[0] = True
         else:
             p[0] = False

     elif p[2] == '<':
         if variables[p[1]] < variables[p[3]]:
             p[0] = True
         else:
             p[0] = False

     elif p[2] == '<=':
         if variables[p[1]] <= variables[p[3]]:
             p[0] = True
         else:
             p[0] = False    
    
#def variable_exists(v):  Didn't need it w didn't work ymkn ...
#    global variables
#    value = None
#    if v in variables.keys():
#        value = variables[v]
#    else:
#        value = None
#   return value
     
def p_compare_id_value(p):
    '''
    compare_idvalue_statement : ID EQEQ expression
                       | ID NOTEQ expression
                       | ID GREATER expression
                       | ID GREATEREQ expression
                       | ID LESS expression
                       | ID LESSEQ expression

     '''
     
     
    if p[2] == '>':
         if variables[p[1]] > p[3]:
             p[0] = True
         else:
             p[0] = False

    elif p[2] == '<':
         if variables[p[1]] < p[3]:
             p[0] = True
         else:
             p[0] = False

    elif p[2] == '>=':
         if variables[p[1]] >= p[3]:
             p[0] = True
         else:
             p[0] = False

    elif p[2] == '<=':
         if variables[p[1]] <= p[3]:
             p[0] = True
         else:
             p[0] = False

    elif p[2] == '==':
         if variables[p[1]] == p[3]:
             p[0] = True
         else:
             p[0] = False

    elif p[2] == '!=':
         if variables[p[1]] != p[3]:
             p[0] = True
         else:
             p[0] = False
    
    #return p[0]



####### Compaison des booleans #################
def p_compare_bool(p):
     '''
     compare_bool_statement : BOOLEAN EQEQ BOOLEAN
                       | BOOLEAN NOTEQ BOOLEAN

     '''


     if p[2] == '==':
         if p[1] == p[3]:
             p[0] = True
         else:
             p[0] = False

     elif p[2] == '!=':
         if p[1] != p[3]:
             p[0] = True
         else:
             p[0] = False



#################AND#######################            
def p_statement_and(p):
    '''
    and_statement : BOOLEAN AND BOOLEAN
                  | BOOLEAN AND compare_statement
                  | compare_statement AND BOOLEAN
                  | BOOLEAN AND compare_ids_statement
                  | compare_ids_statement AND BOOLEAN
                  | BOOLEAN AND compare_idvalue_statement
                  | compare_idvalue_statement AND BOOLEAN
                  | BOOLEAN AND compare_bool_statement
                  | compare_bool_statement AND BOOLEAN
                  | compare_statement AND compare_statement
                  | compare_ids_statement AND compare_ids_statement
                  | compare_idvalue_statement AND compare_idvalue_statement
                  | compare_idvalue_statement AND compare_ids_statement
                  | compare_ids_statement AND compare_idvalue_statement
                  | compare_idvalue_statement AND compare_statement
                  | compare_statement AND compare_idvalue_statement
                  | compare_statement AND compare_ids_statement
                  | compare_ids_statement AND compare_statement
    
    '''
    
    
    if p[1] == True and p[3] == True:
        p[0] = True
        
    elif p[1] == True and p[3] == False:
        p[0] = False
        
    elif p[1] == False and p[3] == False:
        p[0] = False
        
    elif p[1] == False and p[3] == True:
        p[0] = False
        
def p_statement_and_for_ids(p):
    'and_statement_for_ids : ID AND ID'
    
    if variables[p[1]] == True and variables[p[3]] == True:
        p[0] = True
        
    elif variables[p[1]] == True and variables[p[3]] == False:
        p[0] = False
        
    elif variables[p[1]] == False and variables[p[3]] == False:
        p[0] = False
        
    elif variables[p[1]] == False and variables[p[3]] == True:
        p[0] = False
        
###################OR######################

def p_statement_or(p):
    """
    or_statement : BOOLEAN OR BOOLEAN
                  | BOOLEAN OR compare_statement
                  | compare_statement OR BOOLEAN
                  | BOOLEAN OR compare_ids_statement
                  | compare_ids_statement OR BOOLEAN
                  | BOOLEAN OR compare_idvalue_statement
                  | compare_idvalue_statement OR BOOLEAN
                  | BOOLEAN OR compare_bool_statement
                  | compare_bool_statement OR BOOLEAN
                  | compare_statement OR compare_statement
                  | compare_ids_statement OR compare_ids_statement
                  | compare_idvalue_statement OR compare_idvalue_statement
                  | compare_idvalue_statement OR compare_ids_statement
                  | compare_ids_statement OR compare_idvalue_statement
                  | compare_idvalue_statement OR compare_statement
                  | compare_statement OR compare_idvalue_statement
                  | compare_statement OR compare_ids_statement
                  | compare_ids_statement OR compare_statement
    """
    if p[1] == True or p[3] == True:
        p[0] = True
        
    else:
        p[0] = False
        
        
def p_statement_or_for_ids(p):
    'or_statement_for_ids : ID OR ID'
    
    if variables[p[1]] == True or variables[p[3]] == True:
        p[0] = True
        
    else:
        p[0] = False
    

###########################IF####################

ifs = []    

def p_if_statement(p):
    '''
    if_statement : IF LPAREN compare_statement RPAREN LACCOL expression RACCOL
                 | IF LPAREN compare_statement RPAREN LACCOL statements RACCOL
                 | IF LPAREN compare_ids_statement RPAREN LACCOL expression RACCOL
                 | IF LPAREN compare_ids_statement RPAREN LACCOL statements RACCOL
                 | IF LPAREN compare_idvalue_statement RPAREN LACCOL expression RACCOL
                 | IF LPAREN compare_idvalue_statement RPAREN LACCOL statements RACCOL
                 | IF LPAREN and_statement RPAREN LACCOL expression RACCOL
                 | IF LPAREN or_statement RPAREN LACCOL expression RACCOL
                 | IF LPAREN and_statement RPAREN LACCOL statements RACCOL
                 | IF LPAREN or_statement RPAREN LACCOL statements RACCOL 
                 | IF LPAREN BOOLEAN RPAREN LACCOL expression RACCOL
                 | IF LPAREN BOOLEAN RPAREN LACCOL statements RACCOL
                 
    '''
    if p[3]==True:
        p[0] = p[6]

 
        
        
######################IF ELSE######################

def p_if_else_statement(p):
    '''
    if_else_statement : IF LPAREN compare_statement RPAREN LACCOL statements RACCOL ELSE LACCOL statements RACCOL
                      | IF LPAREN compare_statement RPAREN LACCOL expression RACCOL ELSE LACCOL statements RACCOL
                      | IF LPAREN compare_statement RPAREN LACCOL statements RACCOL ELSE LACCOL expression RACCOL
                      | IF LPAREN compare_statement RPAREN LACCOL expression RACCOL ELSE LACCOL expression RACCOL
                      | IF LPAREN compare_statement RPAREN LACCOL statements RACCOL ELSE if_statement
                      | IF LPAREN compare_statement RPAREN LACCOL expression RACCOL ELSE if_statement
                      | IF LPAREN and_statement RPAREN LACCOL statements RACCOL ELSE LACCOL statements RACCOL
                      | IF LPAREN and_statement RPAREN LACCOL expression RACCOL ELSE LACCOL statements RACCOL
                      | IF LPAREN and_statement RPAREN LACCOL statements RACCOL ELSE LACCOL expression RACCOL
                      | IF LPAREN and_statement RPAREN LACCOL expression RACCOL ELSE LACCOL expression RACCOL
                      | IF LPAREN and_statement RPAREN LACCOL statements RACCOL ELSE if_statement
                      | IF LPAREN and_statement RPAREN LACCOL expression RACCOL ELSE if_statement
                      | IF LPAREN or_statement RPAREN LACCOL statements RACCOL ELSE LACCOL statements RACCOL
                      | IF LPAREN or_statement RPAREN LACCOL expression RACCOL ELSE LACCOL statements RACCOL
                      | IF LPAREN or_statement RPAREN LACCOL statements RACCOL ELSE LACCOL expression RACCOL
                      | IF LPAREN or_statement RPAREN LACCOL expression RACCOL ELSE LACCOL expression RACCOL
                      | IF LPAREN or_statement RPAREN LACCOL expression RACCOL ELSE if_statement
                      | IF LPAREN or_statement RPAREN LACCOL statements RACCOL ELSE if_statement
                      | IF LPAREN compare_idvalue_statement RPAREN LACCOL statements RACCOL ELSE LACCOL statements RACCOL
                      | IF LPAREN compare_idvalue_statement RPAREN LACCOL expression RACCOL ELSE LACCOL statements RACCOL
                      | IF LPAREN compare_idvalue_statement RPAREN LACCOL statements RACCOL ELSE LACCOL expression RACCOL
                      | IF LPAREN compare_idvalue_statement RPAREN LACCOL expression RACCOL ELSE LACCOL expression RACCOL
                      | IF LPAREN compare_idvalue_statement RPAREN LACCOL expression RACCOL ELSE if_statement
                      | IF LPAREN compare_idvalue_statement RPAREN LACCOL statements RACCOL ELSE if_statement
                      | IF LPAREN compare_ids_statement RPAREN LACCOL statements RACCOL ELSE LACCOL statements RACCOL
                      | IF LPAREN compare_ids_statement RPAREN LACCOL expression RACCOL ELSE LACCOL statements RACCOL
                      | IF LPAREN compare_ids_statement RPAREN LACCOL statements RACCOL ELSE LACCOL expression RACCOL
                      | IF LPAREN compare_ids_statement RPAREN LACCOL expression RACCOL ELSE LACCOL expression RACCOL
                      | IF LPAREN compare_ids_statement RPAREN LACCOL expression RACCOL ELSE if_statement
                      | IF LPAREN compare_ids_statement RPAREN LACCOL statements RACCOL ELSE if_statement
                      | IF LPAREN BOOLEAN RPAREN LACCOL statements RACCOL ELSE LACCOL statements RACCOL
                      | IF LPAREN BOOLEAN RPAREN LACCOL expression RACCOL ELSE LACCOL statements RACCOL
                      | IF LPAREN BOOLEAN RPAREN LACCOL statements RACCOL ELSE LACCOL expression RACCOL
                      | IF LPAREN BOOLEAN RPAREN LACCOL expression RACCOL ELSE LACCOL expression RACCOL
                      | IF LPAREN BOOLEAN RPAREN LACCOL expression RACCOL ELSE if_statement
                      | IF LPAREN BOOLEAN RPAREN LACCOL statements RACCOL ELSE if_statement
                      | IF LPAREN compare_statement RPAREN LACCOL statements RACCOL ELSE if_else_statement
                      | IF LPAREN compare_statement RPAREN LACCOL expression RACCOL ELSE if_else_statement
                      | IF LPAREN compare_idvalue_statement RPAREN LACCOL statements RACCOL ELSE if_else_statement
                      | IF LPAREN compare_idvalue_statement RPAREN LACCOL expression RACCOL ELSE if_else_statement
                      | IF LPAREN compare_ids_statement RPAREN LACCOL statements RACCOL ELSE if_else_statement
                      | IF LPAREN compare_ids_statement RPAREN LACCOL expression RACCOL ELSE if_else_statement
                      | IF LPAREN and_statement RPAREN LACCOL statements RACCOL ELSE if_else_statement
                      | IF LPAREN and_statement RPAREN LACCOL expression RACCOL ELSE if_else_statement
                      | IF LPAREN or_statement RPAREN LACCOL statements RACCOL ELSE if_else_statement
                      | IF LPAREN or_statement RPAREN LACCOL expression RACCOL ELSE if_else_statement
                      | IF LPAREN BOOLEAN RPAREN LACCOL statements RACCOL ELSE if_else_statement
                      | IF LPAREN BOOLEAN RPAREN LACCOL expression RACCOL ELSE if_else_statement

    ''' 
    
    if len(p) == 12:
        if p[3] == True:
            p[10] = None
            p[0] = p[6]
        
        else:
            p[6] = None
            p[0] = p[10]
        
    else :
        if p[3] == True:
            p[0] = p[6]
        
        else:
            p[6] = None
            p[0] = p[9]
        

#def p_if_else_extend(p):
#    '''if_else_extend : IF LPAREN compare_statement RPAREN LACCOL statements RACCOL ELSE if_else_statement

#    '''
###################WHILE#################

#def p_while(p):
#    '''
#    while_statement : WHILE LPAREN compare_statement RPAREN RACCOL expression LACCOL
#
#    '''
#    if p[3]==True:
#        p[0] = (p[1], p[3], p[6])
    
#    else : 
#        print("comparaison fausse")

#for some reason katkhdm ghir en tant que boucle infinie... Problème au niveau de l'incrémentation qui n'est pas prise en considération dans next iteration(???)
def p_loop_while(p):
    '''while_statement : WHILE LPAREN compare_statement RPAREN LACCOL statements RACCOL
                       | WHILE LPAREN compare_statement RPAREN LACCOL expression RACCOL
                       | WHILE LPAREN compare_ids_statement RPAREN LACCOL statements RACCOL
                       | WHILE LPAREN compare_ids_statement RPAREN LACCOL expression RACCOL
                       | WHILE LPAREN compare_idvalue_statement RPAREN LACCOL statements ID INC RACCOL
                       | WHILE LPAREN compare_idvalue_statement RPAREN LACCOL expression ID INC RACCOL
                       | WHILE LPAREN and_statement RPAREN LACCOL statements RACCOL
                       | WHILE LPAREN and_statement RPAREN LACCOL expression RACCOL
                       | WHILE LPAREN or_statement RPAREN LACCOL statements RACCOL
                       | WHILE LPAREN or_statement RPAREN LACCOL expression RACCOL
                       | WHILE LPAREN BOOLEAN RPAREN LACCOL statements RACCOL
                       | WHILE LPAREN BOOLEAN RPAREN LACCOL expression RACCOL
    '''
    
    
    ###do it using if => didn't work :/
    i=0
    stmts=[]
    while p[3]==True:
        stmts.append(p[6])
        i=i+1
        variables[p[7]]=variables[p[7]]+1
        if (i == 100):
            print("error : 7ala9a makatsalash !")
            break
    p[0] = stmts
    


def p_loop_while_fake(p):
    '''while_fake_statement : WHILE LPAREN ID LESS INT RPAREN LACCOL statements ID INC RACCOL
                            | WHILE LPAREN ID LESS INT RPAREN LACCOL expression ID INC RACCOL
    '''
    
    ###do it using if
    i=0
    stmts=[]  
    while variables[p[3]]<p[5]:
        stmts.append(p[8])
        i=i+1
        variables[p[9]]=variables[p[9]]+1
        variables[p[3]]=variables[p[9]]
        if (i == 150):
            print("error : 7ala9a makatsalash !")
            break
    p[0] = stmts
        

def p_doWhile(p):
    '''
    doWhile_statement : DO LACCOL expression RACCOL WHILE LPAREN compare_statement RPAREN
                      | DO LACCOL statements RACCOL WHILE LPAREN compare_statement RPAREN
                      | DO LACCOL expression RACCOL WHILE LPAREN compare_idvalue_statement RPAREN
                      | DO LACCOL statements RACCOL WHILE LPAREN compare_idvalue_statement RPAREN
                      | DO LACCOL expression RACCOL WHILE LPAREN compare_ids_statement RPAREN
                      | DO LACCOL statements RACCOL WHILE LPAREN compare_ids_statement RPAREN
                      | DO LACCOL expression RACCOL WHILE LPAREN and_statement RPAREN
                      | DO LACCOL expression RACCOL WHILE LPAREN or_statement RPAREN
                      | DO LACCOL statements RACCOL WHILE LPAREN and_statement RPAREN
                      | DO LACCOL statements RACCOL WHILE LPAREN or_statement RPAREN
                      | DO LACCOL expression RACCOL WHILE LPAREN BOOLEAN RPAREN
                      | DO LACCOL statements RACCOL WHILE LPAREN BOOLEAN RPAREN
    '''
    #p[0] = (p[1], p[3], p[7])

    i=0
    stmts=[]
    while p[7] == True:
        stmts.append(p[3])
        i=i+1
        if(i==100):
            print("error : 7ala9a makatsalash !")
            break
    p[0] = stmts
        

###############Ajout de l'INC et DEC############

def p_inc(p):
    '''
    inc_statement : ID INC

    '''
    variables[p[1]] = variables[p[1]] + 1
    #p[0] = variables[p[1]]
    #return p[0]
    
def p_inc_assign(p):
    'inc_assign_statement : ID EQ term INC'
    variables[p[1]] = p[3] + 1

def p_dec(p):
    '''
    dec_statement :  ID DEC
    '''
    variables[p[1]] = variables[p[1]]-1

def p_dec_assign(p):
    'dec_assign_statement : ID EQ term DEC'
    variables[p[1]] = variables[p[3]] - 1


############# FOR ############

def p_for(p):
    '''
    for_statement : FOR LPAREN ID IN RANGE LPAREN INT RPAREN RPAREN LACCOL expression RACCOL
                  | FOR LPAREN ID IN RANGE LPAREN INT RPAREN RPAREN LACCOL statements RACCOL

    '''   
    
    stmts= []
    if p[7] > 0:
        i = 0 
        variables[p[3]] = 0
        while i < p[7]:
            stmts.append(p[11])
            i = i+1
        p[0] =stmts
    else:
        print("error : makaynsh f 7oudoud l7ala9a")

    


################Les Fonctions #############
functions = {}

#######Body de la fonction########

# def p_instruction_list(p):
#     '''
#         instruction_list : instruction_list statement
#                         | instruction_list expression
#                         | statements
#                         | instruction_list statements

#     '''
  
#     if len(p) == 2:
#         p[0] = [p[1]]
#     else:
#         if(not isinstance(p[1], list)):
#             p[1] = [p[2]]
#         else:
#             p[1].append(p[2])
#         p[0] = p[1]

######Arguments for appel#########
def p_argument_list(p):
    '''
        argument_list : expression
                      | argument_list VIRGULE expression
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        if(not isinstance(p[1], list)):
            p[1] = [p[3]]
        else:
            p[1].append(p[3])
        p[0] = p[1]


############Parametre Fonction############

def p_parameter_list(p):
    '''
    parameter_list : expression
                   | parameter_list VIRGULE expression
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        if(not isinstance(p[1], list)):
            p[1] = [p[3]]
        else:
            p[1].append(p[3])
        p[0] = p[1]

         #
##########La fonction avec et sans return##########
def p_fonction(p):
    '''
    fonction : FCT ID LPAREN parameter_list RPAREN LACCOL statements RACCOL
         | FCT ID LPAREN RPAREN LACCOL statements RACCOL
         | FCT ID LPAREN parameter_list RPAREN LACCOL statements return RACCOL
         | FCT ID LPAREN RPAREN LACCOL statements return RACCOL
    '''

    if(len(p) == 8):
        functions[p[2]] = p[6]
        
    elif(len(p) == 9) and (p[4]==')') : 
        
        functions[p[2]] = p[7]
        
    elif(len(p) == 9) and (p[4]!=')') : 
            functions[p[2]] = p[7]
            
    elif(len(p) == 10) : 
        functions[p[2]] = p[8] 

#########Fonction qui retourne ID###########
def p_fonction_return_id(p):
    '''
    fonction_return_id : FCT ID LPAREN parameter_list RPAREN LACCOL statements return_id RACCOL
                   | FCT ID LPAREN RPAREN LACCOL statements return_id RACCOL
    '''

    if(len(p) == 10):
        functions[p[2]] = p[8]
        
    elif(len(p) == 9) : 
        functions[p[2]] = p[7]

############Appel Fonction##########"
def p_appel(p):
    '''
    appel_fonction : ID LPAREN argument_list RPAREN
               | ID LPAREN  RPAREN
               | ID LPAREN ID RPAREN

    '''

    p[0] = functions[p[1]]
        #p[0] = ('appel_func', p[1])
        #p[0] = ('appel_func', p[1], p[3])


########Return###########
def p_return(p):
    '''
    return : RETURN LPAREN expression RPAREN
    '''
    p[0] = p[3]


#########Return special pour ID#######
def p_return_id(p):
    '''
    return_id : RETURN LPAREN ID RPAREN
    '''
    p[0] = variables[p[3]]

############################SCAN###########

def p_input_statement(p):
    '''
        input_statement : TYPEINT ID EQ SCAN LPAREN STRING RPAREN
                        | TYPEFLOAT ID EQ SCAN LPAREN STRING RPAREN
                        | TYPESTRING ID EQ SCAN LPAREN STRING RPAREN
    '''
    
    if(p[1]=='tss7a'):
        print(p[6])
        value = input()
        value = int(value)
        if(isinstance(value,int)) :
            variables[p[2]] = value
            p[0] = p[2]

        
    if(p[1]=='youdr'):
        print(p[6])
        value = input()
        value = float(value)
        if(isinstance(value,float)) :
            variables[p[2]] = value
            p[0] = p[2]
    
    if(p[1]=='iwaliwn'):
        print(p[6])
        value = input()
        value = str(value)
        if(isinstance(value,str)) :
            variables[p[2]] = value
            p[0] = p[2]
            



##############CLASS####################################
classes={}
objects={}
vars={}
func={}


def p_types(p):
    '''
    varval : INT
            | FLOAT
            | STRING
            | BOOLEAN
    '''
    p[0] = p[1]

def p_class_variables(p):
    '''class_variables : class_variables class_variable
                       | class_variable
        '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]
        


def p_class_variable(p):
    ''' class_variable : PUBLIC ID EQ varval
                       | PRIVATE ID EQ varval
    '''
    vars[p[2]]=p[4]
    p[0]=p[2]
    
def p_class_funcs(p):
    '''class_fonctions : class_fonctions class_fonction
                       | class_fonction
        '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_class_funcs_return(p):
    '''class_fonctions_return_id : class_fonctions_return_id class_fonction_return_id
                       | class_fonction_return_id
        '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]
        
        
def p_class_func(p):
    '''class_fonction : PUBLIC fonction
                      | PRIVATE fonction
    '''
    
def p_class_func_return(p):
    '''class_fonction_return_id : PUBLIC fonction_return_id
                                | PRIVATE fonction_return_id
    '''
    
        
def p_class(p):
    '''statement : CLASS ID LACCOL class_variables RACCOL
                | CLASS ID EXTENDS ID LACCOL class_variables RACCOL
                | CLASS ID LACCOL class_variables class_fonctions RACCOL
                | CLASS ID EXTENDS ID LACCOL class_variables class_fonctions RACCOL
                | CLASS ID LACCOL class_variables class_fonctions_return_id RACCOL
                | CLASS ID EXTENDS ID LACCOL class_variables class_fonctions_return_id RACCOL
    '''
    if len(p)==6:
        classes[p[2]]=p[4]
    else:
        classes[p[2]]=p[6]+classes[p[4]]

def p_declare_object(p):
    '''
    statement : ID LCROCHET ID RCROCHET
    '''
    if p[1] in classes:
        objects[p[3]]=p[1]
    else:
        print(f"makaynsh tawant 3ndou had smiya' {p[1]} '")

def p_call_object_var(p): 
    '''statement : ID POINT ID
    '''
    if p[1] in objects:
        class_name=objects[p[1]]
        if class_name in classes:
            class_variables=classes[class_name]
            if p[3] in class_variables and p[3] in vars:
                    value=vars[p[3]]
                    p[0]=value
            else:
                print(f"'{p[3]}' mashi variable f had tawant {class_name}")
        else:
            print(f"makaynsh tawant 3ndou had smiya' {class_name} '")
    else:
        print(f"makaynsh shi objet 3ndou had smiya' {p[1]} '")
        
def p_error(p):
     print("Error : Rak Kht2ti f Syntaxe !")
     
def p_empty(p):
    'empty :'
    pass     
     
     
debugfile = 'parser.out'

mylex = TLexer()

lexeur = mylex.lexer


data='''
a=1

b=1
daala b (tss7a a,tss7a b) {
a=5+1
a=a+1
a++
a=b+a
ig(b==1)
{  
 a=4*3+5
 b=56+5
 a=a+b
 }
rarid(a)

}
b(a)

'''

lexeur.input(data)


while True:
    tok = lexeur.token()
    if not tok: 
        break
    print(tok)

parser = yacc.yacc()

datap = parser.parse(data)

print(datap)

