import java.util.Comparator;

public class TweetsCountComparator implements Comparator<TwitterAccount> {

    public int compare(TwitterAccount acc1, TwitterAccount acc2){
        if(acc1.getTweetCount() > acc2.getTweetCount()){
            return -1;
        }else if(acc1.getTweetCount() < acc2.getTweetCount()){
            return 1;
        }
        return 0;
    }
}
