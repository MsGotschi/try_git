initial = input("what is your first  INITIAL?")
last_initial = input("what is the first INITIAL of your last name? ")
month = input("what month is your birthday? jan/ef/mar/apr/may/jun/jul etc")

alpha1="abcdefg"
alpha2="hijklmn"
alpha3="opqrst"
alpha4="uvwxyz"

if initial in alpha1:
    elf1 = "Merry"
elif initial in alpha2:
    elf1 = "Happy"
elif initial in alpha3:
    elf1 = "Bubbly"
else:
    elf1="Sparkly"

if last_initial in alpha1:
    elf2 = "Jingle"
elif last_initial  in alpha2:
    elf2 = "Jangle"
elif last_initial  in alpha3:
    elf2 = "Tingle"
else:
    elf2="Spangle"

if month=="jan" or month=="feb" or month=="mar":
    elf3 = "Buttons"
elif month=="apr" or month=="may" or month=="jun":
    elf3 = "Bells"
elif month=="jul" or month=="aug" or month=="sep":
    elf3 = "Bubbles"
else:
    elf3="Baubles"

print("your elf name is: ", elf1, " ", elf2, " ", elf3)




    
