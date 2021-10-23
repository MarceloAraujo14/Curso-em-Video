package resolucaodatela;
import java.awt.Toolkit;
import java.awt.Dimension;


public class ResolucaoDaTela {
    public static void main(String[] args) {
    Toolkit tk = Toolkit.getDefaultToolkit();
    Dimension d = tk.getScreenSize();
        System.out.println("A resolução da tela é " + d.width +  "x" + d.height + "p");
    }
}
