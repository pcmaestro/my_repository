package cursojava08variablesDeInstanciaYclase;

public class Main {

	public static void main(String[] args) {
		
		//yo puedo usar directamente lo declarado como static
		Juguete.numeroSerie = "XXX";
		
		Juguete j1 = new Juguete();
		j1.setNombre("Patines");
		j1.altura = 15;

		Juguete j2 = new Juguete();
		j2.setNombre("Peonza");
		j2.altura = 5;
		
		System.out.println("juguetes:");
		System.out.println(j1.getNombre() + 
				" altura: " + j1.altura +
				" numero de serie: " + j1.numeroSerie
				);
		System.out.println(j2.getNombre() + 
				" altura: " + j2.altura + 
				" numero de serie: " + j2.numeroSerie);
	}

}
