class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            function_id, function_type, function_time = log.split(":")
            fid = int(function_id)
            ftime = int(function_time)
            
            if function_type == "start":
                if stack:
                    res[stack[-1]] += ftime - prev_time 
                stack.append(fid)
                prev_time = ftime
            if function_type == "end":
                res[stack.pop()] += ftime - prev_time + 1
                prev_time = ftime + 1
        
        return res