


class Human:
  ##attribute/properties
  number_of_legs=0
  number_of_hands=0
  engergy=0
  mouth=0
  eyes=0
  jumping_ability=False
  number_of_ears=0
  name=""
  nostrils=0
  #constructor
  def __init__(slef,name,eyes,number_of_legs,number_of_hands,number_of_ears, mouth):
    slef.name=name
    slef.eyes=eyes
    slef.number_of_legs=number_of_legs
    slef.number_of_hands=number_of_hands
    slef.number_of_ears=number_of_ears
    slef.mouth

  def clap(slef,num_of_hands):
      print("paaa")
    
  #def clap(slef):
      #available_hands=slef.number_of_hands
      #return f"clapping with {available_hands} hands"

    
      


human1 =Human("stanley",2,2,2,2,1)
print(human1.name)
print(human1.eyes)
print(human1.number_of_legs)
print(human1.number_of_hands)
print(human1.number_of_ears)
print(human1.mouth)
print(human1.clap(2))
print(type(human1))


#stanley = Human("stanley",2,2,1,2,1)
#dice =Human("dice",1,1,0,0,1)
#print(f"stanley is {stanley.clap()}")
#print(f"dice is {dice.clap()}")


