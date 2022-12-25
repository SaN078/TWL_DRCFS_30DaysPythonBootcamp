from bs4 import BeautifulSoup


class human:
    def __init__(self,name:str, age:int , type_:str) -> None:
        self.name = name
        self.age = age
        self.type_ = type_



    def display(self):
        return f"My name is {self.name} and my age is {self.age}"

    
    def can_fly(self, type_: str):
        if self.name <= 10 and self.type_ == "bird":
            return True
        return False

    @classmethod
    def from_ppl(cls, name: str , age: int) -> "human":
        cls.something = 'sangeet'
        ppl_instance = cls(name, age, "ppl")
        return ppl_instance
    


    @classmethod




ppl = 'ppl'

Pramika =  human("Pramika", 17, ppl)

print()
