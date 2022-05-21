#! /usr/bin/env python3
# numberGuesser.py - The most advanced number guesser! Can it get upgraded? Probably.
import random, json
import functions as func

print("""###############################################################################################################

                                W  ・  E  ・  L  ・  C  ・  O  ・  M  ・  E

###############################################################################################################
    """)

info = 'difficulty_info.json'    # relative paths just save everything in the same folder
saved = 'scores.json'          # otherwise use the absolute path
with open(info) as f:
    diff_dict = json.load(f)

mode = ''
data = {}                      # placeholder. Gets updated later
try:
    with open(saved, 'r') as r:
        data = json.load(r)    # loads a file if it exists
except FileNotFoundError:
    pass
name = input("What is your name?: ")
if name in data:
    print(f"\nWelcome back, {name.title()}!"
            f"\nLet's continue where you left off. Your current score is * {data[name]} *!")
else:
    print("\nI see this is your first time playing this.\nHave fun, let's see how good you are at guessing!")
    data[name] = 0

while True:
    mode = func.choose_diffs(mode, name, saved, data)
    max_num = diff_dict[mode]['max']
    number = random.randint(1, diff_dict[mode]['max'])
    hints = func.create_hints(number, max_num, mode)   # and hints fitting wichever mode is chosen

    for i in range(len(hints)):
        points = func.guess_points(mode, i, number, hints, saved, data)
        data[name] += points
        if points > 0:
            print(diff_dict[mode]['msg'][str(i)])
            break
        elif mode == 'evil' or mode == 'satan':
            number = random.randint(1, max_num)
            hints = func.create_hints(number, max_num, mode)   # Because number changes each round, so do the hints
        elif i == len(hints)-1:               # Reveal the answer ONLY when the person missed every chance.
            print(f"You missed your shots.\nThe number was {number}!")
    if data[name] >= 15 and data[name] - points < 15:
        print("\nYou have gained more than 15 Points. You've unlocked 'evil' and 'satan' modes!")
        difficulties = ["baby", "medium", "impossible", "evil", "satan"]
    print(f"\n +++++++++++++++ The current score is : {data[name]} +++++++++++++++") 
    func.retry(input("\nDo you want to try again? (yes/no): "), saved, data)