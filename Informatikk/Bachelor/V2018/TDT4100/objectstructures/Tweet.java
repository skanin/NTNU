package objectstructures;

public class Tweet {
	private Tweet orig;
	private String tweetText;
	private TwitterAccount account;
	private Tweet tweet;
	private int count;
	private boolean isRewteet = false;
	
	public Tweet(TwitterAccount account, String tweetText) {
		this.account = account;
		this.tweetText = tweetText;
		account.tweets.add(this);
	}
	
	public Tweet(TwitterAccount account, Tweet tweet) {
		if(tweet.account == account) {
			throw new IllegalArgumentException("Can't retweet your own tweet");
		}
		this.isRewteet = true;
		this.account = account;
		this.tweet = tweet;
		tweet.count += 1;
		this.tweetText = tweet.getText();
		if(tweet.getOriginalTweet() != null) {
			Tweet temp = tweet.getOriginalTweet();
			for(int i = 0; i < count; i++) {
				temp = temp.getOriginalTweet();
			}
			temp.getOwner().reTweets.add(this);
		}else {
			tweet.getOwner().reTweets.add(this);
		}
		account.tweets.add(this);
	}
	
	public String getText() {
		return tweetText;
	}
	
	public TwitterAccount getOwner() {
		return account;
	}
	
	
	public Tweet getOriginalTweet() {
		if(tweet != null) {
			if(tweet.getOriginalTweet() == null) {
				orig = tweet;
				return orig;
			}else {
				return tweet.getOriginalTweet();
			}
		}
		return null;
	}
	
	public int getRetweetCount() {
		return count;
	}
}
