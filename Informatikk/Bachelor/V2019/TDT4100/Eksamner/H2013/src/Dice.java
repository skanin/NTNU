import java.util.Random;

public class Dice {

    public static final int MAX_DIE_VALUE = 6;
    private final int[] dice;
    private Random r = new Random();

    public Dice(int dieCount){
        this.dice = new int[dieCount];
    }

    @Override
    public String toString(){
        String out = "";
        for(int i = 0; i < dice.length; i++){
            if(i == dice.length-1){
                out += dice[i];
            }else {
                out += dice[i] + "-";
            }
        }
        return out;
    }

    public int getValueCount(int value){
        int count = 0;
        for(int i : dice){
            if(i == value){
                count++;
            }
        }
        return count;
    }

    public int getHighestValueOfSame(int count, int butNot){
        int min = Integer.MAX_VALUE;
        int antall = Integer.MAX_VALUE;

        for(int i : dice){
            if(getValueCount(i) == count && i != butNot && getValueCount(i) < antall){
                min = i;
                antall = getValueCount(i);
            }
        }
        return min;
    }

    public int getStraightSum(int startValue, int endValue){
        int sum = 0;
        for(int i = startValue; i <= endValue; i++){
            if(getValueCount(i) < 1){
                return 0;
            }
            sum += i;
        }
        return sum;
    }

    public void roll(){
        for(int i = 0; i < dice.length; i++){
            dice[i] = (int) Math.floor(r.nextInt() * MAX_DIE_VALUE + 1);
        }
    }


}
