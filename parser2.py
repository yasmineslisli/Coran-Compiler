import ply.yacc as yacc
from pyarabic import *

from lexer import tokens

def p_phrase(p):
    '''phrase : V1  
              | V2 
              | V3 
              | V4 
              | V5'''
    p[0] = p[1]

def p_V1(p):
    '''V1 : FI3L 7ARF IsmMajror moudafIlayh IsmMawsol FI3L
          | V1 V2'''
    if(len(p) == 7):
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
        print('Verset 1 correct')
    else:
        p[0] = p[1] + p[2]

def p_V2(p):
    '''V2 : C
          | V2 V3'''
    if(len(p) == 2):
        p[0] = p[1]
        print('Verset 2 correct')
    else:
        p[0] = p[1] + p[2]

def p_V3(p):
    '''V3 : FI3L 7ARF MOUBTADAA KHABAR
          | V3 V4'''
    if(len(p) == 5):
        p[0] = p[1] + p[2] + p[3] + p[4]
        print('Verset 3 correct')
    else:
        p[0] = p[1] + p[2]

def p_V4(p):
    '''V4 : IsmMawsol C
          | V4 V5'''
    if(p[1] == 'الَّذِي'):
        print('Verset 4 correct')
    p[0] = p[1] + p[2]
    

def p_V5(p):
    'V5 : T T IsmMawsol 7ARF FI3L'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    print('Verset 5 correct')

def p_C(p):
    '''C : T J 
         | T T J'''
    if(len(p) == 3):
        p[0] = p[1] + p[2]
    elif(len(p) == 4):
        p[0] = p[1] + p[2] + p[3]

def p_T(p):
    '''T : FI3L 
         | MAF3OULBIH'''
    p[0] = p[1]

def p_J(p):
    'J : 7ARF IsmMajror'
    p[0] = p[1] + p[2]

def p_error(p):
    print("Erreur de syntaxe")
    
parser = yacc.yacc()
while True:
    try:
        s = input('entrez le verset :')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)

