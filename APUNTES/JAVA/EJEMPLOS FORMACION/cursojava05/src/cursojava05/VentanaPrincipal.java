package cursojava05;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class VentanaPrincipal extends JFrame implements ActionListener {
	//en java se define aqui todo lo que se va a usar en 
	//diferentes metodos de esta clase, y luego cada metodo
	//usa lo definido aquí como quiera
	JTextField entradaEuros = new JTextField(10);
	
	// esta clase hereda de JFrame, por ello
	// todo lo que estuviera en JFrame es como si
	// estuviera aquí tambien,
	// muy importante: por ello, VentanaPrincipal
	// puede ser considerado como si fuera un JFrame

	public VentanaPrincipal() {
		System.out.println("se ejecuta el constructor");
		this.prepararVentana();
	}

	void convertirAdolares() {
		
		
	}
	
	// metodo que prepara todo lo que tiene la ventana
	void prepararVentana() {
		// componentes de la ventana
		JLabel labelTexto = new JLabel();
		labelTexto.setText("introduce los euros");

		JButton boton = new JButton("Convertir a Dolares");
		//para decirle al boton que codigo ejecutar cuando se le pulse
		//debo indicarle donde está el codigo del 
		//metodo actionPerformed. 
		//poniendo addActionLister(this) se ejecutara el 
		//metodo actionPerformed que tenemos mas abajo
		boton.addActionListener(this);
		
		JPanel panel = new JPanel();

		panel.add(labelTexto);
		panel.add(entradaEuros);
		panel.add(boton);
		
		this.setContentPane(panel);
		this.setSize(600, 200);
		this.setLocation(100, 100);
		this.setVisible(true);
		this.setDefaultCloseOperation(3);
	}// end prepararVentana

	
	public void actionPerformed(ActionEvent e) {
		System.out.println("boton pulsado");
		String introducido  = entradaEuros.getText();
		double introducidoDouble = Double.parseDouble(introducido);
		double dolares = introducidoDouble * 1.13;
		JOptionPane.showMessageDialog(this, "dolares: " + dolares);
		
	}

}// end class
