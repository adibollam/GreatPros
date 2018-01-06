import java.io.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;


public class DataWriter {
    public static final String url = "jdbc:sqlite:/Users/adibollam/GreatPros/Database/masterjava.db";
    public static final String destinationFile = "/Users/adibollam/GreatPros/Java/DataFiles/Parsed/Total.csv";


    public void loadToDatabase(String line){

        String table = ("CREATE TABLE IF NOT EXISTS parsedData (\n"
                        + " Date text,\n"
                        + " JobType VARCHAR(60),\n"
                        + " Cost VARCHAR(1),\n"
                        + " Sales VARCHAR(1),\n"
                        + " Source VARCHAR(1),\n"
                        + " Zip integer\n"
                        + ");");
        String insertsql = "INSERT OR IGNORE INTO parsedData VALUES " + line;


        try (Connection conn = DriverManager.getConnection(url);
             Statement stmt = conn.createStatement();
             PreparedStatement pstmt = conn.prepareStatement(insertsql)
             ) {
            stmt.execute(table);
            pstmt.executeUpdate();


        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

    }

    public void selectRows(){
        String sqlselect = "SELECT city, COUNT(*) as demand  FROM cities as a, parsedData as b WHERE a.zip = b.zip and city !=  ' ' GROUP BY city ORDER BY COUNT(*) DESC";
        BufferedWriter bufferedWriter = null;
        try {
            Connection conn = DriverManager.getConnection(url);
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sqlselect);

            //Opened file for writing.
            try {
                FileWriter fileWriter = new FileWriter(destinationFile);
                bufferedWriter = new BufferedWriter(fileWriter);

            } catch(FileNotFoundException ex) {
                System.out.println("Unable to open file '" + destinationFile + "'");
            }
            catch(IOException ex) {
                ex.printStackTrace();
            }

            //For each line extracted from database write to a file.
            while(rs.next()){
                try {
                    System.out.println(rs.getString("city") + "," + rs.getInt("demand") + "\n");
                    bufferedWriter.write(rs.getString("city") + "," + rs.getInt("demand") + "\n");
                } catch(IOException ex) {
                    ex.printStackTrace();
                }
            }

            try {
                bufferedWriter.close();
            }  catch(IOException ex) {
                ex.printStackTrace();
            }






        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }



    }

    public void writefile(ResultSet results){
        try{
            while(results.next()){
                System.out.println(results.getString("city"));
            }
        }
        catch (SQLException e){
            System.out.println(e.getMessage());

        }

    }
}
