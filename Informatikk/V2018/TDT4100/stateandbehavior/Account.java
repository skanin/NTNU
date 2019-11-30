package stateandbehavior;

public class Account {
	private double balance = 0;
	private double interestRate = 0;
	
	public void deposit(double in) {
		if(in >= 0) {
			balance = balance + in;
		}else{
			System.out.println("Du må legge inn en positiv sum");
		}
	}
	
	public void setInterestRate(double rate) {
		interestRate = rate;
	}
	
	public double getInterestRate() {
		return interestRate;
	}
	
	public double getBalance() {
		return balance;
	}
	
	public void addInterest() {
		balance = balance + (balance*(interestRate/100));
	}
	
	@Override
	public String toString() {
		String str = "Kontoen har " + getBalance() + " kroner disponibelt. Renten er for �yeblikket " + getInterestRate();
		return str;
	}
	
	public static void main(String[] args) {
		Account ac = new Account();
		ac.setInterestRate(5);
		ac.deposit(100);
		ac.addInterest();
		System.out.println(ac.getBalance());
		System.out.println(ac.getInterestRate());
		System.out.println(ac.toString());
	}
}
