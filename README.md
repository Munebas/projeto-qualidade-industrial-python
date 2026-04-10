#  Sistema de Gestão de Qualidade Industrial

Este projeto foi desenvolvido como parte de um desafio de automação para uma linha de montagem industrial. O objetivo é substituir a inspeção manual por um sistema lógico que valida peças de acordo com critérios técnicos.

##  Funcionalidades
* **Cadastro de Peças:** Entrada de dados (ID, peso, tamanho e cor).
* **Validação Automática:** O sistema aplica regras de negócio para aprovar ou reprovar a peça.
* **Gestão de Logística:** Cálculo automático de caixas fechadas (cada 10 peças aprovadas).
* **Relatório de Produção:** Exibe o total de peças, aprovadas, reprovadas e caixas prontas.

##  Regras de Negócio
Para ser aprovada, a peça deve seguir:
* **Peso:** Entre 95g e 105g.
* **Tamanho:** Entre 10cm e 20cm.
* **Cor:** Azul ou Verde.

##  Tecnologias Utilizadas
* Python 3
* Bibliotecas: `os` (limpeza de terminal) e `time` (pausas do sistema).

##  Autor
* **Seu Nome** - [Seu Link do LinkedIn ou e-mail]
