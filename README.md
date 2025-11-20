# 💥 Desafio-Free-Fire: Simulação de Combate e Cura

Este projeto Python simula o núcleo da lógica de gerenciamento de vida e recursos (kits médicos) de um jogador em um jogo do estilo Battle Royale, como o Free Fire. É um exercício prático em **Programação Orientada a Objetos (POO)**.

O desafio consiste em garantir que o jogador sobreviva a uma sequência de eventos de dano e cura, gerenciando de forma correta seu inventário de Kits Médicos.

## 🎯 Objetivo do Desafio

O foco principal é na classe `Jogador` e na integridade de seus métodos:

1.  **Integridade do Dano (`sofrer_dano`):** Garantir que a vida seja subtraída corretamente e que o jogador seja "abatido" se a vida chegar a zero.
2.  **Gerenciamento de Recursos (`usar_kit_medico`):** O método deve verificar se há kits disponíveis antes de usá-los e garantir que a vida nunca ultrapasse o valor da `vida_maxima`.
3.  **Encapsulamento:** Usar a classe para manter o estado (`vida_atual`, `kits_medicos`) e o comportamento do jogador de forma organizada.

## 🚀 Como Executar

### 1. Pré-requisitos

Certifique-se de que o **Python 3** está instalado em sua máquina.

### 2. Baixar e Salvar o Código

Copie o código Python fornecido e salve-o em um arquivo chamado `desafio_free_fire.py`.

### 3. Execução

Abra seu terminal ou prompt de comando, navegue até o diretório do arquivo e execute o comando:

```bash
python desafio_free_fire.py
