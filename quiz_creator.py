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
import json

def display_welcome():
    welcome_text = pyfiglet.figlet_format("Welcome to Quiz Maker!")
    print(welcome_text)
    
#check for duplicate questions
def is_question_duplicate(filename, question):
    #Check if the file exists and is not empty
    try:
        with open(filename, "r", encoding="utf-8") as file:
            #loop the the question to find duplicate
            for line in file:
                line = line.strip()
                if line:
                    saved_question = json.loads(line)
                    if saved_question["question"].lower() == question.lower():
                        return True # Duplicate found
            return False#return false when question not found
        
    except (FileNotFoundError, json.JSONDecodeError):
        return False
    
            
#view the questions
def view_questions(filename):
    with open(filename, "r", encoding="utf-8") as file:
        print(f"These are the questions inside {filename}")

        for line_number, line in enumerate(file, 1): 
            line = line.strip()
            if line: 
                data = json.loads(line) 
                
                print("Question:", data["question"])
                
                for i, choice in enumerate(data["choices"], 1):
                    print(f"  choice_{i}: {choice}")
                print("Answer:", data["answer"])
                print("-" * 40)


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
            topic_name = input("Enter the filename to open (e.g., math): ").strip()
            filename = topic_name + "_questions.txt"
            if os.path.exists(filename):
                view_questions(filename)
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
    
    formatted_content = ""
    
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if line:  
                data = json.loads(line)
                # Format the question and choices
                question_text = f"Question: {data['question']}\n"
                choices_text = ""
                for i, choice in enumerate(data["choices"], 1):
                    choices_text += f"  choice_{i}: {choice}\n"
                answer_text = f"Answer: {data['answer']}\n"
                        
                formatted_content += question_text + choices_text + "\n" + answer_text + "\n"

    # Get current time as a formatted string
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    
    #Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"Quiz Maker: {filename} is sent on {current_time}"
    
    #questions and answer will be printed in the mail
    body = f"Here are the questions from your quiz program:\n\n{formatted_content}"
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
    choice_1 = input("Enter choice 1: ").strip()
    choice_2 = input("Enter choice 2: ").strip()
    choice_3 = input("Enter choice 3: ").strip()
    choice_4 = input("Enter choice 4: ").strip()
    
    #select what is the correct answer
    correct = ""
    while correct not in ['1', '2', '3', '4']:
        correct = input("Which is the correct answer? (1/2/3/4): \n").lower().strip()
        
        questions_format = {
            "question": question,
            "choices": [choice_1, 
                    choice_2, 
                    choice_3, 
                    choice_4],
            "answer": f"choice_{correct}"
                            }
        
        if correct not in ['1', '2', '3', '4']:
            print("Invalid choice, please select 1, 2, 3, 4\n")
    
    #All of the input of the user will be stored in a text file created
    if not is_question_duplicate(filename, question):
        with open(filename, "a") as file:
            file.write(json.dumps(questions_format) + "\n")
    else:
        print(f"\nThis question already is already in {filename}\n!")
    
    #ask the user again to input a question or quit the program
    quiz_maker = ask_quit(filename)
