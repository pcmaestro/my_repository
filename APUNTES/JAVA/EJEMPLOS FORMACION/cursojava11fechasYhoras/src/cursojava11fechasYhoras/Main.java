package cursojava11fechasYhoras;

import java.text.SimpleDateFormat;
import java.util.Date;

public class Main {

	public static void main(String[] args) {
		//el tipo mas basico y comun de dato en java para 
		//manejar fechas y horas es Date
		Date ahora = new Date();
		
		System.out.println("ahora: " + ahora);
		//para sacar la fecha y hora de forma mas legible:
		SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
		System.out.println("ahora, formato español: " + sdf.format(ahora));
				
		System.out.println(ahora.getTime());
		System.out.println("tiempo de ejecucion del programa");
		
		Date fin = new Date();
		System.out.println( "tiempo tardado(ms): " + 
				(fin.getTime()-ahora.getTime()) );
	}

}
