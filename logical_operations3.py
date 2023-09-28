user_name=input(" pls enter your name: ")
maths_grade_score=input(" pls enter your maths grade score in lower case: ")
if maths_grade_score=="c" or maths_grade_score=="b" or maths_grade_score=="a":
    print("Dear",user_name,"you passed the course!!")
elif maths_grade_score!="c" or maths_grade_score!="b" and maths_grade_score=="a":
    print("you still passed the course.")
else:
    print("Dear",user_name,"you failed the course!!")