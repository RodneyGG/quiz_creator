# Quiz Creator Program

This program allows the user to create a quiz by asking a series of questions and storing them in a text file.
The following is an explanation of how the program works:

1. **Imports**:
   The program uses the following modules:
   - `os`: Handles file operations like checking if a file exists.
   - `smtplib`: Used to send the quiz via email.
   - `email.mime.text` and `email.mime.multipart`: Used for creating and formatting the email.
   - `pyfiglet`: Used to display the welcome message in ASCII art.
   - `time`: Used to get the current date and time for the email subject.

2. **Display Welcome Message**:
   The program displays a welcome message using the `pyfiglet` module to generate a large ASCII banner.

3. **File Selection**:
   - The user can either open an existing file or create a new one.
   - If the user chooses to create a new file, they are asked to specify a topic or subject for the quiz, and a new file is created with the topic's name.
   - If the file already exists, the program will offer the user an option to choose a different filename.

4. **Main Loop**:
   The main loop of the program is responsible for collecting questions, answer choices, and the correct answer from the user, and writing the information to a text file.
   - The program prompts the user to input a question and four answer choices (A, B, C, D).
   - The user must specify which of the answer choices is correct.
   - The program checks if the question already exists in the file to prevent duplicates.
   - If the question is not a duplicate, it writes the question, answer choices, and the correct answer to the text file.
   - After each question, the program asks the user if they want to add more questions, view the questions, send the questions via email, or exit the program.
   - The loop continues until the user chooses to exit by selecting option 0.

5. **Add a New Question**:
   The program allows the user to add new questions to the selected file:
   - The user is asked to input the question text and four answer choices (a, b, c, d).
   - The user must also specify the correct answer by selecting one of the choices (a, b, c, or d).
   - The question and answers are written to the text file, and the answer is marked with the letter of the correct answer.

6. **Check for Duplicate Questions**:
   Before saving a new question, the program checks if the question already exists in the file to avoid duplicate entries. If a duplicate is found, the program will notify the user and not add the question again.

7. **Menu Options**:
   After adding a question, the program asks the user if they want to:
   - **Add more questions**: Returns to the question input process.
   - **View the questions**: Displays all the questions in the file.
   - **Send the quiz via email**: Sends the quiz content as an email to a specified recipient.
   - **Exit**: Closes the program.

8. **Send Quiz via Email**:
   The user can choose to send the quiz content via email:
   - The program connects to a Gmail SMTP server and sends the quiz questions to a specified email address.
   - It includes the current date and time in the email subject.

9. **Exit the Program**:
   If the user selects the exit option, the program ends.

The program keeps running until the user chooses to exit.
