import java.util.Scanner;

public class VetorInteiros {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Definindo o tamanho do vetor
        System.out.print("Digite o tamanho do vetor: ");
        int tamanho = scanner.nextInt();

        // Criando o vetor com o tamanho especificado
        int[] vetor = new int[tamanho];

        // Preenchendo o vetor com valores inseridos pelo usuário
        System.out.println("Digite " + tamanho + " números inteiros:");
        for (int i = 0; i < tamanho; i++) {
            vetor[i] = scanner.nextInt(); // Atribui valor ao vetor na posição i
        }

        // Exibindo os valores armazenados no vetor
        System.out.println("Os valores armazenados no vetor são:");
        for (int i = 0; i < tamanho; i++) {
            System.out.println("Posição " + i + ": " + vetor[i]);
        }

        scanner.close();
    }
}
