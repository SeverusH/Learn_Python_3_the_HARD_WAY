bool1 = True and True
print(bool1 == True)
bool2 = False and True
print(bool2 == False)
bool3 = 1 == 1 and 2 == 1
print(bool3 == False)
bool4 = "test" == "test"
print(bool4 == True)
bool5 = 1 != 0 and 2 == 1
print(bool5 == False)
bool6 = True and 1 == 1
print(bool6 == True)
bool7 = False and 0 != 0
print(bool7 == False)
bool8 = True or 1 == 1
print(bool8 == True)
bool9 = "test" != "testing"
print(bool9 == True)
bool10 = 1 != 0 and 2 == 1
print(bool10 == False)
bool11 = "test" != "testing"
print(bool11 == True)
bool12 = "test" == 1
print(bool12 == False)
bool13 = not (True and False)
print(bool13 == True)
bool14 = not (1 == 1 and 0 != 1)
print(bool14 == False)
bool15 = not (10 == 1 or 1000 == 1000)
print(bool15 == False)
bool16 = not (1 != 10 or 3 == 4)
print(bool16 == False)
bool17 = not ("testing" == "testing" and "Zed" == "Cool Guy")
print(bool17 == True)
bool18 = 1 == 1 and not ("testing" == 1 or 1 == 0)
print(bool18 == True)
bool19 = "chunky" == "bacon" and not (3 == 4 or 3 == 3)
print(bool19 == False)
bool20 = 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
print(bool20 == False)

print("test" and "test")
print("" and "test")
print(1 and 1)
print(False and input("> "))
print(True or input("> "))
print("" or "test")
print("" or 0)
print("test" or input("> "))
