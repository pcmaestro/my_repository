package vista;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;

public class VentanaPrincipal extends JFrame {

	private JPanel contentPane;
	private JMenuItem menuListarLibros;
	private JMenuItem menuRegistrarLibro;

	/**
	 *	MAIN QUE NO VAMOS A USAR
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					VentanaPrincipal frame = new VentanaPrincipal();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public VentanaPrincipal() {
		setTitle("Aplicacion de Gestion Libreria");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 462, 392);
		
		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);
		
		JMenu mnLibros = new JMenu("Libros");
		menuBar.add(mnLibros);
		
		menuRegistrarLibro = new JMenuItem("Registrar Nuevo Libro");
		mnLibros.add(menuRegistrarLibro);
		
		menuListarLibros = new JMenuItem("Listar Libros");
		mnLibros.add(menuListarLibros);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setLayout(new BorderLayout(0, 0));
		setContentPane(contentPane);
	}

	public JMenuItem getMenuListarLibros() {
		return menuListarLibros;
	}
	public JMenuItem getMenuRegistrarLibro() {
		return menuRegistrarLibro;
	}
}
