/**
 * ServicioSOAPServiceLocator.java
 *
 * This file was auto-generated from WSDL
 * by the Apache Axis 1.4 Apr 22, 2006 (06:55:48 PDT) WSDL2Java emitter.
 */

package webservice;

public class ServicioSOAPServiceLocator extends org.apache.axis.client.Service implements webservice.ServicioSOAPService {

    public ServicioSOAPServiceLocator() {
    }


    public ServicioSOAPServiceLocator(org.apache.axis.EngineConfiguration config) {
        super(config);
    }

    public ServicioSOAPServiceLocator(java.lang.String wsdlLoc, javax.xml.namespace.QName sName) throws javax.xml.rpc.ServiceException {
        super(wsdlLoc, sName);
    }

    // Use to get a proxy class for ServicioSOAPPort
    private java.lang.String ServicioSOAPPort_address = "http://localhost:52500/servicio";

    public java.lang.String getServicioSOAPPortAddress() {
        return ServicioSOAPPort_address;
    }

    // The WSDD service name defaults to the port name.
    private java.lang.String ServicioSOAPPortWSDDServiceName = "ServicioSOAPPort";

    public java.lang.String getServicioSOAPPortWSDDServiceName() {
        return ServicioSOAPPortWSDDServiceName;
    }

    public void setServicioSOAPPortWSDDServiceName(java.lang.String name) {
        ServicioSOAPPortWSDDServiceName = name;
    }

    public webservice.ServicioSOAP getServicioSOAPPort() throws javax.xml.rpc.ServiceException {
       java.net.URL endpoint;
        try {
            endpoint = new java.net.URL(ServicioSOAPPort_address);
        }
        catch (java.net.MalformedURLException e) {
            throw new javax.xml.rpc.ServiceException(e);
        }
        return getServicioSOAPPort(endpoint);
    }

    public webservice.ServicioSOAP getServicioSOAPPort(java.net.URL portAddress) throws javax.xml.rpc.ServiceException {
        try {
            webservice.ServicioSOAPPortBindingStub _stub = new webservice.ServicioSOAPPortBindingStub(portAddress, this);
            _stub.setPortName(getServicioSOAPPortWSDDServiceName());
            return _stub;
        }
        catch (org.apache.axis.AxisFault e) {
            return null;
        }
    }

    public void setServicioSOAPPortEndpointAddress(java.lang.String address) {
        ServicioSOAPPort_address = address;
    }

    /**
     * For the given interface, get the stub implementation.
     * If this service has no port for the given interface,
     * then ServiceException is thrown.
     */
    public java.rmi.Remote getPort(Class serviceEndpointInterface) throws javax.xml.rpc.ServiceException {
        try {
            if (webservice.ServicioSOAP.class.isAssignableFrom(serviceEndpointInterface)) {
                webservice.ServicioSOAPPortBindingStub _stub = new webservice.ServicioSOAPPortBindingStub(new java.net.URL(ServicioSOAPPort_address), this);
                _stub.setPortName(getServicioSOAPPortWSDDServiceName());
                return _stub;
            }
        }
        catch (java.lang.Throwable t) {
            throw new javax.xml.rpc.ServiceException(t);
        }
        throw new javax.xml.rpc.ServiceException("There is no stub implementation for the interface:  " + (serviceEndpointInterface == null ? "null" : serviceEndpointInterface.getName()));
    }

    /**
     * For the given interface, get the stub implementation.
     * If this service has no port for the given interface,
     * then ServiceException is thrown.
     */
    public java.rmi.Remote getPort(javax.xml.namespace.QName portName, Class serviceEndpointInterface) throws javax.xml.rpc.ServiceException {
        if (portName == null) {
            return getPort(serviceEndpointInterface);
        }
        java.lang.String inputPortName = portName.getLocalPart();
        if ("ServicioSOAPPort".equals(inputPortName)) {
            return getServicioSOAPPort();
        }
        else  {
            java.rmi.Remote _stub = getPort(serviceEndpointInterface);
            ((org.apache.axis.client.Stub) _stub).setPortName(portName);
            return _stub;
        }
    }

    public javax.xml.namespace.QName getServiceName() {
        return new javax.xml.namespace.QName("http://webservice/", "ServicioSOAPService");
    }

    private java.util.HashSet ports = null;

    public java.util.Iterator getPorts() {
        if (ports == null) {
            ports = new java.util.HashSet();
            ports.add(new javax.xml.namespace.QName("http://webservice/", "ServicioSOAPPort"));
        }
        return ports.iterator();
    }

    /**
    * Set the endpoint address for the specified port name.
    */
    public void setEndpointAddress(java.lang.String portName, java.lang.String address) throws javax.xml.rpc.ServiceException {
        
if ("ServicioSOAPPort".equals(portName)) {
            setServicioSOAPPortEndpointAddress(address);
        }
        else 
{ // Unknown Port Name
            throw new javax.xml.rpc.ServiceException(" Cannot set Endpoint Address for Unknown Port" + portName);
        }
    }

    /**
    * Set the endpoint address for the specified port name.
    */
    public void setEndpointAddress(javax.xml.namespace.QName portName, java.lang.String address) throws javax.xml.rpc.ServiceException {
        setEndpointAddress(portName.getLocalPart(), address);
    }

}
