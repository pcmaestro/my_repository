package cursojava13colecciones;

import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		
		ArrayList<String> palabras = new ArrayList<String>();
		palabras.add("paisaje");
		palabras.add("montaña");
		palabras.add("playa");
		//recorrer una lista:
		for (String p : palabras) {
			System.out.println(p);
		}
		System.out.println("primera palabra: " + palabras.get(0));
		palabras.remove(0);
		System.out.println("primera palabra, despues de borrar: " + 
				palabras.get(0));
		System.out.println("elementos en palabras: " + palabras.size());
	}//End main

}//end class






