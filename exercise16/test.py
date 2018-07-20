from sys import argv

script, filename = argv

reader = open(filename, 'r')
writer = open(filename, 'w')

print("Open:", reader.read())

txt = input("Write > ")
writer.write(txt)

print("Written:", reader.read())

writer.close()

print("Closed:", reader.read())

reader.close()
