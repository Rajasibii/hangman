import random
from hangman_words import words
from hangman_art import stages

a = random.choice(words)
print(a)
underscore = []
for i in a:
    underscore += "_"
print(underscore)
b = 0
TRUE =True
while TRUE != False:
    guess = input("enter the letter: ").lower()
    for j in range(0,len(a)):
        if guess == a[j]:
            if guess in underscore:
                print(f"sorry, you already entered the character {guess}")
                break
            underscore[j] = a[j]
            print(underscore)
    if guess not in a:
        print(stages[6-b])
        print(f"{''.join(underscore)}")
        if stages[6-b] == stages[0]:
            print("sorry,you loose better luck next time!!!")
            break
        b+=1
    if "_"not in underscore:
        print("you win")
        break
print(f"{''.join(underscore)}")
