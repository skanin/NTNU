package interfaces.twitter;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

import com.google.common.collect.Lists;

public class TwitterAccount {
	
	private String username;
	private List<TwitterAccount> following;
	private List<TwitterAccount> followers;
	protected List<Tweet> tweets; 
	protected List<Tweet> reTweets;
	
	public TwitterAccount(String username) {
		this.username = username;
		this.following = new ArrayList<TwitterAccount>();
		this.followers = new ArrayList<TwitterAccount>();
		this.tweets = new ArrayList<Tweet>();
		this.reTweets = new ArrayList<Tweet>();
	}
	
	public String getUserName() {
		return this.username;
	}
	
	public void follow(TwitterAccount account) {
		if(!isFollowing(account) && this.username != account.getUserName()) {
			following.add(account);
			account.followers.add(this);
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
			account.followers.remove(this);
		}else {
			System.out.println("You are not following " + account.getUserName());
		}
	}
	
	public boolean isFollowing(TwitterAccount account) {
		return following.contains(account);
	}
	
	public boolean isFollowedBy(TwitterAccount account) {
		return followers.contains(account);
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
	
	public int getFollowerCount() {
		return followers.size();
	}
	
	public List<TwitterAccount> getFollowers(Comparator<TwitterAccount> comp){
		List<TwitterAccount> sorted = this.followers;
		if(comp == null) {
			return this.followers;
		}else {
			Collections.sort(sorted, comp);
			return sorted;
		}
	}
	
	public static void main(String[] args) {
		TwitterAccount Nils = new TwitterAccount("Nils");
		TwitterAccount Kari = new TwitterAccount("Kari");
		TwitterAccount Ole = new TwitterAccount("Ole");
		TwitterAccount Sander = new TwitterAccount("Sander");
		
		Sander.follow(Ole);
		
		Nils.follow(Ole);
		Kari.follow(Ole);
		
		System.out.println(Ole.followers);
		System.out.println("Kari: " + Kari);
		System.out.println("Nils: " + Nils);
		UserNameComparator u = new UserNameComparator();
		System.out.println(Sander.getFollowers(null));
	}
}
