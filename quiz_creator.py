"""
For Assignment 9: Quiz Creator
Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and 
the correct answer. Write the collected data to a text file. Ask another question until the user chose 
to exit.
"""
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyfiglet
import time

def display_welcome():
    welcome_text = pyfiglet.figlet_format("Welcome to Quiz Maker!")
    print(welcome_text)
    
#check for duplicate questions
def is_question_duplicate(filename, question):
    with open(filename, "r") as file:
        contents = file.read()
        return f"Question: {question}" in contents


#view the questions
def view_questions(filename):
    with open(filename, "r") as file:
        print(f"These are the question inside {filename}")
        print(file.read())

#ask the user to quit
def ask_quit(filename):
    while True:
        ask_user = input("Do you want to exit the program?\nType Only The Number\
            \n1.Add More Question\n2.View the Question\n3.Send question to email\n0.Exit\n").strip()
        if ask_user == "1":
            return True
        elif ask_user == "2":
            view_questions(filename)
        elif ask_user == "3":
            send_email(filename)
        elif ask_user == "0":
            return False
        else:
            print("Invalid Input\n")

#select or create a new file         
def select_file():
    while True:
        choice = input("Do you want to:\n1. Open an existing file\n2. Create a new file\nEnter 1 or 2: ").strip()
        if choice == "1":
            filename = input("Enter the filename to open (e.g., topic_questions.txt): ").strip()
            if os.path.exists(filename):
                return filename  
            else:
                print(f"The file {filename} doesn't exist. Please try again.\n")
        elif choice == "2":
            #Ask the user what subject or topic the question will he or she be making
            topic = input("Enter the Subject or Topic of the question: ").strip().lower()
            filename = f"{topic}_questions.txt"
            #check if filename is already exists
            while True:
                try:
                    open(filename, "x")
                    break
                except FileExistsError:
                    print(f"The file '{filename}' already exists.\n")
                    new_filename = input("Please enter a new filename: ").strip()
                    filename = new_filename + "_questions.txt"
            return filename  
        else:
            print("Invalid choice, please enter 1 or 2 only.\n")
            
def send_email(filename):
    sender_email = "quizmakeroop@gmail.com"
    password = "toae vefn frlq balq"  
    receiver_email = input("Enter the recipient's email address: ").strip()

    #thankyou stackoverflow
    #read the content of the file
    with open(filename, "r") as file:
        quiz_content = file.read()

    # Get current time as a formatted string
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    
    #Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"Quiz Maker: {filename} is sent on {current_time}"

    #questions and answer will be printed in the mail
    body = f"Here are the questions from your quiz program:\n\n{quiz_content}"
    message.attach(MIMEText(body, "plain"))

    #connect to the gmail SMTP server and send the email 
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!\n")
    except Exception as email_error:
        print(f"Error: {email_error}")

#display welcome text
display_welcome()

#Make a filename named "{Topic or subject}_questions.txt" to store the question and make it in snake case
filename = select_file()

#Initailize quiz maker to true to run the program if its false the loop break
quiz_maker = True

while quiz_maker:
    #Ask the user to input a question
    question = input("\nEnter your question: ").strip()
    
    #input choices for A, B, C, D
    choice_a = input("Enter choice A: ").strip()
    choice_b = input("Enter choice B: ").strip()
    choice_c = input("Enter choice C: ").strip()
    choice_d = input("Enter choice D: ").strip()
    
    #select what is the correct answer
    correct = ""
    while correct not in ['a', 'b', 'c', 'd']:
        correct = input("Which is the correct answer? (a/b/c/d): ").lower().strip()
        if correct not in ['a', 'b', 'c', 'd']:
            print("Invalid choice, please select a, b, c, or d\n")
    
    #All of the input of the user will be stored in a text file created
    if not is_question_duplicate(filename, question):
        with open(filename, "a") as file:
            file.write(f"Question: {question}\n")
            file.write(f"a) {choice_a}\n")
            file.write(f"b) {choice_b}\n")
            file.write(f"c) {choice_c}\n")
            file.write(f"d) {choice_d}\n")
            file.write(f"Answer: {correct}\n\n")
    else:
        print(f"\nThis question already is already in {filename}\n!")
    
    #ask the user again to input a question or quit the program
    quiz_maker = ask_quit(filename)
