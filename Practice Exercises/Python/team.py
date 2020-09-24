roster = []
prompt1 = "Would you like to add a player to the list? (Yes/No) "
prompt2 = "Would you like to add another player? (Yes/No) "

# Validate a yes or no response from user
def yes_or_no(prompt):
    response = input(prompt)
    if response.lower() not in ["yes","no"]:
        print("You have entered an invalid response. Please select 'Yes' or 'No'.")
        print()
        yes_or_no(prompt)
    return response.lower()

# Print roster of players
def print_roster():
    print(f"There are {len(roster)} players on the team.")
    for idx, player in enumerate(roster):
            print(f"Player {idx+1}: {player}")

# Add player to roster and print roster
def add_name():
    player = input("Enter the name of the player to add to the team: ")
    roster.append(player)
    add_more = yes_or_no(prompt2)
    print()
    if add_more == "yes":
        add_name()
    else:
        print_roster()            
            
# Prompt user to add initial player to roster
def will_add():
    add_first = yes_or_no(prompt1)
    print()
    if add_first == "yes":
        add_name()
    else:
        print_roster()

# Print name of goalkeeper
def print_goalkeeper(idx):
    print(f"Great!!! The goalkeeper for the game will be {roster[int(idx)-1]}.")
        
# Validate goalkeeper selection
def validate_goalkeeper():
    try:
        idx = int(input(f"Please select the goal keeper by selecting the player number. (1-{len(roster)}) "))
    except ValueError:
        print(f"Please select a number between 1 and {len(roster)}, inclusive.")
        validate_goalkeeper()
    else:
        if not(idx in range(1,len(roster)+1)):
            print("Your selection does not match any player's number.")
            print()
            validate_goalkeeper()
        return idx    
        
# Prompt user to select a goalkeeper from roster
def goalkeeper():
    if bool(roster):
        goalkeeper = validate_goalkeeper()
        print_goalkeeper(goalkeeper)

will_add()
print()
goalkeeper()
