#que 1 : Sum of first n postive integers.
n= int(input("enter the number"))
total=0
for i in range (1,n+1):
    total+=i
print(f"sum of postive integers is {total}")

#que 2:Count the occurence of a substring
s= input("enter a string")
sub= input("enter the substring")
print("occerences",s.count(sub))

#que 3: count the occurence of each word in a sentence.
sentence=input("enter the sentence")
words=sentence.split()
for w in set(words):
    print(words.count(w))
 
 #que 4: swap first two characters
s1= "python"
s2="language"
new_s1=s2[ :2]+s1[2: ]
new_s2=s1[ :2]+s2[2: ]
print(new_s1,new_s2)

#que 5: Using string nethod
s= "lovely"
if len(s)<3:
    result=s
elif s.endswith("ing"):
    result=s+"ly"
else:
    result=s+"ing"
print(result)

#que 6: using replacce 
s= iput("enter a string")
pos_not=s.find("not")
pos_poor=s.find("poor")
s = input("Enter string: ")
if pos_not!= -1 and pos_poor!= -1 and pos_not> pos_poor:
    s = s[:pos_not] + "good" + s[pos_poor+4:]
print(s)

#que 7: GCD of two number.
#que 8: chevk whether s list contain a sublist
main_list = [1, 2, 3, 4, 5, 6]
sub_list = [3, 4]

# wue 9: Second smallest number in list
num = list(map(int(input("Enter numbers: ")).split()))
nums = sorted(set(nums))
print("Second smallest:", nums[1])

#que 10 unique values from list
lst = list(map(int(input("Enter numbers: ")).split()))
print(list(set(lst)))

#que11 unzip a list of tuple into individual lists.
lst = [(1,2), (3,4), (5,6)]
a = []
b = []

for x, y in lst:
    a.append(x)
    b.append(y)

print(a)
print(b)

#que 12 convert a list of tuples into a dict 
lst = [("a",1), ("b",2), ("c",3)]
d = {}
for k, v in lst:
    d[k]=v
print(d)


#que 13 sort a dict (ascending/ dec)by value 

#que 14: find 3 values in a dict
d = {"a":10, "b":30, "c":50, "d":20}
values = sorted(d.values(), reverse=True)
print(values[:3])

#que 15 list of fibonaaci series up to n
n = int(input("Enter n: "))
a = 0
b = 1
fib_list = [a, b]
while True:
    next = a + b
    if next > n:
        break
    fib_list.append(next)
    a = b
    b = next
print(fib_list)

#que 16 count frequencies in list using dict
lst = [1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2]
freq = {}
for x in lst:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
print(freq)

#que 17: Sum of odd and even series
# factorial function
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f
def odd_series(n):
    s = 0
    for i in range(1, n + 1, 2):
        s = s + (i*i) / fact(i)
    return s
def even_series(n):
    s = 0
    for i in range(2, n + 1, 2):
        s = s + (i*i) / fact(i)
    return s
    
n = int(input("Enter n: "))
print("Sum of odd series =", odd_series(n))
print("Sum of even series =", even_series(n))

#que 18. Python Program to Find Factorial of Number Using Recursion

#que 19Write a Python function that takes a list and returns a new list with unique elements of the first list.
lst = [1, 2, 2, 3, 4, 4, 5]

unique = []
for item in lst:
    if item not in unique:
        unique.append(item)
print(unique)

#que 20 Mini project
import random

try:
    user_id = input("Enter User ID: ")
    name = input("Enter your name: ")
    words = input("Enter some words (separated by space): ").split()
    if len(words) < 2:
        raise ValueError("Please enter at least two words!")
    w1 = random.choice(words)
    w2 = random.choice(words)
    number = str(random.randint(10, 99))
    special = random.choice(["@", "#", "$", "%", "&", "!"])
    w1 = w1.capitalize()
    password = w1 + w2 + number + special
    if len(password) < 8:
        password += "Xy@12
        user_data = (user_id, name, password)
    print("\nUser data stored:")
    print(user_data)

except Exception as e:
    print("Error:", e)
