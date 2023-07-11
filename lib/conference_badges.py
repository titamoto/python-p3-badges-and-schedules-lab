def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    names_list = []
    # for name in names:
    #     names_list.append(f"Hello, my name is {name}.")
    [names_list.append(f"Hello, my name is {name}.") for name in names]
    return names_list

def assign_rooms(names):
    greet_list = []
    num = 1
    while num < 9:
        greet_list.append(f"Hello, {names[num-1]}! You'll be assigned to room {num}!")
        num += 1
    return greet_list

def printer(names):
    [print(badge) for badge in batch_badge_creator(names)]
    [print(assignment) for assignment in assign_rooms(names)]
