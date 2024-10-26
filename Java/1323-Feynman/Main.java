import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite a quantidade de números: ");
        int numero = scanner.nextInt();
        
        int valorAnterior = 0;
        int resultado = 0;

        for (int i = 1; i <= numero; i++) {

            int valor = scanner.nextInt();
        
            
            for (int j = 1; j <= valor; j++) {
                resultado = (j * j) + valorAnterior;
                valorAnterior = resultado; 
            }

            valorAnterior = 0;
            System.out.println("Resultado para " + i + ": " + resultado);
             
        }

        scanner.close();
    }
}
