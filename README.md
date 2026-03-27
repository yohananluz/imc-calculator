# Calculadora de IMC em Python

Projeto em Python para calcular o **Índice de Massa Corporal (IMC)** a partir do peso e da altura. Há duas formas de uso: **interface gráfica** (janela) e **terminal** (linha de comando). A lógica do cálculo e da classificação fica centralizada em `imc.py`.

## Funcionalidades

- Entrada de **peso (kg)** e **altura (m)**.
- Cálculo do IMC: peso ÷ altura².
- **Classificação** com faixas usualmente associadas à OMS: Abaixo do peso, Peso normal, Sobrepeso, Obesidade.
- **Validação**: valores não numéricos, zero ou negativos são tratados com mensagens de erro.
- Na interface gráfica é possível usar **vírgula ou ponto** nos decimais (ex.: `1,75` ou `1.75`). No terminal, use **ponto** (ex.: `1.75`), conforme o `imc.py` atual.

## Requisitos

- **Python 3.10+** (testado com 3.12).
- **tkinter** (biblioteca padrão; incluída na instalação completa do Python no Windows). Se faltar, reinstale o Python marcando os componentes **tcl/tk**.

## Estrutura do projeto

| Arquivo / pasta | Função |
|------------------|--------|
| `imc.py` | Função `calcular_imc` e programa para o **terminal** (`python imc.py`). |
| `imc_gui.py` | Janela com **tkinter**; importa `calcular_imc` de `imc.py`. |
| `run_python.bat` | Usado pelos outros `.bat`: procura Python 3.10–3.13 em pastas comuns e no PATH (`py`, `python`). |
| `run_gui.bat` | Abre a **interface gráfica**. Se não houver Python, exibe como instalar. |
| `run_terminal.bat` | Roda a versão **terminal**; mesmo comportamento de detecção do Python. |
| `.vscode/settings.json` | Interpretador Python sugerido para o Cursor/VS Code. |
| `.vscode/launch.json` | Configurações de execução/debug (F5). |

## Como obter o código

Clone o repositório (substitua pela URL do seu remoto, se for outra):

```bash
git clone https://github.com/yohananluz/imc-calculator.git
cd imc-calculator
```

Ou baixe o ZIP e abra a pasta no Cursor/VS Code.

## Passo a passo: usar a calculadora

### Opção A — Interface gráfica (recomendado no Windows)

1. Abra a pasta do projeto no explorador de arquivos.
2. Dê **dois cliques** em **`run_gui.bat`**.  
   O projeto precisa ter **Python 3 instalado** na máquina. O `run_python.bat` tenta vários caminhos comuns (Python 3.10 a 3.13 em `AppData` e `Program Files`) e depois `py -3` e `python`. Se nada for encontrado, a janela do prompt mostra links para instalar ([python.org](https://www.python.org/downloads/) ou `winget`).
3. Na janela, informe **peso** e **altura**, clique em **Calcular**. O IMC e a classificação aparecem abaixo.

**Alternativa pelo terminal** (na pasta do projeto):

```powershell
python imc_gui.py
```

Se o comando `python` abrir a Microsoft Store ou der erro, use o caminho completo do executável ou o `run_gui.bat`.

### Opção B — Terminal (linha de comando)

1. Abra o PowerShell ou CMD na pasta do projeto.
2. Execute:

```powershell
python imc.py
```

3. Digite o peso quando pedido, depois a altura em **metros** com **ponto** decimal (ex.: `1.75`).
4. Leia o IMC e a classificação na saída.

**Atalho no Windows:** dois cliques em **`run_terminal.bat`** (ajuste o caminho do Python no arquivo, se necessário).

### Opção C — Cursor / VS Code

1. **Arquivo → Abrir pasta** e selecione a pasta do projeto.
2. Instale a extensão **Python**, se ainda não tiver.
3. Abra o painel **Run and Debug** (ou **Executar e depurar**).
4. Escolha no topo:
   - **IMC: interface gráfica** — para rodar `imc_gui.py`;
   - **IMC: terminal (prompt)** — para rodar `imc.py`.
5. Pressione **F5** ou clique no botão de iniciar.

O arquivo `.vscode/settings.json` aponta um interpretador em `Python312`; se o seu for outro, altere `python.defaultInterpreterPath` nas configurações da workspace.

## Observação sobre o `python` no Windows

Às vezes o comando `python` no PATH aponta para um atalho da **Microsoft Store**. Nesse caso, instale o Python em [python.org](https://www.python.org/downloads/) (marcando **Add python.exe to PATH**) ou use **`run_gui.bat` / `run_terminal.bat`** com o caminho correto do `python.exe`.

## Licença e uso

Este projeto é educacional. O IMC é apenas um indicador numérico; interpretação médica ou nutricional deve ser feita por profissional habilitado.
