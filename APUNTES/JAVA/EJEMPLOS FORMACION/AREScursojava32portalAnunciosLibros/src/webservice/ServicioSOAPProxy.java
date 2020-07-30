package webservice;

public class ServicioSOAPProxy implements webservice.ServicioSOAP {
  private String _endpoint = null;
  private webservice.ServicioSOAP servicioSOAP = null;
  
  public ServicioSOAPProxy() {
    _initServicioSOAPProxy();
  }
  
  public ServicioSOAPProxy(String endpoint) {
    _endpoint = endpoint;
    _initServicioSOAPProxy();
  }
  
  private void _initServicioSOAPProxy() {
    try {
      servicioSOAP = (new webservice.ServicioSOAPServiceLocator()).getServicioSOAPPort();
      if (servicioSOAP != null) {
        if (_endpoint != null)
          ((javax.xml.rpc.Stub)servicioSOAP)._setProperty("javax.xml.rpc.service.endpoint.address", _endpoint);
        else
          _endpoint = (String)((javax.xml.rpc.Stub)servicioSOAP)._getProperty("javax.xml.rpc.service.endpoint.address");
      }
      
    }
    catch (javax.xml.rpc.ServiceException serviceException) {}
  }
  
  public String getEndpoint() {
    return _endpoint;
  }
  
  public void setEndpoint(String endpoint) {
    _endpoint = endpoint;
    if (servicioSOAP != null)
      ((javax.xml.rpc.Stub)servicioSOAP)._setProperty("javax.xml.rpc.service.endpoint.address", _endpoint);
    
  }
  
  public webservice.ServicioSOAP getServicioSOAP() {
    if (servicioSOAP == null)
      _initServicioSOAPProxy();
    return servicioSOAP;
  }
  
  public int myService() throws java.rmi.RemoteException{
    if (servicioSOAP == null)
      _initServicioSOAPProxy();
    return servicioSOAP.myService();
  }
  
  
}