public class Person1 implements Named {

    private String givenName;
    private String familyName;
    private String fullName;

    public Person1(String givenName, String familyName){
        this.givenName = givenName;
        this.familyName = familyName;
    }

    public void setGivenName(String name){
        this.givenName = name;
    }

    public String getGivenName(){
        return this.givenName;
    }

    public void setFamilyName(String name){
        this.familyName = name;
    }

    public String getFamilyName(){
        return this.familyName;
    }

    public void setFullName(String name){
        this.fullName = givenName + " " + familyName;
    }

    public String getFullName(){
        return this.fullName;
    }

}
