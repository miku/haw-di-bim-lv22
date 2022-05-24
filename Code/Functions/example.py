def sum_of_first_n_integers(n):
    s = 0
    for i in range(1, n + 1):
      s += i
    return s

s = sum_of_first_n_integers(10)
print(s)


def underline(s, char="."):
    return s + "\n" + char * len(s)


print(underline("Hello World"))