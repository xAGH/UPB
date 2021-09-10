import java.util.Scanner;

public class calculadora{

    static int eleccion(){

        while (true){
            Scanner input = new Scanner(System.in);
            System.out.print ("Bienvenido a la calculadora.\n1. Suma.\n2. Resta.\n3. Multiplicación.\n4. División.\n5. Residuo/módulo.\n6. Salir.\nOpcion:");

            try{
                int eleccion = input.nextInt();

                if(eleccion < 0 || eleccion > 6){
                    System.out.println("Seleccionó un valor fuera de los parámetros.");
                    System.out.print("\033[H\033[2J");
                }
                else{
                    return eleccion;
                }
            }
            catch(Exception e){
                System.out.println("Seleccione un número del 1 al 6");
            }
        }
    }

    static float[] pedirNumeros(){

        while (true){

            try {
                Scanner input = new Scanner(System.in);
                float numero1, numero2;

                System.out.print("Ingrese el primer número: ");
                numero1 = input.nextFloat();
        
                System.out.print("Ingrese el segundo número: ");
                numero2 = input.nextFloat();

                return new float[]{numero1, numero2};
            } 
            catch (Exception e) {
                System.out.println("Ingresó un valor no permitido.");
            }
        }
    }

    static float sumaOperacion(float numero1, float numero2){
        float suma = numero1 + numero2;
        return suma;
    }

    static float restaOperacion(float numero1, float numero2){
        float resta = numero1 - numero2;
        return resta;
    }

    static float multiplicacionOperacion(float numero1, float numero2){
        float multiplicacion = numero1 * numero2;
        return multiplicacion;
    }

    static float divisionOperacion(float numero1, float numero2){
        float division = numero1 / numero2;
        return division;
    }

    static float restoOperacion(float numero1, float numero2){
        float resto = numero1 % numero2;
        return resto;
    }

    public static void main(String[] args){
        int i = 0;

        while (i != 1){

            int eleccion = eleccion();

            if (eleccion == 6){
                System.out.print("Hasta luego.");
                i = 1;
            }

            else{
                float resultado = 0;
                float numeros[] = pedirNumeros();
                switch(eleccion){
                    
                    case 1:
                        resultado = sumaOperacion(numeros[0], numeros[1]);
                    break;
        
                    case 2:
                        resultado = restaOperacion(numeros[0], numeros[1]);
                    break;
        
                    case 3:
                        resultado = multiplicacionOperacion(numeros[0], numeros[1]);
                    break;
        
                    case 4:
                        resultado = divisionOperacion(numeros[0], numeros[1]);
                    break;
        
                    case 5:
                        resultado = restoOperacion(numeros[0], numeros[1]);
                    break;
                }
                System.out.print("\033[H\033[2J");
                System.out.println("El resultado es: " + resultado);
            }
        }
    }
}