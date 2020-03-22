import java.io.*;
import java.util.HashMap;

public class Store {

    private HashMap<Item, Integer> storage = new HashMap<>();
    private String name;

    public Store(String name){
        this.name = name;
    }

    public String getName(){
        return name;
    }

    public void addItem(Item item, int quantity){
        storage.put(item, quantity);
    }

    public int getQuantity(Item item){
        if(storage.containsKey(item)) return storage.get(item);
        return 0;
    }

    public void load(InputStream inputStream) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(inputStream));

        while(br.ready()){
            String line = br.readLine();
            int colonPos = line.indexOf(':');
            int hyphenPos = line.indexOf('-');

            String name = line.substring(0, colonPos);
            int price = Integer.parseInt(line.substring(colonPos+1, hyphenPos));
            int quantity = Integer.parseInt(line.substring(hyphenPos+1));

            storage.put(new Item(name, price), quantity);
        }
        br.close();
    }

    public void save(String out) throws IOException{
        BufferedWriter bw = new BufferedWriter(new FileWriter(out));

        for(Item i : storage.keySet()){
            bw.write(i.getName() + ":" + i.getPrice() + "-" + storage.get(i) + "\n");
        }

        bw.close();
    }

    public void printItems(){
        for(Item i : storage.keySet()){
            System.out.println(i.getName() + ":" + i.getPrice() + "-" + storage.get(i));
        }
    }

    private boolean hasMore(Item i){
        return getQuantity(i) > 0;
    }

    public void removeItem(Item item){
        if(storage.containsKey(item) && hasMore(item)) addItem(item, getQuantity(item)-1);
    }

    public static void main(String[] args){
        Store s = new Store("Rema1000");
        try{
            s.load(new FileInputStream("src/items.txt"));
        } catch(IOException e){
            System.out.println(e);
        }

        s.printItems();

    }

}
