import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class ObservableHighscoreList {

    private final int maxSize;
    private List<Integer> list;
    private List<ObservableListListener> listeners = new ArrayList<>();

    public ObservableHighscoreList(int maxSize){
        this.maxSize = maxSize;
        this.list = new ArrayList<>(10);
    }

    public int size(){
        return list.size();
    }

    public int getElement(int i){
        if(i < 0 || i > size() - 1) throw new IllegalArgumentException("Out of bounds");
        return list.get(i);
    }

    public void addResult(int result){
        if(result < list.get(size() - 1) || size() < maxSize){
            for(int i = 0; i < size(); i++){
                if(result < list.get(i)) {
                    list.add(i, result);
                    fireListChanged(this, i);
                }
            }
            if(size() > maxSize) list.remove(size() - 1);
        }
    }

    private void fireListChanged(ObservableHighscoreList list, int pos){
        for(ObservableListListener l : listeners){
            l.listChanged(list, pos);
        }
    }

    public void printList(){
        for(int i : list){
            System.out.println(i);
        }
    }


    public static void main(String[] args){
        ObservableHighscoreList list = new ObservableHighscoreList(2);
        System.out.println(list.size());
        list.addResult(5);
        list.addResult(9);
        list.addResult(1);

        list.printList();
    }

}
