"""Some functions for guesser_from_hell."""
import sys, json


def create_hints(number, max, diff):
    if diff == 'satan':
        hints = [
            f"Why the fuck did you summon me... But sure, if you win, you'll get tons of points!"
            "\nTry your worst, I'll even give you a hint:\nI bet it's not bigger than {max} hahahaha: ", 
            "No más pistas para ti. Buena suerte jjjjjjjj: ", 
            "Saya bahkan tidak tahu apakah ini berarti apa-apa: "
        ]
    else:
        hints = []
        if diff == 'evil':
            hints.append(f"The number changes every round and you lose points if you're wrong!"
                        f"(Hint: Now it is between 1 and {max}):" )
        else:
            hints.append(f"\nTry to guess my number. (Hint: It is between 1 and {max}): ")
        if number > int(max/2):
            word = 'bigger'
        else:
            word = 'equal or smaller'
        hints.append(f"\nNope, try again. (Hint: It is {word} than {int(max/2)}): ")
        if number % 2 == 0:
            value = 'even'
        else:
            value = 'odd'
        hints.append(f"\nYou've got one last shot. (Hint: It is {value}!): ")
        if max != 30:
            hints.append("Bonus round, try not to waste it (You should be ashamed if you expected more hints...): ")
    return hints


def valid_number(value, max):
        while True:
            try:
                if value.lower() == "quit":
                    quit = input("Do you want to pussy out? (yes/no): ")
                    if quit == "yes":
                        print("Come try me again.")
                        sys.exit()
                elif int(value) > max or int(value) < 1:
                    value = input(f"The number is out of range. Try something between 1 and {max}: ")
                elif isinstance(int(value), int):
                    return int(value)
            except ValueError:
                value = input("\nType a number.\nAnd don't be a smartass and write numbers as words...."
                    f"\nPick something between 1 and {max}, or else you'll need to scroll up for the hints lol: ")


def choose_diff(diff_list):
    while True:
        prompt = input(f"Choose a difficulty ({' / '.join(diff_list)}): ").lower()
        if prompt not in diff_list:
            print('\nThat is not a valid difficulty.')
        else:
            return prompt


def change_diff(diff_list, same):
    diff_list.remove(same)
    prompt = input(f"\nWould you like to change difficulty? ({' / '.join(diff_list)}): ")
    while True:
        if prompt in diff_list:
            break
        elif prompt == "no":
            prompt = same
            break
        prompt = input("\nChoose a valid mode, or don't change the difficulty."
                    f"\nSo, would you like to change it? ({' / '.join(diff_list)}): ")
    return prompt
        

def retry(data, file):
    retry = input("\nDo you want to continue? (yes/no): ").lower()
    while True:
        if retry == "yes":
            return None
        elif retry == "no":
            print("\n\nWhatever.")
            with open(file, 'w') as f:
                json.dump(data, f)
            sys.exit()
        retry = input("\nIt is a simple yes or no question for fuck's sake."
                      "Do you want to keep having fun? (yes/no): ")
