import re

#search method
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
#Only the first occurance of match

x = re.search("Portugal", txt)
print(x) #Returns None

#findall method
print(f"The original text is: {txt}")
x = re.findall("ai", txt)
print(x) #Returns a list

x = re.findall("Portugal", txt)
print(x) #Empty List

#split method (same as string.split())
x = re.split("\s", txt)
print(x)

#split with maxsplit parameter 
x = re.split("\s", txt, 1)
print(x)

#sub method
x = re.sub("\s", "9", txt)
print(x)

#sub method with count parameter
x = re.sub("\s", "9", txt, 2)
print(x)

############################################
'''
Match Object

object containing information 
about the search and the result.

.span() 
returns a tuple containing 
the start-, and end positions of the match.

.string 
returns the string passed into the function

.group() 
returns the part of the string 
where there was a match
'''
#search method
x = re.search("^The.*Spain$", txt) 
print(x)

x = re.search(r"\bS\w+", txt)
print(x.span())

x = re.search(r"\bS\w+", txt)
print(x.string)

x = re.search(r"\bS\w+", txt)
print(x.group())

############################################
'''
Meta Characters

characters with special meaning

[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"world$"	
*	Zero or more occurrences	"aix*"	
+	One or more occurrences	"aix+"	
{}	Exactly the specified number of occurrences	"al{2}"	
|	Either or	"falls|stays"

Special Sequences

a \ followed by a character in the list below for a special purpose

\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string

Sets

a set of characters inside [] with a special meaning

[arn]	Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
