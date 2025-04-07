"""
For Assignment 9: Quiz Creator
Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and 
the correct answer. Write the collected data to a text file. Ask another question until the user chose 
to exit.
"""

def ask_quit():
    while True:
        ask_user = input("Do you want to exit the program?\nType Only The Number\
            \n1. Add More Question\n0.Exit").strip()
        if ask_user == "1":
            return True
        elif ask_user == "0":
            return False
        else:
            print("Invalid Input")


#Ask the user what subject or topic the question will he or she be making
topic = input("Enter the Subject or the Topic of the question: ").strip().lower()

#Make a filename named "{Topic or subject}_questions.txt" to store the question and make it in snake case
filename = f"{topic}_questions.txt"

#Initailize quiz maker to true to run the program if its false the loop break
quiz_maker = True

while quiz_maker:
    #Ask the user to input a question
    question = input("\nEnter your question: ")
    
    #input choices for A, B, C, D
    choice_a = input("Enter choice A: ")
    choice_b = input("Enter choice B: ")
    choice_c = input("Enter choice C: ")
    choice_d = input("Enter choice D: ")
    
    #select what is the correct answer
    correct = ""
    while correct not in ['a', 'b', 'c', 'd']:
        correct = input("Which is the correct answer? (a/b/c/d): ").lower()
        if correct not in ['a', 'b', 'c', 'd']:
            print("Invalid choice, please select a, b, c, or d")
    
    #All of the input of the user will be stored in a text file created
    with open(filename, "a") as file:
        file.write(f"Question: {question}\n")
        file.write(f"  a) {choice_a}\n")
        file.write(f"  b) {choice_b}\n")
        file.write(f"  c) {choice_c}\n")
        file.write(f"  d) {choice_d}\n")
        file.write(f"Answer: {correct}\n")
    
    #ask the user again to input a question or quit the program
    quiz_maker = ask_quit()
