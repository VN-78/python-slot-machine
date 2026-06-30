MAX_LINES = 3


def deposit():
    while True:
        amount = input("what would u like to deposit ? $")
        # verify weather the nuumber is actually an number 
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("the amount should be greater than 0 !!")
        else:
            print("please enter an valid number")
    # print("check",amount)
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would u bet on ? (1-"+ str(MAX_LINES) +")")
        # verify weather the nuumber is actually an number 
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("the lines should be between the limit !!")
        else:
            print("please enter an valid number")
    # print("check",amount)
    return lines

def main():
    print("slot-machine!")
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)
    
    
if __name__ == "__main__":
    main()

