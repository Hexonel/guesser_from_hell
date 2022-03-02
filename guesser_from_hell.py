#! /usr/bin/env python3
# numberGuesser.py - The most advanced number guesser! Can it get upgraded? Probably.
import random, json
import functions as func

print(
"""###############################################################################################################

                                W  ・  E  ・  L  ・  C  ・  O  ・  M  ・  E

###############################################################################################################""")

info = './difficulties.json'    # relative paths just save everything in the same folder
data = './scores.json'          # otherwise use the absolute path
with open(info) as f:
    diff_dict = json.load(f)

users = {}                      # placeholder. Gets updated later
try:
    with open(data, 'r') as r:
        users = json.load(r)    # loads a file if it exists
except FileNotFoundError:
    pass
name = input("What is your name?: ")
if name in users:
    print(f"\nWelcome back, {name}!")
else:
    print("\nI see this is your first time playing this. Have fun, let's see how good you are at guessing!")
    users[name] = 0

difficulties = ["baby", "medium", "impossible"]
diff_input = func.choose_diff(difficulties)
while True:
    max_number = diff_dict[diff_input]["max"]
    number = random.randint(1, max_number)      # generates a number
    hints = func.create_hints(number, max_number, diff_input)   # and hints fitting wichever mode is chosen
    for i in range(len(hints)):
        prompt = func.valid_number(input(hints[i]), max_number)
        if prompt == number:
            const = 3 - i
            if i == 3:                  # want to reward that extra round in baby / medium mode
                const = 1
            print(diff_dict[diff_input]['messages'][str(i+1)])
            users[name] += diff_dict[diff_input]['point'] * const
            break           # this is it, if you've got it right
        diff_dict[diff_input]['minus']
        if diff_input == 'evil' or diff_input == 'satan':
            number = random.randint(1, max_number)
            hints = func.create_hints(number, max_number, diff_input)   # Because number changes each round, so do the hints
        if i == len(hints)-1:       # Reveal the answer ONLY when the person missed every chance.
            print(f"The number was {number}.")
    if users[name] >= 15:       # evil and satan modes are available only when your score is 15 or higher
        print("\nYou have gained a total of 15 Points. \nYou've UNLOCKED 'evil' and 'satan' modes!")
        difficulties = ["baby", "medium", "impossible", "evil", "satan"]
    else:
        difficulties = ["baby", "medium", "impossible"]
    print(f"\n ++++++++++ The current score is : {users[name]} ++++++++++") 
    func.retry(users, data)     # saves the whole 'user' dict
    diff_input = func.change_diff(difficulties, diff_input)
