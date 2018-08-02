s = input()
count = 0
i = 0
j = 1
k = 2
while j < (len(s)):
    if s[i] == 'b' and s[j] == 'o' and s[k] == 'b':
        count=count+1
    i = i + 1
    j = j + 1
    k = k + 1
print(count)
