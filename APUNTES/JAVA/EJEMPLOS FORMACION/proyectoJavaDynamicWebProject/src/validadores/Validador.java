package validadores;

import java.util.regex.Matcher; 
import java.util.regex.Pattern;

public class Validador {
	
	private boolean validacion;
	
	public boolean validarTexto(String text) {
		
		Pattern patrontxt = Pattern.compile("[a-zA-ZÒ—0-9]");
	      
	    Matcher matcher = patrontxt.matcher(text);
	      
	    boolean matchfound = matcher.find();
	    
	    if(matchfound) {
	    	validacion = true;
	    }else {
	    	validacion = false;
	    }
		
		return validacion;
		
	}//end validarTexto
	
	public boolean validarTf(String text) {
		Pattern patrontf = Pattern.compile("[0-9]{9}");
		
		Matcher matcher = patrontf.matcher(text);
		
		boolean matchfound = matcher.find();
		
		if(matchfound) {
			validacion = true;
		}else {
			validacion = false;
		}
		
		return validacion;
	}//end validarTf
	
	public boolean validarEmail(String text) {
		Pattern patronEmail = Pattern.compile("[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,6}", Pattern.CASE_INSENSITIVE);
		
		Matcher matcher = patronEmail.matcher(text);
		
		boolean matchfound = matcher.find();
		
		if(matchfound) {
			validacion = true;
		}else {
			validacion = false;
		}
		
		return validacion;
	}//end validarEmail
	
	public boolean validarCilindrada(String text) {
		Pattern patronCil = Pattern.compile("[0-9]{4}");
		
		Matcher matcher = patronCil.matcher(text);
		
		boolean matchfound = matcher.find();
		
		if(matchfound) {
			validacion = true;
		}else {
			validacion = false;
		}
		
		return validacion;
	}//end validarCilindrada
	
	public boolean validarPrecio(String text) {
		Pattern patronPrecio = Pattern.compile("[0-9]");
		
		Matcher matcher = patronPrecio.matcher(text);
		
		boolean matchfound = matcher.find();
		
		if(matchfound) {
			validacion = true;
		}else {
			validacion = false;
		}
		
		return validacion;
	}//end validarCilindrada
	
}//end class
