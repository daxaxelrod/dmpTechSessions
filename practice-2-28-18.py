def turn_on_tv(channel_number):
    frequency = channel_number**2
    if frequency > 20000:
        print("i can't print that it's too high")
    else:
        print("turning on the tv to channel {}".format(channel_number))
    return frequency

# my_frequency = turn_on_tv(2)

user_channel = int(raw_input("What channel do you want? "))

my_frequency = turn_on_tv(user_channel)
