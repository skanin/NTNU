import java.io.*;
import java.nio.Buffer;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Scanner;

public class Quiz {

    private Collection<Question> questions = new ArrayList<>();

    public void addQuestion(Question question){
        if(!questions.contains(question)) questions.add(question);
    }

    public void run(){
        Scanner sc = new Scanner(System.in);

        for(Question q : questions){
            q.askQuestion(System.out);
            while(sc.hasNextLine()){
                String ans = sc.nextLine();
                if(q.checkAnswer(ans)){
                    System.out.println("Correct");
                    break;
                }
                System.out.println("Wrong, try again!");
            }
        }
        sc.close();
    }

    public void init() {
        addQuestion(new Question("Hva heter hovedstaden i Norge?", "Oslo"));
        addQuestion(new Question("Hva slags ost er månen laget av?", "Roquefort", "Camembert", "Roquefort", "Brie"));
        addQuestion(new Question("Hvor høy er Galdhøpiggen?", "2469", "2469", "2471"));
        addQuestion(new Question("Er Java gøy?", "ja"));
    }

    public void init(Reader reader) throws IOException {
        BufferedReader br = new BufferedReader(reader);

        while(br.ready()){
            String question = br.readLine();
            if(question == null || question.trim().length() == 0){
                break;
            }
            String answer = br.readLine();
            Collection<String> options = new ArrayList<>();
            while(br.ready()){
                String option = br.readLine();
                if(option == null || option.trim().length() == 0){
                    break;
                }
                options.add(option);
            }
            addQuestion(new Question(question, answer, options));
        }
    }

    public static void main(String[] args){
        Quiz q = new Quiz();
        try {
            q.init(new FileReader("src/questions.txt"));
        }catch (IOException e){
            System.out.println(e);
        }
        q.run();

        Question q1 = new Question(" ", " ", new ArrayList<>());
    }



}
