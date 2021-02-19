import java.util.Comparator;

public class UsernameComparator implements Comparator<TwitterAccount> {

    @Override
    public int compare(TwitterAccount acc1, TwitterAccount acc2){
        return acc1.getUsername().compareTo(acc2.getUsername());
    }

}
