for word in ["dog","cat","fish"]:
    print(word)

#while loop
#i=1
#while i>0:
#    print(i)
#    i+=1

#set
A={1,4,5,7}
B={3,5,8,9}
print(A | B)
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

#frozenset
vowel=('a','e','i','o','u')
fset=frozenset(vowel)
print(fset)

#dictionary
sdict={"name":"sharon","class":"IT"}
print(sdict)
print(sdict.items())
print(sdict.values())
print(sdict.keys())

#built in fun
import math
print(max(10,20,30))
print(min(10,38,74))
print(abs(-10))
print(pow(2,2))
print(math.floor(10.4))
print(math.ceil(10.4))

#strings
s1="Hello"
print(len(s1))
print(type(s1))
s2=s1.replace("Hello","Worlds")
print(s2)

s1 = "Sharon Reshma"
print(s1.find("r"))
print(s1.rfind("r"))

str = "Python is a very good language"
print(str.split(" "))
print(str.partition("a"))