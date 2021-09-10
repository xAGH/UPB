import java.util.ArrayList;

public class Banco{

    private ArrayList<Empleado> empleados = new ArrayList<>();

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
}

