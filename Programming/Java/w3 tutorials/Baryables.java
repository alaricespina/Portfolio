public class Baryables {
	public static void main(String[] args){
		String name = "Variables";
		int thisNum = 13;

		System.out.println(thisNum);
		System.out.println(name);

		//Assigning variable type first before value
		int secondNum;
		secondNum = 26;
		System.out.println(secondNum);

		//Reassigning variables will overwrite previous
		secondNum = 39;
		System.out.println(secondNum);

		//Final Variables
		final int thirdNum = 52;
		//thirdNum = 63, this will result to error
		System.out.println(thirdNum);

		//Declaration of Other variables
		//int myNum = 5;
		//float myFloatNum = 5.99f;
		//char myLetter = 'D';
		//boolean myBool = true;
		String myText = "Hello";

		System.out.println(myText + name);

		//Declaring Multiple Variables
		int x = 5, y = 6, z = 50;
		System.out.println(x + y + z);
	}
}