from abc import ABC, abstractmethod
class Calculator (ABC): 
    def __init__ (self, num1 , num2  ,operation  ) : 
        self.operation = operation 
        self.num1 = num1 
        self.num2 = num2 
    @abstractmethod 
    def compute (self) : 
        pass 
    