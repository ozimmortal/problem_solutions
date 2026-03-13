class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        initial = Counter()

        for b in bills:
            if b == 10:
                if 5 in initial:
                    initial[5] -= 1
                    initial[b] += 1
                    if initial[5] == 0:
                        del initial[5]
                else:
                    return False
                    
            elif b == 20:
                if 5 in initial:
                    if 10 in initial:
                        initial[5] -= 1
                        initial[10] -= 1
                        initial[b] += 1
                        if initial[5] == 0:
                            del initial[5]
                        if initial[10] == 0:
                            del initial[10]
                    elif initial[5] >= 3:
                        initial[5] -= 3
                        initial[b] += 1
                        if initial[5] == 0:
                            del initial[5]
                    else:
                        return False
                else:
                    return False
            else:
                initial[b] += 1
        return True
        