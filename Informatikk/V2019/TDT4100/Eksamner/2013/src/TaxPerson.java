public class TaxPerson extends TaxEntity {

    protected TaxPerson(String idnr, String name, double percent){
        super(idnr, name, percent);
    }

    @Override
    public boolean checkId(String id){
        return id.trim().matches("\\d{11}");
    }

    /*
    @Override
    public boolean checkId(String id){
        if(id.trim().length() != 11){
            return false;
        }else {
            for(int i = 0; i < 11; i++){
                if(!Character.isDigit(id.charAt(i))){
                    return false;
                }
            }
        }
        return true;
    }
     */

}
