import java.io.*;
import java.util.Scanner;

public class TestIO {

    private String filename;

    public TestIO(String filename){
        this.filename = filename;
    }

    public void write() throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new FileWriter(filename));

        while (true){
            String text = sc.nextLine();
            if(text.equals("Exit")) break;
            bw.write(text + "\n");
        }
        bw.close();
    }

    public void print() throws IOException{
        BufferedReader br = new BufferedReader(new FileReader(filename));

        while(br.ready()){
            System.out.println(br.readLine());
        }
        br.close();
    }

    public static void main(String[] args){
        TestIO testIO = new TestIO("src/test.txt");

        try{
            testIO.write();
            testIO.print();
        } catch (IOException e){
            System.out.println(e);
        }


    }

}
