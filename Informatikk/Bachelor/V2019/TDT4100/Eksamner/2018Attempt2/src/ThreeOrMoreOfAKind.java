import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;

public class ThreeOrMoreOfAKind implements DiceScorer {



    public Dice getScore(Dice dice){
        HashMap<Integer, Integer> threeOrMore = new HashMap<>();

        for(int value : dice){
            if(threeOrMore.containsKey(value)) continue;
            if(dice.getValueCount(value) >= 3){
                threeOrMore.put(value, dice.getValueCount(value));
            }
        }

        if(threeOrMore.isEmpty()) return null;

        int max = 0;
        int valueWithMax = 0;
        int score = 0;

        for(int key : threeOrMore.keySet()){
            int tempScore = (int) (key * 100 * Math.pow(2, threeOrMore.get(key)-3));
            if(threeOrMore.get(key) > max && score < tempScore) {
                max = threeOrMore.get(key);
                valueWithMax = key;
                score = tempScore;
            }else if(max == threeOrMore.get(key) && tempScore > score){
                max = threeOrMore.get(key);
                score = tempScore;
            } else if(score == tempScore){
                max = max > threeOrMore.get(key) ? max : threeOrMore.get(key);
            }
        }

        Collection<Integer> dieValues = new ArrayList<>();
        for(int i = 0; i < threeOrMore.get(valueWithMax); i++){
            dieValues.add(valueWithMax);
        }

        return new Dice(dieValues, score);
    }


    public static void main(String[] args){
        Dice d = Dice.valueOf("[2, 2, 2, 2, 2, 2, 5, 5, 5]");
        ThreeOrMoreOfAKind t = new ThreeOrMoreOfAKind();
        System.out.println(t.getScore(d));
    }
}
