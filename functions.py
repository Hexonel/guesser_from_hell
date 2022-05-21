import sys, json

"""All the functions used in n_g"""
with open('difficulty_info.json') as f:
    diff_dict = json.load(f)


def show_scores(data):
    """Show the high scores."""
    sort_scores = sorted(data.items(), key=lambda x: x[1], reverse=True)
    message = '\n\n\t\t===== The guessing hall of fame: =====\n'
    for i in sort_scores:
        message += (f"\t\t\t{i[0].title()}: {i[1]} points\n")
    print(message)


def quit_sequence(file, data):
    """Checks if you want to quit"""

    quit = input("Done already? (yes/no): ")
    if quit.lower() == 'yes':
        print("\n\n\tWhatever.")
        with open(file, 'w') as f:      # write mode, so the file is empty
            json.dump(data, f)  
        sys.exit()
    else:
        return None


def delete_user(file, data, user):
    """Deletes a user and kicks you out of the game."""
    prompt = input("Do you want to delete your username? (yes/no): ")
    try:
        if prompt.lower() == 'yes':
            del (data[user])
            print(f"The user {user.title()} has successfully been removed!"
                    "\n\tSee you again!")
            with open(file, 'w') as f:
                json.dump(data, f)  
            sys.exit()
        elif prompt.lower() == 'no':
            return None
    except ValueError:
        prompt = input("Answer with yes or no.\n Would you like to delete your current username?: (yes/no): ")



def valid_number(value, max_num, file, data):
    """Checks if your input is a number, 'quit', or something else."""

    while True:
        try:
            if value.lower() == "quit":
                quit_sequence(file, data)
            elif int(value) > max_num or int(value) < 1:
                value = input(f"The number is out of range. Try something between 1 and {max_num}: ")
            elif isinstance(int(value), int):
                return int(value)
        except ValueError:
            value = input(f"\nType a number.\nAnd don't be a smartass and write numbers as words....\n"
            "Pick something between 1 and {maxNum}: ")


def choose_diffs(mode, name, file, data):
    """Checks whether to change difficulties."""

    if data[name] >= 15:
        difficulties = ["baby", "medium", "impossible", "evil", "satan"]
    else:
        if mode == 'evil' or mode == 'satan':
            mode = ''
        difficulties = ["baby", "medium", "impossible"]

    print("\nType 'quit' anytime to quit.\nType 'score' to see the scoreboard.\nType 'delete' to delete your current username.\n")

    if mode:
        difficulties.remove(mode)
        choice = input(f"Would you like to change difficulty? ({' / '.join(difficulties)}): ")
        while True:
            if choice.lower() == 'score':
                show_scores(data)
                choice = input(f"Would you like to change difficulty? ({' / '.join(difficulties)}): ")
            elif choice in difficulties:
                return choice
            elif choice.lower() == 'delete':
                delete_user(file, data, name)
                choice = input(f"Would you like to change difficulty? ({' / '.join(difficulties)}): ")
            elif choice.lower() == "no":
                return mode
            elif choice.lower() == 'quit':
                quit_sequence(file, data)
                choice = input(f"Would you like to change difficulty? ({' / '.join(difficulties)}): ")
            else:
                choice = input("\nChoose a valid mode, or don't change the difficulty.\n"
                                f"So, would you like to change it? ({' / '.join(difficulties)}): ")
    else:
        while True:
            first_choice = input(f"Choose a difficulty ({' / '.join(difficulties)}): ")
            if first_choice in difficulties:
                return first_choice
            elif first_choice.lower() == 'score':
                show_scores(data)
            elif first_choice.lower() == 'delete':
                delete_user(file, data, name)
                first_choice = input(f"Would you like to change difficulty? ({' / '.join(difficulties)}): ")
            elif first_choice.lower() == 'quit':
                quit_sequence(file, data)
    

def create_hints(number, max, mode):
    if mode == 'satan':     # satan is a special snowflake
        hints = [
            f"Why the fuck did you summon me... But sure, if you win, you'll get tons of points!"
            f"\nTry your worst, I'll even give you a hint:\nSomething tells me it's not bigger than {max}: ", 
            "No más pistas para ti. Buena suerte jjjjjjjj: ", 
            "Saya bahkan tidak tahu apakah ini berarti apa-apa: "
        ]
    else:
        hints = []      # a list of hints, depending on the number and the mode
        if mode == 'evil':
            hints.append(f"The number changes every round and you lose points if you're wrong!"
                        f"(Hint: Now it is between 1 and {max}):" )
        else:
            hints.append(f"\nTry to guess my number. (Hint: It is between 1 and {max}): ")
        if number > int(max/2):
            word = 'bigger'
        else:
            word = 'equal to or smaller'
        hints.append(f"\nNope, try again. (Hint: It is {word} than {int(max/2)}): ")
        if number % 2 == 0:
            value = 'even'
        else:
            value = 'odd'
        hints.append(f"\nYou've got one last shot. (Hint: It is {value}!): ")
    return hints


def guess_points(mode, index, number, hints, file, data):
    """Checks if your guess matches the number, and gives points accordingly."""

    guess = valid_number(input(hints[index]), diff_dict[mode]['max'], file, data)
    if guess == number:
        return diff_dict[mode]['points'] * (3-index)
    elif mode == 'evil' or mode == 'satan':
        return diff_dict[mode]['minus']
    else:
        return 0


def retry(choice, file, data):
    """Ask a player if they want to try again."""

    while True:
        try:
            if choice == "yes":
                return None
            elif choice.lower() == "no":
                quit_sequence(file, data)
        except ValueError:
            continue
        choice = input("\nIt's a simple yes or no question for fuck's sake.\n"
                    "Do you want to keep having fun? (yes/no): ")