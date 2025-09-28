#Python Practical Task ..
#que1 -sum of first n postive integers.
n=int(input("enter the number:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i+=1
print(sum)
    
#que:2 count occurences of substring in a string
string="dhruti ,bhandari, trisha,bhandari"
sub_string="bhandari"
a=string.count(sub_string)
print(f"ocurrences:{a}")

#que:3 count the occurence of each word in a sentence
sentence='i love india. india is my country'
words=sentence.split()
for i in words:
    print(f"occurrnces of each word is {i,words.count(i)}")

#que4 swap first two character of two strings
s1="dhruti"
s2="bhandari"
new_s1=s2[:2]+s1[2:]
new_s2=s1[:2]+s2[2:]
print(f"after swap s1 is {new_s1}")
print(f"after swap s2 is {new_s2}")

#que5 add'ing'at the end of given string(len 3). if already end with 'ing'then add '
string=loving
if len<3:
    result=string
elif string.endswith("ing"):
    result=string+"ly"
else:
    result=s+"ing"
print(result)

#que6 find the first apperance of substring not and poor from the given string.if the 'not'follows the the poor replace the whole substring with good .
s="india is not a poor country"
s_not=s.find("not")
s_poor=s.find("poor")
if s_not>s_poor:
    s=s.repace("not",good)
print(s)

#que7 find greatest common divisor of two number.
a=56
b=98
while b:
    a, b = b, a % b
print("GCD is:", a)

#que8 check whether a list contain a sublist.

#que9 find the second smallest number in list 
nums = [4,7,3,8,2,1,9]
nums.sort()
print("Second smallest:", nums[1])

# que15 Fibonacci series up to n
n = 7
a= 0
b=1
for i in range(n):
    a, b = b, a + b
print(a,end="")

#que 16 Write a Python program using function to find the sum of odd series and even series. Odd series- 12/1!+32/3!+52/5!+….n Even series-22/2!+42/4!+62/6!+..n
n = int(input("Enter the value of n: "))

odd_sum = 0
even_sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        even_sum +=i
        i**2
    else:
        odd_sum +=i
        i**2
print(f"Sum of odd series of {n}: {odd_sum}")
print(f"Sum of even series of {n}: {even_sum}")




    