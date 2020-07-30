package controladores;

import java.util.Map;

import modelo.Anuncio;
import modelo.ServicioAnuncios;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class ControladorRegistroAnuncio {

	@Autowired
	private ServicioAnuncios servicioAnuncios;
	
	@Autowired
	private ControladorInicio controladorInicio;
	
	@RequestMapping("registroAnuncio")
	public String registroAnuncio(Map<String, Object> model){
		model.put("objetoForm", new Anuncio());
		return "WEB-INF/vista/registroAnuncio.jsp";		
	}
	
	@RequestMapping("guardarAnuncio")
	public String guardarAnuncio(Anuncio objetoForm, 
			Map<String, Object> model){
		servicioAnuncios.registrarAnuncio(objetoForm);
		return controladorInicio.inicio(model);
	}
	
}
