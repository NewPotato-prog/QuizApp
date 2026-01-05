from pickle import UnpicklingError, dump, load
from typing import Any

from question import Question

class Manager:
    def __init__(self) -> None:
        self.file_path : str = "questions.bin"
        self.questions : list[Question] = []
        
        self.readFile()
    
    def readFile(self):
        # TODO : Check if file exists
        file = open(self.file_path, "rb")
        questions = []
        try :
            questions  : Any = load(file)
        except UnpicklingError or EOFError:
            print("File is corrupted! Recreating")
            file.close()
            file = open(self.file_path, "wb")
            dump([], file)

        self.questions = questions

    def showQuestions(self):
        for question in self.questions:
            print(question.text)

    def writeFile(self):
        file = open(self.file_path, "wb")
        dump(self.questions, file)
    
    def addQuestion(self):
        text = input("Enter the question: ")
        type = input("Enter the type of question (MCQ/One word/Numeric): ")
        answer = input("Enter the answer: ")
        category = input("Enter the category: ")
        options = input("Enter the options (seperated by comma): ")
        options = options.split(",")
        question = Question(text, type, answer, category, options)
        
        self.questions.append(question)
        self.writeFile()

    def showOptions(self):
        print("CHOOSE AN OPTION")
        print("1. Show Questions")
        print("2. Add a Question")
        print("2. Exit")
        while True:
            i = input("Enter your choice: ")
            if i == "1":
                self.showQuestions()
            elif i == "2":
                self.addQuestion()
            elif i == "3":
                break
            else:
                print("Invalid Choice")
                continue

Manager().showOptions()


        