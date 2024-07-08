#while and for loops

#while loops

# x=0
# while (x<5):
#     print(x)
#     x=x+1

#for loop

# for x in range(5, 10):
#     print(x)


#Array (data set)
days= ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
for d in days:
    #if (d=="fri"):break         #use for to stop the loop
    if(d=="fri"): continue        #use for to skip the d 
    print(d)