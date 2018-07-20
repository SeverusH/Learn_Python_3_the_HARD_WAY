i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers: print(num)

# The following is the extra exercise.

numbers = []

def while_loop_print(range, step):
    i = 0
    while i < range:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
        print(f"i = {i}, Numbers = {numbers}")

while_loop_print(5, 2)
