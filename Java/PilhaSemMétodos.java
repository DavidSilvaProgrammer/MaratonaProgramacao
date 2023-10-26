import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o tamanho da pilha: ");
        int tamanhoPilha = scanner.nextInt();

        int[] pilha = new int[tamanhoPilha];
        int top = -1;

        System.out.println("Operações na Pilha:");
        System.out.println("Digite um número para adicionar na pilha, ou -1 para sair.");

        int numero;
        while (true) {
            System.out.print("Operação: ");
            numero = scanner.nextInt();

            if (numero == -1) {
                break; // Encerra o loop quando o usuário digita -1
            } else {
                if (top < tamanhoPilha - 1) {
                    pilha[++top] = numero;
                    System.out.println("Elemento " + numero + " adicionado à pilha.");
                } else {
                    System.out.println("A pilha está cheia. Não é possível adicionar mais elementos.");
                }
            }
        }

        System.out.println("\nDesempilhando elementos:");
        while (top >= 0) {
            int elemento = pilha[top--];
            System.out.println("Elemento " + elemento + " removido da pilha.");
        }

        System.out.println("Pilha esvaziada.");

        scanner.close();
    }
}
