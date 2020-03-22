package account;

public class Account {
    private double balance;
    private double interestRate;

    public Account(){
        this.balance = 0;
        this.interestRate = 0;
    }

    public void deposit(double sum){
        if(sum >= 0){
            this.balance += sum;
        }else{
            System.out.println("You can't deposit negative");
        }
    }

    public void addInterest(){
        this.balance += this.balance * (interestRate/100);
    }
    
    public double getBalance(){
        return this.balance;
    }

    public double getInterestRate(){
        return this.interestRate;
    }

    public void setInterestRate(double rate){
        this.interestRate = rate;
    }
}
