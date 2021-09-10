public class Empleado {
    
    // ATRIBUTOS
    private int id;
    private String nombre;
    private int salario;
    private double comision = 0;
    private double horasExtra = 0;
    private double auxTransporte = 0;

    // CONSTRUCTORES
    public Empleado(String nombre, int salario){
        setNombre(nombre);
        setSalario(salario);
    }

    public Empleado(int id, String nombre, int salario){
        setId(id);
        setNombre(nombre);
        setSalario(salario);
    }

    public Empleado(int id, String nombre, int salario, double comision, double horasExtra, double auxTransporte){
        setId(id);
        setNombre(nombre);
        setSalario(salario);
        setComision(comision);
        setHorasExtra(horasExtra);
        setAuxTransporte(auxTransporte);
    }

    // SETTERS
    public void setId(int id) {
        this.id = id;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setSalario(int salario) {
        this.salario = salario;
    }

    public void setComision(double comision){
        this.comision = comision;
    }

    public void setHorasExtra(double horasExtra){
        this.horasExtra = horasExtra;
    }

    public void setAuxTransporte(double auxTransporte){
        this.auxTransporte = auxTransporte;
    }

    //GETTERS
    public int getId(){
        return id;
    } 

    public int getSalario(){
        return salario;
    }

    public String getNombre(){
        return nombre;
    }

    public double getComision(){
        return comision;
    } 

    public double getHorasExtra(){
        return horasExtra;
    }

    public double getAuxTransporte(){
        return auxTransporte;
    }
}
