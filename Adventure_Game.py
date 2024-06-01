#Task 1

place = input("Choose a place (forest/cave): ")

if place == "forest":
    action = input("Choose an action (climb a tree/cross a river): ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":


#Task 2

    action = input("Choose an action (light a torch/proceed in the dark): ")
    if action == "light a torch":
        print("You can see your way!")
    else:
        print("You'll have to feel your way through!")


#Task 3

elif place != "forest/cave":
    pass