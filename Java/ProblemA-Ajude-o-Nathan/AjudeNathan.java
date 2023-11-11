import java.util.Scanner;

public class AjudeNathan
{
	public static void main(String[] args) {
	    
	    int t, k,thiago,nathan; 
	    String valores[]; //String[] valores;
	    
	    Scanner input = new Scanner(System.in);
	    
		System.out.println("Casos de testes:");
		t = input.nextInt();
		
		input.nextLine();
		
		for (int i=0;i<t;i++){
		
		    valores = input.nextLine().split(" ");
		
		    k= Integer.parseInt(valores[0]);
		    thiago= Integer.parseInt(valores[1]);
		    nathan= Integer.parseInt(valores[2]);
		    
		    if (((thiago+nathan)/k)%2 == 0){
		        System.out.println("Thiago");
		    }else{
		        System.out.println("Nathan");
		    }
		    
		}
		
	}
}
