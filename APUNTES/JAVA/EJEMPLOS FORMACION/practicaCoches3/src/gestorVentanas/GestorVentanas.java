package gestorVentanas;

import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.net.URL;
import java.util.ArrayList;

import javax.swing.ButtonGroup;
import javax.swing.DefaultListModel;
import javax.swing.ImageIcon;
import javax.swing.JComboBox;
import javax.swing.JOptionPane;
import javax.swing.SwingUtilities;

import daos.CochesDAO;
import daos.CochesDAOimplArchivo;
import daos.CochesDAOimplArrayList;
import modelo.Coche;
import vista.PanelEdicion;
import vista.PanelInicial;
import vista.PanelListado;
import vista.PanelRegistro;
import vista.VentanaPrincipal;

public class GestorVentanas implements ActionListener {

	// Objeto ArrayList donde se guardan los coches
	CochesDAO cochesDAO = new CochesDAOimplArchivo();

	// Objetos de la ventana principal y los paneles
	private VentanaPrincipal ventanaPrincipal = new VentanaPrincipal();
	private PanelInicial panelInicial = new PanelInicial();
	private PanelListado panelListado = new PanelListado();
	private PanelRegistro panelRegistro = new PanelRegistro();
	private PanelEdicion panelEdicion = new PanelEdicion();

	// Contenido del Combo Box de cilindrada
	private String[] cilindradas = { "Seleccionar", "1.600cc", "1.800cc", "2.000cc" };

	// Variable de indice para edicion
	private static int indiceCocheSeleccionado = -1;

	// Variable de indice para borrar
	int indiceBorrar = -1;
	
	//Objeto coche
	Coche c = new Coche();


	public GestorVentanas() {

		// Añadimos los Listener de eventos

		ventanaPrincipal.getMenuRegistro().addActionListener(this);
		ventanaPrincipal.getMenuListado().addActionListener(this);

		// URL urlImagen =
		// ImageIcon.class.getClassLoader().getResource("src\\imagenes\\coche_fantastico.jpg");
		panelInicial.getLabelImagen().setIcon(new ImageIcon("src\\imagenes\\coche_fantastico.jpg"));

		panelListado.getBotonEditar().addActionListener(this);
		panelListado.getBotonBorrar().addActionListener(this);

		panelRegistro.getInputMarca().addActionListener(this);
		panelRegistro.getInputModelo().addActionListener(this);
		panelRegistro.getInputColor().addActionListener(this);
		panelRegistro.getRadioDiesel().addActionListener(this);
		panelRegistro.getRadioGasolina().addActionListener(this);
		panelRegistro.getComboCilindrada().addActionListener(this);
		panelRegistro.getInputPrecio().addActionListener(this);
		panelRegistro.getBotonRegistrar().addActionListener(this);

		// Añadimos el contenido del Combo Box
		for (String i : cilindradas) {
			panelRegistro.getComboCilindrada().addItem(i);
		}

		panelEdicion.getInputMarca().addActionListener(this);
		panelEdicion.getInputModelo().addActionListener(this);
		panelEdicion.getInputColor().addActionListener(this);
		panelEdicion.getRadioDiesel().addActionListener(this);
		panelEdicion.getRadioGasolina().addActionListener(this);
		panelEdicion.getComboCilindrada().addActionListener(this);
		panelEdicion.getInputPrecio().addActionListener(this);
		panelEdicion.getBotonModificar().addActionListener(this);

		// Indicamos el panel que cargará inicialmente
		ventanaPrincipal.setContentPane(panelInicial);

		// Hacemos visible la ventana principal
		ventanaPrincipal.setVisible(true);
	}

	private void cargarPanelListadoCoches() {
		ventanaPrincipal.setContentPane(panelListado);
		ArrayList<Coche> coches = cochesDAO.listarCoches();
		DefaultListModel<String> listModel = new DefaultListModel<String>();

		for (Coche c : coches) {
			listModel.addElement(c.toString());
		} // end for

		panelListado.getList().setModel(listModel);

	}

	@Override
	public void actionPerformed(ActionEvent e) {

		// Obtención de la fuente del evento
		Object elementoSeleccionado = e.getSource();

		// Menú

		if (elementoSeleccionado == ventanaPrincipal.getMenuRegistro()) {
			ventanaPrincipal.setContentPane(panelRegistro);

		} else if (elementoSeleccionado == ventanaPrincipal.getMenuListado()) {
			this.cargarPanelListadoCoches();

		} else if (elementoSeleccionado == panelRegistro.getBotonRegistrar()) {
			String marca = panelRegistro.getInputMarca().getText();
			String modelo = panelRegistro.getInputModelo().getText();
			String color = panelRegistro.getInputColor().getText();

			ButtonGroup grupoRadio = new ButtonGroup();
			grupoRadio.add(panelRegistro.getRadioDiesel());
			grupoRadio.add(panelRegistro.getRadioGasolina());

			String motor = null;

			if (panelRegistro.getRadioDiesel().isSelected()) {
				motor = "Diesel";
			} else if (panelRegistro.getRadioGasolina().isSelected()) {
				motor = "Gasolina";
			}

			int indiceSeleccionado = panelRegistro.getComboCilindrada().getSelectedIndex();
			String cilindrada = cilindradas[indiceSeleccionado];

			String precio = panelRegistro.getInputPrecio().getText();

			if (marca == null || modelo == null || color == null || motor == null || cilindrada == null
					|| precio == null) {

				JOptionPane.showMessageDialog(null, "Debes indicar datos en todos los campos");

			} else {

				Coche coche = new Coche(marca, modelo, color, motor, cilindrada, precio);

				cochesDAO.registrarCoche(coche);

				JOptionPane.showMessageDialog(null, "Coche registrado correctamente");

				panelRegistro.getInputMarca().setText(null);
				panelRegistro.getInputModelo().setText(null);
				panelRegistro.getInputColor().setText(null);
				panelRegistro.getRadioDiesel().setSelected(false);
				panelRegistro.getRadioGasolina().setSelected(false);
				panelRegistro.getComboCilindrada().setSelectedIndex(0);
				panelRegistro.getInputPrecio().setText(null);
				marca = null;
				modelo = null;
				color = null;
				motor = null;
				cilindrada = null;
				precio = null;
			} // end if valores de registro null

		} else if (elementoSeleccionado == panelListado.getBotonBorrar()) {
			int indiceBorrar = panelListado.getList().getSelectedIndex();

			if (indiceBorrar == -1) {
				JOptionPane.showMessageDialog(null, "Selecciona un elemento");
			} else {
				cochesDAO.borrarCoche(indiceBorrar);
				JOptionPane.showMessageDialog(null, "Coche eliminado");
				this.cargarPanelListadoCoches();
			}

		} else if (elementoSeleccionado == panelListado.getBotonEditar()) {

			indiceCocheSeleccionado = panelListado.getList().getSelectedIndex();
			
			System.out.println("El valor de indiceCocheSeleccionado en L187 es " + indiceCocheSeleccionado);
			
			System.out.println("La longitud de la lista es " + panelListado.getList().getModel().getSize());
			
			if (indiceCocheSeleccionado == -1) {
				JOptionPane.showMessageDialog(null, "Selecciona un elemento");
			} else {
				ventanaPrincipal.setContentPane(panelEdicion);
				//Almacenamos en c el objeto coche seleccionado
				c = cochesDAO.obtenerCoche(indiceCocheSeleccionado);
				panelEdicion.getInputMarca().setText(c.getMarca());
				panelEdicion.getInputModelo().setText(c.getModelo());
				panelEdicion.getInputColor().setText(c.getColor());

				if (c.getMotor().equals("Diesel")) {
					panelEdicion.getRadioDiesel().setSelected(true);
				} else if (c.getMotor().equals("Gasolina")) {
					panelEdicion.getRadioGasolina().setSelected(true);
				} // end if motor

				for (String i : cilindradas) {
					panelEdicion.getComboCilindrada().addItem(i);
				}

				if (c.getCilindrada().equals("1.600cc")) {
					panelEdicion.getComboCilindrada().setSelectedIndex(0);
				} else if (c.getCilindrada().equals("1.800cc")) {
					panelEdicion.getComboCilindrada().setSelectedIndex(1);

				} else if (c.getCilindrada().contentEquals("2.000cc")) {
					panelEdicion.getComboCilindrada().setSelectedIndex(2);
				} // end if cilindrada

				panelEdicion.getInputPrecio().setText(c.getPrecio());
			} // end if indiceCocheSeleccionado

			System.out.println("El valor de indiceCocheSeleccionado en L225 es " + indiceCocheSeleccionado);
			
		} else if (elementoSeleccionado == panelEdicion.getBotonModificar()) {
			
			System.out.println("El valor de indiceCocheSeleccionado en L227 es " + indiceCocheSeleccionado);
			
			String marca = panelEdicion.getInputMarca().getText();
			String modelo = panelEdicion.getInputModelo().getText();
			String color = panelEdicion.getInputColor().getText();

			ButtonGroup grupoRadio = new ButtonGroup();
			grupoRadio.add(panelEdicion.getRadioDiesel());
			grupoRadio.add(panelEdicion.getRadioGasolina());

			String motor = null;

			if (panelEdicion.getRadioDiesel().isSelected()) {
				motor = "Diesel";
			} else if (panelEdicion.getRadioGasolina().isSelected()) {
				motor = "Gasolina";
			} // end if radio

			int indiceSeleccionado = panelEdicion.getComboCilindrada().getSelectedIndex();
			String cilindrada = cilindradas[indiceSeleccionado];

			String precio = panelEdicion.getInputPrecio().getText();
			
			cochesDAO.actualizarCoche(marca, modelo, color, motor, cilindrada, precio, indiceCocheSeleccionado);

			JOptionPane.showMessageDialog(null, "Coche modificado");

			this.cargarPanelListadoCoches();

		} // end if boton modificar

		SwingUtilities.updateComponentTreeUI(ventanaPrincipal);

	}// end ActionPerformed

	private Object getRadioGasolina() {
		// TODO Auto-generated method stub
		return null;
	}

	private Object getRadioDiesel() {
		// TODO Auto-generated method stub
		return null;
	}

}// end class GestorVentanas
