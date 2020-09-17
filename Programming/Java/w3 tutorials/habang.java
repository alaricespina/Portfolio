public class habang{
	public static void main(String[] args) {

		//While Loop
		int i = 0;
		while (i < 5) {
			System.out.println(i);
			i++;


		//Do While Loop

		i = 0;
		do {
			System.out.println(i);
			i++;
		}
		while (i < 6);
		}

		//For Loop
		System.out.println("------------");

		for (int j = 0; j < 10; j++){
			System.out.println(j);
		}

		//For each loop
		System.out.println("------------");

		String[] cars = {"Volvo","BMW","Mercedes"};
		for (String x: cars) {
			System.out.println(x);
		}

		//for break
		System.out.println("------------");
		for (int a = 0; a < 10; a++) {
		  if (a == 4) {
		    break;
		  }
		  System.out.println(a);
		}

		//for continue
		System.out.println("------------");
		for (int b = 0; b < 10; b++) {
		  if (b == 4) {
		    continue;
		  }
		  System.out.println(b);
		}
		System.out.println("Halaman");
		//while break
		System.out.println("------------");
		i = 0;
		while (i < 10) {
		  System.out.println(i);
		  i++;
		  if (i == 4) {
		    break;
		  }
		}

		//while continue
		System.out.println("------------");
		i = 0;
		while (i < 10) {
		  if (i == 4) {
		    i++;
		    continue;
		  }
		  System.out.println(i);
		  i++;
		}
	}
}