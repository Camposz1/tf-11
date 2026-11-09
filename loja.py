# ==============================================================================
# TIPOS DE CLIENTE (POLIMORFISMO PARA DESCONTO - SEM ELSE)
# ==============================================================================

class TipoNormal:
    """Responsável por calcular o desconto para clientes do tipo Normal (0%)."""

    def calcular_desconto(self, valor_dinheiro):
        return valor_dinheiro.calcular_percentual(0)


class TipoVip:
    """Responsável por calcular o desconto para clientes do tipo VIP (10%)."""

    def calcular_desconto(self, valor_dinheiro):
        return valor_dinheiro.calcular_percentual(10)


class TipoFuncionario:
    """Responsável por calcular o desconto para clientes do tipo Funcionário (20%)."""

    def calcular_desconto(self, valor_dinheiro):
        return valor_dinheiro.calcular_percentual(20)


# ==============================================================================
# CLASSES DE VALOR (OBJECT CALISTHENICS: WRAP PRIMITIVES - 1 ATRIBUTO)
# ==============================================================================

class Cpf:
    """Responsável por encapsular e validar o formato do CPF."""

    def __init__(self, valor_texto):
        if len(valor_texto) != 11:
            raise ValueError("cpf invalido")
        self._valor = valor_texto


class Email:
    """Responsável por encapsular e validar o formato do e-mail."""

    def __init__(self, valor_texto):
        if not valor_texto:
            raise ValueError("email vazio")
        if "@" not in valor_texto:
            raise ValueError("email invalido")
        self._valor = valor_texto


class Cep:
    """Responsável por encapsular e validar o formato do CEP."""

    def __init__(self, valor_texto):
        if len(valor_texto) != 8:
            raise ValueError("cep invalido")
        self._valor = valor_texto


class Dinheiro:
    """Responsável por encapsular valores monetários operando sempre em centavos inteiros."""

    def __init__(self, centavos_inteiros):
        self._centavos = int(centavos_inteiros)

    def somar(self, outro_dinheiro):
        return Dinheiro(self._centavos + outro_dinheiro._centavos)

    def subtrair(self, outro_dinheiro):
        return Dinheiro(self._centavos - outro_dinheiro._centavos)

    def multiplicar_por_quantidade(self, quantidade):
        return Dinheiro(self._centavos * quantidade)

    def calcular_percentual(self, percentual_inteiro):
        centavos_desconto = round(self._centavos * (percentual_inteiro / 100.0))
        return Dinheiro(centavos_desconto)

    def __str__(self):
        reais = self._centavos / 100.0
        return f"R$ {reais:.2f}"


class Status:
    """Responsável por gerenciar os estados do pedido sem usar comandos if/elif de decisão."""

    def __init__(self, codigo_status):
        self._codigo = codigo_status
        self._mapeamento_descricao = {
            "A": "aberto",
            "P": "pago",
            "C": "cancelado"
        }

    def esta_aberto(self):
        return self._codigo == "A"

    def __str__(self):
        return self._mapeamento_descricao.get(self._codigo, "")


# ==============================================================================
# ENTIDADES DO DOMÍNIO (MÁXIMO 3 ATRIBUTOS POR CLASSE)
# ==============================================================================

class Pessoa:
    """Responsável por encapsular os dados pessoais de um cliente."""

    def __init__(self, nome_completo, cpf_objeto, email_objeto):
        self._nome = nome_completo
        self._cpf = cpf_objeto
        self._email = email_objeto

    def formatar_para_relatorio(self):
        return self._nome


class Endereco:
    """Responsável por encapsular a localização e o endereço de um cliente."""

    def __init__(self, nome_rua, nome_cidade, cep_objeto):
        self._rua = nome_rua
        self._cidade = nome_cidade
        self._cep = cep_objeto

    def obter_cidade(self):
        return self._cidade


class Cliente:
    """Responsável por integrar a pessoa, o endereço e o tipo de desconto de um cliente."""

    def __init__(self, pessoa_objeto, endereco_objeto, tipo_cliente_objeto):
        self._pessoa = pessoa_objeto
        self._endereco = endereco_objeto
        self._tipo_cliente = tipo_cliente_objeto

    def formatar_identificacao(self):
        nome = self._pessoa.formatar_para_relatorio()
        cidade = self._endereco.obter_cidade()
        return f"{nome} - {cidade}"

    def calcular_desconto(self, valor_total_dinheiro):
        return self._tipo_cliente.calcular_desconto(valor_total_dinheiro)


class Produto:
    """Responsável por guardar as informações essenciais de um produto."""

    def __init__(self, nome_produto, preco_dinheiro):
        self._nome = nome_produto
        self._preco = preco_dinheiro

    def formatar_item(self, quantidade):
        subtotal = self._preco.multiplicar_por_quantidade(quantidade)
        return f"{quantidade} x {self._nome} = {subtotal}"

    def calcular_subtotal(self, quantidade):
        return self._preco.multiplicar_por_quantidade(quantidade)


class ItemDoPedido:
    """Responsável por relacionar um produto com a quantidade comprada."""

    def __init__(self, produto_objeto, quantidade_unidades):
        self._produto = produto_objeto
        self._quantidade = quantidade_unidades

    def formatar_para_relatorio(self):
        return self._produto.formatar_item(self._quantidade)

    def calcular_subtotal(self):
        return self._produto.calcular_subtotal(self._quantidade)


# ==============================================================================
# COLEÇÕES DE PRIMEIRA CLASSE (FIRST-CLASS COLLECTIONS)
# ==============================================================================

class ItensDoPedido:
    """Coleção de primeira classe responsável exclusivamente por gerenciar a lista de itens do pedido."""

    def __init__(self):
        self._itens = []

    def adicionar_item(self, item_objeto):
        self._itens.append(item_objeto)

    def esta_vazia(self):
        return len(self._itens) == 0

    def calcular_total(self):
        total = Dinheiro(0)
        for item inpython3 loja.py > saida-original.txt

