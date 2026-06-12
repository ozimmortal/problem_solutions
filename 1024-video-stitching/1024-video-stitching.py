class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()

        count = 0
        start , end = -1 , 0
        for clip in clips:
            if clip[0] > end or end >= time:
                break
            elif start < clip[0] <= end:
                count += 1
                start = end

            end = max(end , clip[1])
        
        return count if end >= time else -1
            
        