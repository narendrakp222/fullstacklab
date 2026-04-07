# num=int(input('Enter the number to check whether the given number is prime or not ?'))
# # 1 and itself divide hoke remainder zero
# if num>1:
#     for i in range(2,int(num**0.5)):
#         if num%i==0:
#             break
#     else:
#         print(f"{num} is prime")
# fibonnaci series  0 1 1 2 3 5 8 
# term=int(input('Enter the term:'))
# first=0
# last=1
# if term==1:
#     print(first)
# else:
#     print(f"{first}\n{last}")
#     for i in range(2,term):
#         sum=first+last
#         first,last=last,sum
#         print(sum)
# extraction of digits 
# 3342
# num=3342
# n=num
# result=0
# count=0
# while num>0:
#     count+=1
#     last=num%10
#     result=result*10+last
#     print(last)
#     num=num//10
# print(count)
# print(result==n)
# num=int(input('Enter the number for no of factors exist'))  # 36 1 36 2 18 3 12 4 9 6 6 
# lis=[]
# for i in range(1,int(num**0.5)+1):
#     if num%i==0:
#         lis.append(i)
#         if num//i != i:
#             lis.append(num//i)
# lis.sort()
# print(lis)
# list=[3,2,3,2,2,3,5,7,8,9,22,1,7,2,4]  
# di=dict()
# for i in range(len(list)):
#     if list[i] in di:
#         di[list[i]]+=1
#     else:
#         di[list[i]]=1
# print(di)