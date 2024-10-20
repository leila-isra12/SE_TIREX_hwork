from calculator import Calculator 

class Addition (Calculator) : 
    def __init__ (self ,  num1 , num2 ,operation = "add" ): 
        super().__init__(num1, num2, operation)
    def compute (self ) : 
        return self.num1 + self.num2 
    