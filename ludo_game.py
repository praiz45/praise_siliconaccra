class Player:
    ##attribute/property
  name=""
  age=0
  num_of_hands=0
  eyes=0
  mouth=0
  nostrils=0
  energy=0
      #constructor
  def __init__(slef,name,age,num_of_hands,eyes,mouth,): 
    slef.name=name
    slef.age=age
    slef.num_of_hands=num_of_hands
    slef.eyes=eyes
    slef.mouth=mouth
    
    
  #def roll(self,hands):
       #print("clatter")
  
  def clattering(slef):
    available_fingers=slef.num_of_hands
    return f"clattering with {available_fingers} hands"

#player1=Player("jax",12,2,2,1)
#print(player1.name)
#print(player1.age)
#print(player1.num_of_hands)
#print(player1.eyes)
#print(player1.mouth)

jax=Player("jax",14,2,2,1)
print(f"jax is {jax.clattering()}")


      
    

