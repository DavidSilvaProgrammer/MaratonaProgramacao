import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o tamanho da pilha: ");
        int tamanhoPilha = scanner.nextInt();
        
        Stack<Integer> pilha = new Stack<>();
        
        System.out.println("Operações na Pilha:");
        System.out.println("Digite um número para adicionar na pilha, ou -1 para sair.");
        
        int numero;
        while (true) {
            System.out.print("Operação: ");
            numero = scanner.nextInt();
            
            if (numero == -1) {
                break; // Encerra o loop quando o usuário digita -1
            } else {
                pilha.push(numero);
                System.out.println("Elemento " + numero + " adicionado à pilha.");
            }
        }
        
        System.out.println("\nDesempilhando elementos:");
        while (!pilha.isEmpty()) {
            int elemento = pilha.pop();
            System.out.println("Elemento " + elemento + " removido da pilha.");
        }
        
        System.out.println("Pilha esvaziada.");
        
        scanner.close();
    }
}

