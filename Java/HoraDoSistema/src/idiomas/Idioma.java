package idiomas;

import java.util.Locale;

public class Idioma {
    public static void main(String[] args) {
        Locale local = Locale.getDefault();
        System.out.println("O idioma do sistema é " + local.getDisplayLanguage());

    }
}
