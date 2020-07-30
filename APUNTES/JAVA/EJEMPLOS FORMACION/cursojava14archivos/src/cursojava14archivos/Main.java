package cursojava14archivos;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;

public class Main {

	public static void main(String[] args) {
		
		//File sirve para rutas de archivos o carpeta pero no 
		//vale para trabajar su contenido
		File archivo = new File("archivo.txt");
		
		//para escribir texto:
		try {
			//asi agrega texto
			//FileWriter fw = new FileWriter(archivo,true);
			//y asi pisa el contenido del archivo:
			FileWriter fw = new FileWriter(archivo);
			BufferedWriter bw = new BufferedWriter(fw);
			PrintWriter pw = new PrintWriter(bw);
			
			pw.println("En un luegar de la Mancha");
			pw.println("De cuyo nomrbe no quiero acordarme");
			
			pw.close();
			bw.close();
			fw.close();
			System.out.println("archivo creado correctamente");
		} catch (IOException e) {
			System.out.println("no pude crear un file writer del archivo");
		}
		
		
		//para leer un archivo de texto:
		
		try {
			FileReader fr = new FileReader(archivo);
			BufferedReader br = new BufferedReader(fr);
			String linea = "";
			while ( (linea=br.readLine()) != null ) {
				System.out.println(linea);
			}
			br.close();
			fr.close();			
		} catch (FileNotFoundException e) {
			System.out.println("no puedo leer del archivo");
		} catch (IOException e) {
			System.out.println("error al leer");
		}
		
		
	}//end main

}
