from typing import Any


class Question:
    text: str
    type: str # MCQ / One word / numeric?
    answer : str | int | float
    category : str | None# History, Geo, Math etc.
    options : list[str | int | float] | None

    def __init__(self, text : str, type : str, answer : str, category : str | None= None, options : list[str | int | float] | None = None ) -> None:
        self.text = text
        self.type = type
        self.answer = answer
        self.category = category
        self.options = options
    
    def toJson(self) -> dict[str, Any]:
        return {
            "text" : self.text,
            "type" : self.type,
            "answer" : self.answer,
            "category" : self.category,
            "options" : self.options
        }