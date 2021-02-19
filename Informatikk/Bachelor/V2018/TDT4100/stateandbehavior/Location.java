package stateandbehavior;

public class Location {
	int x = 0;
	int y = 0;
	
	void up() {
			y = y-1;
	}
	
	void down() {
		y = y + 1;
	}
	
	void left() {
			x = x - 1;
	}
	
	void right() {
		x = x + 1;
	}
	
	int getX() {
		return x;
	}
	
	int getY() {
		return y;
	}
	
	@Override
	public String toString() {
		String str = "X posisjonen er " + getX() + ". Y posisjonen er " + getY();
		return str;
	}
	
	public static void main(String[] args) {
		Location loc = new Location();
		loc.up();
		loc.up();
		loc.right();
		loc.down();
		loc.left();
		System.out.println(loc.getX());
		System.out.println(loc.getY());
		System.out.println(loc.toString());
	}
}
