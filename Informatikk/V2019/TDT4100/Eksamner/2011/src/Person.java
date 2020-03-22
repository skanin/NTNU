import java.util.Date;

public class Person {

    private char gender;
    private Date dateOfBirth;
    private final String[] F = "376189452".split("");
    private final String[] G = "5432765432".split("");
    private String ssn;

    public Person(char gender){
        if("MF".indexOf(Character.toUpperCase(gender)) > 0) throw new IllegalArgumentException("");
        this.gender = gender;
    }

    public char getGender(){
        return this.gender;
    }

    public Date getDateOfBirth(){
        return this.dateOfBirth;
    }

    public void setDateOfBirth(Date date){
        this.dateOfBirth = date;
    }

    private boolean checkSsnDate(String date){
        try {
            int day = Integer.parseInt(date.substring(0,2));
            int month = Integer.parseInt(date.substring(2, 4));
            int year = Integer.parseInt(date.substring(4));
            return day == dateOfBirth.getDay() && month == dateOfBirth.getMonth() && year == dateOfBirth.getYear();
        } catch(NumberFormatException e) {
            return false;
        }
    }

    private boolean checkN3(String n){
        try {
            int j = Integer.parseInt(n);
            if(gender == 'M'){
                return j % 2 != 0;
            }else {
                return j % 2 == 0;
            }
        } catch(NumberFormatException e){
            return false;
        }
    }

    private boolean checkN1n2(String n){
        try{
            int j = Integer.parseInt(n);
            return true;
        } catch (NumberFormatException e){
            return false;
        }
    }

    private boolean checkK1k2(String n){
        try{
            int k1 = Integer.parseInt(n.substring(9,9));
            int k2 = Integer.parseInt(n.substring(10,10));

            String[] numbers = n.substring(0,10).split("");

            int vsK1 = 0;

            for(int i = 0; i < F.length; i++){
                vsK1 += Integer.parseInt(F[i])* Integer.parseInt(numbers[i]);
            }

            int vsK2 = 0;
            for(int i = 0; i < G.length; i++){
                vsK2 += Integer.parseInt(G[i])* Integer.parseInt(numbers[i]);
            }

            return (11 - (vsK1 % 11)) < 10 && (11 - (vsK2 % 11)) < 10;

        } catch (NumberFormatException e){
            return false;
        }
    }

    public void setSsn(String ssn){
        if(ssn.length() != 11 ||
                !checkSsnDate(ssn.substring(0,6)) ||
                !checkN3(ssn.substring(8,8)) ||
                !checkN1n2(ssn.substring(6, 8)) ||
                !checkK1k2(ssn)) throw new IllegalArgumentException("");
        this.ssn = ssn;
    }

    public static void main(String[] args){
        Person p = new Person('M');

        p.setDateOfBirth(new Date(98, 6, 27));
        p.setSsn("27069842513");
    }

}
