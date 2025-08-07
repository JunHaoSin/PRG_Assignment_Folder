
#Main Menu Function#
def Main_Menu():
    print("--- Main Menu ----\n"
          "(N)ew game\n"
          "(L)oad saved game\n"
          "(Q)uit"
          "------------------")
    Choice=str(input("Your choice? ")).upper()

    if Choice == "N":
        Name=str(input("Greetings, miner! What is your name? "))
        print(f"Pleased to meet, {Name}. Welcome to Sundrop Town!")

        return Name
    
    if Choice == "L":
        print("WIP")

    if Choice == "Q":
        print("WIP")

#Game#

Day=0

First_Time = True

while True:
    if First_Time == True:
        print('---------------- Welcome to Sundrop Caves! ----------------')
        print('You spent all your money to get the deed to a mine, a small\n'
              'backpack, a simple pickaxe and a magical portal stone.\n'
              '\n'
              'How quickly can you get the 500 GP you need to retire\n'
              'and live happily ever after? ')
        print("-----------------------------------------------------------")
        First_Time = True



    if First_Time == False:
        print("WIP")