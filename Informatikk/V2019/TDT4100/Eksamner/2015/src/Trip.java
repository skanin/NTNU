public class Trip {

    private final Path expPath;
    private Path actualPath;


    public Trip(Path p){
        this.expPath = p;
        this.actualPath = new Path();
    }

    public void registerSegment(double distance, double duration){
        if(actualPath.getNumSegments() == expPath.getNumSegments()) throw new IllegalArgumentException();
        Segment pathSegment = expPath.getSegmentAt(distance, true);
        double expDistance = pathSegment.getLengde();
        if (expDistance != distance) throw new IllegalArgumentException();
        double segmentDistance = expDistance - expPath.getDistance(null, expPath.getSegmentAt(distance, false));
        double segmentDuration = duration - actualPath.getDuration();
        actualPath.addSegment(segmentDistance, segmentDuration);
    }

    public Path getExpectedPath(){
        return this.expPath;
    }

    public double estimateTime(double distance, double duration){
        double remainingTime = 0.0;
        for(Segment s : this.getExpectedPath()){
            distance -= s.getLengde();
            if(remainingTime > 0.0) {
                remainingTime += s.getTid();
            }else if (distance < 0){
                remainingTime = s.getFart() * (-distance);
            }
        }
        return remainingTime;
    }



}
