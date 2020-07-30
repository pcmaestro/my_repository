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

public class PanelListado extends JPanel {
	private JScrollPane scrollPane;
	private JButton botonEditar;
	private JButton botonBorrar;
	private JList list;

	/**
	 * Create the panel.
	 */
	public PanelListado() {
		setLayout(null);
		
		JLabel lblNewLabel = new JLabel("LISTADO DE COCHES");
		lblNewLabel.setBounds(278, 26, 144, 19);
		lblNewLabel.setFont(new Font("Tahoma", Font.PLAIN, 15));
		add(lblNewLabel);
		
		scrollPane = new JScrollPane();
		scrollPane.setBounds(30, 60, 700, 303);
		add(scrollPane);
		
		list = new JList();
		scrollPane.setViewportView(list);
		
		botonEditar = new JButton("EDITAR");
		botonEditar.setBounds(79, 373, 89, 36);
		add(botonEditar);
		
		botonBorrar = new JButton("BORRAR");
		botonBorrar.setBounds(518, 373, 89, 35);
		add(botonBorrar);

	}
	public JList getList() {
		return list;
	}

	public JButton getBotonEditar() {
		return botonEditar;
	}
	public JButton getBotonBorrar() {
		return botonBorrar;
	}
}
