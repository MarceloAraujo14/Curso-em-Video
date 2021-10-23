package supercalculadora;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SuperCalculadora {
    private JPanel mainPane;
    private JSpinner spnValor;
    private JButton btnCalc;
    private JLabel lblRest;
    private JLabel lblCub;
    private JLabel lblRQ;
    private JLabel lblRC;
    private JLabel lblVA;
    private JPanel Entradas;
    private JLabel lblInfo;
    private JPanel Saidas;
    private JPanel nomes;
    private JPanel imagem;
    private JPanel valores;

    public SuperCalculadora() {
        //Deixando os resultados invisiveis
        valores.setVisible(false);
        nomes.setVisible(false);

        //Ação do botão de calcular
        btnCalc.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                //Deixando os resultados visiveis
                valores.setVisible(true);
                nomes.setVisible(true);

            //Adquirindo o valor do spinner
            int valor = (int) spnValor.getValue();
            //calculando resto da div por 2
            int rest = valor % 2;
            //calculando o valor ao cubo
            float cubo = (float)Math.pow(valor, 3);
            //calculando o valor da raiz quadrada
            float rq = (float) Math.sqrt(valor);

            float rc = (float) Math.cbrt(valor);
            int va = Math.round(valor);

            lblRest.setText(Integer.toString(rest));
            lblCub.setText(Float.toString(cubo));
            lblRQ.setText(Float.toString(rq));
            lblRC.setText(Float.toString(rc));
            lblVA.setText(Integer.toString(va));

            }
        });
    }

    public static void main(String[] args) {
        JFrame window = new JFrame("Super Calculadora");
        window.setContentPane(new SuperCalculadora().mainPane);
        window.setVisible(true);
        window.setResizable(false);
        window.pack();
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
