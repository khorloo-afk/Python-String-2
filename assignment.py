# You can remove 'pass' if you written code in the function 

# Exercise 1
def is_valid_email(text):
    at=False
    dot=False
    for i in range(len(text)):
        if text[i]=="@":
            at=True
        if text[i]==".":
            dot=True
    if at and dot:
        return "Valid"
    return "Invalid"
# Exercise 2
def remove_vowels(text):
    vowels="aeiouAEIOU"
    s=""
    for i in range(len(text)):
        if text[i] not in vowels:
            s=s+text[i]
    return s

# Exercise 3
def get_initials(text):
    split = text.split()
    print(split[0].upper()[0] + "." + split[1].upper()[0] + ".")
# Exercise 4
def extract_year(text):
    # Write your code here
    pass

# Exercise 5
def is_palindrome(text):
    # Write your code here
    pass

