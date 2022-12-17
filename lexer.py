import ply.lex as lex
from pyarabic import *

tokens = ['FI3L', '7ARF', 'IsmMajror', 'moudafIlayh','IsmMawsol','MAF3OULBIH','MOUBTADAA','KHABAR']

t_ignore = ' \t'
t_FI3L=u'اقْرَأْ|خَلَقَ|عَلَّمَ|يَعْلَمْ'
t_7ARF=u'بِ|وَ|لَمْ|مِنْ'
t_IsmMajror=u'اسْمِ|عَلَقٍ|الْقَلَمِ'
t_moudafIlayh=u'رَبِّكَ'
t_IsmMawsol=u'الَّذِي|مَا'
t_MAF3OULBIH=u'الإِنسَانَ'
t_MOUBTADAA=u'رَبُّكَ'
t_KHABAR=u'الأَكْرَمُ'
# t_lettre=u'[بتثجحخادذرزسأشصضطظعغفقكلمنهـوي]'

def t_error(t):
    print("Caractère incorrect '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = input('entrez')
lexer.input(data)

#change lextoken
while 1:
    tok = lexer.token()
    if not tok:
        break
    print(tok)