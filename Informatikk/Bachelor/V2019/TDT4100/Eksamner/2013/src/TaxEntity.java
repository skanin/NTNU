public abstract class TaxEntity {

    final private String idnr;
    private String name;
    private double percent;
    private long formue;
    private long gjeld;
    private long inntekt;
    private long fradrag;
    private String commune;

    protected TaxEntity(String idnr, String name, double percent){
        if(!checkId(idnr)) throw new IllegalArgumentException();
        this.idnr = idnr;
        setName(name);
        setPercent(percent);
    }

    public String getId(){
        return idnr;
    }

    public String getCommune(){
        return commune;
    }

    private boolean checkPositive(long number){
        return number >= 0;
    }

    private boolean checkPercent(double percent){
        return 0.0 < percent && percent < 100.0;
    }

    private boolean checkName(String name){
        int count = 0;
        for(int i = 0; i < name.length(); i++){
            String c = String.valueOf(name.charAt(i));
            if(c.matches("[a-åA-Å]")){
                count++;
            }
        }
        return count >= 3;
    }

    protected abstract boolean checkId(String id);

    public void setName(String name){
        if(!checkName(name)) throw new IllegalArgumentException();
        this.name = name;
    }

    public void setPercent(double percent){
        if(!checkPercent(percent)) throw new IllegalArgumentException();
        this.percent = percent;
    }

    public long getTax(){
        long tax = 0;
        double inntektskatt = (inntekt - fradrag) * percent;
        double formueskatt = (formue - gjeld) * percent/100;

        tax = (long) (inntektskatt + formueskatt);
        return tax;
    }



}
