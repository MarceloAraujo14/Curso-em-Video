package cev.packs;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SomaValor extends JDialog{

    private JTextField txtVal;
    private JTextField txtVal2;
    private JButton btnSomar;
    private JLabel lblResultado;
    private JPanel painelPrincipal;

    public SomaValor() {

        setContentPane(painelPrincipal);
        setModal(true);


        btnSomar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
            int n1 = Integer.parseInt(txtVal.getText());
            int n2 = Integer.parseInt(txtVal2.getText());
            int s = n1 + n2;
            lblResultado.setText(Integer.toString(s));

            }
        });
    }

    public static void main(String[] args) {
        SomaValor dialog = new SomaValor();
        dialog.pack();
        dialog.setVisible(true);
        System.exit(0);
    }
}
