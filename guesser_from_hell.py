#! usr/local/env python3
# numberGuesser.py - The most advanced number guesser! Can it get upgraded? Probably.
import random, json
import functions as func

print(
"""###############################################################################################################

                                W  ・  E  ・  L  ・  C  ・  O  ・  M  ・  E

###############################################################################################################""")

info = './difficulties.json'
data = './scores.json'
with open(info) as f:
    diff_dict = json.load(f)

users = {}
try:
    with open(data, 'r') as r:
        users = json.load(r)
except FileNotFoundError:
    with open(data, 'w') as w:
        json.dump(users, w)
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
    number = random.randint(1, max_number)
    hints = func.create_hints(number, max_number, diff_input)
    for i in range(len(hints)):
        prompt = func.valid_number(input(hints[i]), max_number)
        if prompt == number:
            const = 3 - i
            if i == 3:
                const = 1
            print(diff_dict[diff_input]['messages'][str(i+1)])
            users[name] += diff_dict[diff_input]['point'] * const
            break
        diff_dict[diff_input]['minus']
        if diff_input == 'evil' or diff_input == 'satan':
            number = random.randint(1, max_number)
            hints = func.create_hints(number, max_number, diff_input)   # Because number changes each round
    if users[name] >= 15:
        print("\nYou have gained a total of 15 Points. \nYou've UNLOCKED 'evil' and 'satan' modes!")
        difficulties = ["baby", "medium", "impossible", "evil", "satan"]
    else:
        difficulties = ["baby", "medium", "impossible"]
    print(f"\n ++++++++++ The current score is : {users[name]} ++++++++++") 
    func.retry(users, data)
    diff_input = func.change_diff(difficulties, diff_input)