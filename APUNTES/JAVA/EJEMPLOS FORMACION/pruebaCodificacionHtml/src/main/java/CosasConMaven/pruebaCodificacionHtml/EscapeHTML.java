package CosasConMaven.pruebaCodificacionHtml;

import org.apache.commons.text.StringEscapeUtils;


public class EscapeHTML extends StringEscapeUtils {
		
		public String parsearEntidad(String text) {
	         
	        String textConverted = StringEscapeUtils.escapeHtml4(text); 
			
		return textConverted;
		}
		
}

