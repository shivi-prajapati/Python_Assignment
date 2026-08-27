# Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%)
# , DA(5%), PF(3%) and taxes deduction as below:
# Salary(Lakhs) : Tax(%)
# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%
# ctc=int(input('Enter Your CTC'))
# deduction= ctc - ctc*(0.1+0.05+0.03)
# if ctc < 500000 :
#     tax_rate=0.0
# elif 500000<=ctc<1000000 :
#     tax_rate=0.1
# elif 1000000<=ctc<2000000 :
#     tax_rate=0.2
# elif 2000000<=ctc :
#     tax_rate=0.3
# annual_salary=deduction - deduction*tax_rate
# monthly_salary = annual_salary/12
# print(monthly_salary)

# Write a program that take a user input of three angles and will find out whether it can 
# form a triangle or not.
# anglex=int(input('enter a angle:'))
# angley=int(input('enter a angle:'))
# anglez=int(input('enter a angle:'))
# if anglex >0 and angley>0 and anglez>0 :
#     if anglex + angley + anglez == 180 :
#         print("It is a triangle")
#     else : 
#         print('It is not a triangle')
# else:
#     print("It is not a triangle")


#Write a program that will take user input of cost price and selling price and determines 
# whether its a loss or a profit.
# sellprice= int(input('Enter Selling Price'))
# costprice= int(input('Enter Cost Price'))
# if sellprice/costprice>1 :
#     print('Profit')
# elif sellprice/costprice<1 :
#     print('Loss')
# else :
#     print('No Profit No Loss')


# Write a menu-driven program -
# cm to ft
# km to miles
# USD to INR
# exit
# menu= int(input('''Hello User! Choose one to convert
# 1. cm to ft
# 2. km to miles
# 3. usd to inr
# 4. exit
# '''))
# if menu==1 :
#     x=int(input('enter value in cm :'))
#     x= x/30.48
#     print(x)
# elif menu==2 :
#     x=int(input('enter value in km :'))
#     x = x * 0.621371
#     print(x)
# elif menu==3 :
#     x=int(input('enter value in USD :'))
#     x = x * 95.70
#     print(x)
# else :
#     print('Exit')


# Exercise 12: Display Fibonacci series up to 10 terms.
# prev=0
# cur=1
# print(prev)
# print(cur)
# for i in range(8) :
#     next=prev + cur
#     prev = cur
#     cur= next
#     print(next)


#Reverse a given integer number.
# x=input('Enter Number :')    #int does not have length and indices 
# for i in range(len(x)-1,-1,-1):
#     print(x[i])


#Write a program that keeps on accepting a number from the user until 
# the user enters Zero. Display the sum and average of all the numbers.
# sum=0
# count=0
# num=int(input('enter a number :'))
# while num!=0 :
#     sum = sum + num
#     count += 1
#     num=int(input('enter a number :'))
# print('Sum :',sum)
# print('Average :',sum/count)


#Write a program which will find all such numbers which are divisible by 7 but 
#are not a multiple of 5, between 2000 and 3200 (both included). The numbers 
# obtained should be printed in a comma-separated sequence on a single line.
# for i in range(2000,3201):
#     if i%7==0 and i%5!=0 :
#         print(i,end=',')


#Write a program, which will find all such numbers between 1000 and 3000 (both included) 
#such that each digit of the number is an even number. The numbers obtained should be 
#printed in a space-separated sequence on a single line.
# for i in range(1000,3001) :
#     digits=str(i)
#     count_odd=0
#     for d in digits :
#         if int(d)%2 != 0 :    #d is fetcing one character in string and checking
#             count_odd += 1
#     if count_odd==0:
#         print(i,end='\t')


                


    



