

def split_and_join(line):
    # write your code here
    new_line = ""
    for c in line:
         new_line += "-" if c == " " else c
    return new_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)