# Engineering Software Mecsol

Desktop application in Python for structural analysis of beam systems, with a graphical interface built in PySide6 and result visualization using Matplotlib.

This project was created to make an existing structural analysis routine more accessible to engineering students by replacing code-only input with a desktop workflow for data entry, calculation, visualization, and graph export.

## PT-BR

### Visão geral

O `Engineering Software Mecsol` é um aplicativo desktop para análise estrutural de vigas. O projeto combina:

- interface gráfica com `PySide6`
- processamento numérico com `NumPy`
- visualização de resultados com `Matplotlib`

O programa permite carregar um conjunto de dados de exemplo ou informar manualmente os dados da estrutura para calcular e visualizar:

- esforço normal
- esforço cortante
- momento fletor
- tensão equivalente de Von Mises
- deformada da estrutura
- deslocamento máximo

Também é possível exportar o gráfico exibido para arquivo `.png`.

### Stack

- Python
- PySide6
- Matplotlib
- NumPy

### Como executar

Exemplo em Windows:

```powershell
py -3.10 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python run.py
```

Se você estiver usando outra versão do Python, o ponto mais importante é que ela seja compatível com `PySide6`.

### Fluxo de uso

1. Abra a aplicação com `python run.py`.
2. Na tela inicial, escolha entre usar dados de exemplo ou inserir dados manualmente.
3. Se optar pela entrada manual, preencha:
   - dados gerais da estrutura
   - coordenadas nodais
   - incidência dos elementos
   - graus de liberdade
4. Execute o processamento da estrutura.
5. Navegue entre os elementos e entre os domínios de resultado para visualizar os gráficos.
6. Exporte a figura atual em `.png`, se necessário.

### Estrutura do projeto

- `run.py`
  Launcher compatível da aplicação.
- `gui/`
  Janela principal e controladores da interface.
- `ui/`
  Arquivos gerados e base visual da interface Qt.
- `resources/`
  Recursos Qt compilados e imagens usadas pela UI.
- `beam_analysis/`
  Contém as rotinas numéricas principais:
  - montagem da estrutura
  - rigidez do elemento
  - carregamento distribuído
  - reconstrução de tensões
  - reconstrução da deformada

### Arquivos importantes

- `run.py`
  Entrada principal da aplicação.
- `gui/main_window.py`
  Implementação principal da janela.
- `requirements.txt`
  Dependências Python do projeto.

### Contexto do projeto

Este projeto adapta para Python e interface gráfica uma rotina de análise estrutural originalmente usada em contexto acadêmico. O objetivo principal é facilitar o uso por estudantes e reduzir a necessidade de editar código diretamente para obter resultados estruturais e gráficos.

---

## EN

### Overview

`Engineering Software Mecsol` is a desktop application for beam structural analysis. The project combines:

- a graphical interface built with `PySide6`
- numerical processing with `NumPy`
- result visualization with `Matplotlib`

The application lets users load sample data or manually enter structural data to calculate and visualize:

- axial force
- shear force
- bending moment
- Von Mises equivalent stress
- deformed structural shape
- maximum displacement

The current graph can also be exported as a `.png` image.

### Stack

- Python
- PySide6
- Matplotlib
- NumPy

### How to run

Example on Windows:

```powershell
py -3.10 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python run.py
```

If you use another Python version, the main requirement is compatibility with `PySide6`.

### Usage flow

1. Start the application with `python run.py`.
2. On the first screen, choose sample data or manual input.
3. If you choose manual input, fill in:
   - general structural data
   - nodal coordinates
   - element connectivity
   - degrees of freedom
4. Run the structural processing step.
5. Switch between elements and result domains to inspect the generated plots.
6. Export the current plot to `.png` if needed.

### Project structure

- `run.py`
  Compatibility launcher for the application.
- `gui/`
  Main window and GUI controllers.
- `ui/`
  Generated Qt files and visual interface definition.
- `resources/`
  Compiled Qt resources and images used by the UI.
- `beam_analysis/`
  Main numerical routines for:
  - structural assembly
  - element stiffness
  - distributed loading
  - stress reconstruction
  - deformed shape reconstruction

### Important files

- `run.py`
  Main application entry point.
- `gui/main_window.py`
  Main window implementation.
- `requirements.txt`
  Python dependency list.

### Project context

This project brings an academic structural analysis routine into Python with a desktop UI. The main goal is to make the workflow more accessible to students by reducing direct code editing and making calculation and graph generation easier to use.
