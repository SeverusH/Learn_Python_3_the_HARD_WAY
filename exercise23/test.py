import sys
script, input_file = sys.argv


def main(language_file):
    line = language_file.readline()
    if line:
        cooked_string = line.strip()
        raw_bytes_utf_8 = cooked_string.encode("utf-8")
        raw_bytes_utf_16 = cooked_string.encode("utf-16")
        raw_bytes_utf_32 = cooked_string.encode("utf-32")
        #raw_bytes_big5 = cooked_string.encode("big5")

        print(cooked_string)
        print(raw_bytes_utf_8)
        print(raw_bytes_utf_16)
        print(raw_bytes_utf_32)
        #print(raw_bytes_big5)
        print()

        main(language_file)

language_file = open(input_file, encoding = "utf-8")

main(language_file)

language_file.close()
