def count_vowel(text):
    vowel="AEIOUaeiou"
    count=0
    for i in text:
        if i in vowel:
            count+=1
    return count
m=count_vowel("hello")
print(m)