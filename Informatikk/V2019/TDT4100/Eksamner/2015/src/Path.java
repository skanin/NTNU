import java.util.*;

public class Path implements Iterable<Segment> {

    private List<Segment> segments;

    public Path(Segment ... s){
        this.segments = new ArrayList<>(Arrays.asList(s));
    }

    public int getNumSegments(){
        return segments.size();
    }

    public void addSegment(Segment s){
        if(!segments.contains(s)) segments.add(s);
    }

    public void addSegment(double lengde, double tid){
        segments.add(new Segment(lengde, tid));
    }

    public Segment getSegment(int i){
        if(i < 0 || i > segments.size()-1) throw new IllegalArgumentException();
        return segments.get(i);
    }

    public double getDuration(){
        return segments.stream().mapToDouble(Segment::getTid).sum();
    }

    public double getDistance(Segment fromSegment, Segment uptoSegment){
        if((fromSegment == null && segments.contains(uptoSegment)) ||
        (segments.contains(fromSegment) && uptoSegment == null)){
            double distance = 0.0;
            for(Segment s : segments){
                if(s == uptoSegment){
                    return distance;
                }else if(fromSegment == null || s == fromSegment || distance > 0.0){
                    distance += s.getLengde();
                }
            }
            return distance;
        }
        throw new IllegalArgumentException();
    }

    public Segment getSegmentAt(double distance, boolean next){
        for(Segment s : segments) {
            if (distance == 0.0) return next ? s : null;
            distance -= s.getLengde();
            if(distance < 0.0 || (distance == 0.0 && (!next))) return s;
        }
        return null;
    }

    @Override
    public Iterator<Segment> iterator(){
        return segments.iterator();
    }
}
