import java.sql.Time;

public class TimeSlot implements Comparable<TimeSlot>{

    private static int asHours(int minutes){return minutes/60;}
    private static int asMinutes(int minutes){return minutes%60;}

    private final String description;
    private final int startTime, endTime;

    public TimeSlot(String description, int hours, int minutes, int duration){
        this.description = description;
        this.startTime = hours * 60 + minutes;
        this.endTime = this.startTime + duration;
    }

    @Override
    public String toString(){
        return this.description + "@" + twoDigits(asHours(startTime)) + ":" +
                twoDigits(asMinutes(startTime)) + "-" +
                twoDigits(asHours(endTime)) + ":" + twoDigits(asMinutes(endTime));
    }

    private String twoDigits(int minutes){
        return minutes < 10 ? "0" + minutes : Integer.toString(minutes);
    }

    public DayTime getStartTime(){
        return new DayTime(asHours(startTime), asMinutes(startTime));
    }

    public DayTime getEndTime(){
        return new DayTime(asHours(endTime), asMinutes(endTime));
    }

    public int getDuration(){
        return endTime - startTime;
    }

    public String getDescription(){
        return description;
    }


    public boolean contains(int hours, int minutes){
        minutes = hours * 60 + minutes;
        return startTime <= minutes && endTime > minutes;
    }

    public boolean overlaps(TimeSlot other){
        return startTime < other.endTime && endTime > other.startTime;
    }

    @Override
    public int compareTo(TimeSlot t1){
        int diff = startTime - t1.startTime;
        if(diff == 0){
            return endTime - t1.endTime;
        }
        return diff;
    }

    public static void main(String[] args){
        TimeSlot t = new TimeSlot("TDT4100-forelesning", 10, 15, 105);
        System.out.println(t);
    }

}
