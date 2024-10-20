from calculator import Calculator 

class Division (Calculator) : 
    def __init__ (self ,  num1 , num2 ,operation = "mul" ): 
       super().__init__(num1, num2, operation)
    def compute (self ) : 
        if (self.num2 == 0) : 
            return "divison by zero is not allowed" 
        else : 
            return self.num1 / self.num2 
    