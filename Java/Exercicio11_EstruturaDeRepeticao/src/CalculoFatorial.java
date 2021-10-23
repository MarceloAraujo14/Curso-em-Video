import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

public class CalculoFatorial {
    private JPanel root;
    private JSpinner spiFat;
    private JLabel lblFat;

    public CalculoFatorial() {
        spiFat.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {

                double n = (int) spiFat.getValue();
                double fat=1;

                while (n>0){
                    fat = fat * n;
                    n--;
                }
                lblFat.setText(Double.toString(fat));
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("CalculoFatorial");
        frame.setContentPane(new CalculoFatorial().root);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
