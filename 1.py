def convert_to_base10(string):
    base10_nums = []
    for char in string:
        if 'a' <= char <= 'z':
            base10_nums.append(ord(char) - ord('a') + 1)
    return base10_nums

string = "hello"
base10_nums = convert_to_base10(string)
print(base10_nums)
