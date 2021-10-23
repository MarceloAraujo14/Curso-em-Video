package classes;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Calendar;

public class Main extends JDialog {

    private JPanel rootPanel;
    private JButton btnCalc;
    private JSpinner txtAN;
    private JLabel lblIdade;

    public Main() {

        setContentPane(rootPanel);
        setModal(true);


        //ação do botão
        btnCalc.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int data = Calendar.getInstance().get(Calendar.YEAR);
                int an = (int) txtAN.getValue();
                int id = data - an;
                lblIdade.setText(Integer.toString(id));
            }
        });
    }

    public static void main(String[] args){

        Main window = new Main();
        window.pack();
        window.setVisible(true);
        System.exit(0);
    }
}
