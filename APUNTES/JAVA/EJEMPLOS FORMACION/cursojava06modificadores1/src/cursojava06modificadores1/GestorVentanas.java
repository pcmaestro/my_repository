package cursojava06modificadores1;

public class GestorVentanas {

	
	void mostrarVentanaPrincipal() {
		VentanaPrincipal ventana = new VentanaPrincipal();
		//no puedo acceder directaemnte a la altura
		//ventana.altura = 300;
		
		ventana.prepararVentana();
		
		System.out.println(
				"altura de la ventana: " + ventana.getAltura());
	}

	
}
