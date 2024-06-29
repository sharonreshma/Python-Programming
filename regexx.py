#Backslash
import re
s="Welcome to python.com"
f=re.search(r'\.',s)
print(f)

#square brackets
str="represent a character class consisting of a set of characters that we wish to match"
pat="[a-m]"
r=re.findall(pat,str)
print(r)

pattern = r"\b\w+ee\b"
text = "Feel the breeze and see the trees."
matches = re.findall(pattern, text)
print("Matches:", matches)

pattern = r"\bcat\b"
replacement = "dog"
text = "I have a cat named Cat."
new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print("Original:", text)
print("Replaced:", new_text)


#^
#negation     
import re
pattern = r"[^aeiou]"
text = "Hello, World!"
matches = re.findall(pattern, text)
print("Matches:", matches)


#$
import re 
string ="Hello World!"
pattern = r"World!$"
match = re.search(pattern, string) 
if match: 
	print("Match found!") 
else: 
	print("Match not found.") 
