t='i love how it was you'

from googletrans import Translator
tr = Translator()
def en2jpn(text):
    return tr.translate(text=text, src="en", dest="ja").text


print(en2jpn(t))