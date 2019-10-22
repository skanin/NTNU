import java.io.FileOutputStream;
import java.io.IOException;
import java.util.HashMap;

public class ShoppingCart {

    private HashMap<Item, Integer> cart = new HashMap<>();
    private final Store store;

    public ShoppingCart(Store store){
        this.store = store;
    }

    public void addToCart(Item i){
        store.removeItem(i);
        if(!cart.containsKey(i)) cart.put(i, 0);
        cart.put(i, cart.get(i)+1);
    }

    public void removeFromCart(Item i){
        if(cart.containsKey(i)){
            if(cart.get(i) > 0){
                store.addItem(i, store.getQuantity(i)+1);
            }
        }
    }

    public void printCart(){
        for(Item i : cart.keySet()){
            System.out.println(i.getName() + ":" + cart.get(i));
        }
    }

    public static void main(String[] args){
        Item i1 = new Item("Bananas", 12);
        Item i2 = new Item("Apples", 20);
        Item i3 = new Item("Oranges", 15);
        Item i4 = new Item("Weed", 420);

        Store s = new Store("REMA1000");
        ShoppingCart sc = new ShoppingCart(s);

        s.addItem(i1, 5);
        s.addItem(i2, 5);
        s.addItem(i3, 3);
        s.addItem(i4, 1);

        try{
            s.save("src/Items2.txt");
        } catch (IOException e){
            System.out.println(e);
        }

        sc.addToCart(i1);
        try{
            s.save("src/Items2.txt");
        } catch (IOException e){
            System.out.println(e);
        }
        sc.printCart();
        s.printItems();
    }

}
