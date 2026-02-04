class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        output = []
        new_code_line = ""
        open_comment_block = False


        for line in source:
            i = 0
            n = len(line)

            while i < n:
                if open_comment_block:

                    if i + 1 < n and line[i] == "*" and line[i + 1] == "/":
                        open_comment_block = False
                        i += 2
                    else:
                        i += 1
                else:
                    if i + 1 < n and line[i] == "/" and line[i + 1] == "*":
                        open_comment_block = True
                        i += 2
                    elif i + 1 < n and line[i] == "/" and line[i + 1] == "/":
                        break
                    else:
                        new_code_line += line[i]
                        i += 1
                    

            if not open_comment_block and new_code_line:
                output.append(new_code_line)
                new_code_line = ""
        return output





        