# int

a = 1
b = 2
c = a + b

print(c)

# float

f = 1.0
g = 2.0
h = f * g

print(h)

# string, formatting

s = "hello world"
name = "martin"
t = "hello {}".format(name)
print(t)

# bool

u = True
v = False
w = u and v
x = u or v

print(w)
print(x)

# list

l = ["a", "b", "c"]
print(len(l), l)
l.append("d")
print(len(l), l)

for v in l:
    print(v)
    
for i, v in enumerate(l):
    print(i, v)

# tuple

fixed = ("a", "b", "c")
# fixed.append("d") # TypeError

# dictionary

menu = {
    "pizza": 8.5,
    "water": 2.5,
}

order = ["pizza", "pizza", "water"]

total = 0
for item in order:
    total = total + menu[item]

print("total: {}".format(total))

for k, v in menu.items():
    print(k, v)


# set

a = set([1, 2, 2, 3, 3, 4])
print(a)

b = set([4, 5, 6])
print(b)

print(a.union(b))
print(a.intersection(b))