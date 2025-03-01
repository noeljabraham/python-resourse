# todo find the first non repeated character

word="tetterzazaz"

for char in word:
    if word.count(char) ==1:
        print(char)
        break