class Power:
    
    def __init__(self,base,exponent):
        self.base = base
        self.exponent = exponent
        
    def find_the_power(self):
        print(pow(self.base,self.exponent))
    
P = Power(10,3)
P.find_the_power()
