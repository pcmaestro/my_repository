package vista;

import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;

public class PanelInsertarLibro extends JPanel {
	private JTextField entradaTitulo;
	private JTextField entradaAutor;
	private JTextField entradaPrecio;
	private JTextField entradaPaginas;
	private JButton botonRegistrarLibro;

	/**
	 * Create the panel.
	 */
	public PanelInsertarLibro() {
		setLayout(null);
		
		JLabel lblIntroduceLosDatos = new JLabel("Introduce los datos del libro");
		lblIntroduceLosDatos.setBounds(126, 6, 178, 16);
		add(lblIntroduceLosDatos);
		
		JLabel lblTitulo = new JLabel("titulo:");
		lblTitulo.setBounds(123, 61, 61, 16);
		add(lblTitulo);
		
		JLabel lblAutor = new JLabel("autor:");
		lblAutor.setBounds(123, 103, 61, 16);
		add(lblAutor);
		
		JLabel lblPrecio = new JLabel("precio:");
		lblPrecio.setBounds(123, 141, 61, 16);
		add(lblPrecio);
		
		JLabel lblPaginas = new JLabel("paginas:");
		lblPaginas.setBounds(123, 179, 61, 16);
		add(lblPaginas);
		
		entradaTitulo = new JTextField();
		entradaTitulo.setBounds(199, 56, 130, 26);
		add(entradaTitulo);
		entradaTitulo.setColumns(10);
		
		entradaAutor = new JTextField();
		entradaAutor.setColumns(10);
		entradaAutor.setBounds(199, 98, 130, 26);
		add(entradaAutor);
		
		entradaPrecio = new JTextField();
		entradaPrecio.setColumns(10);
		entradaPrecio.setBounds(199, 136, 130, 26);
		add(entradaPrecio);
		
		entradaPaginas = new JTextField();
		entradaPaginas.setColumns(10);
		entradaPaginas.setBounds(199, 174, 130, 26);
		add(entradaPaginas);
		
		botonRegistrarLibro = new JButton("Registrar Libro");
		botonRegistrarLibro.setBounds(163, 226, 117, 29);
		add(botonRegistrarLibro);

	}
	public JButton getBotonRegistrarLibro() {
		return botonRegistrarLibro;
	}
	public JTextField getEntradaPaginas() {
		return entradaPaginas;
	}
	public JTextField getEntradaPrecio() {
		return entradaPrecio;
	}
	public JTextField getEntradaAutor() {
		return entradaAutor;
	}
	public JTextField getEntradaTitulo() {
		return entradaTitulo;
	}
}
