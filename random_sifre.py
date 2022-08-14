from random import choice  # choice seçim demek

chars = "abcdefghijklmnopqrstuvwxyz._"  # chars karakter demek

length = int(input("Kaç karakterli şifre istediğinizi girin: "))  # length uzunluk demek

password = ""

while len(password) != length:
    c = choice(chars)
    if c not in password:
        password += c
    if len(password) == 28:
        break

print(password)

