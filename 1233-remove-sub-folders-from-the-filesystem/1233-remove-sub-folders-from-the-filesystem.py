class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        folder_set = set(folder)
        res = []

        for f in folder:
            res.append(f)
            prefix = ""
            for i in range(len(f)):
                if f[i] == "/" and prefix in folder_set:
                    res.pop()
                    break
                prefix += f[i]
        return res
        
