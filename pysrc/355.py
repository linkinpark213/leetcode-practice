from typing import List


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = []
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        newsFeed = []
        ptr = len(self.tweets) - 1
        while len(newsFeed) < 10 and ptr >= 0:
            if self.tweets[ptr][0] == userId or (userId in self.follows and self.tweets[ptr][0] in self.follows[userId]):
                newsFeed.append(self.tweets[ptr][1])
            ptr -= 1
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.follows.keys():
            self.follows[followerId] = []
        self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.follows.keys():
            self.follows[followerId] = []
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


if __name__ == '__main__':
    twitter = Twitter()
    print(twitter.postTweet(1, 5))
    print(twitter.getNewsFeed(1))
    print(twitter.follow(1, 2))
    print(twitter.postTweet(2, 6))
    print(twitter.getNewsFeed(1))
    print(twitter.unfollow(1, 2))
    print(twitter.getNewsFeed(1))
