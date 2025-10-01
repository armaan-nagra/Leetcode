class Twitter(object):

    def __init__(self):
        self.follows = {} #userId -> (all the people this user follows)
        self.tweets = {} #user Id -> (time, tweet id)
        self.time = 0

    def postTweet(self, userId, tweetId):
        if not userId in self.tweets:
            self.tweets[userId] = [(self.time,tweetId)]
        else:
            self.tweets[userId].append((self.time,tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId):
        heap = []
        followees = self.follows.get(userId, set())
        users = followees | {userId}

        for uid in users:
            if uid in self.tweets and self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][idx]
                heapq.heappush(heap, (-time, tweetId, uid, idx))
        
        res = []
        while heap and len(res) < 10:
            neg_time, tweetId, uid, idx = heapq.heappop(heap)
            res.append(tweetId)

            if idx > 0:
                time, tweetId = self.tweets[uid][idx-1]
                heapq.heappush(heap, (-time, tweetId, uid, idx - 1))
        
        return res
        

    def follow(self, followerId, followeeId):
        if followerId not in self.follows:
            self.follows[followerId] = set([followeeId])
        else:
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)