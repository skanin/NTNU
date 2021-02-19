import java.util.*;

public class Dice implements Iterable<Integer>{
    private List<Integer> dieValues = new ArrayList<Integer>();
    private int score = -1;

    public Dice(Collection<Integer> dieValues, int score){
        for(int value : dieValues){
            if(value < 1 || value > 6){
                throw new IllegalArgumentException();
            }
            dieValues.add(value);
        }
        this.score = score;
    }


    public Dice(int dieCount){
        this(Dice.randomDieValues(dieCount), -1);
    }

    public Dice(Dice dice, int score){
        this(dice.dieValues, score);
    }

    public static Collection<Integer> randomDieValues(int dieCount){
        Collection<Integer> temp = new ArrayList<Integer>();
        for(int i = 0; i < dieCount; i++){
            temp.add((int) (Math.random() * 6 + 1));
        }
        return temp;
    }

    @Override
    public String toString(){
        String result = "[";
        for(int die : dieValues){
            if(result.length() > 1){
                result = result + ", ";
            }
            result = result + die;
        }

        if(getScore() >= 0){
            result = result + " = " + getScore();
        }
        return result;
    }

    public static Dice valueOf(String s){
        // "[1, 1, 3] = 200"
        int score = -1;
        int scorePos = s.indexOf('=');
        if(scorePos >= 0){
            score = Integer.parseInt(s.substring(scorePos+1).trim());
            s = s.substring(0, scorePos).trim();
        }

        if(s.startsWith("[") && s.endsWith("]")){
            s = s.substring(1, s.length()-1);
        }else {
            throw new IllegalArgumentException();
        }

        String[] dieValues = s.split(",");
        Collection<Integer> temp = new ArrayList<Integer>();
        for(int i = 0; i < dieValues.length; i++){
            temp.add(Integer.parseInt(dieValues[i]));
        }

        return new Dice(temp, score);
    }


    public int getScore(){
        return this.score;
    }

    public int getDieCount(){
        return dieValues.size();
    }

    public int getDieValue(int dieNum){
        if(dieNum < 0 || dieNum > this.dieValues.size()){
            throw new IllegalArgumentException();
        }
        return dieValues.get(dieNum-1);
    }

    public int getValueCount(int value){
        return Collections.frequency(dieValues, value);
    }

    public void setScore(int score){
        if(this.score >= 0){
            throw new IllegalArgumentException();
        }
        this.score = score;
    }

    public Dice add(Dice dice){
        Collection<Integer> temp = new ArrayList<Integer>(dice.dieValues);
        temp.addAll(this.dieValues);
        return new Dice(temp, -1);
    }

    public Dice remove(Dice dice){
        Collection<Integer> temp = new ArrayList<>(dieValues);
        for(int i : dice.dieValues){
            temp.remove(i);
        }
        return new Dice(temp, -1);
    }

    @Override
    public Iterator<Integer> iterator(){
        return this.dieValues.iterator();
    }

    public int computeDieScores(Collection<Dice> dies){
        return dies.stream().mapToInt(Dice::getScore).sum();
    }
}
