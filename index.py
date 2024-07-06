# 1) Write a program that takes a student's score as input and prints their Marksheet on predefined grading criteria.

marksheet=int(input("enter your marks!"))
if(marksheet>=90 and marksheet<=100):
    {
        print("Your grade is A+")
    };
elif(marksheet>=80):{
    print("Your grade is A ")
};
elif(marksheet>=70):{
    print("YOUr grade is B")
};
elif(marksheet>=60):{
    print("Your grade is C")
};
else:{
    print("YOu  are fail!")
}