package cursojava06modificadores1;

public class Main {

	public static void main(String[] args) {
		
		//tipos de dato mas comunes:
		
		String frase = "hola";
		//frase = 123; da error
		int numero = 123;
		double precio = 23.45d;
		double precioDos = 23.45;
		//despues del . puede haber hasta 16 numeros
		
		float altura = 4.666666f;//en un float puede haber 
		//hasta 6 numeros
		
		char letra = 'a';
		char otraLetra = 123;
		
		boolean interruptor = false;
		
		short numeroPequeño = 123;
		long numeroGrande = 1234567890l;
		
		//modificadores en variables
		
		final int maxUsuarios = 200;
		//maxUsuarios = 350; esto da error porque al poner 
		//final al definir la variable, ya no puedo cambiarla
		
		
	}
	
}
