import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;

public class Diner implements CapacityListener {
    private Collection<Table> tables = new ArrayList<Table>();
    private Collection<Seating> seatings = new ArrayList<Seating>();
    private List<CapacityListener> listeners = new ArrayList<>();

    public int getCapacity(boolean includeOccupied){
        if(includeOccupied) return tables.stream().mapToInt(Table :: getCapacity).sum();
        return tables.stream().filter(t -> !isOccupied(t)).mapToInt(Table :: getCapacity).sum();
    }

    public boolean isOccupied(Table table){
        return seatings.stream().anyMatch(s -> s.getTable() == table);
    }

    public void addTable(Table t){
        if(!tables.contains(t)) tables.add(t);
        capacityChanged(this);

    }

    public void removeTable(Table t){
        if(isOccupied(t)) throw new IllegalArgumentException();

        tables.remove(t);
        capacityChanged(this);
    }

    public void mergeTables(Table t1, Table t2, int lostCapacity){
        if(isOccupied(t1) || isOccupied(t2)) throw new IllegalArgumentException();
        Table newTable = new CompositeTable(t1, t2, lostCapacity);
        removeTable(t1);
        removeTable(t2);
        addTable(newTable);
        capacityChanged(this);
    }


    public void splitTable(CompositeTable t){
        if(isOccupied(t)) throw new IllegalArgumentException();
        removeTable(t);
        addTable(t.getT1());
        addTable(t.getT1());
        capacityChanged(this);
    }

    public boolean hasCapacity(Table t, int capacity){
        return !isOccupied(t) && t.getCapacity() >= capacity;
    }

    public Collection<Table> findAvailableTables(int cap){
        return tables.stream().filter(t -> hasCapacity(t, cap)).sorted().collect(Collectors.toList());
    }

    public Seating createSeating(Group group){
        return findAvailableTables(group.getGuestCount()).iterator().hasNext() ? new Seating(findAvailableTables(group.getGuestCount()).iterator().next(), group) : null;
    }

    public boolean addSeating(Group group){
        if(createSeating(group) == null) return false;
        seatings.add(createSeating(group));
        capacityChanged(this);
        return true;
    }

    public void removeSeating(int tableNum){
        for(Seating s : seatings){
            if(s.getTable().getNum() == tableNum){
                seatings.remove(s);
                return;
            }
        }
        capacityChanged(this);
    }

    public void capacityChanged(Diner diner){
        for(CapacityListener l : listeners){
            l.capacityChanged(diner);
        }
    }

    public static void main(String[] args){
        Diner d = new Diner();
        d.addTable(new Table(7));
        d.addTable(new Table(2));
        d.addTable(new Table(9));
        d.addTable(new Table(12));
        d.addTable(new Table(3));

        Collection<Table> tables = d.findAvailableTables(4);
        for (Table t : tables){
            System.out.println(t.getCapacity());
        }
    }

}
