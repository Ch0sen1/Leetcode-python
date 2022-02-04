class Twitter:

    def __init__(self):
        self.time = 0
        self.follower_followee = defaultdict(set)
        self.user_tweets = defaultdict(deque)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        tweets = self.user_tweets[userId]
        tweets.append((self.time, tweetId))
        if len(tweets) > 10:
            tweets.popleft()
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        feed.extend(self.user_tweets[userId])
        heapify(feed)
        for user in self.follower_followee[userId]:
            tweets = self.user_tweets[user]
            for i in range(len(tweets)-1, -1, -1):
                if len(feed) < 10:
                    heappush(feed, tweets[i])
                else:
                    if feed[0][0] < tweets[i][0]:
                        heappushpop(feed, tweets[i])
                    else:
                        break
        return [heappop(feed)[1] for i in range(len(feed))][::-1]
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId != followeeId:
            self.follower_followee[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followerId != followeeId:
            self.follower_followee[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)