import csv
import os


def Menu(v):
    print('Olá, usuário! O que você deseja fazer? ')
    print()

    for option in v:
        print(option)


def CriarTabela(): #opção 1 - criar uma tabela
    tab = []
    tab.append(['Mês', 'Ganhos', 'Gastos', 'Saldo'])
    return tab


def GravarTabela(tab, file): #opção 2 - gravar uma tabela
    arq = open(file, 'w')
    try:
        writer = csv.writer(arq, delimiter='\t')
        for t in tab:
            writer.writerow((t[0], t[1], t[2], t[3]))
    finally:
        arq.close()


def LerTabela(file): #opção 3 - ler tabela do arquivo
    matriz = []
    arq = open(file, 'r')
    vazio = 1
    try:
        leitor = csv.reader(arq)
        for linha in leitor:
            if len(linha) != 0:
                matriz.append(linha[0].split('\t'))
            for c in linha:
                if c != '':
                    vazio = 0
                print(c)

        if vazio == 0:
            return matriz
    finally:
        arq.close()

    if vazio == 1:
        print('Arquivo vazio.')
        print()
        return 0


def ApagarTabela(file, opcao): #opção 4 - apagar tabela ou apagar arquivo
    if opcao == 1:
        arq = open(file, 'w')
        try:
            writer = csv.writer(arq)
            writer.writerow('')
        finally:
            arq.close()
    elif opcao == 2:
        os.remove(file)


def ChaveMes(tab): #chave de ordenação pelo mês
    mes = tab[0]
    return (mes)


def ChaveGanhos(tab): #chave de ordenação pelos ganhos
    ganhos= float(tab[1])
    return (ganhos)


def ChaveGastos(tab): #chave de ordenação pelos gastos
    gastos = float(tab[2])
    return (gastos)


def ChaveSaldo(tab): #chave de ordenação pelo saldo
    saldo = float(tab[3])
    return (saldo)


def ListarTabela(tabela, ordem, c): #opção 5 - listar dados da tabela com duas opções de ordenação
    if ordem == 1:
        if c == 1:
            new_table = sorted(tabela, key=ChaveMes)
        elif c == 2:
            new_table = sorted(tabela, key=ChaveGanhos)
        elif c == 3:
            new_table = sorted(tabela, key=ChaveGastos)
        elif c == 4:
            new_table = sorted(tabela, key=ChaveSaldo)

    elif ordem == 2:
        if c == 1:
            new_table = sorted(tabela, key=ChaveMes, reverse=True)
        elif c == 2:
            new_table = sorted(tabela, key=ChaveGanhos, reverse=True)
        elif c == 3:
            new_table = sorted(tabela, key=ChaveGastos, reverse=True)
        elif c == 4:
            new_table = sorted(tabela, key=ChaveSaldo, reverse=True)

    return new_table


def ConsultarRegistro(tab, registro): #opção 6 - consultar um registro
    found = 0
    registro = registro[0].upper() + registro[1:]
    for linha in tab:
        if linha[0] == registro:
            found = 1
            for c in linha:
                print(c, end='\t')
            print()

    if found == 0:
        print('Registro não encontrado.')


def InserirRegistro(tab, mes, ganhos, gastos, saldo): #opção 7 - inserir um registro
    mes = mes[0].upper() + mes[1:]
    tab.append([mes, ganhos, gastos, saldo])


def ApagarRegistro(tab, reg): #opção 8 - apagar registro
    reg = reg[0].upper() + reg[1:]
    for linha in tab:
        if linha[0] == reg:
            tab.remove(linha)


def Listar(tab, tipo, camp=0): #opção 9 - listagem total ou filtrada
    if tipo == 1:
        for linha in tab:
            for c in linha:
                print(c, end='\t')
            print()

    elif tipo == 2: #listagem filtrada
        for c in tab[0]:
            print(c, end='\t')
        print()
        if camp == 1:
            for i in range(1, len(tab)):
                if tab[i][0] in ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'):
                    for c in tab[i]:
                        print(c, end='\t')
                    print()

        elif camp == 2:
            for i in range(1, len(tab)):
                if tab[i][0] in ('Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'):
                    for c in tab[i]:
                        print(c, end='\t')
                    print()

        elif camp == 3:
            for i in range(1, len(tab)):
                if float(tab[i][2]) >= 500:
                    for c in tab[i]:
                        print(c, end='\t')
                    print()

        elif camp == 4:
            for i in range(1, len(tab)):
                if float(tab[i][1]) >= 500:
                    for c in tab[i]:
                        print(c, end='\t')
                    print()

        else:
            for i in range(1, len(tab)):
                if float(tab[i][3]) >= 500:
                    for c in tab[i]:
                        print(c, end='\t')
                    print()


options = ['1 – Criar uma tabela',
           '2 – Gravar tabela em um arquivo',
           '3 – Ler tabela de um arquivo',
           '4 - Apagar tabela do arquivo',
           '5 - Listar dados da tabela corrente',
           '6 - Consultar um registro da tabela corrente',
           '7 - Inserir novo registro na tabela corrente',
           '8 - Apagar registro da tabela corrente',
           '9 - Listagem da tabela corrente',
           '0 - Sair do programa']

Menu(options)
check = 0
tabela = []

while True:
    print()
    choice = int(input('Digite sua opção do menu principal: '))
    if choice in range(0, 10):
        if choice == 1:
            tab = CriarTabela()
            check = 1
            tabela = tab
            print('Tabela criada com sucesso!')

        elif choice == 2:
            while True:
                ar = input('Digite o nome do arquivo no qual deseja gravar a última tabela criada: ')
                L = ar.split('.')
                if L[1] == 'csv':
                    break
                else:
                    print('Extensão inválida. Digite um nome de arquivo com extensão csv!')
            if check == 1:
                GravarTabela(tabela, ar)
                print('Tabela gravada com sucesso!')
            else:
                print('Por favor, escolha a opção 1 e crie uma tabela antes de guardá-la no arquivo. Ou selecione uma tabela pré-existente em um arquivo, escolhendo a opção 3. ')

        elif choice == 3:
            while True:
                table = input('Qual é o arquivo que contém a tabela a ser lida? ')
                L = table.split('.')
                if L[1] == 'csv':
                    break
                else:
                    print('Extensão inválida. Digite um nome de arquivo com extensão csv!')
            mat = LerTabela(table)
            if mat != 0:
                check = 1 #há tabela atual
                tabela = mat[:]
                print('A tabela acima, lida do arquivo "{}", tornou-se sua tabela corrente.' .format(table))

        elif choice == 4:
            while True:
                table = input('Qual é o arquivo que contém a tabela a ser apagada? ')
                L = table.split('.')
                if L[1] == 'csv':
                    break
                else:
                    print('Extensão inválida. Digite um nome de arquivo com extensão csv!')
            while True:
                op = int(input('Você deseja apagar somente a tabela (1) ou o arquivo completo (2)? '))
                if op == 1:
                    print('Tabela apagada com sucesso!')
                    break
                elif op == 2:
                    print('Arquivo apagado com sucesso!')
                    break
            ApagarTabela(table, op)

        elif choice == 5:
            while True:
                n = int(input('Você deseja listar em: \n 1 - Ordem crescente \n 2 - Ordem decrescente \n'))
                if n == 1 or n == 2:
                    break
            dadosTabela = tabela[1:] #dados da tabela sem o cabeçalho
            while True:
                campo = int(input('Escolha o campo para guiar a ordenação: \n 1 - Mês \n 2 - Ganhos \n 3 - Gastos \n 4 - Saldo \n '))
                if campo in range(1, 5):
                    break
                else:
                    print('Opção inválida')
            if check == 1:
                for p in tabela[0]:
                    print(p, end='\t')
                print()
                tabOrdenada = ListarTabela(dadosTabela, n, campo)
                for linha in tabOrdenada:
                    for p in linha:
                        print(p, end='\t')
                    print()
            else:
                print('Não há tabela criada no momento. Por favor, escolha a opção 1 e crie uma tabela antes de listar os dados. Ou selecione uma tabela pré-existente em um arquivo, escolhendo a opção 3.')

        elif choice == 6:
            reg = input('Digite o mês do registro que você deseja consultar: ')
            if check == 1:
                ConsultarRegistro(tabela, reg)
            else:
                print('Não há tabela criada no momento. Por favor, escolha a opção 1 e crie uma tabela antes de consultar registros. Ou selecione uma tabela pré-existente em um arquivo, escolhendo a opção 3.')

        elif choice == 7:
            if check == 1:
                m = input('Digite o mês: ')
                gan = float(input('Digite os ganhos do mês: '))
                g = float(input('Digite os gastos do mês: '))
                s = gan - g
                InserirRegistro(tabela, m, gan, g, s)
                print('Registro inserido com sucesso!')
            else:
                print('Não há tabela criada no momento. Por favor, escolha a opção 1 e crie uma tabela antes de inserir registros. Ou selecione uma tabela pré-existente em um arquivo, escolhendo a opção 3.')

        elif choice == 8:
            if check == 1:
                reg = input('Digite o mês registro que você deseja apagar: ')
                ApagarRegistro(tabela, reg)
                print('Registro apagado com sucesso!')
            else:
                print('Não há tabela criada no momento. Por favor, escolha a opção 1 e crie uma tabela antes de apagar registros. Ou selecione uma tabela pré-existente em um arquivo, escolhendo a opção 3.')

        elif choice == 9:
            if check == 1:
                while True:
                    n = int(input('Você deseja: \n 1 - Listagem completa \n 2 - Listagem filtrada \n'))
                    if n == 1 or n == 2:
                        break
                    else:
                        print('Opção inválida')
                if n == 2:
                    while True:
                        camp = int(input('Escolha um critério de filtragem: \n 1 - Do mês de janeiro até junho \n 2 - Do mês de julho até dezembro \n 3 - Gastos maiores ou iguais a R$500,00 \n 4 - Ganhos maiores ou iguais a R$500,00 \n 5 - Saldos maiores ou iguais a R$500,00 \n '))
                        if camp in range(1,6):
                            break
                        else:
                            print('Opção inválida')
                    Listar(tabela, n, camp)
                else:
                    Listar(tabela, n)
            else:
                print('Não há tabela criada no momento. Por favor, escolha a opção 1 e crie uma tabela antes de listar dados. Ou selecione uma tabela pré-existente em um arquivo, escolhendo a opção 3.')

        elif choice == 0:
            break

    else:
        print('Opção inválida')
