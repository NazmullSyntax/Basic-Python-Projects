import random

words = ['python', 'programming', 'computer', 'algorithm']
word = random.choice(words)
guessed = ['_'] * len(word)
attempts = 6

while attempts > 0 and '_' in guessed:
    print(' '.join(guessed))
    guess = input("Guess a letter: ").lower()
    
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"Wrong! {attempts} attempts left")

if '_' not in guessed:
    print(f"You won! The word was {word}")
else:
    print(f"You lost! The word was {word}")