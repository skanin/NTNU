import java.sql.Time;
import java.util.*;

public class DayPlan implements Iterable<TimeSlot> {

    private List<TimeSlot> timeSlots = new ArrayList<>();


    public void addTimeSlot(TimeSlot t){
        if(!timeSlots.contains(t)) timeSlots.add(t);
        Collections.sort(timeSlots);
    }

    public void removeTimeSlot(TimeSlot t){
        timeSlots.remove(t);
    }

    public TimeSlot getTimeSlot(int hours, int minutes){
        for(TimeSlot t : timeSlots){
            if(t.contains(hours, minutes)){
                return t;
            }
        }
        return null;
    }

    public boolean containsOverlapping(){
        for(int i = 0; i < timeSlots.size(); i++){
            for(int j = 0; j < timeSlots.size(); j++){
                if(i == j) continue;
                if(timeSlots.get(i).overlaps(timeSlots.get(j))){
                    return true;
                }
            }
        }
        return false;
    }

    private static void addTimeSlotIfNonEmpty(Collection<TimeSlot> timeSlots, DayTime startTime, DayTime endTime){
        int duration = (endTime.hours * 60 + endTime.minutes) - (startTime.hours * 60 + startTime.minutes);
        if(duration > 0){
            timeSlots.add(new TimeSlot(null, startTime.hours, startTime.minutes, duration));
        }
    }

    public Collection<TimeSlot> getFreeTime(){
        Collection<TimeSlot> freeTime = new ArrayList<>();
        TimeSlot prev = new TimeSlot(null, 0, 0, 0);
        for(TimeSlot t : timeSlots){
            DayTime startTime = t.getStartTime();
            addTimeSlotIfNonEmpty(freeTime, prev.getEndTime(), startTime);
            DayTime endTime = t.getEndTime();
            if(!prev.contains(endTime.hours, endTime.minutes)){
                prev = t;
            }
        }
        addTimeSlotIfNonEmpty(freeTime, prev.getEndTime(), new DayTime(24, 0));
        return freeTime;
    }

    @Override
    public Iterator<TimeSlot> iterator(){
        return timeSlots.iterator();
    }

    public static void main(String[] args){

    }
}
