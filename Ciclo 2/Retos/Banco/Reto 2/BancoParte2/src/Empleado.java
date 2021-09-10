public class Empleado {
    
    // ATRIBUTOS
    private int id;
    private String nombre;
    private int salario;

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

}
