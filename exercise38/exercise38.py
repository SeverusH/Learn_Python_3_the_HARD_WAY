ten_things = "Apples Oranges Crows Telephone Light Sugar"
print(">>>>ten_things =", ten_things)

print("Wait there are not ten things in that list. Let's fix that.")

stuff = ten_things.split(' ')
print(">>>>stuff =", stuff)
more_stuff = ["Day", "Night", "song", "Frisbee",
                "Corn", "Banana", "Girl", "Boy"]
print(">>>>more_stuff =", more_stuff)

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
    print(f">>>>The {len(stuff)} items are:", stuff)
print(f"<<<<While-Loop-End<<<<")

print("There we go:", stuff)

print("Let's do some things with the stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar
