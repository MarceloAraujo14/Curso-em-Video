import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ComponentAdapter;

public class Main {

    private JPanel root;
    private JSpinner spnA;
    private JSpinner spnB;
    private JSpinner spnC;
    private JButton btnDelta;
    private JLabel lblB;
    private JLabel lblA;
    private JLabel lblC;
    private JPanel paneRes;
    private JLabel lblDeltaRes;
    private JLabel lblSit;

    // Alterando o valor de A,B e C conforme altera o spinner respectivo
    public Main() {

        paneRes.setVisible(false);

        spnA.addComponentListener(new ComponentAdapter() {
        });
        spnA.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {

                lblA.setText(spnA.getValue().toString());
            }
        });
        spnB.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {

                lblB.setText(spnB.getValue().toString());
            }
        });
        spnC.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {

                lblC.setText(spnC.getValue().toString());
            }
        });
        btnDelta.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int a = (int) spnA.getValue();
                int b = (int) spnB.getValue();
                int c = (int) spnC.getValue();

                float delta = (float) ((Math.pow(b,2))-(4*a*c));
                if (delta>0){
                    lblSit.setText("Duas raízes reais diferentes");
                } else {
                    if (delta == 0) {
                        lblSit.setText("Duas raízes reais iguais");
                    } else {
                        lblSit.setText("Não possui raiz real. ");
                    }
                }
                lblDeltaRes.setText(Float.toString(delta));
                paneRes.setVisible(true);
            }
        });
    }

    public static void main(String[] args) {

        JFrame frame = new JFrame("Equação do Segundo Grau");
        frame.setContentPane(new Main().root);
        frame.pack();
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
