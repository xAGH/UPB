import java.util.ArrayList;

public class Banco{

    // ATRIBUTOS
    private ArrayList<Empleado> empleados = new ArrayList<>();

    // MÉTODOS 
    public static double liquidarPrestacionesEmp(Empleado empleado){
        double salario = empleado.getSalario();

        double prima = (8.33 * salario) / 100;
        double cesantias = (8.33 * salario) / 100;
        double interesesCesantias = (12 * cesantias) / 100;
        double vacaciones = (4.16 * salario) / 100;

        double liquidacionPrestaciones = prima + cesantias + interesesCesantias + vacaciones;
        
        return liquidacionPrestaciones;
    }

    public static double liquidarSegSocialEmp(Empleado empleado){
        double salario = empleado.getSalario();

        double salud = (8.5 * salario) / 100;
        double pension = (12 * salario / 100);
        double arl = (0.52 * salario) / 100;

        double liquidacionSegSocial = salud + pension + arl;

        return liquidacionSegSocial;
    }

    public static double liquidarNominaEmp(Empleado empleado){
        double salario = empleado.getSalario();
        double comision = empleado.getComision();
        double horasExtra = empleado.getHorasExtra();
        double totalDevengado = salario + comision + horasExtra;
        double saludPension = ((4 * salario) / 100) * 2;

        double nomina = (totalDevengado - saludPension);
        
        return nomina;
    }

    public static double liquidarParafiscalesEmp(Empleado empleado){
        double salario = empleado.getSalario();
        double comision = empleado.getComision();
        double horasExtra = empleado.getHorasExtra();
        double totalDevengado = salario + comision + horasExtra;
        double compFamiliar = (4 * totalDevengado) / 100;
        double sena = (3 * totalDevengado) / 100;
        double icbf = (2 * totalDevengado) / 100;

        double liquidacionParafiscales = (compFamiliar + sena + icbf);

        return liquidacionParafiscales;
    }

    // SETTERS
    public void setEmpleado(Empleado empleado){
        empleados.add(empleado);
    }

    // GETTERS
    public ArrayList<Empleado> getEmpleados(){
        return empleados;
    }
}