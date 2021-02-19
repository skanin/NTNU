public class Course implements Comparable<Course> {
    private final String code;
    private int year;
    private char semester;
    private final String legalSemesters = "SF";

    public Course(String code){
        this.code = code;
    }

    private boolean checkTime(String time){
        char semester = Character.toUpperCase(time.charAt(0));
        if(legalSemesters.indexOf(semester) == -1) return false;
        try {
            int year = Integer.parseInt(time.substring(1));
            return true;
        } catch (NumberFormatException e){
            return false;
        }
    }

    public void setTime(String time){
        if(checkTime(time)) {
            int year = Integer.parseInt(time.substring(1));
            if(String.valueOf(year).length() == 2 && year < 100){
                year += year < 50 ? 2000 : 1900;
            }
            this.year = year;
            this.semester = Character.toUpperCase(time.charAt(0));
        } else {
            throw new IllegalArgumentException("Invalid time format");
        }
    }

    public String getTime(){
        return "" + semester + year;
    }

    public char getSemester(){
        return semester;
    }

    public String getCode(){
        return code;
    }

    @Override
    public int compareTo(Course c1){
        if(year!= c1.year) {
            return year-c1.year;
        }
        return(c1.semester-semester);
    }



}
