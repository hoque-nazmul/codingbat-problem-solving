def missing_char(str, n):
    if n in range(len(str)):
        li = list(str)
        li.pop(n)
        return ''.join(li)

print(missing_char('kitten', 1) )
print(missing_char('kitten', 0) )
print(missing_char('kitten', 4) )