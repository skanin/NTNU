
public class ForLoopTest extends Dog{
	
	static int count = 0;
	static Dog lara = new Dog();
	
	public static void main(String[] args) {
		if(count == 1) {
			for(int i = 0; i <= 10; i++) {
				System.out.println(i);
			}
		} else {
			int i = 10;
			while(i >= 0) {
				System.out.println(i);
				lara.bark(1);
				i = i - 1;
			}
		}
		
	}

}
