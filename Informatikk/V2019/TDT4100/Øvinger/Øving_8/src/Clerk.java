import java.util.function.BinaryOperator;

public class Clerk implements Employee {

    private Printer printer;
    private int taskCount;

    public Clerk(Printer printer){
        this.printer = printer;
    }

    public double doCalculations(BinaryOperator<Double> op, double val1, double val2){
        taskCount++;
        return op.apply(val1, val2);
    }

    public void printDocument(String document){
        if(printer != null) printer.printDocument(document, this);
        taskCount++;
    }

    public int getTaskCount(){
        return taskCount;
    }

    public int getResourceCount(){
        return 1;
    }

}
