import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int valorAnterior = 0;
        int resultado = 0;
        int valor = -1;

        while (valor != 0) {

            valor = scanner.nextInt();
            if ( valor == 0 ){
                System.exit(valor);;
            }
            
            for (int j = 1; j <= valor; j++) {
                resultado = (j * j) + valorAnterior;
                valorAnterior = resultado; 
            }

            valorAnterior = 0;
            System.out.println(resultado);
             
        }

        scanner.close();
    }
}
