package palpite;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Palpite {
    private JPanel mainFrame;
    private JButton btnChute;
    private JSpinner spnValor;
    private JLabel lblTexto;

    public Palpite() {
        lblTexto.setText("<html>Vou pensar em um valor <br> entre 1 e 5. Tente adivinhar!</html>");
        btnChute.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int num = (int)spnValor.getValue();
                int chute = (int)Math.floor(Math.random()*5)+1;
                String palpite = (num == chute) ? "Você acertou!" : ("Errou! eu pensei no " + chute);
                lblTexto.setText(palpite);
            }
        });
    }

    public static void main(String[] args) {
        JFrame mainFrame = new JFrame("Adivinhe o número");
        mainFrame.setContentPane(new Palpite().mainFrame);
        mainFrame.setVisible(true);
        mainFrame.pack();
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
