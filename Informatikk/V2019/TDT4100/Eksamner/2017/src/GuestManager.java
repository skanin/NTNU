import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class GuestManager implements CapacityListener{

    private Diner diner;
    private List<Group> queue = new ArrayList<Group>();

    public GuestManager(Diner diner){
        this.diner = diner;
    }


    public void groupArrived(Group group){
        if(!diner.addSeating(group)) queue.add(group);
    }


    public void groupDeparted(int tableNum){
        diner.removeSeating(tableNum);
    }

    @Override
    public void capacityChanged(Diner diner) {
        Collection<Group> q = new ArrayList<>(queue);
        queue.clear();
        while(q.iterator().hasNext()){
            Group g = q.iterator().next();
            if(diner.addSeating(g)){
                q.iterator().remove();
            }
        }
        queue.addAll(q);
    }
}
