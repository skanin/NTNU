import java.util.HashMap;

public class Menu {

    /*
    private HashMap<Course, Double> courses;
    private HashMap<Meal, Double> meals;


    public double getPrice(Course c) throws IllegalArgumentException {
        if(!courses.containsKey(c)) throw new IllegalArgumentException();
        return courses.get(c);
    }

    public void updatePrice(Course c, double price){
        courses.put(c, price);
    }

    public double getPrice(Meal m) throws IllegalArgumentException {
        if(!meals.containsKey(m)) throw new IllegalArgumentException();
        double total = meals.get(m);
        if(total == 0.0) for(Course c : m) total += getPrice(c);
        return total;
    }

    public void updatePrice(Meal meal, double price) {
        meals.put(meal, price);
    }
    */

    private HashMap<MenuItem, Double> items = new HashMap<>();

    public double getPrice(Course c) throws IllegalArgumentException {
        if(!items.containsKey(c)) throw new IllegalArgumentException();

        return items.get(c);

    }

    public void updatePrice(MenuItem item, double price){
        items.put(item, price);
    }

    public double getPrice(Meal m){
        if(!items.containsKey(m)) throw new IllegalArgumentException();
        double total = items.get(m);
        if(total == 0.0) for(Course c : m) total += getPrice(c);
        return total;
    }

}
