package digit;

public class Digit {
	private final int system;
	private int value;
	
	public Digit(int system) {
		this.system = system;
		this.value = 0;
	}
	
	public int getValue() {
		return value;
	}
	
	public boolean increment() {
		value++;
		if(value == system) {
			value = 0;
			return true;
		}
		return false;
	}
	
	public int getBase() {
		return system;
	}
}
