public class nrapcasting {
	public static void main(String[] args){
		/*
		Widening Casting 
		converting a smaller type to a larger type size
		byte -> short -> char -> int -> long -> float -> double

		Narrowing Casting 
		(manually)
		converting a larger type to a smaller size type
		double -> float -> long -> int -> char -> short -> byte

		*/

		//Widening
		int myInt = 9;
    	double myDouble = myInt; // Automatic casting: int to double

    	System.out.println(myInt);      // Outputs 9
   		System.out.println(myDouble);   // Outputs 9.0

   		//Narrowing
   		myDouble = 9.78;
    	myInt = (int) myDouble; // Manual casting: double to int

	    System.out.println(myDouble);   // Outputs 9.78
	    System.out.println(myInt);      // Outputs 9

	}
}