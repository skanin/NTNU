import java.util.Arrays;
import java.util.Collection;
import java.util.stream.Collectors;

public class Card {
    private final char suit;
    private final int face;


    public Card(char suit, int face){
        this.suit = suit;
        this.face = face;
    }

    @Override
    public String toString(){
        return String.format("%s%s", suit, face);
    }

    public char getSuit(){
        return suit;
    }

    public int getFace(){
        return face;
    }


    public static void main(String[] args){
        Collection<Card> cards = Arrays.asList(new Card('S', 1), new Card('H', 2),
                new Card('D', 12), new Card('C', 13));

        // Oppgave 1
        cards.stream().filter(c -> c.getSuit() == 'S').forEach(System.out::println);

        // Oppgave 2
        cards.stream().filter(c -> c.getSuit() == 'H').collect(Collectors.toList());

        // Oppgave 3
        cards.stream().map(card -> card.getSuit()).collect(Collectors.toList());

        // Oppgave 4
        cards.stream().map(Card::getFace).reduce((a, b) -> a+b).get();

        // Oppgave 5
        cards.stream().anyMatch(c -> c.getSuit() == 'S' && c.getFace() == 12);

        // Oppgave 6
        cards.stream().
    }

}
