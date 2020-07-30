package cursojava19Random;

import java.util.Random;

public class Main {

	public static void main(String[] args) {
		Random r = new Random();
		int aleatorio = 101 + r.nextInt(100);
		System.out.println(aleatorio);
		
		
	}

}
