import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class TwitterAccount {

    private String username;
    private Collection<TwitterAccount> following;
    private Collection<TwitterAccount> followers;

    private List<Tweet> tweets = new ArrayList<>();

    public TwitterAccount(String username){
        this.username = username;
        this.following = new ArrayList<>();
        this.followers = new ArrayList<>();
    }

    public String getUsername(){
        return this.username;
    }

    public void follow(TwitterAccount twitterAccount) {
        if(this == twitterAccount) throw new IllegalArgumentException();
        if(!isFollowing(twitterAccount)){
            following.add(twitterAccount);
            twitterAccount.addFollower(this);
        }
    }

    private void addFollower(TwitterAccount ta){
        if(!isFollowedBy(ta)) followers.add(ta);
    }

    public void unfollow(TwitterAccount ta){
        following.remove(ta);
        ta.followers.remove(this);
    }

    public boolean isFollowing(TwitterAccount ta){
        return following.contains(ta);
    }

    public boolean isFollowedBy(TwitterAccount ta){
        return followers.contains(ta);
    }


    public void Tweet(String text){
        this.tweets.add(new Tweet(this, text));
    }

    public void reTweet(Tweet tweet){
        this.tweets.add(new Tweet(this, tweet));
    }

    public Tweet getTweet(int i) {
        if(i < 1 || i > getTweetCount()) throw new IllegalArgumentException();
        return tweets.get(getTweetCount() - i);
    }


    public int getTweetCount(){
        return this.tweets.size();
    }

    public int getFollowerCount(){
        return followers.size();
    }

    public int getRetweetCount(){
        int total = 0;
        for(Tweet t : tweets){
            total += t.getRetweetCount();
        }
        return total;
    }

    public Collection<TwitterAccount> getFollowers(Comparator<TwitterAccount> comparator){
        return comparator == null ? followers : followers.stream().sorted(comparator).collect(Collectors.toList());
    }


    @Override
    public String toString(){
        return this.username;
    }

    public static void main(String[] args){
        TwitterAccount ta = new TwitterAccount("Sander");
        TwitterAccount ta1 = new TwitterAccount("Sara");
        TwitterAccount ta2 = new TwitterAccount("Anders");

        ta1.follow(ta);
        ta2.follow(ta);

        UsernameComparator comp = new UsernameComparator();
        System.out.println(ta.getFollowers(comp));
    }

}
