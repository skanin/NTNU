public class Seating {

    private final Table table;
    private final Group group;

    public Seating(Table table, Group group){
        if(table.getCapacity() < group.getGuestCount()) throw new IllegalArgumentException();
        this.table = table;
        this.group = group;
        this.group.setSeating(this);
    }

    public Table getTable(){
        return this.table;
    }

    public Group getGroup(){
        return this.group;
    }
}
