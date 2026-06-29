# 1.reverse string using slicing

# name="Preetha"
# print(name[::-1])

# reverse string using reversed()+join

# text="Sathish loves programming"
# reversed_text="".join(reversed(text))
# print(reversed_text)

# #reverse string by manual

# s="I love programming"
# reversed_s="" 
# for i in s:
#     reversed_s=i+reversed_s
# print(reversed_s)

#Palindrome using slicing

# text="madam"
# if text==text[::-1]:
#     print("Palindrome")
# else:
#     print("Not a  Palindrome")

#FACTORIAL OF A NUMBER

#USING LOOP

# num=int(input("Enter a number : "))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

#USING RECURSION

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print("Factorial : ", factorial(5))

#USING MATH.FACTORIAL()

# import math
# print("Factorial : ", math.factorial(6))

#FIBONAACI 

# def fibonacci_gen(n):
#     a, b = 0,1
#     for i in range(n):
#         print(a,end=" ")
#         a,b=b,a+b
# fibonacci_gen(10)

#FIBONACCI RECURSIVE

# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# series=[fib(i) for i in range(10)]
# print(series)

#FIBONACCI USING GENERATOR FUNCTION

# def generator(n):
#     a,b=0,1
#     for i in range(n):
#         yield a
#         a,b=b,a+b
# for num in generator(10):
#     print(num,end=" ")

#PRIME NUMBER

# num=int(input("Enter a number:"))
# if num<=1:
#     print("Not Prime")
# else:
#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(num , "is Prime")
#     else:
#         print(num , "is Not Prime")

#Armstrong Number

# num=int(input("Enter a number : "))
# digits=len(str(num))
# temp=num
# sum_val=0
# while temp>0:
#     digit=temp%10
#     sum_val=sum_val+digit**digits
#     temp=temp//10
# if sum_val == num:
#     print(num , "is an Armstrong Number")
# else:
#     print(num , "is not an Armstrong Number")

#ANAGRAM USING SORTED METHOD 

# def is_anagram(word1, word2):
#     return sorted(word1.lower()) == sorted(word2.lower())
# print(is_anagram("listen", "silent" ))
# print(is_anagram("Earth", "heart"))
# print(is_anagram("hello", "wolrd"))

#ANAGRAM BY MANUAL LOOP BASED METHOD

# def is_anagram(word1, word2):
#     word1=word1.lower()
#     word2=word2.lower()
#     count1={}
#     count2={}
#     for ch in word1:
#         count1[ch]=count1.get(ch,0)+1
#     for ch in word2:
#         count2[ch]=count2.get(ch,0)+1
#     return count1==count2
# print(is_anagram("listen","silent"))
# print(is_anagram("hello","world"))

#COUNT CHARACTERS IN A STRING

# s=input("Enter a String: ")
# count=0
# for ch in s:
#     count+=1
# print("Total Characters:", count)

#COUNT SPECIFIC TYPES LIKE VOWELS, CONSONANTS AND SPACES ETC

# sentence=input("Enter a sentence:")
# vowels=0
# spaces=0
# consonants=0
# for ch in sentence.lower():
#     if ch in "aeiou":
#         vowels+=1
#     elif ch == " ":
#         spaces+=1
#     elif ch.isalpha():
#         consonants+=1
# print("Vowels:", vowels)
# print("Spaces:", spaces)
# print("Consonants:", consonants)

#COUNT FREQUENCY OF EACH LETTER IN A SENTENCE

# sen=input("Enter a sentence: ")
# count={}
# for ch in sen.lower():
#     count[ch]=count.get(ch,0)+1
# print("Frequency of each characters:", count)

#FIND DUPLICATES in a list

# nums = [1, 2, 3, 2, 4, 5, 1, 6]
# duplicates=[]
# for n in nums:
#     if nums.count(n)>1 and n not in duplicates:
#         duplicates.append(n)
# print("Duplicates:", duplicates)

#find duplicates in  A STRING

# text="Programming"
# duplicates=[]
# for ch in text.lower():
#     if text.count(ch)>1 and ch not in duplicates:
#         duplicates.append(ch)
# print("Duplicates:", duplicates)

#FIND DUPLICATES BY MANUAL
# nums = [1, 2, 3, 2, 4, 5, 1, 6]
# seen = set()
# duplicates = set()

# for n in nums:
#     if n in seen:
#         duplicates.add(n)
#     else:
#         seen.add(n)

# print("Duplicates:", list(duplicates))

#REMOVE DUPLICATES

# nums = [1, 2, 3, 2, 4, 5, 1, 6]
# unique=list(set(nums))
# print("Unique elements:", unique)

#PRESERVE ORDER WHILE REMOVING DUPLICATES

# nums = [1, 2, 3, 2, 4, 5, 1, 6]
# unique=[]
# for n in nums:
#     if n not in unique:
#         unique.append(n)
# print("Unique Elements:", unique)

#REMOVE DUPLICATE ELEMENTS IN  A STRING

# text="programming" 
# unique=""
# for ch in text:
#     if ch not in unique:
#         unique+=ch
# print("Unique Characters:", unique)

#LARGEST NUMBER IN A LIST USING BUILT-IN

# nums = [12, 45, 67, 23, 89, 45]
# largest=max(nums)
# print("Largest number is:", largest)

#LARGEST NUM USING MANUAL LOOP

# nums = [12, 45, 67, 23, 89, 45]
# largest=nums[0]
# for n in nums:
#     if n>largest:
#         largest=n
# print("Largest Number is:", largest)

#User Input Example

# nums=list(map(int,input("Enter numbers separated by space:").split()))
# largest=nums[0]
# for n in nums:
#     if n>largest:
#         largest=n
# print("Largest number:",largest)

#SECOND LARGEST

# nums = [12, 45, 67, 23, 89, 45]
# unique_nums=list(set(nums))
# unique_nums.sort()
# second_largest=unique_nums[-2]
# print("Second largest number:", second_largest)

#SECOND LARGEST BY MANUAL WAY

nums = [12, 45, 67, 23, 89, 45]
largest=second_largest=float('-inf')
smallest=second_smallest=float('inf')
for n in nums:
    if n>largest:
        second_largest=largest
        largest=n
    elif n>second_largest and n!=largest:
        second_largest=n
print("second largest number:", second_largest)        

#SORTING OF NUMBERS

nums = [12, 45, 67, 23, 89, 45]
print("Ascending order:",sorted(nums))
print("Descending order:",sorted(nums,reverse=True))

#SORTING OF STRINGS

words = ["banana", "apple", "cherry", "date"]
print("Alphabetical:",sorted(words))
print("Reverse:",sorted(words,reverse=True))

#SORTING USING KEY FUNCTION
words = ["banana", "apple", "cherry", "date"]
print("By length:",sorted(words,key=len))
print("By last character:",sorted(words,key=lambda x:x[-1]))

#SORTING LIST IN PLACE
nums = [12, 45, 67, 23, 89, 45]
nums.sort()
print(nums)

#SORTING BY MANUAL

nums = [12, 45, 67, 23, 89, 45]
n=len(nums)
for i in range(n):
    for j in range(n-i-1):
        if nums[j]>nums[j+1]:
            nums[j], nums[j+1]=nums[j+1], nums[j]
print("Sorted List:",nums)

