
package com.mycompany.mavenproject1;
 
import java.util.Hashtable;
import java.util.ArrayList;

public class NewClass {
    public static void main(String[] args){
        
        ArrayList<String> semana = new ArrayList();
        
        semana.add("lunes");
        semana.add(1, "martes");
        
        String[] lista = new String[semana.size()];
        semana.toArray(lista);
        
        System.out.println(lista[0]);
        
        
    }
}
