import java.util.Scanner;

public class LeerNumero {

    public static void main(String[] args){
        // Se define in como scanner.
        Scanner in = new Scanner(System.in);

        System.out.print("Ingrese un número entero: ");
        int numero = in.nextInt();

        if(numero > 0){
            System.out.print("Feliz día.");
        }
        else if(numero == 0){
            System.out.print("Vamos muy bien.");
        }
        else{
            System.out.print("Para atrás ni para coger impulso.");
        }
        
        in.close();
    }
}