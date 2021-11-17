public class Banco{
    public static double liquidarPrestaciones(double salario, double comision, double auxilioT){

        double totalDevengado = salario + comision + auxilioT;
        double prima = (totalDevengado * 8.33) / 100;
        double cesantias = (totalDevengado * 8.33) / 100;
        double intereses = (cesantias * 12) / 100;
        double vacaciones = (salario * 4.16) / 100;
        double liquidacion = prima + cesantias + intereses + vacaciones;

        return liquidacion;
    }
}
