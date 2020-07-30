package cursojava10ejercicioDiferencias;

import javax.swing.JFrame;

public class Main {

	public static void main(String[] args) {
		
		JFrame ventana = 
				new JFrame("Haz click en la diferencia de la derecha");
		ventana.setSize(800, 400);
		ventana.setLocation(100,100);
		ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		ventana.setContentPane(new MiPanel(ventana));
		ventana.setVisible(true);
	}

}
