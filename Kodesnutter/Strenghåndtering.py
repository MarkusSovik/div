def check_equal(str1, str2):
    if str1 == str2:
        return True
    else:
        return False

print("I dette programmet skal vi sjekke om to tekster er like. Output blir True om de er lik")
Streng1=input("Skriv inn det du vil ha i tekst1")
Streng2=input("Skriv inn det du vil ha i tekst2")
print(check_equal(Streng1,Streng2))

def reversed_word(str):
    tekstBaklengs=("")
    for bokstaver in range(len(str)-1,-1,-1):
        tekstBaklengs+=str[bokstaver]
    return tekstBaklengs
print("Dette programmet printer teksten din baklengs")
print(reversed_word(input("Skriv inn teksten du vil se baklengs")))

def check_palindrome(str):
    if str==reversed_word(str):
        return True
print("Dette programmet sjekker om teksten din er et palindrom")
print(check_palindrome(input("Skriv inn palindromet, for å sjekke om det er et ekte palindrom")))

def contains_string(str1,str2):
    i=0
    if str2 in str1:
        a=str2[0]
        for ledd in str1:
            if ledd == a:
                if str1[i:i+len(str2)]==str1:
                    return i
    else:
        return -1
en=input("Tekst1")
to=input("Tekst2")
print("Programmet sjekker om tekst nr 2 er i tekst nr 1 og skriver ut hvilken plassering den har")
print(contains_string(en,to))