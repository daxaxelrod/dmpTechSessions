list_name = raw_input("what do you want to name the list ")

my_list = []

while True:
    user_input = raw_input("what do you want to add to the list ")
    if user_input =="quit" or user_input == "q":
        print("sorry to see you go :(")
        break
    if user_input == "show":
        item_counter = 1
        print("_________________{}___________________".format(list_name))
        for food in my_list:
            print("{}) {}".format(item_counter, food))
            item_counter += 1
            # or do work here
        print("______________________________________")


    my_list.append(user_input)
