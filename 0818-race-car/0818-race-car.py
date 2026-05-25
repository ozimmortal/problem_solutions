class Solution:
    def racecar(self, target: int) -> int:
        #               start, step, speed
        queue = deque([( 0 ,    0 ,  1)])
        seen = {(0,1)}
        while queue:

            pos , step , speed = queue.popleft()
            if pos == target:
                return step
            
            for instruction in ["A", "R"]:
                if instruction == "A":
                    if (pos + speed , speed * 2) not in seen:
                        queue.append((pos + speed , step + 1 , speed * 2))
                        seen.add((pos + speed , speed * 2))


                if instruction == "R":
                    if (pos, -1 if speed > 0 else 1) not in seen:
                        queue.append((pos , step + 1 , -1 if speed > 0 else 1 ))
                        seen.add((pos , -1 if speed > 0 else 1))