package practicaVentanaDiferencias;

import javax.swing.JFrame;

public class Main {

	public static void main(String[] args) {	
		
		JFrame ventana = new JFrame("Averigua las diferencias en la imagen de la derecha");
		ventana.setSize(900, 700);
		ventana.setLocation(250, 10);
		ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		ventana.setContentPane(new Panel(ventana));
	    ventana.setVisible(true);
		
		
	}

}
