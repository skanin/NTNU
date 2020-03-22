public class TrainCar {

    private int deadWeight;


    public TrainCar(int weight){
        if(weight < 0) throw new IllegalArgumentException();
        this.deadWeight = weight;
    }

    public int getTotalWeight(){
        return getDeadWeight();
    }

    public void setDeadWeight(int weight){
        if(weight < 0) throw new IllegalArgumentException();
        this.deadWeight = weight;
    }

    public int getDeadWeight(){
        return this.deadWeight;
    }

    @Override
    public String toString(){
        return "[TrainCar, " + getTotalWeight() + "kg]";
    }

}
