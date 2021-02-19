package upOrDownCounter;

public class UpOrDownCounter {
	private int start;
	private int end;
	private int counter;
	public UpOrDownCounter(int start, int end) {
		if(start == end) {
			throw new IllegalArgumentException("Start can't = end");
		}
		this.start = start;
		this.end = end;
		this.counter = start;
	}
	
	public int getCounter() {
		return this.counter;
	}
	
	public boolean count() {
		if (start < end) {
			counter++;
			if(counter == end) {
				return false;
			}
			return true;
		}else if (start > end) {
			counter++;
			if(counter == end) {
				return false;
			}
			return true;
		}
		return false;
	}
}
