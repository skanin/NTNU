import java.util.ArrayList;
import java.util.Collection;

public class Train {

    private Collection<TrainCar> trainCars = new ArrayList<>();

    public void addTrainCar(TrainCar trainCar){
        if(!contains(trainCar)) trainCars.add(trainCar);
    }

    public boolean contains(TrainCar trainCar){
        return trainCars.contains(trainCar);
    }

    public int getTotalWeight(){
        return trainCars.stream().mapToInt(TrainCar::getTotalWeight).sum();
    }

    public int getPassengerCount(){
        int total = 0;
        for(TrainCar t : trainCars){
            total += t instanceof PassengerCar ? ((PassengerCar) t).getPassengerCount() : 0;
        }
        return total;
    }

    public int getCargoWeight(){
        int total = 0;
        for(TrainCar t : trainCars){
            total += t instanceof CargoCar ? ((CargoCar) t).getCargoWeight() : 0;
        }
        return total;
    }

    @Override
    public String toString(){
        String temp = "";
        for(TrainCar t : trainCars){
            temp += t.toString() + "\n";
        }
        return temp;
    }

    public static void main(String[] args){

    }

}
