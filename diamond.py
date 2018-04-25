def diamond_printer(number):
    if number % 2 == 0:
        even = True
    else:
        even = False



    if even:
        print("BRB ill do this later")
    elif not even:
        line_length = number
        midpoint = int(number/2-.5)
        for i in range(number):
            if i == 0 or i == number-1:
                #for the first and the last lines
                spaces = " "* (midpoint)
                print(spaces, "*", spaces)
            else:
                # everything else
                spaces = midpoint - i
                if spaces < 0:
                    spaces = abs(spaces)
                x = line_length-3-(2*spaces)
                print(spaces * " ", "*",
                        x * " ", "*", spaces * " ")
