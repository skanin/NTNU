package interfaces.twitter;

import java.util.Comparator;

public class FollowersCountComparator implements Comparator<TwitterAccount>{

	@Override
	public int compare(TwitterAccount arg0, TwitterAccount arg1) {
		return arg1.getFollowerCount() - arg0.getFollowerCount();
	}
}
