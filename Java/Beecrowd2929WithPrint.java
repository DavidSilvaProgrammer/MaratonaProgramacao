import java.util.Scanner;

public class Main {
    private static int topo = -1;
    private static int[] pilha;
    private static int menorValor = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o número de operações: ");
        int tamanhoPilha = scanner.nextInt();
        pilha = new int[tamanhoPilha]; // Definindo o tamanho da pilha aqui

        System.out.println("Operações na Pilha:");
        System.out.println("Digite 'PUSH V' para adicionar na pilha, 'POP' para remover, ou 'MIN' para consultar o menor valor.");

        for (int i = 0; i < tamanhoPilha; i++) {
            System.out.print("Operação: ");
            String operacao = scanner.next();

            if (operacao.equals("PUSH")) {
                
                int valor = scanner.nextInt();
                push(valor);
                System.out.println("Elemento " + valor + " adicionado à pilha.");
            } else if (operacao.equals("POP")) {
                if (!vazia()) {
                    int elemento = pop();
                    System.out.println("Elemento " + elemento + " removido da pilha.");
                } else {
                    System.out.println("Pilha esvaziada.");
                }
            } else if (operacao.equals("MIN")) {
                if (!vazia()) {
                    int minimo = encontrarMenorValor();
                    System.out.println("Menor valor na pilha: " + minimo);
                } else {
                    System.out.println("Pilha vazia.");
                }
            }
        }

        scanner.close();
    }

    public static boolean vazia() {
        return topo == -1;
    }

    public static boolean cheia() {
        return topo == pilha.length - 1;
    }

    public static void push(int numero) {
        pilha[++topo] = numero;
        if (numero < menorValor) {
            menorValor = numero;
        }
    }

    public static int pop() {
        if (!vazia()) {
            int elemento = pilha[topo--];
            if (elemento == menorValor) {
                menorValor = encontrarMenorValor();
            }
            return elemento;
        } else {
            return -1; // Pilha vazia
        }
    }

    public static int encontrarMenorValor() {
        if (vazia()) {
            return Integer.MAX_VALUE; // Pilha vazia, retorna um valor máximo
        } else {
            int menor = pilha[0];
            for (int i = 1; i <= topo; i++) {
                if (pilha[i] < menor) {
                    menor = pilha[i];
                }
            }
            return menor;
        }
    }
}

