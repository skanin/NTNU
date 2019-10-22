import java.util.ArrayList;
import java.util.Collection;
import java.util.stream.Collectors;

public class YearRegister {

    private int year;
    private Collection<TaxEntity> taxEntities = new ArrayList<>();
    private long maxTax, minTax, avgTax;

    public YearRegister(int year){
        this.year = year;
    }

    @Override
    public String toString(){
        return String.format("YearRegister %d: %d TaxEntities:\n" +
                "Max tax is %d, Min tax is %d, and Average tax is %d", year, taxEntities.size(), maxTax, minTax, avgTax);
    }

    public boolean containsTaxEntity(String id){
        return taxEntities.stream().anyMatch(t -> t.getId().equals(id));
    }

    public boolean addTaxEntity(TaxEntity taxEntity){
        if(!containsTaxEntity(taxEntity.getId())){
            taxEntities.add(taxEntity);
            return true;
        }
        return false;
    }

    public boolean removeTaxEntity(TaxEntity taxEntity){
        return taxEntities.remove(taxEntity);
    }

    public Collection<TaxEntity> getTaxEntitiesInCommune(String name){
        return taxEntities.stream().filter(t -> t.getCommune().equals(name)).collect(Collectors.toList());
    }

    public void makeStatistics(){
        long max = 0;
        long min = Long.MAX_VALUE;
        long all = 0;
        for(TaxEntity t : taxEntities){
            if(t.getTax() < min){
                min = t.getTax();
            }
            if(t.getTax() > max){
                max = t.getTax();
            }
            all += t.getTax();
        }

        this.maxTax = max;
        this.minTax = min;
        this.avgTax = all/taxEntities.size();
    }

    public static void main(String[] args){
        YearRegister y = new YearRegister(2019);
        System.out.println(y);
    }

}
