public class jmethods{
    
    //Methods = functions
    public static void main(String[] args){
        for (int i = 0; i < 3; i++){
            Halaman("Hatdog " + i);
        }
        Halaman("----------------");

        int presyo = HaloHalo(3,40);

        Halaman("Kailangan mo magbayad ng: " + presyo);
        Halaman("----------------");

        double presyo2 = HaloHalo(3.6,39.99);
        Halaman("Discounted presyo pre: " + presyo2);
        Halaman("----------------");

        HaloHalo();

        Halaman("----------------");
        int recursionthing = Makulit(10);
        Halaman("Sagot: "+ recursionthing);
    }

    static void Halaman(String thingymatron){
        System.out.println(thingymatron);
    }

    static int HaloHalo(int x, int y){
        System.out.println("You ordered: " + x + " Halo-Halo for PHP " + y + " each");
        System.out.println("Total Bill amount has been calculated");

        return x * y;
    }

    //Method Overloading

    static double HaloHalo(double x, double y){
        System.out.println("You ordered: " + x + " Halo-Halo for PHP " + y + " each");
        System.out.println("Total Bill amount has been calculated");

        return x * y;
    }

    static void HaloHalo(){
        System.out.println("Sabog, wala ka namang nilagay na order");
    }

    static int Makulit(int x){
        if (x > 0){
            return x + Makulit(x - 1);
        } else {
            return 1;
        }
    }
}