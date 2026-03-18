# Planilha de Metas Semanais — Desktop App

Aplicativo desktop para planejamento e acompanhamento de metas semanais, desenvolvido em Python com interface moderna baseada em CustomTkinter e persistência local em SQLite.

Projetado para uso pessoal e profissional, o software permite organizar atividades por prioridade, status e prazo, com visualização clara e foco em produtividade.

---

## Visão Geral

A aplicação funciona como uma planilha inteligente de metas semanais, inspirada em metodologias de produtividade como SMART e priorização por importância.

Todos os dados são armazenados localmente, sem necessidade de internet ou serviços externos.

---

## Principais Funcionalidades

### Organização de Metas

* Cadastro de metas ou atividades
* Classificação por categoria
* Níveis de prioridade (Alta, Média, Baixa)
* Status de progresso
* Prazo por dia da semana
* Campo de observações

### Produtividade e Planejamento

* Aplicação prática da metodologia SMART
* Regra dos 3 para prioridades altas
* Visualização semanal clara
* Atualização rápida de status
* Marcação direta como concluído

### Interface Profissional

* Tema escuro moderno
* Tabela estilizada com linhas alternadas
* Cores visuais por status
* Navegação simples e eficiente
* Experiência semelhante a aplicativos comerciais

### Persistência de Dados

* Banco de dados SQLite local
* Criação automática do banco na primeira execução
* Armazenamento offline e privado

### Integração com o Sistema

* Opção para iniciar automaticamente com o Windows
* Executável standalone sem dependências externas (após compilação)

---

## Estrutura de Dados

Cada meta contém os seguintes campos:

| Campo       | Descrição                               |
| ----------- | --------------------------------------- |
| Meta        | Descrição da atividade                  |
| Categoria   | Área da vida ou trabalho                |
| Prioridade  | Alta, Média ou Baixa                    |
| Status      | Não iniciado, Em andamento ou Concluído |
| Prazo       | Dia da semana                           |
| Observações | Informações adicionais                  |

---

## Tecnologias Utilizadas

* Python 3.x
* CustomTkinter (GUI moderna)
* Tkinter (base da interface)
* SQLite3 (banco de dados local)
* PyInstaller (empacotamento para .exe)
* Windows Registry (startup automático)

---

## Requisitos para Execução via Python

* Python 3.9 ou superior
* Sistema operacional Windows, Linux ou macOS (modo script)
* Dependências Python instaladas

---

## Instalação para Desenvolvimento

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd planilha-metas
```

### 2. Criar ambiente virtual (recomendado)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install customtkinter
```

---

## Execução do Projeto

```bash
python planilha_metas.py
```

O banco de dados será criado automaticamente no diretório do programa.

---

## Gerar Executável para Windows

### Instalar PyInstaller

```bash
pip install pyinstaller
```

### Compilar o programa

```bash
pyinstaller --onefile --windowed planilha_metas.py
```

Opcional — com nome e ícone personalizados:

```bash
pyinstaller --onefile --windowed --name PlanilhaMetas --icon=icone.ico planilha_metas.py
```

O executável será gerado em:

```
dist/PlanilhaMetas.exe
```

---

## Uso do Aplicativo

### Adicionar uma Meta

1. Preencha os campos superiores
2. Clique em "Adicionar Meta"
3. A meta aparecerá na lista

### Atualizar Status

* Selecione uma meta
* Clique em "Marcar como Concluído"

### Excluir Meta

* Selecione uma meta
* Clique em "Excluir Selecionada"

### Iniciar com o Windows

* Marque a opção "Iniciar com o Windows"
* O aplicativo será registrado na inicialização do usuário

---

## Armazenamento de Dados

Arquivo criado automaticamente:

```
metas_semanais.db
```

Localização:

* Mesmo diretório do executável ou script

Backup pode ser feito copiando esse arquivo.

---

## Segurança e Privacidade

* Todos os dados permanecem localmente
* Nenhuma comunicação com servidores externos
* Não coleta informações pessoais
* Funciona totalmente offline

---

## Limitações Conhecidas

* Não possui sincronização em nuvem
* Não suporta múltiplos usuários simultâneos
* Sem sistema de notificações
* Sem versão mobile

---

## Possíveis Melhorias Futuras

* Dashboard com gráficos de progresso
* Metas recorrentes automáticas
* Sistema de hábitos
* Modo Kanban (arrastar tarefas)
* Pomodoro integrado
* Exportação para Excel ou PDF
* Sincronização em nuvem
* Sistema de backup automático
* Interface multi-semanal
* Versão portátil e versão instalada

---

## Estrutura do Projeto

```
planilha-metas/
│
├── planilha_metas.py
├── metas_semanais.db   (gerado automaticamente)
├── requirements.txt    (opcional)
├── dist/               (após compilação)
└── README.md
```

---

## Licença

Este projeto pode ser utilizado para fins pessoais ou educacionais.
Para uso comercial, recomenda-se adicionar uma licença apropriada (MIT, GPL, etc.).

---

## Autor

Desenvolvido como aplicação desktop de produtividade em Python.

---

## Suporte

Caso ocorra algum problema:

* Verifique a versão do Python
* Confirme as dependências instaladas
* Execute via terminal para visualizar erros
* Teste o executável em outro diretório

---

## Considerações Finais

Este aplicativo oferece uma solução simples, robusta e totalmente offline para planejamento semanal, combinando organização estruturada com uma interface moderna e eficiente.

Ideal para estudantes, profissionais e desenvolvedores que desejam manter foco e clareza nas tarefas da semana.
