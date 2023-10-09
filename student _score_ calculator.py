

 #calculation of student grades scores based on thier subject in science
print("Student grade calculator for science_subject")


#lists showing number of subect in science 
Science=["maths","chemistry","english","physics"]
print("Science_subject")
print(Science)
print()
     
#enter a number which is less than or equal to twenty five(<=25) for all science subject
while True:
    try:
        student_score_maths=int(float(input("enter score for maths: ")))
    except ValueError:
        print("please try again")
        continue
    if student_score_maths <=25:
        break
    else:
        print("number should be less or equal to twenty five (<=25)")
        continue


while True:
    try:
        student_score_chemistry=int(float(input("enter score for chemistry: ")))
    except ValueError:
        print("please try again")
        continue
    if student_score_chemistry <=25:
        break
    else:
        print("number should be less or equal to twenty five (<=25)")
        continue


while True:
    try:
        student_score_english=int(float(input("enter score for english: ")))
    except ValueError:
        print("please try again")
        continue
    if student_score_english <=25:
        break
    else:
        print("number should be less or equal to twenty five (<=25)")
        continue


while True:
    try:
        student_score_physics=int(float(input("enter score for physics: ")))
    except ValueError:
        print("please try again")
        continue
    if student_score_physics <=25:
        break
    else:
        print("number should be less or equal to twenty five (<=25)")
        continue
  
#student total score
total_score_science=student_score_maths+student_score_english+student_score_chemistry+student_score_physics
print(total_score_science)

student_score=total_score_science

#student grades ranging from A to F
if student_score >=80 <=100:
    print("you got an A,VERY GOOD")
elif student_score >=70 <=79:
    print("you got a B,GOOD")
elif student_score >=60 <=69:
    print("you got a C,AVERAGE")
elif student_score >=50 <=59:
    print("you got a D,BELOW AVERAGE")    
elif student_score >=40 <=49:
    print("you got a E,FAIR")    
else:
    print("you got an F,FAIL")



    


