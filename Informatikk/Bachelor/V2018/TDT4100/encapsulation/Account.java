package encapsulation;

public class Account {
	private double balance;
	private double interestRate;
	
	public Account(double balance, double interestRate) {
		if(balance > 0) {
			this.balance = balance;
		}else {
			throw new IllegalArgumentException("Balance must be positive");
		}
		
		if(interestRate > 0) {
			this.interestRate = interestRate;
		}else {
			throw new IllegalArgumentException("Interest rate must be positive");
		}		
	}
	
	public double getBalance() {
		return balance;
	}
	
	public double getInterestRate() {
		return interestRate;
	}
	
	public void setInterestRate(double interestRate) {
		if(interestRate > 0) {
			this.interestRate = interestRate;
		}else {
			throw new IllegalArgumentException("Cannot set negative interest rate");
		}
		
	}
	
	public void deposit(double sum) {
		if(sum > 0) {
			this.balance += sum;
		}else {
			throw new IllegalArgumentException("Cannot deposit negative sum");
		}
	}
	
	public void withdraw(double sum) {
		if (sum > 0 && (balance - sum) >= 0) {
			balance -= sum;
		}else {
			throw new IllegalArgumentException("Cannot withdraw negative sum or you have insufficient funds");
		}
	}
	
	public void addInterest() {
		balance = balance + (balance*(interestRate/100));
	}
}
