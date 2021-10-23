import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


public class TiposdeTriangulos {
    private JPanel rootPane;
    private JSlider sldA;
    private JSlider sldB;
    private JSlider sldC;
    private JButton calcularButton;
    private JLabel lblA;
    private JLabel lblB;
    private JLabel lblC;
    private JLabel lblRes;
    private JPanel TiposdeTriangulos;
    private JPanel painel;


    public TiposdeTriangulos() {
        sldA.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblA.setText(Integer.toString(sldA.getValue()));
            }
        });
        sldB.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblB.setText(Integer.toString(sldB.getValue()));
            }
        });
        sldC.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblC.setText(Integer.toString(sldC.getValue()));
            }
        });

        calcularButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                //puxando os valores das labels pra calcular o triangulo
                int a = sldA.getValue();
                int b = sldB.getValue();
                int c = sldC.getValue();

                boolean triangulo = (a<b+c && b<a+c && c<a+b);


                String tipo = "";
                if (a==b && a==c){
                    tipo = "Equilátero";
                }
                else if (a!=b && b!=c && a!=c){
                    tipo = "Escaleno";
                }
                else {
                    tipo = "Isósceles";
                }

                if (triangulo) {lblRes.setText("Essas medidas formam um triângulo "+ tipo);
                }else {
                    lblRes.setText("Essas medidas não formam um triângulo");}
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Tipos de Triangulos");
        frame.setContentPane(new TiposdeTriangulos().rootPane);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
        frame.setResizable(false);
    }
}
