def medidas_de_inf():
    print('Digite 1 para converter byte para outra unidade.')
    print('Digite 2 para converter kilobyte para outra unidade.')
    print('Digite 3 para converter megabyte para outra unidade.')
    print('Digite 4 para converter gigabyte para outra unidade.')
    print('Digite 5 para converter terabyte para outra unidade.')
    opc = int(input('Digite a opcao: '))

    if opc == 1:
        #byte = float(input('Digite a medida em byte; '))
        print('Digite 1 para converter para kilobyte.')
        print('Digite 2 para converter para megabyte.')
        print('Digite 3 para converter para gigabyte.')
        print('Digite 4 para converter para terabyte.')
        unid = int(input('Digite a opcao: '))
        if unid == 1:
            byte = float(input('Digite a medida em byte; '))
            kb = byte/1000
            print('O valor em kilobytes eh: ', kb)
        elif unid == 2:
            byte = float(input('Digite a medida em byte; '))
            mb = byte/1000000
            print('O valor em megabytes eh: ', mb)
        elif unid == 3:
            byte = float(input('Digite a medida em byte; '))
            gb = byte/1000000000
            print('O valor em gigabytes eh: ', gb)
        elif unid == 4:
            byte = float(input('Digite a medida em byte; '))
            tb = byte/1000000000000
            print('O valor em terabytes eh: ', tb)
        else:
            print('Valor invalido')

    elif opc == 2:
        # byte = float(input('Digite a medida em byte; '))
        print('Digite 1 para converter para byte.')
        print('Digite 2 para converter para megabyte.')
        print('Digite 3 para converter para gigabyte.')
        print('Digite 4 para converter para terabyte.')
        unid = int(input('Digite a opcao: '))
        if unid == 1:
            kb = float(input('Digite a medida em kilobyte; '))
            byte = kb*1000
            print('O valor em bytes eh: ', byte)
        elif unid == 2:
            kb = float(input('Digite a medida em kilobyte; '))
            mb = kb / 1000
            print('O valor em megabytes eh: ', mb)
        elif unid == 3:
            kb = float(input('Digite a medida em kilobyte; '))
            gb = kb / 1000000
            print('O valor em gigabytes eh: ', gb)
        elif unid == 4:
            kb = float(input('Digite a medida em kilobyte; '))
            tb = kb / 1000000000
            print('O valor em terabytes eh: ', tb)
        else:
            print('Valor invalido')

    elif opc == 3:
        print('Digite 1 para converter para byte.')
        print('Digite 2 para converter para kilobyte.')
        print('Digite 3 para converter para gigabyte.')
        print('Digite 4 para converter para terabyte.')
        unid = int(input('Digite a opcao: '))
        if unid == 1:
            mb = float(input('Digite a medida em megabyte; '))
            byte = mb*1000000
            print('O valor em bytes eh: ', byte)
        elif unid == 2:
            mb = float(input('Digite a medida em megabyte; '))
            kb = mb*1000
            print('O valor em kilobytes eh: ', kb)
        elif unid == 3:
            mb = float(input('Digite a medida em megabyte; '))
            gb = mb / 1000
            print('O valor em gigabytes eh: ', gb)
        elif unid == 4:
            mb = float(input('Digite a medida em megabyte; '))
            tb = mb * 1000000
            print('O valor em terabytes eh: ', tb)
        else:
            print('Valor invalido')

    elif opc == 4:
        print('Digite 1 para converter para byte.')
        print('Digite 2 para converter para kilobyte.')
        print('Digite 3 para converter para megabyte.')
        print('Digite 4 para converter para terabyte.')
        unid = int(input('Digite a opcao: '))
        if unid == 1:
            gb = float(input('Digite a medida em gigabyte; '))
            byte = gb*1000000000
            print('O valor em bytes eh: ', byte)
        elif unid == 2:
            gb = float(input('Digite a medida em gigabyte; '))
            kb = gb*1000000
            print('O valor em kilobytes eh: ', kb)
        elif unid == 3:
            gb = float(input('Digite a medida em gigabyte; '))
            mb = gb * 1000
            print('O valor em megabytes eh: ', mb)
        elif unid == 4:
            gb = float(input('Digite a medida em gigabyte; '))
            tb = gb / 1000
            print('O valor em terabytes eh: ', tb)
        else:
            print('Valor invalido')

    elif opc == 5:
        print('Digite 1 para converter para byte.')
        print('Digite 2 para converter para kilobyte.')
        print('Digite 3 para converter para megabyte.')
        print('Digite 4 para converter para gigabyte.')
        unid = int(input('Digite a opcao: '))
        if unid == 1:
            tb = float(input('Digite a medida em terabyte; '))
            byte = tb * 1000000000000
            print('O valor em bytes eh: ', byte)
        elif unid == 2:
            tb = float(input('Digite a medida em terabyte; '))
            kb = tb * 1000000000
            print('O valor em kilobytes eh: ', kb)
        elif unid == 3:
            tb = float(input('Digite a medida em terabyte; '))
            mb = tb * 1000000
            print('O valor em bytes eh: ', mb)
        elif unid == 4:
            tb = float(input('Digite a medida em terabyte; '))
            gb = tb * 1000
            print('O valor em bytes eh: ', gb)
        else: print('Valor invalido')


menu = int(input('Digite 1 para converter e 2 para sair: '))
while menu != 2:
    if menu == 1:
        medidas_de_inf()
        menu = int(input('Digite 1 para converter e 2 para sair: '))
    elif menu == 2:
        break
    else:
        print('Valor invalido')
        menu = int(input('Digite 1 para converter e 2 para sair: '))
