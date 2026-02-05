class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        matches = {}
        output = []
        for p in paths:
            s = p.split(" ")
            root = s[0]
            for f in s[1:]:
                openI = f.find("(")
                closeI = f.find(")")
                content = f[openI+1:closeI+1]
                f_name = root + "/" + f[:openI] 

                if content not in matches:
                    matches[content] = []
                matches[content].append(f_name)
        for k in matches:
            if len(matches[k]) > 1:
                output.append(matches[k])
        return output


        