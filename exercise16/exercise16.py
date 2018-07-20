from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')  # 会清空文件
# target = open(filename, 'r+')
# print(target.read()) # 在'w'/'a'-Mode下无法 read()
# print("Truncating the file. Goodbye!")
# target.truncate() "w"-Mode打开文件已经清除文件，此行并不会清空文件。
# 上一行函数的作用是从文件开头截取（保留）至当前位置，并清除其余内容。
# print(target.read())
print("Now I'm going to ask you for three lines.")

txt = input("line1: ") + '\n'
# line1 = input("line1: ")
txt += input("line2: ") + '\n'
# line2 = input("line2: ")
txt += input("line3: ") + '\n'
# line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(txt)
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# print(target.read())
print("And finally, we close it.")
target.close()
