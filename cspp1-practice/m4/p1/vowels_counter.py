s = input()
i = 0
count = 0
while i<len(s):
    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
            count = count + 1
    i = i + 1
print(count)
