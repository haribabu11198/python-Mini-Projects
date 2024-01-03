from translate import Translator
name=input('enter name:')
class languages():
    def tamil(self):
        translator= Translator(to_lang="tamil")
        translation = translator.translate(name)
        print (translation)
    def telugu(self):
        translator= Translator(to_lang="telugu")
        translation = translator.translate(name)
        print (translation)
    def german(self):
        translator= Translator(to_lang="german")
        translation = translator.translate(name)
        print (translation)
    def hindi(self):
        translator= Translator(to_lang="hindi")
        translation = translator.translate(name)
        print (translation)
    def malayalam(self):
        translator= Translator(to_lang="malayalam")
        translation = translator.translate(name)
        print (translation)
    def kannada(self):
        translator= Translator(to_lang="kannada")
        translation = translator.translate(name)
        print (translation)
    def gujarati(self):
        translator= Translator(to_lang="gujarati")
        translation = translator.translate(name)
        print (translation)
    def french(self):
        translator= Translator(to_lang="french")
        translation = translator.translate(name)
        print (translation)
    def hawaiian(self):
        translator= Translator(to_lang="hawaiian")
        translation = translator.translate(name)
        print (translation)
    
l = languages()
print('------MENU------\n1)tamil\n2)telugu\n3)german\n4)hindi\n5)malayalam\n6)kannada\n7)gujarati\n8)french\n9)hawaii')
while 1:
    choice = int(input('Enter the choice:'))
    if choice == 1:
        l.tamil()
    elif choice == 2:
        l.telugu()
    elif choice==3:
        l.german()
    elif choice==4:
        l.hindi()
    elif choice==5:
        l.malayalam()
    elif choice == 6:
        l.kannada()
    elif choice == 7:
        l.gujarati()
    elif choice == 8:
        l.french()
    else:
        l.hawaiian()
