public class Tweet {

    private TwitterAccount owner;
    private String text;
    private boolean retweet = false;
    private Tweet retweeted;
    private int retweetCount = 0;
    private static int COUNT = 0;

    public Tweet(TwitterAccount ta, String text){
        this.owner = ta;
        this.text = text;
    }

    public Tweet(TwitterAccount ta, Tweet t){
        if(ta == t.getOwner()) throw new IllegalArgumentException();
        this.owner = ta;
        this.text = t.text;
        this.retweeted = t;
        t.retweetCount++;
    }

    public String getText(){
        return this.text;
    }

    public TwitterAccount getOwner(){
        return this.owner;
    }

    public Tweet getOriginalTweet(){
        if(this.retweeted == null) return this;
        Tweet t = this;
        while(t.retweeted != null){
            t = t.retweeted;
        }
        return t;
    }

    public int getRetweetCount(){
        return this.retweetCount;
    }


    public static void main(String[] args){
        TwitterAccount ta = new TwitterAccount("Sander");
        TwitterAccount ta1 = new TwitterAccount("Sara");

        Tweet t = new Tweet(ta, "Hei");
        Tweet t1 = new Tweet(ta1, t);
        Tweet t2 = new Tweet(ta1, t);

        System.out.println(t);
        System.out.println(t2.getOriginalTweet());
    }
}
