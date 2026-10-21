#ranges
# range(10,101,10)
# range(23,57,2)
# range(46)

# for i in range (10,101,10):
#     print (i)
# # table of 8

# for y in range (8,81,8):
#     print(y)


#two ways of srtings using loop

# a="i_f_r_a"

# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])


#break(stops all the loop) continue(skip one of the step) else(works with the break)

# #break(stops all the loop)
# for i in range(1,11):
#     if i==4:
#         break
#     print(i)

# #continue(skip one of the step)
# for i in range(1,11):
#     if i==4:
#         continue
#     print(i)

#else
# for i in range(1,11):
#     if i==5:
#         break
#     print(i)
# else:
#     print("No break encountered")

#reverse

# for i in range (50,0,-1):
#     print(i)

#table
# for i in range(1,11):
#     print(f"5 X {i} = {5*i}")


#sum of numbers
# a=0
# n=int(input("enter the number ypu want the sum then:"))
# for i in range(1,n+1):
#     a=a+i
# print(a)
 
#factorial
# a=1
# n=int(input("enter the number ypu want the factorial then:"))
# for i in range(1,n+1):
#     a=a*i
# print(a)


#even sum and odd sum
# n=int(input("please tell your number:"))
# oddsum=0
# evensum=0

# for i in range(1,n+1):
#     if i%2==0:
#         evensum=evensum+i
#     else:
#         oddsum=oddsum+i
# print(evensum)
# print(oddsum)

#factors of the number
# sum=0
# n=int(input("enter number you want to have factors: "))
# for i in range(1,n):
#     if n%i == 0:
#        sum=sum+i
# if sum == n:
#     print(f"{n} is a perfect number")
# else:
#     print("Not a perfect number")
    

#prime number
# n=int(input("enter number: "))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count==2:
#     print(f"{n} is a prime number")
# else:
#     print("not a prime number")


# reverse a string

# s= input("enter the string:")
# rev=""
# for i in range(len(s)-1,-1,-1):
#     print(i)
#     rev=rev+s[i]
# print(rev)
    
#check it is palindrom

# s=input("enter your string:")
# rev=""

# for i in range(len(s)-1,-1,-1):
#     rev=rev+s[i]
# if rev==s:
#     print("its a palindrom")
# else:
#     print("its not a palindrom")


#count letters , characters and numbers 


# a="P@#yn26at^i5ve"
# char=0
# sp=0
# digits=0

# for i in a:
#     if i.isdigit():
#         digits=digits+1
#     elif i.isalpha():
#         char=char+1
#     else:
#         sp=sp+1
# print(f"number of digits:{digits}, number of characters:{char} and the number of special characters:{sp}")


