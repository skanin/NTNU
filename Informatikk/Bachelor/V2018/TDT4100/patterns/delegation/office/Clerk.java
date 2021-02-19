package patterns.delegation.office;

import java.util.function.BinaryOperator;

import patterns.delegation.office.Printer;

public class Clerk implements Employee {
	
	private Printer printer;
	private int calculationsCount;
	
	public Clerk(Printer printer) {
		this.printer = printer;
		this.calculationsCount = 0;
	}

	@Override
	public double doCalculations(BinaryOperator<Double> operation, double value1, double value2) {
		calculationsCount++;
		return operation.apply(value1, value2);
	}

	@Override
	public void printDocument(String document) {
		calculationsCount++;
		printer.printDocument(document, this);

	}

	@Override
	public int getTaskCount() {
		return calculationsCount;
	}

	@Override
	public int getResourceCount() {
		// TODO Auto-generated method stub
		return 1;
	}

	public static void main(String[] args) {
		BinaryOperator<Double> b = (n1, n2) -> n1+n2;
		Printer p = new Printer();
		Clerk c = new Clerk(p);
		System.out.println(c.doCalculations(b, 10.1, 10.1));
	}
}
