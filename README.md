# 🐍 Automação de planilhas com Python!

Projeto 1 -> Planilha de Funcionários (Médico / Enfermeiro)

É um projeto simples, usado como estudo para o desenvolvimento do Projeto 2. Começei criando a Classe funcionario, que é minha "Classe Pai", por meio dela eu crio a base das "Classes 
Filhas" medico e enfermerio, utilizando o conceito de herança.

funcionario.py

- Começei criando o def __init__() é o construtor da classe, um método especial reconhecido pelo Python para inicializar novos objetos dessa classe, quando for criado uma instância
dessa o Python automaticamente chama o método __init__ dessa classe. É comumente usado par realizar todas as configurações necessárias no objeto, como inicializar atributos.
- Passo os argumentos/parametros
- Em seguida crio os atributos: nome, idade, cargo, qtdHoras, valorHora
- Por fim vem a criação dos métodos ou funções def

medico.py

- Ele herda todos os atributos e métodos da classe funcionario. 
- Modifico o método calcular salario

enfermeiro.py

- Ele herda todos os atributos e métodos da classe funcionario. 
- Modifico o método calcular salario

adicionar_dados.py

É o arquivo responsável por criar a planilha do excel, cajo não esteja criada e passar os dados inseridos na interface para essa planilha especificada.
- Possui o método criar_planilha(): cria uma nova planilha, uma nova folha (sheet), cria os títulos nas celulas e enm seguida salva a planilha.
- O método seguinte é o encontrar_ultima_linha_preenchida(sheet): consiste emu um laço de repetição for que analisa a folha (sheet) passado linha a linha para encontrar a última linha
preenchida.
- Por fim tem o método adicionar_dados(nome, idade, cargo, qtdHoras, valorHora): onde os dados são salvos, é passado o caminho para a planilha, utilzo um try except que tenta abrir a
planilha, caso não encontre gera a planilha, chama o método encontrar_ultima_linha_preenchida(sheet), usa o append para passar os valores e por fim salva as alterações feitas na
planilha.

interface.py

É o código mais longo, e consiste no desenvolvimento da interface gráfica do projeto. Utilizei Tkinter que é uma interface padrão em Python, a que mais tenho familiaridade.

- __init__() é o construtor inicial
- riando_widgets(self): É onde são criados os widgets (Label, Button), que são componentes visuais, os Frames, as telas.
- O método salvar_dados(self): que passa os dados para a planilha chamando o método adicionar_dados() e por fim chama o método para limpar os campos.
- Em seguida criei o método limpar_campos(self): que limpa os campos
- Por fim, temos o método que é calcular_salario(self): que dependendo da escolha do usuário entre "Médico" e "Enfermeiro" ele passa os dados para funcionario de acordo com o que foi
passado.

Projeto 2 -> Propriedade Rural

Ainda não está concluído.
