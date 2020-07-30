package cursojava04;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class Main {

	public static void main(String[] args) {
		//componentes de la ventana
		JLabel labelTexto = new JLabel();
		labelTexto.setText("introduce los euros");
		
		JTextField entradaEuros = new JTextField(10);
		
		JButton boton = new JButton("Convertir a Dolares");
		
		JPanel panel = new JPanel();
		
		panel.add(labelTexto);
		panel.add(entradaEuros);
		panel.add(boton);
		
		//codigo para preparar la ventana
		JFrame ventana = new JFrame();
		ventana.setContentPane(panel);
		
		ventana.setSize(600, 200);
		ventana.setLocation(100, 100);
		ventana.setVisible(true);
		ventana.setDefaultCloseOperation(3);
		
		
	}

}
