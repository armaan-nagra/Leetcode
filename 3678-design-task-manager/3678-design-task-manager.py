class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        #use lazy deletion with hash map
        self.heap = []
        self.taskMap = {} #task id -> (userId, priority)
        for userId, taskId, priority in tasks:
            heapq.heappush(self.heap, [-priority, -taskId])
            self.taskMap[taskId] = (userId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.heap, [-priority, -taskId])
        self.taskMap[taskId] = (userId, priority)

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, currPriority = self.taskMap[taskId]
        self.taskMap[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, [-newPriority, -taskId])
                
    def rmv(self, taskId: int) -> None:
        del self.taskMap[taskId]
        

    def execTop(self) -> int: 
        while self.heap:
            negPriority, negTaskId = heapq.heappop(self.heap)
            taskId = -negTaskId
            priority = -negPriority

            if taskId not in self.taskMap:
                continue
            
            userId, currPriority = self.taskMap[taskId]

            if currPriority != priority:
                continue 
            
            del self.taskMap[taskId]
            return userId
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()