public class nyath{
	public static void main(String[] args){
		int a = 10, b = 5;

		//Max and Min
		System.out.println(Math.max(a,b)); //prints 10
		System.out.println(Math.min(a,b)); //prints 5

		//Sqrt
		System.out.println(Math.sqrt(a)); //3.....

		//Absolute Value
		System.out.println(Math.abs(-9999999));

		//Random Numbers from 0.0(in) to 1.0(out)
		System.out.println(Math.random());

		//Random Numbers between 0 - 100
		int randomNum = (int)(Math.random() * 101);  // 0 to 100
		System.out.println(randomNum);

		//Random Numbers will automatically be generated upon running

	}
}