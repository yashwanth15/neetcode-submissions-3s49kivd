import time
class Twitter:

    def __init__(self):
        self.adj=defaultdict(set)
        self.posts=defaultdict(list)
        self.t=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.adj[userId].add(userId)
        self.posts[userId].append((self.t,tweetId))
        self.t-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        followPosts=[]
        for f in self.adj[userId]:
            posts = self.posts[f]
            idx=len(posts)-1
            t, tweetId = posts[idx]
            heapq.heappush(followPosts, (t, tweetId, f, idx - 1))
        res=[]
        while len(res)<10 and len(followPosts)>0:
            t, tweetId, f, idx = heapq.heappop(followPosts)
            res.append(tweetId)
            if idx>=0:
                t2, tweetId2 = self.posts[f][idx]
                heapq.heappush(followPosts, (t2, tweetId2, f, idx - 1)) 
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.adj[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.adj[followerId].discard(followeeId)
