package cursoemvideo;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Date;

public class TelaRelogio extends JDialog {
    private JLabel lblHora;
    private JButton btnHora;
    private JPanel contentPane;

    public TelaRelogio() {
        setContentPane(contentPane);
        setModal(true);

        Date relogio = new Date();

        btnHora.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                lblHora.setText(relogio.toString());
            }
        });
    }

    public static void main(String[] args) {
        TelaRelogio dialog = new TelaRelogio();
        dialog.pack();
        dialog.setVisible(true);
        System.exit(0);
    }
}


