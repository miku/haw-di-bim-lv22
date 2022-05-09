
rooms = {
    "A": {
        "N": "B",
        "E": "C",
        "desc": "a green room",
    },
    "B": {
        "S": "A",
        "W": "D",
        "desc": "here only a dim light is burning",
    },
    "C": {
        "W": "A",
        "desc": "a room with a single door",
    },
    "D": {
        "E": "B",
        "desc": "nothing to see here"
    }
}

current = "A"

while True:
    r = rooms[current]
    print(r["desc"])
    for k, v in r.items():
        if not k.isupper():
            continue
        print("  There is a door towards {}".format(k))
    
    dir = input()
    current = rooms[current][dir.strip()]
