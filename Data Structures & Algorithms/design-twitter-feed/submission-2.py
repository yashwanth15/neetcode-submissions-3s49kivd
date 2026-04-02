import time
class Twitter:

    def __init__(self):
        self.adj=defaultdict(set)
        self.posts=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.adj[userId].add(userId)
        self.posts[userId].append((-1*time.time(),tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed=[]
        for followed in self.adj[userId]:
            feed.extend(self.posts[followed])
        heapq.heapify(feed)
        res=[]
        k=10
        while len(feed)>0 and k>0:
            timestamp, tweet=heapq.heappop(feed)
            res.append(tweet)
            k-=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.adj[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.adj[followerId].discard(followeeId)
