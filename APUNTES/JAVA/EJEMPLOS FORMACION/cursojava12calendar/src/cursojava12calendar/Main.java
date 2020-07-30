package cursojava12calendar;

import java.util.Calendar;

public class Main {

	public static void main(String[] args) {
		//hay clases de las que no puedo crear directamente objetos
		//usando el operador new
		//sin embargo para obtener un objeto de dicha clase suele haber 
		//otro procedimiento, en este caso en vez de usar new, al llamar
		//a Calendar.getInstance() obtendre un objeto de Calendar
		//con la fecha y hora actual
		Calendar calendar = Calendar.getInstance();
		System.out.println(calendar);
		System.out.println("hoy es:");
		System.out.println("dia: " + calendar.get(Calendar.DAY_OF_MONTH));
		System.out.println("dia de la semana: " + 
		    calendar.get(Calendar.DAY_OF_WEEK));
		final String[] dias = 
			{"domingo","lunes","martes",
					"miercoles","jueves","viernes","sabado"};
		String diaSemana = dias[calendar.get(Calendar.DAY_OF_WEEK)-1];
		System.out.println("dia de la semana: " + diaSemana);
		
		calendar.add(Calendar.DAY_OF_MONTH, 2);
		System.out.println("dentro de dos días, es día: " 
				+ calendar.get(Calendar.DAY_OF_MONTH));
		
	}

}







