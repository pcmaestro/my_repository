package controladores;

import java.util.Map;

import modelo.ServicioAnuncios;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class ControladorInicio {

	
	@Autowired
	private ServicioAnuncios servicioAnuncios;
	
	@RequestMapping("inicio")
	public String inicio(Map<String, Object> model){
		System.out.println("se ejecutó el controlador de inicio");
		model.put("anuncios", servicioAnuncios.obtenerAnuncios());
		return "WEB-INF/vista/inicio.jsp";
	}	
	
}
