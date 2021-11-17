import java.util.Scanner;

public class calculadoraV2{

    static int eleccion(){

        while (true){

            Scanner input = new Scanner(System.in);
            System.out.print ("\nBienvenido a la calculadora.\n1. Suma.\n2. Resta.\n3. Multiplicación.\n4. División.\n5. Residuo/módulo.\n6. Fórmula cuadrática.\n7. Números primos\n8. Salir.\nOpcion:");

            try{
                int eleccion = input.nextInt();

                if(eleccion < 0 || eleccion > 8){
                    System.out.println("Seleccionó un valor fuera de los parámetros.");
                    System.out.print("\033[H\033[2J");
                }
                else{
                    return eleccion;
                }
            }
            catch(Exception e){
                System.out.println("Seleccione un número del 1 al 8");
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

    static float[] pedirNumeros2(){

        while (true){

            try {
                Scanner input = new Scanner(System.in);
                float numero1, numero2, numero3;

                System.out.print("Ingrese el primer número: ");
                numero1 = input.nextFloat();
        
                System.out.print("Ingrese el segundo número: ");
                numero2 = input.nextFloat();

                System.out.print("Ingrese el tercer número: ");
                numero3 = input.nextFloat();

                return new float[]{numero1, numero2, numero3};
            } 
            catch (Exception e) {
                System.out.println("Ingresó un valor no permitido.");
            }
        }
    }

    static int pedirNumero3(){
        
        while(true){

            try {
                Scanner input = new Scanner(System.in);

                System.out.print("Ingrese el número: ");
                int numero = input.nextInt();

                return numero;
            } 

            catch (Exception e) {
                System.out.println("Ocurrió un error.");
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

    static String formulaCuadratucaOperacion(float a,float b, float c){
        double x1, x2, temp;
        temp = b * b -4 * a * c;

        if(temp > 0){

            if(2 * a != 0){

                x1 = -b - Math.sqrt(temp) / 2 * a;
                x2 = -b + Math.sqrt(temp) / 2 * a;
                System.out.print("\033[H\033[2J");
                return "Las soluciones son:\nSolución 1: " + x1 + "\nSolución 2: " + x2;
            }
            else{
                return "División por cero.";
            }
        }   
        else{
            return "Raíz negativa.";
        }
    }

    static String numerosPrimosCalculo(int numero){
        int i = 1, contador = 0, prueba;
        
        while(i <= numero){
            
            prueba = numero % i;

            if(prueba==0){
                contador++;
            }
            i++;
        }
        System.out.print("\033[H\033[2J");
        return contador > 2 ? "El número no es primo.":"El número es primo.";
    }
    
    public static void main(String[] args){
        int i = 0;

        while (i != 1){

            int eleccion = eleccion();

            if (eleccion == 8){
                System.out.print("\033[H\033[2J");
                System.out.print("Hasta luego.");
                i = 1;
            }

            else{

                if(eleccion == 6){
                    float numeros[] = pedirNumeros2();
                    String resultado = formulaCuadratucaOperacion(numeros[0], numeros[1], numeros[2]);
                    System.out.print("\033[H\033[2J");
                    System.out.print(resultado);
                }

                else if(eleccion == 7){
                    int numero = pedirNumero3();
                    String resultado = numerosPrimosCalculo(numero);
                    System.out.print("\033[H\033[2J");
                    System.out.print(resultado);
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
}