package vista;

import javax.swing.JPanel;
import javax.swing.JLabel;
import java.awt.Font;

public class PanelInicial extends JPanel {
	private JLabel labelImagen;

	/**
	 * Create the panel.
	 */
	public PanelInicial() {
		setLayout(null);
		
		JLabel lblNewLabel = new JLabel("SISTEMA DE GESTION DE COCHES");
		lblNewLabel.setFont(new Font("Tahoma", Font.PLAIN, 25));
		lblNewLabel.setBounds(148, 146, 398, 84);
		add(lblNewLabel);
		
		JLabel lblBienvenidosAl = new JLabel("BIENVENIDOS AL");
		lblBienvenidosAl.setFont(new Font("Tahoma", Font.PLAIN, 25));
		lblBienvenidosAl.setBounds(236, 76, 202, 84);
		add(lblBienvenidosAl);
		
		labelImagen = new JLabel("");
		labelImagen.setBounds(196, 221, 275, 179);
		add(labelImagen);

	}
	public JLabel getLabelImagen() {
		return labelImagen;
	}
}
