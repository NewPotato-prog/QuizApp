from pickle import load
from typing import Any

class Manager:
    def __init__(self) -> None:
        self.file_path : str = "questions.bin"
        self.questions : list[dict[str, Any]] = []
        self.readFile()
    
    def readFile(self):
        file = open(self.file_path, "rb")
        self.questions  : list[dict[str, Any]] = load(file)

    def showOptions(self):
        data = self.readFile()
        for question in data:
            print(question["text"])
            print(question["options"])
            print()