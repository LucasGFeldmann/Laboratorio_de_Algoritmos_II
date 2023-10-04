*SISTEMA DE GERENCIAMENTO DE ESTOQUE E VENDA DE PRODUTOS*

Funcionalidades:

 - Estoque
Adição de Produto, Alteração de Dados do Produto, Exclusão de Produtos
 - Vendas
Venda de Produto
 - Apresentação
Apresentar produto, Apresentar produtos de uma categoria
 - Relatório Histórico
Geral de Movimentações, Histórico de Vendas, Histórico de Vendas de um Produto
Arquitetura:

O sistema é dividido em 3 partes: 

Estoque, Vendas e Relatórios. As partes Estoque e Vendas compartilham as funcionalidades de apresentação.

Porém, temos 5 módulos:

 - Módulo Histórico:
Local onde fica armazenado o histórico de transações e apresenta os relatórios do histórico.

 - Menu:
É nele que o Sistema iniciara. Ele contém os menus das três partes do sistema mais o menu inicial onde se pode transitar entre o estoque, as vendas e os relatórios.

 - Vendas:
É neste módulo que contém tudo relacionado às operações de vendas.

 - Estoque:
Onde contém todas as operações relacionadas ao estoque.

 - Utilitários:
Neste módulo contém algumas funções que são utilizadas nos outros módulos.
