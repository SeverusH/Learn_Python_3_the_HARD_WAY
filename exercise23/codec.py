import sys
script, input_file, ouput_file = sys.argv


def main(utf_8_file, bytes_file):
    line = utf_8_file.readline()
    if line:
        cooked_string = line.strip()
        raw_bytes = cooked_string.encode("utf-8")
        bytes_file.write(repr(raw_bytes) + "\n")

        main(utf_8_file, bytes_file)

utf_8_file = open(input_file, encoding = "utf-8")
bytes_file = open(ouput_file, 'w')
main(utf_8_file, bytes_file)
utf_8_file.close()
bytes_file.close()
