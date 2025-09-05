import heapq

class Twitter:

    def __init__(self):
        self.users = {}
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = {'tweets': [], 'following': set()}
            self.users[userId]['following'].add(userId)
        self.users[userId]['tweets'].append((-self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        feed_heap = []
        for followeeId in self.users[userId]['following']:
            if followeeId in self.users:
                for tweet_tuple in self.users[followeeId]['tweets'][-10:]:
                    heapq.heappush(feed_heap, tweet_tuple)

        result = []
        while feed_heap and len(result) < 10:
            negative_timestamp, tweetId = heapq.heappop(feed_heap)
            result.append(tweetId)

        return result
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = {'tweets': [], 'following': set()}
            self.users[followerId]['following'].add(followerId)
        
        if followeeId not in self.users:
            self.users[followeeId] = {'tweets': [], 'following': set()}
            self.users[followeeId]['following'].add(followeeId)

        self.users[followerId]['following'].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users[followerId]['following'] and followerId != followeeId:
            self.users[followerId]['following'].remove(followeeId)