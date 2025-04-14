# Python quiz game

def ask_question():
    while True:
        try:
            print('')
            print('------------------------------------------------------------------------------')
            print(f'{questions[question_number]:^78}') # current question
            print('------------------------------------------------------------------------------')
            print(f'1: {options[question_number][0]}')
            print(f'2: {options[question_number][1]}')
            print(f'3: {options[question_number][2]}')
            print(f'4: {options[question_number][3]}')
            print('------------------------------------------------------------------------------')
            
            answer = int(input('Please enter your answer: '))
            
            if answer > 4 or answer < 1: # if 1,2,3,4 not entered was
                print('That is not an answer. Please enter either 1,2,3,4.')
                continue

            elif not answer == correct_option[question_number]: # wrong answer
                guesses.append(answer)
                break
        
            else: # correct answer
                guesses.append(answer)
                break

        except ValueError: # if 1,2,3,4 was not entered
            print('That is not an answer. Please enter either 1,2,3,4.')
            continue

questions = ('What is the capital city of France?',
             'How many legs does a spider have?',
             'What planet is known as the Red Planet?',
             'Who wrote the play Romeo and Juliet?',
             'What is the freezing point of water in degrees Celsius')

options = (('Paris','Madrid','Moscow','London'),
           ('2','4','6','8'),
           ('Jupiter','Mars','Venus','Mercury'),
           ('Charles Dickens','Jane Austen','William Shakespeare','J.K. Rowling'),
           ('0°C','32°C','10°C','-10°C'))

correct_option = (1,
                  4,
                  2,
                  3,
                  1)

question_number = 0

num_of_questions = len(questions)

guesses = []

score = 0

# Title
print('------------------------------------------------------------------------------')
print(f'{'Quiz Game':^78}')
print('------------------------------------------------------------------------------')

# Questions Output
for x in range(num_of_questions):
    ask_question()
    question_number += 1

# Comparing how many answers are correct
score = sum([1 for i in range(num_of_questions) if guesses[i] == correct_option[i]])

# Final Output
print('')
print('------------------------------------------------------------------------------')
print(f'{f'You got {score} out of {num_of_questions} Questions correct!':^78}')
print('------------------------------------------------------------------------------')
print('')
input('Press the Enter Key to Exit...')