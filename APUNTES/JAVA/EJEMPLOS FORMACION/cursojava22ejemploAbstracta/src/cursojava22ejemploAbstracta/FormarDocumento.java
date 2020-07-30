package cursojava22ejemploAbstracta;

public abstract class FormarDocumento {

	//con final en un metodo el metodo no podra sobre escribirse
	public final void formarDocumento() {
		formarCabecera();
		formarCuerpo();
		formarFirma();
		System.out.println("validando firma...");
		formarPieDePagina();
		System.out.println("finalizando documento");
	}
	
	public abstract void formarCabecera();
	public abstract void formarCuerpo();
	public abstract void formarFirma();
	public abstract void formarPieDePagina();
	
}
