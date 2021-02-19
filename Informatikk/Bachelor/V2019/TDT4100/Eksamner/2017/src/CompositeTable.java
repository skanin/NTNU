public class CompositeTable extends Table{

    private Table t1, t2;

   public CompositeTable(Table t1, Table t2, int lostCap){
       super(t1.getCapacity() + t2.getCapacity() - lostCap);

       this.t1 = t1;
       this.t2 = t2;
   }

    public Table getT1(){
       return this.t1;
    }

    public Table getT2(){
       return this.t2;
    }
}
