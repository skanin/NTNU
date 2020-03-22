package interfaces.twitter;

import java.util.Comparator;

public class UserNameComparator implements Comparator<TwitterAccount>{

	@Override
	public int compare(TwitterAccount arg0, TwitterAccount arg1) {
		return arg0.getUserName().compareTo(arg1.getUserName());
	}
}
