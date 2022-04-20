# #problem 1
# n = int(input("N= "))
# if ( n < 0):
#     print("indoor activity")
# elif n>=0 and n<=4:
#     print("outdoor activity")
# elif  n > 40 :
#     print("indoor activity")
# else : print("none")




#problem No 2
# print("a va b sonlarini kiriting (15 25) shaklda: ")
# a,b = [int(item) for item in input().split(" ")]
# if b**2 == a :
#     print(f"{b} * {b} = {a}")
# elif a**2 == b:
#     print(f"{a} * {a} = {b}")
# else :
#     print("none")



# #problem No 3
# print(" 2 ta son kiriting misol uchun(2 3)")
# a,b = [int(item) for item in input().split(" ")]
# if a > b : print(a)
# elif a == b : print(b)
# else : print(b)



# # problem No 4
# print ( " 3 ta son kiriting (2 3 4)")
# a = int(input("A="))
# b = int(input("B="))
# c = int(input("C="))
# print ( max(a,b,c) , " " , min(a,b,c) )


# # problem 10
# n = int(input("N="))
# if (n % 2 == 0 and n % 3 == 0 and n % 5==0):
#     print("A")
# elif (n%2 == 0 and n%3 ==0):
#     print("B")
# elif (n % 2 == 0 and n % 5 ==0):
#     print("C")
# elif (n%5==0 and n%3 == 0):
#     print("D")
# elif (n % 2 == 0 or n % 3 == 0 or n % 5 == 0):
#     print("E")
# elif (n % 2!=0 and n % 3!=0 and n % 5!=0):
#     print("N")



# # problem No 6
# year=(int(input("input year: ")))
# if(year % 4 ==0):
#     if(year % 100 ==0):
#         if(year % 400 == 0):
#             print("leap year")
#         else:
#             print("normal year")
#     else: print("leap year")
# else: print("normal year")

# # problem 7
# import random
# m = random.randrange(1,7)
# n = int(input("siz o'ylagan son ni kiritind(1,6 gacha) : "))
# if m == n :
#     print("current")
# elif m > n :
#     print("up")
#     n = int(input("N="))
#     if m == n :
#         print("current")
#     else :
#         print("lost game")
# elif m < n :
#     print("down")
#     n = int(input("N="))
#     if m == n:
#         print("current")
#     else:
#         print("lost game")
#
# print("kompyuter o'ylagan son m = ", m)

# #problem 8
# alphaa = input(" hohlagan harfni kiriting : ")
# if alphaa.isupper():
#     print(alphaa.lower())
# elif  alphaa.islower():
#     print(alphaa.upper())
# elif not alphaa.isalpha():
#     print("none")

# # problem 9
# import random
# n = 3
# k = []
# l = []
# strike = 0
# ball = 0
# print("1 dan 9 gacha 3 ta son kiriting : ")
# for x in range(0,3):
#     n = int(input("son: "))
#     k.append(n)
#
# print("1 dan 9 gacha 3 ta son kiriting : ")
# for x in range(0,3):
#     n = int(input("son: "))
#     l.append(n)
#
# # for x in range(0,3):
# #     n = random.randint(0,9)
# #     l.append(n)
# for x in range(0,3):
#     if l[x] == k[x]:
#         strike +=1
#         l[x] = -1
#
#     elif k[x] in l:
#         ball +=1
#
# print(k)
# print(l)
# print (strike,"S", ball, "B")


#problem 10
import re
misol = input("misolni kiriting faqat hozir + va - amallarni bajarishimiz mimkin (14 + 16 ): ")
amalcha = re.split("\s", misol)

if amalcha[1] == '+':
    print(int(amalcha[0]) + int(amalcha[2]))
elif amalcha[1] == '-':
    print(int(amalcha[0]) - int(amalcha[2]))
else :
    print("tushunarsiz amal")