import javax.swing.JOptionPane;
public class Main {
    public static void main(String[] args) {
        int n, s= 0; int i= 0; int c=0; int p=0;

        do
        {   n = Integer.parseInt(JOptionPane.showInputDialog(null, "<html>Informe um número: <br>[0 interrompe] </html>"));
            s += n;
            c +=1;
            if (n%2==0){
                p +=1;
            }else {
                i+=1;
            }
        }while (n!=0);
        JOptionPane.showMessageDialog(null, "A soma dos numeros que você digitou é: " + s + "\nA soma dos numeros que você digitou é: " + s);

    }
}
