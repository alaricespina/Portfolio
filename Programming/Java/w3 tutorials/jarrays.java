public class jarrays {
    public static void main(String[] args){
        String[] mames = {"Manty","Minty","Mert","Morty","Murty"};
        int[][] numeros = {{1,2,3,4,5},{6,7,8}};

        System.out.println("Arrays Initilaized");
        //prints manty
        System.out.println("index 0 at mames array: " +mames[0]);

        //prints 5
        System.out.println("length of mames array: "+ mames.length);

        System.out.println("For Loop for a single dimension array");
        //loop through an array
        for (int i = 0; i < mames.length ; i++){
            System.out.println(mames[i]);
        }

        //2d arrays
        System.out.println("index 1 at index 1 of numeros array: " + numeros[1][1]);

        System.out.println("For Loop for a two dimension array");
        for (int x = 0; x < numeros.length; x++){
            for (int y = 0; y < numeros[x].length; y++){
                System.out.println(numeros[x][y]);
            }
        }
    }
}