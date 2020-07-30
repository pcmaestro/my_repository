package vista;

import javax.swing.JPanel;
import javax.swing.JLabel;
import java.awt.Font;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JRadioButton;
import javax.swing.JComboBox;

public class PanelRegistro extends JPanel implements ItemListener {
	private JTextField inputPrecio;
	private JTextField inputColor;
	private JTextField inputMarca;
	private JTextField inputModelo;
	private JRadioButton RadioDiesel;
	private JRadioButton RadioGasolina;
	private JComboBox comboCilindrada;
	private JButton botonRegistrar;

	/**
	 * Create the panel.
	 */
	public PanelRegistro() {
		setLayout(null);
		
		JLabel lblNewLabel = new JLabel("FORMULARIO DE REGISTRO DE COCHES");
		lblNewLabel.setFont(new Font("Tahoma", Font.PLAIN, 15));
		lblNewLabel.setBounds(222, 11, 306, 14);
		add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("MARCA");
		lblNewLabel_1.setFont(new Font("Tahoma", Font.PLAIN, 12));
		lblNewLabel_1.setBounds(41, 52, 121, 14);
		add(lblNewLabel_1);
		
		JLabel lblNewLabel_1_1 = new JLabel("MODELO");
		lblNewLabel_1_1.setFont(new Font("Tahoma", Font.PLAIN, 12));
		lblNewLabel_1_1.setBounds(41, 92, 121, 14);
		add(lblNewLabel_1_1);
		
		JLabel lblNewLabel_1_2 = new JLabel("COLOR");
		lblNewLabel_1_2.setFont(new Font("Tahoma", Font.PLAIN, 12));
		lblNewLabel_1_2.setBounds(41, 135, 121, 14);
		add(lblNewLabel_1_2);
		
		JLabel lblNewLabel_1_3 = new JLabel("MOTOR");
		lblNewLabel_1_3.setFont(new Font("Tahoma", Font.PLAIN, 12));
		lblNewLabel_1_3.setBounds(41, 171, 121, 14);
		add(lblNewLabel_1_3);
		
		JLabel lblNewLabel_1_4 = new JLabel("CILINDRADA");
		lblNewLabel_1_4.setToolTipText("Seleccione una cilindrada");
		lblNewLabel_1_4.setFont(new Font("Tahoma", Font.PLAIN, 12));
		lblNewLabel_1_4.setBounds(41, 208, 121, 14);
		add(lblNewLabel_1_4);
		
		JLabel lblNewLabel_1_5 = new JLabel("PRECIO");
		lblNewLabel_1_5.setFont(new Font("Tahoma", Font.PLAIN, 12));
		lblNewLabel_1_5.setBounds(41, 245, 121, 14);
		add(lblNewLabel_1_5);
		
		inputPrecio = new JTextField();
		inputPrecio.setBounds(196, 243, 374, 20);
		add(inputPrecio);
		inputPrecio.setColumns(10);
		
		botonRegistrar = new JButton("REGISTRAR");
		botonRegistrar.setBounds(278, 337, 145, 41);
		add(botonRegistrar);
		
		inputColor = new JTextField();
		inputColor.setColumns(10);
		inputColor.setBounds(196, 133, 374, 20);
		add(inputColor);
		
		inputMarca = new JTextField();
		inputMarca.setColumns(10);
		inputMarca.setBounds(196, 50, 374, 20);
		add(inputMarca);
		
		inputModelo = new JTextField();
		inputModelo.setColumns(10);
		inputModelo.setBounds(196, 90, 374, 20);
		add(inputModelo);
		
		RadioDiesel = new JRadioButton("Diesel");
		RadioDiesel.setBounds(278, 168, 109, 23);
		add(RadioDiesel);
		
		RadioGasolina = new JRadioButton("Gasolina");
		RadioGasolina.setBounds(389, 168, 109, 23);
		add(RadioGasolina);		
		
		comboCilindrada = new JComboBox();
		comboCilindrada.setBounds(196, 206, 374, 20);
		add(comboCilindrada);

	}
	public JTextField getInputMarca() {
		return inputMarca;
	}
	public JTextField getInputModelo() {
		return inputModelo;
	}
	public JTextField getInputColor() {
		return inputColor;
	}
	public JRadioButton getRadioDiesel() {
		return RadioDiesel;
	}
	public JRadioButton getRadioGasolina() {
		return RadioGasolina;
	}
	public JComboBox getComboCilindrada() {
		return comboCilindrada;
	}
	public JTextField getInputPrecio() {
		return inputPrecio;
	}
	public JButton getBotonRegistrar() {
		return botonRegistrar;
	}
	@Override
	public void itemStateChanged(ItemEvent e) {
		PanelRegistro panelRegistro = new PanelRegistro();
		if(e.getSource() == panelRegistro.getComboCilindrada()) {
			String seleccionado = (String) panelRegistro.getComboCilindrada().getSelectedItem();
		}
		
	}
}
