public class Group {

    private final int guestCount;


    public Group(int guestCount){
        if(guestCount < 1) throw new IllegalArgumentException();
        this.guestCount = guestCount;
    }

    public int getGuestCount(){
        return this.guestCount;
    }


    private Seating seating;

    public void setSeating(Seating seating){
        this.seating = seating;
    }

    public void changeCount(int i){
        if(seating.getTable().getCapacity() < i) throw new IllegalArgumentException("Ikke stort nok bord");
        this.guestCount = i;
    }

    public void changeCount(int i){
        this.guestCount = i;
    }

}
