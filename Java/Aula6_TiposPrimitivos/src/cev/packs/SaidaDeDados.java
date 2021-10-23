package cev.packs;
import java.util.Scanner;


public class SaidaDeDados {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite o nome do aluno: ");
        String nome = teclado.nextLine();
        System.out.print("Digite a nota do aluno: ");
        float nota = teclado.nextFloat();
        System.out.print("Digite a idade do aluno: ");
        int idade = teclado.nextInt();
        String valor = Integer.toString(idade); // convertendo um inteiro para string
        int val = Integer.parseInt(valor); // convertendo uma string para inteiro

        System.out.printf("Sua nota de %s é %.2f e tem %d anos. \n",nome, nota, val);
    }
}
