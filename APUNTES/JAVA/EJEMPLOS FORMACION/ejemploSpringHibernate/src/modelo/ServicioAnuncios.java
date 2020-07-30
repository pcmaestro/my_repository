package modelo;

import java.util.List;

public interface ServicioAnuncios {

	void registrarAnuncio(Anuncio anuncio);
	List<Anuncio> obtenerAnuncios();
	
}
