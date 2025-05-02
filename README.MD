# Quiz Creator

Quiz Creator is a Python-based application that allows users to create quizzes and take them interactively. The program supports creating customizable question sets, storing them in files, and emailing results. It is designed for both quiz creators and quiz takers, offering a streamlined way to manage quizzes.

## Features

- **Quiz Creator**: 
  - Create quizzes by adding questions, multiple-choice answers, and specifying the correct answer.
  - Prevents duplicate questions in a quiz file.
  - Stores quizzes in topic-based files.

- **Quiz Taker**:
  - Load and take quizzes created by the Quiz Creator.
  - Randomizes the order of questions and answers for each quiz session.
  - Displays scores and detailed feedback at the end of the quiz.

- **Email Integration**:
  - Send quiz files or results via email.
  - Customizable email templates for quiz results.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RodneyGG/quiz_creator.git
   cd quiz_creator
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Main Program**:
   ```bash
   python main_quiz_program.py
   ```

2. **Options**:
   - Choose `1` to create a new quiz or edit an existing one.
   - Choose `2` to take a quiz by selecting an existing quiz file.
   - Choose `3` to exit the application.

3. **Creating a Quiz**:
   - Enter a topic name to create a new quiz file.
   - Add questions and multiple-choice answers.
   - Specify the correct answer for each question.
   - Save and manage your quiz files.

4. **Taking a Quiz**:
   - Select a quiz file.
   - Answer randomized questions.
   - View your score and receive detailed feedback.

5. **Emailing Results**:
   - Send quiz results or files to a specified email address.

## Dependencies

The project uses the following Python libraries:
- `pyfiglet` for ASCII art.
- `smtplib` and `email` for sending emails.
- `json` for handling quiz data.
- `random` for randomizing questions and answers.

Ensure you have Python 3.7+ installed and the required dependencies.