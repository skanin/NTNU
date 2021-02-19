package encapsulation;

public class UpOrDownCounter {
		
	private int stop;
	private int start;
	private int counter = 0;

	public UpOrDownCounter(int start, int stop){
		this.stop = stop;
		this.start = start;
		
		counter = start;
		
		if(start == stop) {
			throw new IllegalArgumentException("Start and stop cannot be the same value");
		}
	}
	
	int getCounter() {
		return counter;
	}
	
	boolean count() {
		if(start > stop) {
			if(getCounter() != stop) {
				counter = counter - 1;
				if(counter == stop) {
					return false;
				}else {
					return true;
				}
				
			}
		}else {
			if(getCounter() != stop) {
				counter = counter + 1;
				if(counter == stop) {
					return false;
				}else {
					return true;
				}
			}
		}
		return false;
	}
}