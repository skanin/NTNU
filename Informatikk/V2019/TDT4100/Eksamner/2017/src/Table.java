import java.util.Comparator;

public class Table implements Comparable<Table> {

    private int capacity;
    private static int NUMCOUNTER = 1;

    private final int num;

    public Table(int capacity){
        this.capacity = capacity;

        this.num = NUMCOUNTER++;
    }

    public int getCapacity(){
        return this.capacity;
    }

    public int getNum(){
        return this.num;
    }

    @Override
    public int compareTo(Table t1){
        return getCapacity() - t1.getCapacity();
    }

    public static void main(String[] args){
        Table t = new Table(4);
        System.out.println(t.getNum());
        Table t1 = new Table(5);
        System.out.println(t1.getNum());
    }
}
