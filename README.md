# Trabalho Final - ES - 11 - Object Calisthenics

### 1. Normalização
A normalização consiste em armazenar cada dado em um único local canônico, fazendo com que outros objetos apenas referenciem essa instância. Na loja feia, os dados da cliente Ana estavam duplicados em múltiplos pedidos, forçando atualizações manuais e propensas a erros em cada pedido. Ao criar um objeto `Cliente` único, todos os seus pedidos agora apontam para a mesma referência na memória.

### 2. Obsessão por Tipos Primitivos
O `Cpf` virou uma classe para que as regras de validação (como ter exatamente 11 dígitos) fiquem encapsuladas no próprio construtor, impedindo a existência de CPFs inválidos no sistema. O programa ganhou garantia de consistência de dados sem precisar de verificações externas repetidas. O `Dinheiro` guarda centavos inteiros para evitar imprecisões de ponto flutuante típicas do tipo `float` em operações financeiras.

### 3. Diga, Não Pergunte
A troca do status agora é feita enviando ordens diretas ao pedido (`pedido.pagar()`), sem consultar getters para decidir o fluxo. A regra de negócio ficou melhor dentro do `Pedido` porque o próprio objeto se torna responsável por validar seus estados internos e garantir a consistência das transações.

### 4. Fail First
O código "hadouken" de validações encadeadas da loja feia foi eliminado ao mover as validações para o construtor dos objetos de valor, que disparam exceções imediatamente ao falhar. As estruturas de `else`/`elif` foram substituídas por retornos antecipados em métodos de controle e por polimorfismo nas estratégias de desconto (`TipoNormal`, `TipoVip`, `TipoFuncionario`).

### 5. Modularização
- **TipoNormal / TipoVip / TipoFuncionario**: Calculam as taxas de desconto específicas para cada categoria de cliente.
- **Cpf / Email / Cep**: Validam e representam dados de identificação e contato.
- **Dinheiro**: Executa operações aritméticas e formatação de valores monetários baseados em centavos.
- **Status**: Gerencia a descrição e a verificação do estado operacional do pedido.
- **Pessoa**: Guarda os dados de identificação pessoal do cliente.
- **Endereco**: Armazena as informações de localização.
- **Cliente**: Agrupa a pessoa, seu endereço e seu plano de desconto.
- **Produto**: Armazena o nome e o preço unitário do item.
- **ItemDoPedido**: Associa um produto a uma determinada quantidade.
- **ItensDoPedido**: Encapsula a lista de itens de um pedido e calcula o subtotal acumulado.
- **Pedido**: Controla as operações de pagamento, cancelamento e relatório individual de compras.
- **Pedidos**: Gerencia o dicionário de todos os pedidos da loja e consolida relatórios globais.

### 6. Dívida Técnica
Todas as restrições e regras do Object Calisthenics foram applied integralmente no projeto. A regra mais difícil de aplicar foi manter o limite estrito de no máximo 3 variáveis de instância por classe ao modelar o `Cliente`, o que exigiu extrair e delegar responsabilidades para as novas entidades `Pessoa` e `Endereco`.
