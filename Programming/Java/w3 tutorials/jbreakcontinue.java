public class jbreakcontinue {
    public static void main(String[] args){

        //Using Break
        System.out.println("For Loop with break");
        System.out.println("-------------------");
        for(int i = 0; i < 10; i++){
            if(i==4){
                break;
            }
            System.out.println(i);
            //Only prints upto 3
        }

        //Using Continue
        System.out.println("For Loop with continue");
        System.out.println("----------------------");
        for (int j = 0; j < 5; j++){
            if (j == 2){
                continue;
            }
            System.out.println(j);
            //will skip printing 2 but print everything else
        }
    }
}