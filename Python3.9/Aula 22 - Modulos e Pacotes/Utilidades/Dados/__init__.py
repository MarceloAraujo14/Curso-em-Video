def leiaDinheiro(n):
    f = input(n).strip()
    try:
        while True:
            if f.isnumeric():
                return float(f)
                break
            elif ',' in f:
                f = f.replace(',', '.')
                return float(f)
                break
            elif '.' in f:
                return float(f)
                break
            else:
                f = input(f'\033[0;31mErro! "{f}" não é um valor válido, digite um valor válido: \033[m')
    except:
        print(f'\033[0;31mErro! "{f}" não é um valor válido, digite um valor válido: \033[m')
        leiaDinheiro(n)

