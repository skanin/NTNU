public class TDT4100DayPlan extends DayPlan {

    private final TDT4100Lecture lecture;

    public TDT4100DayPlan(){
        TDT4100Lecture t = new TDT4100Lecture();
        super.addTimeSlot(t);
        this.lecture = t;

    }

    @Override
    public void addTimeSlot(TimeSlot t){
        if(t.overlaps(t)) {
            throw new IllegalArgumentException("Overlaps with TDT4100 lecture");
        }
        super.addTimeSlot(t);
    }

    @Override
    public void removeTimeSlot(TimeSlot t){
        if(t == this.lecture){
            throw new IllegalArgumentException("Cannot remove TDT4100");
        }

        super.removeTimeSlot(t);
    }

    public static void main(String[] args){
        DayPlan dp = new TDT4100DayPlan();
        System.out.println(dp.getTimeSlot(10, 30));

        dp.addTimeSlot(new TimeSlot("Coffee break", 11, 30, 60));
    }

}
