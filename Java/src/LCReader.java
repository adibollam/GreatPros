import java.io.BufferedReader;
import java.io.IOException;
import java.io.*;
import java.util.*;

public class LCReader{

    List<String> results =  new ArrayList<String>();
    public static final String filepath = "/Users/adibollam/GreatPros/Java/DataFiles/Raw";
    public static final int[] colnum = {0,4};

    public LCReader(){

    }

    public void readFiles() {
        File folder = new File(filepath);
        File[] fileslist = folder.listFiles((dir, name) -> !name.equals(".DS_Store"));
        for (File file : fileslist) {
            if (file.isFile()) {
                results.add(file.getName());

            }
        }
    }

    public void parseFiles(){


        for (String file : results) {
            String fileName = filepath + "/" + file;
            String line = null;
            boolean firstLine = false;


            try {
                DataParser parse = new DataParser();

                DataWriter loadMaster = new DataWriter();

                FileReader fileReader = new FileReader(fileName);
                BufferedReader bufferedReader = new BufferedReader(fileReader);


                while((line = bufferedReader.readLine()) != null) {
                    if(firstLine) {
                        parse.setDate(line.split(",")[colnum[0]]);
                        parse.setjobType(line.split(",")[colnum[1]]);
                        parse.setZip(line.split(",")[colnum[1]]);

                        System.out.println(parse.getNewRow());

                        loadMaster.loadToDatabase(parse.getNewRow());


                    } else {
                        firstLine = true;
                    }

                }
                bufferedReader.close();
            }
            catch(FileNotFoundException ex) {
                System.out.println("Unable to open file '" + fileName + "'");
            }
            catch(IOException ex) {
                ex.printStackTrace();
            }

        }

    }

    public void movefiles(){

    }
}
