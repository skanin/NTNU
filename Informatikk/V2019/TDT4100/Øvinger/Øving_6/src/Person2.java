public class Person2 {

    private String givenName;
    private String familyName;
    private String fullName;

    public Person2(String fullName){
        this.fullName = fullName;
    }

    public void setGivenName(String name){
        this.givenName = name.split(" ")[0];
    }

    public String getGivenName(){
        return this.givenName;
    }

    public void setFamilyName(String name){
        this.familyName = name.split(" ")[1];
    }

    public String getFamilyName(){
        return this.familyName;
    }

    public void setFullName(String name){
        this.fullName = name;
    }

    public String getFullName(){
        return this.fullName;
    }

}
