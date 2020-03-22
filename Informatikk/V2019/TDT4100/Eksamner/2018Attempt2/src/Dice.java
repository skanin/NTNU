import java.util.ArrayList;
import java.util.Collection;
import java.lang.Math;
import java.util.Iterator;
import java.util.List;

public class Dice implements Iterable<Integer> {

    private final List<Integer> dieValues = new ArrayList<>();
    private int score = -1;

    public Dice(Collection<Integer> dieValues, int score){
        for(int i : dieValues){
            if(i < 1 || i > 6) {
                throw new IllegalArgumentException("");
            }
        }
        for(int d : dieValues){
            this.dieValues.add(d);
        }
        this.score = score;
    }

    public Dice(int dieCount){
        this(randomDieValues(dieCount), -1);
    }


    public Dice(Dice dice, int score){
        this(dice.dieValues, score);
    }

    @Override
    public String toString(){
        String temp = "[";

        for(int i = 0; i < dieValues.size(); i++){
            if(i == dieValues.size()-1){
                temp += score > -1 ? dieValues.get(i) + "] = " + score : dieValues.get(i) + "]";
            }else {
                temp += dieValues.get(i) + ", ";
            }
        }

        return temp;
    }

    public static Dice valueOf(String s){
        String s2 = s.strip();
        String[] values = s2.substring(s.indexOf('[')+1, s2.indexOf(']')).split(",");
        String score = s2.indexOf('=') != -1 ? s2.substring(s2.indexOf('=')+1).strip() : "-1";
        Collection<Integer> dieValues = new ArrayList<>();

        try{
            for(String value : values){
                dieValues.add(Integer.parseInt(value.strip()));
            }
            return new Dice(dieValues, Integer.parseInt(score));
        } catch (NumberFormatException e){
            throw new IllegalArgumentException("Invalid format");
        }
    }


    public static Collection<Integer> randomDieValues(int dieCount){
        Collection<Integer> temp = new ArrayList<>();
        for(int i = 0; i < 6; i++){
            temp.add((int) (Math.random()*6 + 1));
        }

        return temp;
    }

    public int getDieCount(){
        return this.dieValues.size();
    }

    public int getDieValue(int dieNum){
        if(dieNum < 0 || dieNum > getDieCount()) throw new IllegalArgumentException("");
        return dieValues.get(dieNum);
    }

    public int getValueCount(int value){
        int count = 0;
        for(int i = 0; i < getDieCount(); i++){
            count += value == getDieValue(i) ? 1 : 0;
        }
        return count;
    }

    public int getScore(){
        return this.score;
    }

    public void setScore(int score){
        if(this.score > -1) throw new IllegalArgumentException("");
        this.score = score;
    }

    public Dice add(Dice dice){
        Collection<Integer> dieValues = new ArrayList<>();
        dieValues.addAll(dice.dieValues);
        dieValues.addAll(this.dieValues);
        return new Dice(dieValues, -1);
    }

    public Dice remove(Dice dice){
        Collection<Integer> dieValues = new ArrayList<>(this.dieValues);
        for(int value : dice.dieValues){
            dieValues.remove(value);
        }
        return new Dice(dieValues, -1);
    }

    @Override
    public Iterator<Integer> iterator(){
        return dieValues.iterator();
    }

    public static void main(String[] args){
        Dice d = new Dice(Dice.randomDieValues(6), 6);
        System.out.println(Dice.valueOf("[1, 2, 1, 6, 4, 3] = 6"));
    }


}
