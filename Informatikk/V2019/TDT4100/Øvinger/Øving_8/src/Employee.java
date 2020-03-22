import java.util.function.BinaryOperator;

public interface Employee {

    double doCalculations(BinaryOperator<Double> op, double val1, double val2);
    void printDocument(String document);
    int getTaskCount();
    int getResourceCount();

}
