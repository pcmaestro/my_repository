package vista;

import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.JTextArea;

public class PanelListarLibros extends JPanel {
	private JTextArea listadoLibros;

	/**
	 * Create the panel.
	 */
	public PanelListarLibros() {
		setLayout(null);
		
		JLabel lblListadoDeLibros = new JLabel("Listado de Libros");
		lblListadoDeLibros.setBounds(168, 16, 108, 16);
		add(lblListadoDeLibros);
		
		listadoLibros = new JTextArea();
		listadoLibros.setBounds(40, 44, 357, 221);
		add(listadoLibros);

	}
	public JTextArea getListadoLibros() {
		return listadoLibros;
	}
}
