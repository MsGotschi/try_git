initial=input("what is your first INITIAL?")
last_initial=input("what is the first INITIALof your last name? ")
month = input("what month is your birthday? jan/feb/mar/apr/may/jun/jul/aug/sep/oct/nov/dec")

alpha1="abcdefg"
alpha2="hijklmn"
alpha3="opqrst"
alpha4="uvwxyz"

if initial in alpha1:
    elf1= 'Merry'
elif initial in alpha2:
    elf1= 'mcjingles'
elif initial in alpha3:
    elf1= 'Snowy'
else:
    elf1='Bubbly'

if last_initial in alpha1:
    elf2= 'Jolly'
elif last_initial in alpha2:
    elf2= 'Tinsel'
elif last_initial in alpha3:
    elf2= 'Holly'
else:
    elf2='Robyn'

if month=="jan" or month=="feb" or month=="mar":
    elf3=" angel"
elif month=="apr" or month=="may" or month=="jun":
    elf3=" cup cake"
elif month=="jul" or month=="aug" or month=="sep":
    elf3=" cup cake"
else:
    elf3="tree"
print(elf1,elf2,elf3)
