import java.util.ArrayList;
import java.util.Scanner;

public class ListaInteiros {
    public static void main(String[] args) {
        // Criando uma lista de inteiros
        ArrayList<Integer> lista = new ArrayList<>();

        // Criando um Scanner para ler a entrada do usuário
        Scanner scanner = new Scanner(System.in);

        // Perguntando ao usuário quantos números ele quer inserir
        System.out.println("Quantos números você deseja adicionar à lista?");
        int n = scanner.nextInt();

        // Lendo os números do usuário e adicionando na lista
        System.out.println("Digite os números:");
        for (int i = 0; i < n; i++) {
            int numero = scanner.nextInt();
            lista.add(numero); // Método que adiciona o elemento na lista
        }

        // Exibindo os elementos da lista
        System.out.println("Os números inseridos na lista são:");
        for (int numero : lista) {
            System.out.println(numero);
        }

        // Fechando o scanner
        scanner.close();
    }
}
