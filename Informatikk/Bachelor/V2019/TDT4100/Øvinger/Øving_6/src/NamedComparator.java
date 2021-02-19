import java.util.Comparator;

public class NamedComparator implements Comparator<Named> {

    @Override
    public int compare(Named p1, Named p2){
        if(p1.getFamilyName().compareTo(p2.getFamilyName()) == 0){
            return p1.getGivenName().compareTo(p2.getGivenName());
        }
        return p1.getFamilyName().compareTo(p2.getFamilyName());
    }


    public static void main(String[] args){


    }

}
