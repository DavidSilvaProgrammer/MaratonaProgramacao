public class Pilha {
    private int tamanhoMaximo;
    private int topo;
    private int[] elementos;

    public Pilha(int tamanho) {
        tamanhoMaximo = tamanho;
        elementos = new int[tamanho];
        topo = -1; // Inicializa o topo da pilha
    }

    public boolean estaVazia() {
        return topo == -1;
    }

    public boolean estaCheia() {
        return topo == tamanhoMaximo - 1;
    }

    public void empilhar(int valor) {
        if (!estaCheia()) {
            elementos[++topo] = valor;
        } else {
            System.out.println("A pilha está cheia. Não é possível empilhar.");
        }
    }

    public int desempilhar() {
        if (!estaVazia()) {
            return elementos[topo--];
        } else {
            System.out.println("A pilha está vazia. Não é possível desempilhar.");
            return -1; // Valor de erro
        }
    }

    public int topo() {
        if (!estaVazia()) {
            return elementos[topo];
        } else {
            System.out.println("A pilha está vazia.");
            return -1; // Valor de erro
        }
    }
}


*********************************


public class Main {
    public static void main(String[] args) {
        Pilha pilha = new Pilha(5);

        pilha.empilhar(1);
        pilha.empilhar(2);
        pilha.empilhar(3);

        System.out.println("Topo da pilha: " + pilha.topo()); // Deve imprimir "Topo da pilha: 3"

        int valorDesempilhado = pilha.desempilhar();
        System.out.println("Valor desempilhado: " + valorDesempilhado); // Deve imprimir "Valor desempilhado: 3"

        System.out.println("Topo da pilha após desempilhar: " + pilha.topo()); // Deve imprimir "Topo da pilha após desempilhar: 2"
    }
}
  
