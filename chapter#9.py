

# a=1
# while a!=20:
#     print(a)
#     a=a+1

#print on separate line
# a=456
# b=a%10
# print(b)
# a=a//10
# c=a%10
# print(c)
# a=a//10
# print(a)

# a=int(input("Enter:"))
# while a>0:
#     print(a%10)
#     a=a//10


a=int(input("Enter your number:"))
copy=a
rev=0
while a>0:
    rev=rev*10+a%10
    a=a//10

if rev==copy:
    print("its palindrom")
else:
    print("its not")
  
    
# formula use is rev=rev*10+a%10