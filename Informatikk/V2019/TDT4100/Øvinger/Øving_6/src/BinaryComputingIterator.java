import java.util.Arrays;
import java.util.Iterator;
import java.util.function.BinaryOperator;

public class BinaryComputingIterator implements Iterator<Double> {

    private Iterator<Double> it1, it2;
    private BinaryOperator<Double> op;
    private Double default1, default2;

    public BinaryComputingIterator(Iterator<Double> iterator1, Iterator<Double> iterator2, BinaryOperator<Double> operator){
        this.it1 = iterator1;
        this.it2 = iterator2;
        this.op = operator;
    }

    public BinaryComputingIterator(Iterator<Double> iterator1, Iterator<Double> iterator2, Double default1, Double default2, BinaryOperator<Double> operator){
        this(iterator1, iterator2, operator);
        this.default1 = default1;
        this.default2 = default2;
    }

    @Override
    public boolean hasNext(){
        if(it1.hasNext() && it2.hasNext()) return true;
        if(it1.hasNext() && (!it2.hasNext() && default2 != null)) return true;
        if((!it1.hasNext() && default1 != null) && it2.hasNext()) return true;
        return false;
    }

    @Override
    public Double next(){
        if(it1.hasNext() && it2.hasNext()){
            return op.apply(it1.next(), it2.next());
        }

        if(it1.hasNext() && (!it2.hasNext() && default2 != null)){
            return op.apply(it1.next(), default2);
        }

        if((!it1.hasNext() && default1 != null) && it2.hasNext()){
            return op.apply(default1, it2.next());
        }

        return null;
    }

    public static void main(String[] args){
        Iterator<Double> iterator1 = Arrays.asList(2.0, 3.0).iterator();
        Iterator<Double> iterator2 = Arrays.asList(5.0).iterator();

        BinaryOperator<Double> addition = (a,b) -> a + b;

        BinaryComputingIterator binaryComputingIterator = new BinaryComputingIterator(iterator1, iterator2, null, 10.0, addition);

        System.out.println(binaryComputingIterator.next());
        System.out.println(binaryComputingIterator.hasNext());
        System.out.println(binaryComputingIterator.next());
        System.out.println(binaryComputingIterator.hasNext());
    }

}
