formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

lines = (
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)

print(lines)
print(*lines)
print(formatter.format(*lines))
# print(formatter.format(lines))

lines2 = {  # 花括号似乎并不表示数组
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
}

print(lines2)
print(*lines2)
print(formatter.format(*lines2))
# print(formatter.format(lines))

print(repr(lines))
# print(repr(*lines))
