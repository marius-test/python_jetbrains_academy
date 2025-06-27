import string
from random import choice

# Fill up the variables
wordlist = ['python', 'java', 'kotlin', 'javascript']
chosen_word = choice(wordlist)
guessed_letters = set()
tries = 8
message = 'You lost!'

# Create the result list to make dashes and track user progression
result_list = []
i = 0
for x in chosen_word:
    result_list.append('-')

# Start the game
print('H A N G M A N\n')

play = False
while not play:
    action = input('Type "play" to play the game, "exit" to quit')
    if action == 'exit':
        quit()
    if action == 'play':
        play = True

print()
while tries > 0:
    print('\n' + ''.join(result_list))

    # Check for a winner
    if chosen_word == ''.join(result_list):
        message = f'You guessed the word!\nYou survived!'
        break

    letter = input(f'Input a letter: ')

    # Check for input errors
    if len(letter) != 1:
        print('You should input a single letter')
        continue
    if letter not in string.ascii_lowercase:
        print('Please enter a lowercase English letter')
        continue
    if letter in guessed_letters:
        print('You\'ve already guessed this letter')
        continue

    # Play the round
    guessed_letters.add(letter)
    if letter in chosen_word:
        index = 0
        for x in chosen_word:
            if letter == chosen_word[index]:
                result_list[index] = letter
            index += 1
    else:
        print('That letter doesn\'t appear in the word')
        tries -= 1

# End the game and display results
print(message)
