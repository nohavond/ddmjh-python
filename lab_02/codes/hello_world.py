
# základní hello world
# tím začneme
def hello():
    print("Hello world")



# složitější fce 
def age():
    print('Jak se jmenuješ?')
    name = input()
    age = int(input('Kolik ti je let?')) # fuce input má možnost rovnou vypsat text
    print('Je ti:', age)


# čtení textu
print('Napiš text:', end=' ')
text = input()
print("Tvůj text:", text, end='\n\n')


# čtení čísla
num = int(input('Napiš číslo: ')) # lze text vložit přimo do input
print("Tvoje číslo:", num)

