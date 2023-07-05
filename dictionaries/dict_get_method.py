player_dict = {"Ankit":100,"Naresh":89,"Rahul":90,"Murali":75,"Subodh":1}

print(f"Players name in the match: {player_dict.keys()}")

print("Enter player name to search: ")
player_name = input()

runs = player_dict.get(player_name,-1)

if runs != -1:
    print(f"{player_name} has scored {runs}")
else:
    print("Player not found.")