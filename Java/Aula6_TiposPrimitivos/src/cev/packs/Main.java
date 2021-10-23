package cev.packs;

//Tipos primitivos
public class Main {

    public static void main(String[] args) {

        //inteiros
        int idade = 3;
        int idade1 = (int) 3; //(int) é um typecast
        //Integer idade2 = new Integer(3); essa forma não é mais utilizada (Wrapper Class)

        //real
        float sal = 1825.54f;
        float sal1 = (float) 1825.54;
        //Float sal = new Float(1825.54);

        //string
        char letra = 'G';
        char letra1 = (char) 'G';
        //Character letra2 = new Character('G');

        //lógico
        boolean casado = false;
        boolean casado1 = (boolean) false;
        //Boolean casado2 = new Boolean(false);


    }
}

// Familia |   Tipo  |  Classe   |  Tamanho  | Exemplo
// Logico    boolean   Boolean      1 bit       true

// Literais  char      Character    1 byte      'A'
//            -        String      1 byte/cada  "Java"

// Inteiros  byte      Byte         1 byte      127
//           short     Short        2 bytes     32 767
//           int       Integer      4 bytes     2 147 483
//           long      Long         8 bytes     2^63

// Reais     float     Float        4 bytes     3.4e+38
//           double    Double       8 bytes     1.8e+308