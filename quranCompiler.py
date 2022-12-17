import ply.lex as lex
import ply.yacc as yacc
from pyarabic import *



#################################   LEXER   #################################
tokens = ['FI3L', '7ARF', 'IsmMajror','IsmMawsol','MAF3OULBIH','MOUBTADAA','KHABAR','ISM','DARFZ','BADAL','NA3T','DAMIR']

t_ignore = ' \t'
t_FI3L=u'اقْتَرِبْ|اسْجُدْ|تُطِعْ|نَدْعُ|يَدْعُ|نَسْفَعًا|يَرَى|يَنتَهِ|تَوَلَّى|كَذَّبَ|أَمَرَ|كَانَ|صَلَّى|يَنْهَى|رَأَيْ|اسْتَغْنَى|رَّآ|اقْرَأْ|خَلَقَ|عَلَّمَ|يَعْلَمْ|يَطْغَى'
t_7ARF=u'لْ|فَ|لا|سَ|أَنَّ|أَوْ|عَلَى|أَ|إِلَى|أَن|لَ|إِنَّ|كَلاَّ|بِ|وَ|لَمْ|مِنْ|إِن'
t_IsmMajror=u'النَّاصِيَةِ|التَّقْوَى|الْهُدَى|اسْمِ|عَلَقٍ|الْقَلَمِ'
t_IsmMawsol=u'الَّذِي|مَا'
t_MAF3OULBIH=u'الزَّبَانِيَةَ|نَادِيَ|عَبْدًاَ'
t_MOUBTADAA=u'رَبُّكَ'
t_KHABAR=u'الأَكْرَمُ'
t_ISM=u'رَبِّكَ|الإِنسَانَ|الرُّجْعَى|اللَّهَ'
t_DARFZ=u'إِذَا'
t_BADAL=u'نَاصِيَةٍ'
t_NA3T=u'خَاطِئَةٍ|كَاذِبَةٍ'
t_DAMIR=u'ه|هُ|تَ'
# t_lettre=u'[بتثجحخادذرزسأشصضطظعغفقكلمنهـوي]'

def t_error(t):
    print("Caractère incorrect '%s'" % t.value[0])
    t.lexer.skip(1)




#################################   PARSER   #################################
def p_phrase(p):
    '''phrase : V1  
              | V2 
              | V3 
              | V4 
              | V5
              | V6
              | V7
              | V8
              | V9
              | V10
              | V11
              | V12
              | V13
              | V14
              | V15
              | V16
              | V17
              | V18
              | V19'''
    p[0] = p[1]


def p_V1(p):
    '''V1 : FI3L 7ARF IsmMajror ISM IsmMawsol FI3L
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
    '''V5 : T T IsmMawsol 7ARF FI3L
          | V5 V6'''
    if(len(p) == 6):
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        print('Verset 5 correct')
    else:
        p[0] = p[1] + p[2]

def p_V6(p):
    '''V6 : 7ARF 7ARF ISM 7ARF FI3L
          | V6 V7'''
    if(len(p) == 6):
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        print('Verset 6 correct')
    else:
        p[0] = p[1] + p[2] 

def p_V7(p):
    '''V7 : 7ARF FI3L DAMIR FI3L
          | V7 V8'''
    if(len(p) == 5):
        p[0] = p[1] + p[2] + p[3] + p[4]
        print('Verset 7 correct')
    else:
        p[0] = p[1] + p[2] 

def p_V8(p):
    '''V8 : 7ARF 7ARF ISM ISM
          | V8 V9'''
    if(len(p) == 5):
        p[0] = p[1] + p[2] + p[3] + p[4]
        print('Verset 8 correct')
    else:
        p[0] = p[1] + p[2] 

def p_V9(p):
    '''V9 : 7ARF FI3L DAMIR IsmMawsol FI3L
          | V9 V10'''
    if(len(p) == 6):
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        print('Verset 9 correct')
    else:
        p[0] = p[1] + p[2] 

def p_V10(p):
    '''V10 : MAF3OULBIH DARFZ FI3L
           | V10 V11'''
    if(len(p) == 4):
        p[0] = p[1] + p[2] + p[3] 
        print('Verset 10 correct')
    else:
        p[0] = p[1] + p[2] 

def p_V11(p):
    '''V11 : 7ARF FI3L DAMIR 7ARF FI3L J
           | V11 V12'''
    if(len(p) == 7):
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
        print('Verset 11 correct')
    else:
        p[0] = p[1] + p[2] 

def p_V12(p):
    '''V12 : 7ARF FI3L J
           | V12 V13'''
    if(len(p) == 4):
        p[0] = p[1] + p[2] + p[3]
        print('Verset 12 correct')
    else:
        p[0] = p[1] + p[2] 

def p_V13(p):
    '''V13 : 7ARF FI3L DAMIR 7ARF FI3L 7ARF FI3L
           | V13 V14'''
    if(len(p) == 8):
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]
        print('Verset 13 correct')
    else:
        p[0] = p[1] + p[2] 

def p_V14(p):
    '''V14 : 7ARF 7ARF FI3L 7ARF 7ARF ISM FI3L
           | V14 V15'''
    if(len(p) == 8):
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]
        print('Verset 14 correct')
    else:
        p[0] = p[1] + p[2] 

def p_V15(p):
    '''V15 : 7ARF 7ARF 7ARF 7ARF FI3L 7ARF FI3L J
           | V15 V16'''
    if(len(p) == 9):
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8]
        print('Verset 15 correct')
    else:
        p[0] = p[1] + p[2] 

def p_V16(p):
    '''V16 : BADAL NA3T NA3T
           | V16 V17'''
    if(len(p) == 4):
        p[0] = p[1] + p[2] + p[3]
        print('Verset 16 correct')
    else:
        p[0] = p[1] + p[2] 

def p_V17(p):
    '''V17 : 7ARF 7ARF FI3L MAF3OULBIH DAMIR
           | V17 V18'''
    if(len(p) == 6):
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        print('Verset 17 correct')
    else:
        p[0] = p[1] + p[2] 

def p_V18(p):
    '''V18 : 7ARF FI3L MAF3OULBIH
           | V18 V19'''
    if(len(p) == 4):
        p[0] = p[1] + p[2] + p[3]
        print('Verset 18 correct')
    else:
        p[0] = p[1] + p[2] 

def p_V19(p):
    'V19 : 7ARF 7ARF FI3L DAMIR 7ARF FI3L 7ARF FI3L'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8]
    print('Verset 19 correct')

def p_C(p):
    '''C : T J 
         | T T J'''
    if(len(p) == 3):
        p[0] = p[1] + p[2]
    elif(len(p) == 4):
        p[0] = p[1] + p[2] + p[3]

def p_T(p):
    '''T : FI3L 
         | ISM'''
    p[0] = p[1]

def p_J(p):
    'J : 7ARF IsmMajror'
    p[0] = p[1] + p[2]

def p_error(p):
    print("Erreur de syntaxe")
    



#################################   PROGRAM   #################################
lexer = lex.lex()
parser = yacc.yacc()
while True:
    try:
        data = input('Entrez le(s) verset(s) : ')
        print("------------------------")
        if not data: continue
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok.type + ": " + tok.value)
        print("------------------------")
        result = parser.parse(data)
        if(result):
            print(result)
    except EOFError:
        break

