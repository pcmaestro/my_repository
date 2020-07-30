package practicaJuegoPelota;

import java.awt.Color;

import javax.swing.JFrame;


public class Main {

	public static void main(String[] args) {
		JFrame ventana = new JFrame("Lleva la bola a la zona de meta");
		ventana.setSize(800, 600);
		ventana.setLocation(100,100);
		ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		ventana.setContentPane(new MiPanel());
		ventana.setVisible(true);
		
	}

}
