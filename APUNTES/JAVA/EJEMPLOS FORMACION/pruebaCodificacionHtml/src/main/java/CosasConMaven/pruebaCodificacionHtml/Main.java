package CosasConMaven.pruebaCodificacionHtml;


public class Main {

	public static void main(String[] args) {
		
		EscapeHTML conversor = new EscapeHTML();
		
		String text = "En mi opinión España va bién";	
		
		String textConvertido = conversor.parsearEntidad(text);
		
		System.out.println(textConvertido);

	}

}
