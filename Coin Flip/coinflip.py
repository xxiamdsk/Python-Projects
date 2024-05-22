import random
import os


def toss_coin():
    list1 = ["heads", "tails"]
    return random.choice(list1)


def main():
    while True:
        flag = False  # Declaring a variable which will be used afterwards to break out of 2 nested while loops
        # at the same time
        # Clears the shell/terminal (where all the text is)
        os.system("cls")

        answer = input("Pick a side for the coin toss (heads/tails): ")

        # Input validation
        if answer.lower() not in ["heads", "tails"]:
            # removed the print statement here because its not required since the while loop clears
            # the statement anyways
            continue

        result = toss_coin()

        print(f"You got... {result}")

        if answer.lower() == result:
            print("Nice, you won the coin toss!!")
        else:
            print("OOF. Better luck next time.")

        # Ask the user if they want to play again
        while True:
            answer_y = input("Wanna play again? (yes/no): ")
            if answer_y.lower() == "no":
                flag = True
                break
            elif answer_y.lower() == "yes":
                break  # if answer_y is "yes" then break out of only the innermost while loop and start the game again
            else:
                continue

        if flag:  # Checking if the flag variable is True
            break


if __name__ == "__main__":
    main()


