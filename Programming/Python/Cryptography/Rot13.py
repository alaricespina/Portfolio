#In python 3 string maketrans which required importing is now str.maketrans
rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')

raw = "Hatdog"
print("Raw Text: " + raw)
encrypted = raw.translate(rot13trans)

print("Encrypted Text: " + encrypted)