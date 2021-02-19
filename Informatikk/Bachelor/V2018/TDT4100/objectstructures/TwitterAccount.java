package objectstructures;

import java.util.ArrayList;
import java.util.List;

import com.google.common.collect.Lists;

public class TwitterAccount {
	
	private String username;
	private List<TwitterAccount> following;
	private List<TwitterAccount> isFollowedBy;
	protected List<Tweet> tweets; 
	protected List<Tweet> reTweets;
	
	public TwitterAccount(String username) {
		this.username = username;
		this.following = new ArrayList<TwitterAccount>();
		this.isFollowedBy = new ArrayList<TwitterAccount>();
		this.tweets = new ArrayList<Tweet>();
		this.reTweets = new ArrayList<Tweet>();
	}
	
	public String getUserName() {
		return this.username;
	}
	
	public void follow(TwitterAccount account) {
		if(!isFollowing(account) && this.username != account.getUserName()) {
			following.add(account);
			account.isFollowedBy.add(this);
		}else {
			if(this.username == account.getUserName()) {
				System.out.println("You can't follow yourself");
			}else {
				System.out.println("You are already following " + account.getUserName());
			}
			
		}
	}
	
	public void unfollow(TwitterAccount account) {
		if(isFollowing(account) && this.username != account.getUserName()) {
			following.remove(account);
			account.isFollowedBy.remove(this);
		}else {
			System.out.println("You are not following " + account.getUserName());
		}
	}
	
	public boolean isFollowing(TwitterAccount account) {
		return following.contains(account);
	}
	
	public boolean isFollowedBy(TwitterAccount account) {
		return isFollowedBy.contains(account);
	}
	
	public void tweet(String text) {
		Tweet t = new Tweet(this, text);
	}
	
	public void retweet(Tweet tweet) {
		Tweet t = new Tweet(this, tweet);
	}
	
	 
	public Tweet getTweet(int i) {
		List<Tweet> reversed = new ArrayList<Tweet>();
		for(int j = tweets.size()-1; j >= 0; j--) {
			reversed.add(tweets.get(j));
		}
		return reversed.get(i-1);
	}
	
	public int getTweetCount() {
		return this.tweets.size();
	}
	
	public int getRetweetCount() {
		return this.reTweets.size();
	}
	
	public static void main(String[] args) {
		TwitterAccount Nils = new TwitterAccount("Nils");
		TwitterAccount Kari = new TwitterAccount("Kari");
		TwitterAccount Ole = new TwitterAccount("Ole");
		
		Nils.tweet("YO");
		System.out.println("Nils: " + Nils.getTweet(1));
		Ole.retweet(Nils.getTweet(1));
		System.out.println("Ole: " + Ole.getTweet(1));
		Kari.retweet(Ole.getTweet(1));
		System.out.println("Kari: " + Kari.getTweet(1));
		
		System.out.println("Ole original: " + Ole.getTweet(1).getOriginalTweet());
		System.out.println("Kari original: "  + Kari.getTweet(1).getOriginalTweet());
	}
}
