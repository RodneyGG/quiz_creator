"""
For Assignment 10: Quiz
Create the Quiz program that read the output file of the Quiz Creator. 
The user will answer the randomly selected question and check if the answer is correct.
"""
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyfiglet
import time
import json
import random

#welcome the user 
def display_welcome():
    welcome_text = pyfiglet.figlet_format("Welcome to Quiz Taker!")
    print(welcome_text)

#print the score of the quiz taker
#ask for the quiz taker email and it will  email the score and the quiz to her 


#select the file
def select_quiz():
    topic_name = input("Enter the filename to open (e.g., math): ").strip()
    filename = topic_name + "_questions.txt"
    if os.path.exists(filename):
        return filename  
    else:
        print(f"The file {filename} doesn't exist. Please try again.\n")

#the program will load the exam
def load_questions(filename):
    questions = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                questions.append(json.loads(line))
    return questions

def ask_questions(questions):
    #It will then start a quiz and set the score to 0.
    score = 0
    quiz_log = ""
    
    #the program will randomize the order of the question
    random.shuffle(questions)
    
    for item, question in enumerate(questions, 1):
        print(f"\nQ{item}: {question['question']}")
        
        #the program will randomize the choices
        original_choices = question["choices"]
        shuffle_choices = original_choices[:]      
        random.shuffle(shuffle_choices)

        labeled_choices = {
            label: choice for label, choice in zip(["A", "B", "C", "D"], shuffle_choices)
        }

        # Display choices
        for label, choice in labeled_choices.items():
            print(f"    {label}. {choice}")
            
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        while answer not in labeled_choices:
            answer = input("Invalid. Enter A, B, C, or D: ").strip().upper()
            
        correct_index = int(question["answer"].split("_")[1]) - 1
        correct_choice = original_choices[correct_index]

        user_choice = labeled_choices[answer]
        
        if user_choice == correct_choice:
            print(" Correct!")
            #Plus 1 every correct answer
            score += 1
        else:
            print(f" Incorrect. Correct answer: {correct_choice}")
            
        quiz_log += f"Q{item}: {question["question"]}\n"
        for label, choice in labeled_choices.items():
            is_correct = "" 
            if choice == correct_choice:
                is_correct += "✅"
            quiz_log += f"    {label}. {choice}{is_correct}\n"
        
        quiz_log += f"Your answer: {answer}. {user_choice}\n\n"
    
    return score, quiz_log
            

#welcome the users
display_welcome()

quiz_taker = True

while quiz_taker:
    #ask the user for the topic of the exam
    filename = select_quiz()
    #Ask the user for its full name 
    full_name = input("Enter Name: ")
    
    questions = load_questions(filename)
    
    score, quiz_log = ask_questions(questions)
    
    print(f"Your Score is :{score}/{len(questions)}")
    print(quiz_log)