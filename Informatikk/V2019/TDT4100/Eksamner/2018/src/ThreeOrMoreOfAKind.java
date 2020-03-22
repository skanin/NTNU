import java.util.ArrayList;
import java.util.Collection;

public class ThreeOrMoreOfAKind implements DieScorer {

    private Collection<DieScorer> diceScorers;

    private int getScore(final int value, int count){
        return value * 100 * (int) Math.pow(count-3, 2);
    }

    protected int getBestValue(final Dice dice){
        int value = 0;
        int max = 0;
        for(int i = 1; i <= 6; i++){
            int count = dice.getValueCount(i);
            int score = getScore(i, count);
            if(count >= 3 && score > max){
                value = i;
                max = score;
            }
        }
        return value;
    }


    public Dice getScore(Dice dice){
        int best = getBestValue(dice);
        if(best == 0){
            return null;
        }

        int count = dice.getValueCount(best);
        Collection<Integer> dieValues = new ArrayList<>(count);
        for(int i = 0; i < count; i++){
            dieValues.add(best);
        }
        return new Dice(dieValues, getScore(best, count));
    }

    public Collection<Dice> computeDiceScores(Dice dice){
        Collection<Dice> result = new ArrayList<>();
        while(dice.getDieCount() > 0){
            Dice best = null;
            for(DieScorer d : diceScorers){
                Dice score = d.getScore(dice);
                if(score != null && (best == null || score.getScore() > best.getScore()) ){
                    best = score;
                }
            }
            if(best == null) {
                break;
            }else {
                result.add(best);
                dice = dice.remove(best);
            }
        }
        return result;
    }

    public static void main(String[] args){
        Collection<Integer> test = new ArrayList<>();
        System.out.println(test);
    }
}
