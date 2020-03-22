import java.io.OutputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;

public class Question {

    private String question, answer;
    private List<String> options = new ArrayList<>();


    public Question(String question, String answer, Collection<String> options){
        this.question = question;
        this.answer = answer;
        Collection<String> tempOptions = new ArrayList<>(options);
        if(!tempOptions.contains(answer) && !tempOptions.isEmpty()) throw new IllegalArgumentException("Answer not in options");
        this.options.addAll(tempOptions);
    }

    public Question(String question, String answer, String ... options){
        this(question, answer, Arrays.asList(options));
    }

    public void askQuestion(PrintStream ps){
        ps.println(question);
        for(int i = 0; i < options.size(); i++){
            ps.println();
            ps.println(i+1 + ": " + options.get(i));
        }
    }

    public boolean checkAnswer(String answer){
        if(this.answer.equals(answer)){
            return true;
        }
        try{
            int index = Integer.parseInt(answer);
            return options.get(index - 1).equals(this.answer);

        }catch (NumberFormatException e){
            return false;
        }catch (IndexOutOfBoundsException e){
            return false;
        }
    }



    public static void main(String[] args){

    }
}
