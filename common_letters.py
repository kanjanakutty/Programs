#Write a python program to find out common letters between 2 strings
def common_letters():
    str1=input("Enter the string1:  ")
    str2=input("Enter the string2:  ")
    s1=set(str1)
    s2=set(str2)
    print(s1)
    print(s2)
    common_letter=s1&s2
    print(common_letter)
common_letters()
a="naina"
b="reene"
