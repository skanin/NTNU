public class Gender {

    private final String label;

    public Gender(String label){
        this.label = label;
    }

    @Override
    public String toString(){
        return this.label;
    }

    public static Gender MALE = new Gender("male"), FEMALE = new Gender("female");

    public static Gender valueOf(String label) {
        if (MALE.label.equals(label)) {
            return MALE;
        } else if (FEMALE.label.equals(label)) {
            return FEMALE;
        }
        return null;
    }
}
