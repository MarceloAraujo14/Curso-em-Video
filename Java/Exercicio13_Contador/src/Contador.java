import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Contador {
    private JPanel root;
    private JSlider sliInicio;
    private JSlider sliFinal;
    private JSlider sliPasso;
    private JButton btnContar;
    private JTextPane txtCont;
    private JLabel lblInicio;
    private JLabel lblFim;
    private JLabel lblPasso;

    public Contador() {
        sliInicio.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblInicio.setText(Integer.toString(sliInicio.getValue()));
            }
        });
        sliFinal.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblFim.setText(Integer.toString(sliFinal.getValue()));
            }
        });
        sliPasso.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblPasso.setText(Integer.toString(sliPasso.getValue()));
            }
        });
        btnContar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int i = sliInicio.getValue();
                int f = sliFinal.getValue();
                int p = sliPasso.getValue();
                String cont = "";
                if (f<i){
                    for (i=i;i>=f;i-=p){
                    cont = cont + i + "\n";
                    }
                }else{
                for (i=i;i<=f;i+=p){
                    cont = cont + i + "\n";
                    }
                }

                txtCont.setText(cont);
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Contador");
        frame.setContentPane(new Contador().root);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
