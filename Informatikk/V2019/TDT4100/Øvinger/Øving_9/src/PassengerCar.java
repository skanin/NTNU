public class PassengerCar extends TrainCar {

    private int passengerCount;


    public PassengerCar(int deadWeigth, int passengerCount){
        super(deadWeigth);
        this.passengerCount = passengerCount;
    }

    @Override
    public int getTotalWeight(){
        return (getPassengerCount() * 80) + super.getTotalWeight();
    }

    public int getPassengerCount(){
        return passengerCount;
    }

    public void setPassengerCount(int i){
        if(i < 0) throw new IllegalArgumentException();
        this.passengerCount = i;
    }

    @Override
    public String toString(){
        return "[PasserngerCar, " + getPassengerCount() + " passengers, " + getTotalWeight() + "kg]";
    }

}
