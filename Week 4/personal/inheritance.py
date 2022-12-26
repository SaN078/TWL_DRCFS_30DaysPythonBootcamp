class Animal:
    def __init__(self,name:str,age:int,type_:str) -> None:
        self.name = name
        self.age = age
        self.type_ = type_



        #private attributes
        self._ate = False 



        def __str__(self):
            return f"I am {self.name}. I am {self.age} years old I am a {self.type_}."

        def eat_food(self):
            self._ate = True

        def has_eaten(self):
            return self._ate

        
            


class dog(Animal):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, 'dog')

    def meow(self) -> str:
        return'meow meow'





kali = dog('kali', 6)
print(kali)
