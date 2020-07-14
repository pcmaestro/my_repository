
package com.mycompany.mavenproject1;
 
import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JList;
import javax.swing.JRadioButton;
import javax.swing.JTextArea;
import javax.swing.ListSelectionModel;



public class NewClass {
  public static void main(String[] args) {
      
      String[] array = {"rojo", "verde", "azul"};
      JComboBox cbx = new JComboBox(array);
      
      cbx.setSelectedIndex(1);
      
      int indice = cbx.getSelectedIndex();
      
      String seleccionado = array[1];
      
      System.out.println(seleccionado);
      
      
      
      
      
      
  }
}
