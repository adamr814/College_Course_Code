def greet(person, first_time=False):
    if first_time:
        return "First time for everything, right? Welcome " + person
    return "Hello, " + person

def greet_all(people):
    for person in people:
        print(greet(person, True))
    
friends = ["Bob", "Josh",  "Austin"]

greet_all(friends)