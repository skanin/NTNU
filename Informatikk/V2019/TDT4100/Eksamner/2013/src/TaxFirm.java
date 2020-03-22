import java.util.ArrayList;
import java.util.List;

public class TaxFirm extends TaxEntity {

    private List<Integer> liste = new ArrayList<>();

    protected TaxFirm(String idnr, String name, double percent){
        super(idnr, name, percent);
    }

    @Override
    public boolean checkId(String id){
        return id.matches("[8-9]\\d{8}");
    }

/*
    @Override
    public boolean checkId(String id){
        if(id.trim().length() == 9 && (id.charAt(0) == '8' || id.charAt(0) == '9')){
            for(int i = 0; i < 9; i++){
                if(!Character.isDigit(id.charAt(i))){
                    return false;
                }
            }
            return true;
        }
        return false;
    }
*/

    public List<Integer> getListe(){
        return liste;
    }

    public static void main(String[] args){
        TaxFirm t = new TaxFirm("994444444", "Sander", 3.4);
        System.out.println(t.checkId("994444444"));
        t.liste.add(1);
        t.getListe().add(4);
        System.out.println(t.getListe().size());
    }


}
