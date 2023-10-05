class Division:

    def divide_me(self, num,denom):
        return num/denom
    
division =Division()
print(division.divide_me(4,0))

class converter:
    def divide(self,num,denom):
        try:
            result=num/denom
        #except ZeroDivisionError:
        except (ZeroDivisionError, TypeError) as e:
            #print("cant do this")
            print(f"cant do this-{e}")
        except SyntaxError:
            print("Syntax error")
        else:
            print(f"this is your result -{result}") 
        finally:
            print("This is the last statement")  

converter=Converter()
converter.divide(12,0)






    #try:
    #x=-1
    #if x<0
    # raise ValueError("x cannot be negative") 

      
          