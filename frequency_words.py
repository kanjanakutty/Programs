#Write a frequency of words in a string
flower =["orange", "grapes", "banana"  ,"orange"]
print(set(flower))

def freq_words():
    str=input("enter a string")
    li=str.split()
    print(li)
    d={}

    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)
freq_words()
