data = range(20)
list(data)
print("hello ghana")
ror = [1,2,3,4]

#def mean(list):
#   mean = sum(list)/len(list)
#   return mean

#print(mean([2,3,4,9,8.9]))

def mean(value):
    if type(value) == dict:
        mean = sum(value.values())/len(value)
    else:
        mean = sum(value)/len(value)
    
    return mean

student_grade ={"meleena":34,"frosch":32.3,"jackson":88,"grace":56}
#print(mean(student_grade))
print(mean([2,3,4,9,8.9]))

#True
#if type(5) == int:
#    print("Greater")
#else:
 #   print("Great by non")
#type(5) == str




def speed(distance):
    if distance == 50:
        return " driving at a normal  speed"
    elif distance > 50:
        return "take it easy"
    else:
        return "too slow"
while True:
    try:
        use_intp = int(float(input("Enter your distance:")))
        print(speed(use_intp))
        break
    except(ValueError):
        print("invalid input")
print(type(use_intp),use_intp)


user_name = input("enter user name:")
User_sun = input("enter your surname")
response = f"Hello Mr {User_sun} {user_name}!"
print(response)




