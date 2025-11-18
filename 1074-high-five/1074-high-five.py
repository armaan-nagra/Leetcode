class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        id_score = {}

        for s_id, s_score in items:
            if s_id not in id_score:
                id_score[s_id] = []
            heapq.heappush(id_score[s_id], s_score)
                
            if len(id_score[s_id]) > 5:
                heapq.heappop(id_score[s_id])

        result = []

        for s_id in sorted(id_score.keys()):
            top_five = id_score[s_id]
            avg = sum(top_five) // len(top_five)
            result.append([s_id, avg])
        
        return result
                

        
        
            
