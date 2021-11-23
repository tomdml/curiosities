import random

#All output
def draw_game(inc, guesses, word):
	#Clear terminal
	print('\n'*100)

	#Draw the hangman - Using template.format(outputs[incorrect])
	print('      +---+\n      {}   |\n      {}   |\n     {}{}{}  |\n     {} {}  |\n          |\n    ========='.format(*['       ', '|      ', '|O     ', '|O |   ', '|O/|   ', '|O/|\\  ', '|O/|\\/ ', '|O/|\\/\\'][inc]))

	#Print the guessed letters and the remaining letters in the word - ['*', c][c in guesses] returns * or the character
	print(*set(guesses), '\n', *[('*', c)[c in guesses] for c in word],sep='')

#Pull a random word from the provided wordlist
word = random.choice(open('words.txt').read().splitlines())

guesses, inc = [], 0

#Game loop
while 1:

	#Output to screen (incorrect, list of guesses, word as str)
	draw_game(inc, guesses, word)	

	#If 6 incorrect guesses, lose game
	if inc >= 7: print('you lose'); break

	#Else if all guessed letters are in the word, win game
	if set(guesses) >= set(word): print('congratulations you win'); break

	#Else append guess to guess list
	guesses.append(input('Please enter your next guess:')[0])

	#Increment incorrect counter by 1 if guess not in word
	inc += (1,0)[guesses[-1] in word]