class Veiculo:
    def __init__(self, placa: str, marca: str, modelo: str, valor_diaria: float):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.valor_diaria = float(valor_diaria)
        self.disponivel = True

    def __repr__(self) -> str:
        return f"Placa: {self.placa} | {self.marca} {self.modelo} | Diária: {self.valor_diaria:.2f} | Disponível: {self.disponivel}"


class Carro(Veiculo):
    def __init__(self, placa: str, marca: str, modelo: str, valor_diaria: float, categoria: str):
        super().__init__(placa, marca, modelo, valor_diaria)
        self.categoria = categoria

    def __repr__(self) -> str:
        return (
            f"[CARRO] Placa: {self.placa} | {self.marca} {self.modelo} | Categoria: {self.categoria} | "
            f"Diária: {self.valor_diaria:.2f} | Disponível: {self.disponivel}"
        )


class Moto(Veiculo):
    def __init__(self, placa: str, marca: str, modelo: str, valor_diaria: float, cilindradas: int):
        super().__init__(placa, marca, modelo, valor_diaria)
        self.cilindradas = int(cilindradas)

    def __repr__(self) -> str:
        return (
            f"[MOTO] Placa: {self.placa} | {self.marca} {self.modelo} | Cilindradas: {self.cilindradas} | "
            f"Diária: {self.valor_diaria:.2f} | Disponível: {self.disponivel}"
        )


class Cliente:
    def __init__(self, cpf: str, nome: str, cnh: str):
        self.cpf = cpf
        self.nome = nome
        self.cnh = cnh

    def __repr__(self) -> str:
        return f"Cliente: {self.nome} | CPF: {self.cpf} | CNH: {self.cnh}"


class Locacao:
    def __init__(self, cliente: Cliente, veiculo: Veiculo, quantidade_dias: int):
        self.cliente = cliente
        self.veiculo = veiculo
        self.quantidade_dias = int(quantidade_dias)

    def calcular_total(self) -> float:
        return self.quantidade_dias * self.veiculo.valor_diaria


def encontrar_cliente_por_cpf(clientes, cpf: str):
    for c in clientes:
        if c.cpf == cpf:
            return c
    return None


def encontrar_veiculo_por_placa(veiculos, placa: str):
    for v in veiculos:
        if v.placa == placa:
            return v
    return None


def listar_veiculos_disponiveis(veiculos):
    for v in veiculos:
        if v.disponivel is True:
            print(v)


def listar_veiculos_por_categoria(veiculos, categoria: str):
    categoria = categoria.strip()
    for v in veiculos:
        if isinstance(v, Carro) and v.categoria.lower() == categoria.lower():
            print(v)


def main():
    veiculos = []
    clientes = []
    locacoes = []

    while True:
        opcao = input(
            "\n--- DriveX - Menu ---\n"
            "1. Cadastrar Veículo\n"
            "2. Cadastrar Cliente\n"
            "3. Consultar Veículos Disponíveis\n"
            "4. Consultar Veículos por Categoria (Carro)\n"
            "5. Realizar Locação\n"
            "6. Relatório de Faturamento (locações ativas)\n"
            "0. Sair\n"
            "Escolha: "
        )

        if opcao == '0':
            print('Saindo...')
            break

        if opcao == '1':
            tipo = input('Digite o tipo do veículo (carro/moto): ').strip().lower()
            placa = input('Placa: ').strip()

            if encontrar_veiculo_por_placa(veiculos, placa) is not None:
                print('Erro: já existe um veículo com essa placa.')
                continue

            marca = input('Marca: ').strip()
            modelo = input('Modelo: ').strip()
            valor_diaria = float(input('Valor diária: ').strip())

            if tipo == 'carro':
                categoria = input('Categoria (ex: SUV, Sedan, Hatch): ').strip()
                veiculos.append(Carro(placa, marca, modelo, valor_diaria, categoria))
                print('Carro cadastrado com sucesso!')
            elif tipo == 'moto':
                cilindradas = int(input('Cilindradas (ex: 125, 250): ').strip())
                veiculos.append(Moto(placa, marca, modelo, valor_diaria, cilindradas))
                print('Moto cadastrada com sucesso!')
            else:
                print('Tipo inválido. Use carro ou moto.')

        elif opcao == '2':
            cpf = input('CPF: ').strip()

            if encontrar_cliente_por_cpf(clientes, cpf) is not None:
                print('Erro: já existe um cliente com esse CPF.')
                continue

            nome = input('Nome: ').strip()
            cnh = input('CNH: ').strip()
            clientes.append(Cliente(cpf, nome, cnh))
            print('Cliente cadastrado com sucesso!')

        elif opcao == '3':
            print('\n--- Veículos disponíveis ---')
            listar_veiculos_disponiveis(veiculos)

        elif opcao == '4':
            categoria = input('Digite a categoria (ex: SUV): ').strip()
            print(f"\n--- Veículos da categoria {categoria} ---")
            listar_veiculos_por_categoria(veiculos, categoria)

        elif opcao == '5':
            cpf = input('CPF do cliente: ').strip()
            cliente = encontrar_cliente_por_cpf(clientes, cpf)
            if cliente is None:
                print('Erro: cliente não encontrado.')
                continue

            placa = input('Placa do veículo: ').strip()
            veiculo = encontrar_veiculo_por_placa(veiculos, placa)
            if veiculo is None:
                print('Erro: veículo não encontrado.')
                continue

            if veiculo.disponivel is False:
                print('Erro: veículo indisponível para locação.')
                continue

            quantidade_dias = int(input('Quantidade de dias: ').strip())
            veiculo.disponivel = False

            loc = Locacao(cliente, veiculo, quantidade_dias)
            locacoes.append(loc)

            print('Locação realizada com sucesso!')
            print(f'Total da locação: {loc.calcular_total():.2f}')

        elif opcao == '6':
            faturamento = 0.0
            for l in locacoes:
                faturamento += l.calcular_total()

            print(f"\n--- Faturamento bruto atual (locações ativas) ---\nFaturamento: R$ {faturamento:.2f}")

        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    main()

