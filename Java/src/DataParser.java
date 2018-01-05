import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class DataParser {
    public String zipcode;
    public String jobtype;
    public String dayonly;

    public DataParser(){

    }
    public void setDate(String datetime) {
        Pattern pattern = Pattern.compile("(\\d{1,2}/\\d{1,2}/\\d{4})");
        Matcher date = pattern.matcher(datetime);
        while(date.find()){
            dayonly = date.group();
        }

    }
    public void setZip(String address){

        Pattern pattern = Pattern.compile(".*(Zip=)");
        Matcher zip = pattern.matcher(address);
        while(zip.find()) {
            zipcode = address.substring(zip.end(), zip.end() + 5);
        }

    }
    public void setjobType(String address){

        Pattern pattern = Pattern.compile(".*(jobtype=)");
        Matcher job = pattern.matcher(address);
        while(job.find()) {
            jobtype = address.substring(job.end(), address.length() - 1);
        }
    }
    public String getNewRow(){
        return dayonly + "," + jobtype + "," + "x" + "," + "x" + "," + "x" + "," + zipcode;
    }
}
