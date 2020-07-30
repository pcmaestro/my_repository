package vista;

import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.JList;
import java.awt.Color;
import javax.swing.JButton;
import javax.swing.JScrollPane;

public class PanelListarLibros extends JPanel {
	private JList jListLibros;
	private JButton botonEditar;
	private JButton botonBorrar;
	private JScrollPane scrollPane;

	/**
	 * Create the panel.
	 */
	public PanelListarLibros() {
		setLayout(null);
		
		JLabel lblListadoDeLibros = new JLabel("Listado de Libros");
		lblListadoDeLibros.setBounds(168, 16, 108, 16);
		add(lblListadoDeLibros);
		
		scrollPane = new JScrollPane();
		scrollPane.setBounds(54, 61, 351, 189);
		add(scrollPane);
		
		jListLibros = new JList();
		scrollPane.setViewportView(jListLibros);
		
		botonBorrar = new JButton("BORRAR");
		botonBorrar.setBounds(49, 265, 117, 29);
		add(botonBorrar);
		
		botonEditar = new JButton("EDITAR");
		botonEditar.setBounds(168, 265, 117, 29);
		add(botonEditar);

	}
	public JList getJListLibros() {
		return jListLibros;
	}
	public JButton getBotonEditar() {
		return botonEditar;
	}
	public JButton getBotonBorrar() {
		return botonBorrar;
	}
}
