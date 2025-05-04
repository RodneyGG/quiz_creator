#Make a Program that calls quiz taker and quiz creator in just one file
#Import quiz creator and quiz taker
import quiz_taker
import quiz_creator
import pyfiglet
import os

def welcome_text():
    ascii_banner = pyfiglet.figlet_format("Quiz Forge", font="doom")
    print(ascii_banner)

#make a choice if it want to make or take a quiz
main_quiz_program = True

while main_quiz_program:
    os.system('cls')
    welcome_text()
       
    choice = input("Please Type The Number\n1 = Quiz Creator\n2 = Quiz Taker\n3 = Exit\n").strip()
    if choice == "1":
        quiz_creator.main()
    elif choice == "2":
        quiz_taker.main()
    elif choice == "3":#quit the program
        main_quiz_program = False
    else:
        print("PLEASE ONLY ENTER 1,2,3. Thank YOU")

