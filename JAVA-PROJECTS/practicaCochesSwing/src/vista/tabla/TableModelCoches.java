package vista.tabla;

import java.util.ArrayList;

import javax.swing.table.AbstractTableModel;

import modelo.Coche;

public class TableModelCoches extends AbstractTableModel{

	String[] cabecerasColumnas = {"MARCA", "MODELO", "COLOR", "MOTOR", "CILINDRADA", "PRECIO"};
	
	String[][] data = null;
	
	public TableModelCoches(ArrayList<Coche> coches) {
		
		data = new String[coches.size()][6];
		
		for (int i = 0 ; i < coches.size() ; i++) {
			
			data[i] = new String[6];
			data[i][0] = coches.get(i).getMarca();
			data[i][1] = coches.get(i).getModelo();
			data[i][2] = coches.get(i).getColor();
			data[i][3] = coches.get(i).getMotor();
			data[i][4] = coches.get(i).getCilindrada();
			data[i][5] = coches.get(i).getPrecio();
		}
		
	}
	
	@Override
	public String getColumnName(int columna) {
		
		return cabecerasColumnas[columna];
		
		
	}
	
	@Override
	public int getColumnCount() {
		
		return cabecerasColumnas.length;
	}

	@Override
	public int getRowCount() {
		
		return data.length;
	}

	@Override
	public Object getValueAt(int rowIndex, int columnIndex) {
		
		return data[rowIndex][columnIndex];
	}

}
