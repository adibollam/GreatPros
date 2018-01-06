public class Main {
    public static void main(String[] args) {

        LCReader loader = new LCReader();
        loader.readFiles();
        loader.parseFiles();

        DataWriter selector = new DataWriter();
        //selector.writefile(selector.results);
        selector.selectRows();




    }
}
