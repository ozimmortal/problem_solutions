def swap_case(s):
    new_string = ""
    for ch in s:
        if ch.isalpha():
            if ch.islower():
                new_string += ch.upper()
            else:
                new_string += ch.lower()
        else:
            new_string += ch
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)