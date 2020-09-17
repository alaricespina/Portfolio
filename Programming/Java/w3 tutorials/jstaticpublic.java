public class jstaticpublic {
    public static void main(String[] args){

        //Static can be called anywhere
        notmove();

        //Public needs object to be called
        jstaticpublic halaman = new jstaticpublic();
        halaman.nasapubliko();
    }

    static void notmove(){
        System.out.println("Static Function to");
    }

    public void nasapubliko(){
        System.out.println("Public Function to");
    }
}