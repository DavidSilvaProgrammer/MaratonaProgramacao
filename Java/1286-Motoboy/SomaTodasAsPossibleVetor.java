import java.util.ArrayList;
import java.util.List;

public class SomaCombinacoes {
    public static void main(String[] args) {
        // Definindo um vetor de inteiros
        int[] vetor = {1, 2, 3, 4};  // Você pode alterar os valores deste vetor
        List<Integer> somas = new ArrayList<>();  // Lista para armazenar as somas

        // Calculando todas as somas possíveis de elementos
        for (int i = 0; i < vetor.length; i++) {
            for (int j = i; j < vetor.length; j++) {
                int soma = 0;
                // Soma de todos os elementos entre o índice i e o índice j
                for (int k = i; k <= j; k++) {
                    soma += vetor[k];
                }
                somas.add(soma);  // Adicionando a soma à lista
            }
        }

        // Imprimindo as somas armazenadas
        System.out.println("Todas as somas possíveis de elementos do vetor são:");
        for (int soma : somas) {
            System.out.println(soma);
        }
    }
}
