package Arreglos;

public class promedioEstudiantes {
    public static void main(String[] args) {
        String[][] estudiantes = new String[3][3];

        estudiantes[0][0] = "Estudiante 1";
        estudiantes[0][1] = "Apellido 1";
        estudiantes[0][2] = "4.5";

        estudiantes[1][0] = "Estudiante 2";
        estudiantes[1][1] = "Apellido 2";
        estudiantes[1][2] = "8";

        estudiantes[2][0] = "Estudiante 3";
        estudiantes[2][1] = "Apellido 3";
        estudiantes[2][2] = "3.5";

        Float[] acumulado = new Float[3];
        
        for(int i = 0;i < estudiantes.length; i++){
            acumulado[i] = Float.parseFloat(estudiantes[i][2]);
        }

        float suma = 0;

        for(int j = 0;j < acumulado.length;j++){
            suma += acumulado[j];
        } 

        Float promedio = suma / acumulado.length;

        System.out.println("El promedio es: " + promedio);
    }
}
