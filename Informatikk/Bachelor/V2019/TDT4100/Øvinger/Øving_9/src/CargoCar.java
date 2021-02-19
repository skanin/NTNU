public class CargoCar extends TrainCar {

    private int cargoWeight;

    public CargoCar(int deadWeigth, int cargoWeigth){
        super(deadWeigth);
        this.cargoWeight = cargoWeigth;
    }

    public int getCargoWeight(){
        return cargoWeight;
    }

    public void setCargoWeight(int weight){
        if(weight < 0) throw new IllegalArgumentException();
        this.cargoWeight = weight;
    }

    @Override
    public int getTotalWeight(){
        return cargoWeight + super.getTotalWeight();
    }

    @Override
    public String toString(){
        return "[CargoCar, " + getTotalWeight() + "kg]";
    }

}
