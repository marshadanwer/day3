
#Conditional Logical opertor are either "True or False" , "Yes or No" , "0 or 1"

#equal to                               ==
#less than                              <
#greater than                           >
#less than or equal to                  <=
#greater than or equal to               >=
#not equal to                           !=

# is 4 equal to 4?
print(4 == 4) #True
print(4!=4)
print(4>3)
print(4<3)
print(3<=5)
print(5>=3)

#Application of Logical Operator
Ali_age=4
minimum_school_age=5
print(Ali_age==minimum_school_age) #True

#input function and logical operator
minimum_school_age=5
Ali_age=input("how old is Ali?")  #input function
Ali_age=int(Ali_age)
print(type(Ali_age))
print(Ali_age==minimum_school_age)  #logical operator