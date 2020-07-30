package vista;

import javax.swing.JPanel;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JList;
import javax.swing.JButton;
import java.awt.Color;
import javax.swing.UIManager;
import javax.swing.border.LineBorder;
import javax.swing.JScrollPane;
import javax.swing.JTable;

public class PanelListado extends JPanel {
	private JButton botonEditar;
	private JButton botonBorrar;
	private JTable tabla;

	/**
	 * Create the panel.
	 */
	public PanelListado() {
		setLayout(null);
		
		JLabel lblNewLabel = new JLabel("LISTADO DE COCHES");
		lblNewLabel.setBounds(278, 26, 144, 19);
		lblNewLabel.setFont(new Font("Tahoma", Font.PLAIN, 15));
		add(lblNewLabel);
		
		botonEditar = new JButton("EDITAR");
		botonEditar.setBounds(79, 373, 89, 36);
		add(botonEditar);
		
		botonBorrar = new JButton("BORRAR");
		botonBorrar.setBounds(518, 373, 89, 35);
		add(botonBorrar);
		
		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(59, 61, 609, 301);
		add(scrollPane);
		
		tabla = new JTable();
		scrollPane.setViewportView(tabla);

	}


	public JButton getBotonEditar() {
		return botonEditar;
	}
	public JButton getBotonBorrar() {
		return botonBorrar;
	}
	public JTable getTabla() {
		return tabla;
	}
}
