public class nyifnyen{
	public static void main(String[] args){
		int x = 20;
		int y = 30;

		//Simple if else
		if (x < y) {
			System.out.println("Halaman");
		} else {
			System.out.println("Hatdog");
		}

		//else if
		if (x > y) {
			System.out.println("Mas malaki ang x");
		} else if (x == y) {
			System.out.println("Parehas lang sila");
		} else if (x < y) {
			System.out.println("Mas malaki ang y");
		}

		//ternary operator
		String hakdug = (x < y) ? "HAHAHAHAA" : "lol";		
		System.out.println(hakdug);
	}
}