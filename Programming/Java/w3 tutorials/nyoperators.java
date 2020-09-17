public class nyoperators{
	public static void main(String[] args){
		
		int a = 10, b = 20;
		/*

		Arithmetic

		+	Addition	Adds together two values	x + y	
		-	Subtraction	Subtracts one value from another	x - y	
		*	Multiplication	Multiplies two values	x * y	
		/	Division	Divides one value by another	x / y	
		%	Modulus	Returns the division remainder	x % y	
		++	Increment	Increases the value of a variable by 1	++x	
		--	Decrement	Decreases the value of a variable by 1	--x
		
		*/

		System.out.println(a+b); //30
		System.out.println(a-b); //-10
		System.out.println(a*b); //200
		System.out.println(b/a); //2
		System.out.println(b%a); //0
		System.out.println(++a); //11
		System.out.println(--a); //10 because 11 on previous
		System.out.println("---------------");

		/*

		Assignment

		=	x = 5	x = 5	
		+=	x += 3	x = x + 3	
		-=	x -= 3	x = x - 3	
		*=	x *= 3	x = x * 3	
		/=	x /= 3	x = x / 3	
		%=	x %= 3	x = x % 3

		*/

		int c;

		c = 5;
		c += 3; //8
		System.out.println(c);
		c -= 3; //5
		System.out.println(c);
		c *= 3; //15
		System.out.println(c);
		c /= 3; //5
		System.out.println(c);
		c %= 3; //2
		System.out.println(c);
		System.out.println("---------------");

		/*

		Comparison

		==	Equal to	x == y	
		!=	Not equal	x != y	
		>	Greater than	x > y	
		<	Less than	x < y	
		>=	Greater than or equal to	x >= y	
		<=	Less than or equal to	x <= y
		*/

		int m = 69, n = 28;
		System.out.println(m == n); //false
		System.out.println(m != n); //true
		System.out.println(m > n); //true
		System.out.println(m < n); //false
		System.out.println(m >= n); //true
		System.out.println(m <= n); //false
		System.out.println("---------------");

		/*

		Logical 


		&& 	Logical and	Returns true if both statements are true	x < 5 &&  x < 10	
		|| 	Logical or	Returns true if one of the statements is true	x < 5 || x < 4	
		!	Logical not	Reverse the result, returns false if the result is true	!(x < 5 && x < 10)
		*/

		System.out.println(m >= n && n <= m); //true
		System.out.println(m == n || m != n); //true
		System.out.println(!(m <= n && m < n)); //true
	}
}
