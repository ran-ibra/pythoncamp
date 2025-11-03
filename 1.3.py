'''
Create a program that analyzes a given text string and provides:
. Character frequency count (case-insensitive)
. Word count
. Most common character (excluding spaces)
. Palindrome check
. Reverse the string
Expected Output:
Enter text: Python Programming
Total characters (with spaces): 18
Total characters (without spaces): 16
Total words: 2
Character frequency: {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, 'r':
2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}
Most common character: p, r, o, n, g, m (appears 2 times)
Is palindrome: No
Reversed: gnimmargorP nohtyP
Hints:
Use .lower() for case-insensitive comparison
Use dictionaries to count frequency
Use .split() for word count'''
text= input("enter text: ")
print(f"# chars with spaces {len(text)}")

words= ''.join(text.split())
print(f"# chars without spaces {len(words)}")
print(f"# word {len([i for i in (text.split())])}")
dictt= {}
for key in text:
    dictt.update(
    {key:dictt.get(key,0)+1}
    )
sorted_by_value_desc = sorted(dictt.items(), key=lambda item: item[1], reverse=True)

getmax= max(dictt.items(), key=lambda m :m[1])

print (f"most frequant {getmax}")
# get palindrome
# i=0 , j =len(words)-1
# for i , j in words:
#     f =False
#     if words[j]!=words[i]:
#         print(" not palindrom")
#         f= True
#         break
#     i+=1
#     j-=1
reversed_str = words[::-1]
p = (words == words[::-1])
if (p):
    print ("pallindrom")
else :
    print("Not a pallindrom")
    
print(f"Reversed: {text[::-1]}")


