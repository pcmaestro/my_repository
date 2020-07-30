package com;

import java.awt.List;
import java.net.URI;
import java.net.URISyntaxException;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import javax.ws.rs.PathParam;
import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.FormParam;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.Response.Status;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;

import daos.CocheDAO;
import daos.MasterDAO;
import daosimpl.CocheDAOimpl;
import model.Coche;

@Path("recursos")
public class Recursos {
	
	
	@GET
	@Produces(MediaType.TEXT_PLAIN)
	public String metodo() {
		String var = "Recursos de API-RESTful";
		
		return var;
	}
	
	@Path("listado-json")
	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public ArrayList<Coche> listarCochesJson() {		
		
		CocheDAO coche = new CocheDAOimpl();
		
		ArrayList<Coche> coches = coche.obtenerCoches();
		
		return coches;
		
	}
	@GET
	@Path("listado-xml")
	@Produces(MediaType.APPLICATION_XML)
	public String listarCochesXml() throws JsonProcessingException {		
		CocheDAO coche = new CocheDAOimpl();		
		ArrayList<Coche> coches = coche.obtenerCoches();		
		XmlMapper xmlMapper = new XmlMapper();
		String xml = xmlMapper.writeValueAsString(coches);
		
		return xml;
	}
	
	@GET
	@Path("obtener-coche")
	@Produces(MediaType.APPLICATION_JSON)
	public Response obtenerCocheJson(@QueryParam("id") String id) {

		Coche coche = new Coche();
		
		Map<Integer, String> error = new HashMap<Integer, String>();
		error.put(404, "not found");
		
		int nid;
		
		if (id.contentEquals("")) {
			nid = 0;
			
		}else {
						
			nid = Integer.parseInt(id);
		}//end if
		
		
		CocheDAO c = new CocheDAOimpl();
		
		coche = c.obtenerCochePorId(nid);
			
		if(coche.getId() != 0) {
			
			return Response.ok(coche).build();	
	
		}else {
			
			return Response.serverError().type(MediaType.APPLICATION_JSON).entity(error).build();
		}		

	}//end obtenerCocheJson
	
	@GET
	@Path("obtener-coche/{id}")
	@Produces(MediaType.APPLICATION_JSON)
	public Response obtenerCocheJson2(@PathParam("id") int id) {
		
		System.out.println("El id elegido es " + id);
		
		Coche coche = new Coche();
		
		CocheDAO c = new CocheDAOimpl();
		
		coche = c.obtenerCochePorId(id);
		
		System.out.println(coche.toString());
			
		if(coche.getId() != 0) {
			
			return Response.ok(coche).build();	
	
		}else {
			
			return Response.status(Status.NOT_FOUND).build();
		}		

	}//end obtenerCocheJson
	
	@DELETE
	@Path("borrar-coche/{id}")
	@Produces(MediaType.APPLICATION_JSON)
	public Response borrarCoche(@PathParam("id") int id) {
		
		CocheDAO c = new CocheDAOimpl();
		
		c.borrarCoche(id);
		
		return Response.noContent().build();
		
	}//end borrarCoche
	
	@POST
	@Path("registrar-coche")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	public Response registrarCoche(Coche coche) throws URISyntaxException {
		
		CocheDAO c = new CocheDAOimpl();
		
		int idGenerado = c.registrarCoche(coche);
		
		URI uri = new URI("http://localhost:8080/aplicacionREST/servicios/hola/json/" + idGenerado);
		
		return Response.created(uri).build();
	}
	
	@PUT
	@Path("modificar-coche/{id}")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	public Response modificarCoche(@PathParam("id") int id, Coche coche) {

		CocheDAO c = new CocheDAOimpl();
		
		//Comprobamos si el id existe
		int idModificar = c.obtenerCochePorId(id).getId();
		
		//Ejecutamos la modificación
		int cocheModificado = c.modificarCoche(id, coche);			

		System.out.println("El valor de marca en Recursos es " + coche.getMarca());
		System.out.println("El valor de color en Recursos es " + coche.getColor());
		
		if(idModificar > 0) {
			if(cocheModificado == 1) {
				return Response.ok().build();
			}else {
				return Response.notModified().build();
			}		
		}else {
			return Response.status(404).build();
		}
		
	}//end modificarCoche
	
	
}//end class
	