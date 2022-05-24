class Module:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses
    
    def credits(self):
        return sum([c.credits for c in self.courses])

class Course:
    def __init__(self, name, credits):
        self.name = name
        if credits < 1:
            raise ValueError('credits must be greater than 0')
        self.credits = credits
        
        

it = Module("IT", [Course("Intro", 5), Course("Coding", 5)])

print(it.name)
print(it.credits())