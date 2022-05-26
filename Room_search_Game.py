import os


rooms_data = [{'room_number': 1, 'items': [[12, "apple"], [32, "apple"]]},
              {'room_number': 2, 'items': [[13, 'banana'], [42, "apple"]]},
              {'room_number': 3, 'items': [[14, 'orange'], [52, "apple"]]},
              {'room_number': 4, 'items': [[15, 'mango'], [62, "apple"]]},
              {'room_number': 5, 'items': [[16, 'pineapple'], [72, "apple"]]},
              {'room_number': 6, 'items': [[17, 'berries'], [82, "apple"]]},
              {'room_number': 7, 'items': [[18, 'apricot'], [92, "apple"]]},
              {'room_number': 8, 'items': [[19, 'guava'], [102, "apple"]]},
              {'room_number': 9, 'items': [[20, 'dragon fruit'], [112, "apple"]]},
              {'room_number': 10, 'items': [[21, 'lemon'], [122, "apple"]]},
              {'room_number': 11, 'items': [[22, 'tomato'], [132, "apple"]]},
              {'room_number': 12, 'items': [[23, 'potato'], [142, "apple"]]}]
current_room = 1
items_picked = [(101, 1, ""), ]
rooms = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']


def display_map():
    global current_room
    global rooms
    rooms = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    rooms[current_room - 1] = rooms[current_room-1] + "*"
    print('\n\n' + rooms[0] + '\t' + rooms[1] + '\t' + rooms[2] + '\t' + rooms[3])
    print(rooms[4] + '\t' + rooms[5] + '\t' + rooms[6] + '\t' + rooms[7])
    print(rooms[8] + '\t' + rooms[9] + '\t' + rooms[10] + '\t' + rooms[11] + '\n\n')


def display_items():
    global current_room
    global rooms_data

    print("\nCurrent Room :\t{}\n".format(current_room))

    i = 1
    for ID, item in rooms_data[current_room-1]['items']:
        print(i, "\tID:  {}\t\tName:  {}".format(ID, item))
        i += 1


def multiple_rooms_search():
    found = False
    global items_picked

    item_found = []
    rooms_to_be_searched = input("Enter the address numbers of the rooms to be searched with a comma in between :\t").lstrip().rstrip()
    to_search = rooms_to_be_searched.split(',')
    rooms_to_be_searched = [my_room.lstrip().rstrip() for my_room in to_search]

    rooms_to_be_searched = [int(my_room) for my_room in rooms_to_be_searched]

    item_name = input("Enter the name of Item that you want to pick from these set of rooms,"
                      " please enter correct spellings"
                      ":\t").lstrip().rstrip()
    for room in rooms_to_be_searched:
        if room > 12 or room < 1:
            continue
        for ID, item in rooms_data[room - 1]['items']:

            if item == item_name:
                item_found.append([rooms_data[room-1]['room_number'], ID, item])
                found = True

    if found == False:
        print("Not Found")

    print("\n")
    i = 1
    for a, b, c in item_found:
        print(i, "\t\troom number : {}\t\titem ID : {}\t\tfound the  {}".format(a, b, c))
        i += 1


def move():
    global current_room

    set = ['N', 'S', 'E', 'W']
    direction = input("Enter the direction in which you want to move\n"
                      "Kindly select from the following\n"
                      "N\tS\tE\tW\n\t")
    direction = direction.upper().lstrip().rstrip()
    while direction not in set:
        os.system("cls")
        print("Invalid direction ! \n")
        direction = input("Enter the direction in which you want to move\n"
                          "Kindly select from the following\n"
                          "N\tS\tE\tW")
        direction = direction.upper().lstrip().rstrip()
    if direction == 'S':
        current_room = current_room + 4
    elif direction == 'N':
        current_room = current_room - 4
    elif direction == 'E':
        current_room += 1
    elif direction == 'W':
        current_room -= 1
    else:
        print("invalid processing occurred")

    if current_room <= 0:
        current_room = 12 + current_room
    elif current_room > 12:
        current_room = current_room - 12
    print()
    '''print("This room has following items\n\n")
    for i, item in enumerate(rooms_data[current_room - 1]['items']):
        print(i, ":\t", item)'''

    print()
    print()
    display_map()
    display_items()
    print('\n')
    display_menu()

    return


def pick_item():
    found = False
    global current_room
    global items_picked

    try:
        item_num = int(input("Enter the Item ID that you want to pick from current room:\t").lstrip().rstrip())
        i = 1
        for ID, item in rooms_data[current_room - 1]['items']:
            if ID == item_num:
                items_picked.append((ID, item))
                found = True
                return
            i += 1
        if found == False:
            print("Not Found")
    except:
        print("Please Enter a Digit/Number, Other Characters are not allowed")


def show_item():
    global current_room
    global items_picked
    print("\n\tYou currently have the following items in your Bag/List/Custody")
    for i, item in enumerate(items_picked):
        print("\t", i+1, ":\t\t", "ID : {}\t\tName : {}\t".format(item[0], item[1]))
    print("\n")


def drop_item():
    found = False
    global current_room
    global items_picked

    try:
        item_num = int(input("Enter the Item ID that you want to drop from your Bag/List/Custody:\t").lstrip().rstrip())
        i = 0
        for data in items_picked:
            if data[0] == item_num:
                a = items_picked.pop(i)
                found = True
                return
            i += 1
        if found == False:
            print("Not Found")
    except:
        print("Please Enter a Digit/Number, Other Characters are not allowed")


def display_menu():
    menu = ["1.\tEnter 1 to Move by directions\n",
            '2.\tEnter 2 to pick an item and enter the item id after you are prompted to do so\n',
            '3.\tEnter 3 to see the list of picked items\n',
            '4.\tEnter 4 to drop an item, Enter the item id after you are prompted to do so\n',
            '5.\tEnter 5 to search for an item in multiple rooms and enter the name of item '
            'after you are prompted to do so, with correct spellings\n']

    for i in menu:
        print(i)
    option = input("Enter the number of Operation you want to perform :\t ")
    option = int(option.lstrip().rstrip())

    if option == 1:
        move()
    elif option == 2:
        pick_item()
    elif option == 3:
        show_item()
    elif option == 4:
        drop_item()
    elif option == 5:
        multiple_rooms_search()
    else:
        print("Invalid Number Entered\n"
              "The Operation with this ID i.e. {} doesn't exist\n\n".format(option))
        display_menu()
going = True
while going:
    os.system('cls')
    display_map()
    display_menu()
    status = input("\n\n\tEnter Y if you want to continue/Play again\n\tEnter N if you want to exit\n\t")
    status = status.lstrip().rstrip().upper()
    status = status[0]
    if status == 'N':
        going = False
    print('\n\n\n\n\n')


