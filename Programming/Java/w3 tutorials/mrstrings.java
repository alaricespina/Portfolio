public class mrstrings {
	public static void main(String[] args)	{
		String greeting = "Hello";
		System.out.println("String length:" + greeting.length());
		System.out.println(greeting);

		System.out.println(greeting.toUpperCase());   
		System.out.println(greeting.toLowerCase());

		//Finding a character
		String txt = "Please locate where 'locate' occurs!";
		System.out.println(txt.indexOf("locate")); // Outputs 7

		//String Concatenation using +
		String firstName = "John";
		String lastName = "Doe";
		System.out.println(firstName + " " + lastName);

		//String Concatenation using string.concat(string)
		firstName = "John ";
		lastName = "Doe";
		System.out.println(firstName.concat(lastName));

		//Using backslash escape character
		// Error: txt = "We are the so-called "Vikings" from the north.";

		//Correct
		txt = "We are the so-called \"Vikings\" from the north.";
		System.out.println(txt);

		/*
		Other Escape characters
	
		\n	New Line	
		\r	Carriage Return	
		\t	Tab	
		\b	Backspace	
		\f	Form Feed

		*/

		//Adding a string and an integer
		String a = "10";
		int b = 20;
		System.out.println(a+b);
	}

}