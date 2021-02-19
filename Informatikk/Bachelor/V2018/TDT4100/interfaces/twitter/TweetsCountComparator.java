package interfaces.twitter;

import java.util.Comparator;

public class TweetsCountComparator implements Comparator<TwitterAccount>{

	@Override
	public int compare(TwitterAccount arg0, TwitterAccount arg1) {
		return arg1.getTweetCount() - arg0.getTweetCount();
	}
	public static void main(String[] args) {
		TwitterAccount t1 = new TwitterAccount("Sander");
		TwitterAccount t2 = new TwitterAccount("Marcus");
		
		t1.tweet("Yo");
		TweetsCountComparator u = new TweetsCountComparator();
		System.out.println(u.compare(t1, t2));
	}
}
