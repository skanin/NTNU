public class Segment {

    final private double lengde, tid;

    public Segment(double lengde, double tid){
        this.lengde = lengde;
        this.tid = tid;
    }

    public double getLengde(){
        return this.lengde;
    }

    public double getTid(){
        return this.tid;
    }

    public double getFart(){
        return lengde/tid;
    }

}
