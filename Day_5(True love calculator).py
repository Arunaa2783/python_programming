print("Welcome to true love calculator!")
name1=input("Enter your name:\t")
name2=input("Enter their name:\t")
name=name1+name2
name=name.lower()
name=list(name)
s1=list("true")
s2=list("love")

number_of_char_in_true=0
number_of_char_int_love=0

for i in name:
    if i in s1 :
        # print(i,end="")
        number_of_char_in_true+=1
# print(number_of_char_in_true)

for i in name:
    if i in s2:
        # print(i,end="")
        number_of_char_int_love+=1
# print(number_of_char_int_love)
# print(f"Your love score is:{number_of_char_in_true}{number_of_char_int_love}")

love_score=number_of_char_in_true+number_of_char_int_love

if love_score>90:
    print(f"Your love score is {love_score} you both go together link cook and mentos")
elif 50<love_score<=90:
    print(f"Your love score is {love_score} perfect match")
elif 30<love_score<=50:
    print(f"Your love score is {love_score} not a perfect match")
else:
    print(f"Your love score is {love_score} you both are friends")



