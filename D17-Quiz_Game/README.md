# ❓ Quiz Game - Day 17 (Object-Oriented Programming)

## 📌 Project Overview

This project is a **command-line Quiz Game** built using Python as part of **Day 17** of the *100 Days of Python* course.

The main goal of this project is to understand and apply **Object-Oriented Programming (OOP)** concepts by designing a quiz system using **classes, objects, and methods**.

The game asks True/False questions, tracks the user’s score, and displays the final result at the end.

---

## 🎯 How the Quiz Works

1. Questions are loaded from a dataset
2. Each question is converted into a `Question` object
3. A `QuizBrain` object controls quiz flow
4. The user answers questions one by one
5. The score is updated after each question
6. The quiz ends when all questions are answered

---

## 🧠 Concepts Learned & Applied

---

## 1️⃣ Object-Oriented Programming (OOP)

This project is fully built using **OOP principles**, which helps organize logic into meaningful components.

Key concepts applied:

* Classes
* Objects
* Attributes
* Methods
* Encapsulation

---

## 2️⃣ The `Question` Class

The `Question` class represents a **single quiz question**.

```python
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

Each `Question` object stores:

* `text` → the question itself
* `answer` → the correct answer

This makes questions easy to manage and reusable.

---

## 3️⃣ The `QuizBrain` Class

The `QuizBrain` class controls the **entire quiz logic**.

```python
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
```

It tracks:

* Current question index
* List of question objects
* User score

---

## 4️⃣ Managing Quiz Flow

### 🔹 `still_has_questions()`

Checks whether there are more questions left in the quiz.

```python
def still_has_questions(self):
    return self.question_number < len(self.question_list)
```

This keeps the quiz running until all questions are answered.

---

### 🔹 `next_question()`

Displays the next question and collects user input.

```python
def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(...)
    self.check_answer(user_answer, current_question.answer)
```

This method:

* Retrieves the current question
* Increments question count
* Sends the answer for validation

---

### 🔹 `check_answer()`

Validates the user’s answer and updates the score.

```python
def check_answer(self, user_answer, correct_answer):
```

It:

* Compares answers (case-insensitive)
* Increments score if correct
* Displays feedback and current score

---

## 5️⃣ Creating Objects from Data

Questions are created dynamically from external data:

```python
for question in data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)
```

This shows how **raw data is transformed into objects**, a key OOP skill.

---

## 6️⃣ Main Program Execution

The quiz runs using a `while` loop:

```python
while quiz.still_has_questions():
    quiz.next_question()
```

This cleanly separates:

* Game logic (inside classes)
* Program execution (main file)

---

## 🔄 Program Flow Summary

1. Load question data
2. Create `Question` objects
3. Store them in a question bank
4. Initialize `QuizBrain`
5. Loop through questions
6. Check answers and update score
7. Display final score at the end

---

## 🛠 Skills Strengthened

* Object-oriented thinking
* Designing classes and methods
* Using attributes to store state
* Encapsulation of logic
* Separating responsibilities across files
* Writing cleaner, scalable Python code

---

## ✅ Conclusion

This project marks a major shift from procedural programming to **object-oriented design**.
By separating responsibilities into classes, the code becomes easier to understand, maintain, and extend.

Day 17 is an important foundation for building **larger, real-world applications** in Python.

---
