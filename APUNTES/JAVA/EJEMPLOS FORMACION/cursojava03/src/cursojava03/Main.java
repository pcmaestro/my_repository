package cursojava03;

import javax.swing.JFrame;

/**
 * 
 * @author aressancho
 *
 * Clase que muestra como hacer una ventana de verdad
 */
public class Main {

	public static void main(String[] args) {
		//dominar java es saber programar en java 
		//nuestras cosas y saber usar las que ya hay, y 
		//las que pueda conseguir de frameworks 
		//y librerias externas
		
		JFrame ventana = new JFrame();
		ventana.setVisible(true);
		ventana.setSize(500, 200);
		ventana.setLocation(100, 200);
		ventana.setDefaultCloseOperation(3);
		
		JFrame ventanaDos = new JFrame();
		ventanaDos.setVisible(true);
		ventanaDos.setSize(200, 400);
		ventanaDos.setLocation(300, 100);
		ventanaDos.setDefaultCloseOperation(3);
		
	}//end main

}//end class
