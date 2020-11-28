s_c = 0 
try: 
    contenido = clipboard.get_selection()
    for c,i in enumerate(contenido):
        if i == ' ':
            s_c += 1
        else:
            break
except:
    contenido = ''

if contenido == ' '*s_c or contenido == '':
    text = ' '*s_c+'#'*(72-s_c)
else:
    s_l = 72 - len(contenido) - 6 
    text = ' '*s_c + '#'*(s_l//2) + '   ' + contenido[s_c:] + '   ' + '#'*(s_l//2) + '#'*(s_l%2)
 
text = '#'*72 
keyboard.send_keys(text)

