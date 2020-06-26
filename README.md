# *Use a Cabeça! Aprenda a Programar*

[toc]

Programas gerados durante o aprendizado de programação com base no livro *Use a Cabeça! Aprenda a Programar*.
 Esse repositório contém todos os exercícios em Python organizados nos capítulos de 1 a 12. 

Os capítulos estão nomeados de acordo com o projeto de cada capítulo,  desde os mais simples, como o 'Hello World' do capítulo 1 até o complexo 'Jogo da Vida' do capítulo 11. 

## Os capítulos

###  *Print*, *if* ,*while*, e *booleanos*

#### Capítulo 1: Hello World

Nesse capítulo foram aprendidos conceitos básicos de ciência da computação, a saber, o desenvolvimento de a aplicação do pensamento computacional mediante o desenvolvimento de um pseudocódigo, sua passagem para o código, uma visão geral de linguagens de alto e baixo nível e a instalação do **Python**, que é a linguagem utilizada pelo livro.

[rock.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/HelloWorld/rock.py): Primeira linha de código escrita em *Python*, que usa a função *print* para exibir a frase *You rock*.

[frase.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/HelloWorld/rock.py): Programa que gera frases aleatórias.



#### Capítulo 2: Calculadora Canina

Nesse capítulo, foram aprendidos os conceitos de input e output, o funcionamento das variáveis, a procedência das operações matemáticas e o *statement* **if**. 

[calculadoracanina.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/CalculadoraCanina/calcudadoracanina.py): Recebe um input com a idade do cachorro e calcula sua idade em anos humanos.

[firstlast.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/CalculadoraCanina/firstlast.py): Exercício de inverter o valor de variáveis.

[imc.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/CalculadoraCanina/imc.py): Com o mesmo funcionamento da calculadora canina, esse programa calcula o [Índice de Massa Corporal]([https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal](https://pt.wikipedia.org/wiki/Índice_de_massa_corporal)) do usuário a partir da massa e da altura.

[rascunho.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/CalculadoraCanina/rascunho.py): Rascunho de um exercício do capítulo. 



#### Capítulo 3: Pedra, papel, tesoura

Com base no aprendizado do controlador de fluxo **while** e no uso do módulo **random**, criou-se um jogo no qual o jogador insere uma das três opções (pedra, papel ou tesoura) e o computador, já tendo em mente uma escolha própria, fornece o resultado.

[pedrapapeltesoura.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/PedraPapelTesoura/pedrapapeltesoura.py): Jogo de pedra, papel ou tesoura em que se coleta informações do usuário, compara-se com a escolha prévia do computador e depois gera-se o resultado.

[cores.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/PedraPapelTesoura/cores.py): Jogo em que o computador escolhe uma cor e o jogador deve adivinhar qual é. Ao final, é exibido o número de tentativas.



### Listas, iteração, loop for, *bubble sort* e funções

 #### Capítulo 4: Listas e iteração

Do aprendizado deste capítulo destacam-se os conceitos de **listas**, listas paralelas e a **iteração** com base no *loop* **for**.  Também foi aprendido como se referir a determinados itens da lista. Na segunda parte do capítulo, aprendi o funcionamento do **bubble sort** e, ao fim, da função **sort**, já incorporada no **Python**.

[bubbles_r_us.py]([https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/Itera%C3%A7%C3%A3oeListas/bubbles_r_us.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/IteraçãoeListas/bubbles_r_us.py)): Ainda sem conhecer o loop *for*, realizei a iteração da lista com o loop *while*.

[bubbles_r_us(for).py]([https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/Itera%C3%A7%C3%A3oeListas/bubbles_r_us(for).py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/IteraçãoeListas/bubbles_r_us(for).py)): Com o uso do loop for, o arquivo itera sobre duas listas paralelas, uma indicando o número de bolhas de uma solução e a outra indicando o custo destas soluções. Cria-se uma lista com cada solução e seu custo. Também utiliza-se do bubble sort para determinar as soluções mais eficientes e reordená-las da mais para a menos eficiente.

[fibonacci.py]([https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/Itera%C3%A7%C3%A3oeListas/fibonacci.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/IteraçãoeListas/fibonacci.py)): Usando **apenas** dos conceitos de listas e iteração, criei, para testar meus conhecimentos, uma calculadora de números da sequência de Fibonacci.

[has_coconut.py]([https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/Itera%C3%A7%C3%A3oeListas/has_coconut.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/IteraçãoeListas/has_coconut.py)): Com duas listas paralelas, uma de smoothies e outra de booleanos, o programa determina se determinada bebida (smoothie) tem ou não coco (coconut).

[loop_sim_e_nao.py]([https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/Itera%C3%A7%C3%A3oeListas/loop_sim_e_nao.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/IteraçãoeListas/loop_sim_e_nao.py)): Cria aleatoriamente 999 respostas variando entre 'sim' e 'não'.

[smoothies.py]([https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/Itera%C3%A7%C3%A3oeListas/smoothies.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/IteraçãoeListas/smoothies.py)): Prática de manipulação de listas.



#### Capítulo 5: Funções 

Nesse capítulo aprendi a refatorar códigos com o uso de **funções**, bem como o escopo de variáveis globais e locais, o que são **parâmetros**, entre outras coisas. 

[auau.py]([https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/Fun%C3%A7%C3%B5es/auau.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/Funções/auau.py)): Define uma função que, a partir dos parâmetros peso e nome exibe o latido de um cachorro.

[dogs.py]([https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/Fun%C3%A7%C3%B5es/dogs.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/Funções/dogs.py)): Ainda sem o conhecimento de funções, cria-se duas listas paralelas que contêm, respectivamente, o nome dos cachorros e seu peso para, a partir disso, definir seu latido.

[how_get_there.py]([https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/tree/master/Code/Fun%C3%A7%C3%B5es](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/tree/master/Code/Funções)): Define uma função que, a partir de uma distância, define qual é o melhor modo de se chegar ao destino.

[definindo_avatares.py]([https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/Fun%C3%A7%C3%B5es/definindo_avatares.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/Funções/definindo_avatares.py)): Recebe como parâmetros as características de um avatar, como cor do cabelo, cor dos olhos, sexo, presença de óculos ou barba e exibe mensagens com base nas escolhas do usuário.



#### Capítulo 6: Índice de legibilidade Flesch

Para reunir todos os conceitos dos capítulos anteriores, desenvolveu-se um programa que analisa o [Índice de Legibilidade Flesch-Kincaid](https://pt.wikipedia.org/wiki/Legibilidade_de_Flesch) de um texto e seu respectivo grau de entendimento para pessoas de certa escolaridade. Resumidamente, esse Índice calcula a facilidade de leitura de um texto e se esse texto poderia ser entendido por alunos de 11 anos que cursam o 7º ano do Ensino Fundamental ou se é um texto que só poderia ser compreendido por alunos da Graduados.

[compute_readability.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/IndicadordeLegibilidadeFlesch/compute_readabillity.py): Importa o módulo [chomsky.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/IndicadordeLegibilidadeFlesch/chomsky.py), que contêm um texto de Noam Chomsky, para, a partir da contagem do número de sílabas, palavras e frases, calcular o Índice de Legibilidade Flesch-Kincaid daquele texto.

[just_a_module.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/IndicadordeLegibilidadeFlesch/just_a_module.py): Programa que, quando é o código *main*, exibe a frase: "Eu sou a main", e quando é um módulo de outro exibe a frase: "Sou só um módulo".

[main.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/IndicadordeLegibilidadeFlesch/main.py): Exibe na tela "Saudações da main" quando este é o módulo main

### Objetos, recursão e dicionários

#### Capítulo 7: A corrida de Turtles

Com uma introdução aos **objetos**, seus atributos e métodos, o capítulo se utilizou das  turtles do Python para criar uma corrida de tartarugas, na qual tartarugas de várias cores distintas correm em uma pista.

[analyze.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/CorridadeTartarugas/analyze.py): Este programa é o mesmo do capítulo passado, porém com *Docstrings* e explicações.

[cory_analyze.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/CorridadeTartarugas/cory_analyze.py): Importa o módulo *analyze.py* para analisar um texto.

[turtle_run.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/CorridadeTartarugas/turtle_run.py): Código que cria 5 *turtles* de cores distintas e, a partir do módulo *random* define a movimentação delas. Ao final, é exibida na tela uma mensagem com o nome da vencedora. 



#### Capítulo 8: Fibonacci e Fractais

Nesse capítulo aprendi a usar o **método recursivo**, criando um caso base e um caso recursivo para a resolução de problemas como  o cálculo da sequência de Fibonacci. Contudo, para que isso fosse possível, também foi preciso aprender a utilizar **dicionários** para armazenar valores e tornar o programa exponencialmente mais eficiente.

[palindromo.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/FibonaccieFractais/palindromo.py): Determinando quais palavras são palíndromos a partir de métodos simples de manipulação de strings.

[palindromo_recursao.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/FibonaccieFractais/palindromo_recursao.py): Mediante os conceitos de recursão, criou-se um programa que determina quais palavras são palíndromos.

[soma_recursiva.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/FibonaccieFractais/soma_recursiva.py): Somando recursivamente os itens de uma lista

[dicionario.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/FibonaccieFractais/dicionario.py): Criando um programa que utiliza de um dicionário para armazenar os dados de vários usuários e, a partir do número de amigos de cada um deles, definir quem é o usuário mais antissocial.

[fractais.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/FibonaccieFractais/fractais.py): Com os conceitos de turtles e recursão, o código cria fractais na tela

[fibonacci_recursao.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/FibonaccieFractais/fibonacci_recursao.py): Código que associa conceitos de dicionários e recursão para criar um programa mais efetivo que calcula os números da sequência de Fibonacci.



#### Capítulo 9: Crazy Libs

Aprendendo a utilizar as funções open() e close() do Python, bem como a ler e a escrever em arquivos, seja a partir de seu path absoluto ou relativo, criei um jogo que  lê um arquivo com um texto e, com base no input fornecido pelo usuário, gera um novo arquivo de texto com frases absurdas e muito engraçadas.

[crazy_lib.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/CrazyLibs/crazy_lib.py): Programa que abre *lib.txt* para identificar palavras em caixa alta e substituí-las por input do usuário, posteriormente editando o arquivo *crazy_lib.txt*, no qual é inserido o texto com  as palavras já substituídas.



### Web API, GUI e Classes de objetos

#### Capítulo 10: Mapa da ISS

Utilizando dos conceitos de API e com o uso do JSON, captei as informações referentes à localização da Estação Espacial Internacional (ISS, em inglês), criando uma janela com turtles que indica, precisamente, a posição da ISS.

[london.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/MapadaISS/london.py): Usa dicionários para determinar a temperatura em Londres.

[ISS.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/MapadaISS/ISS.py): Captura a API da Estação Espacial Internacional (*International Space Station*, em inglês) para, com a utilização do JSON e do módulo requests, obter a localização, em tempo real, da *ISS*. Importando os turtles e utilizando o arquivo *earth.gif*, cria uma tela cujo fundo é o mapa do planeta. E, a partir do arquivo *iss.gif*, exibe na tela a Estação Espacial, com sua localização sendo atualizada em tempo real.



#### Capítulo 11: Jogo da Vida

Nesse capítulo criei uma interface de usuário que contém o [Jogo da Vida](https://pt.wikipedia.org/wiki/Jogo_da_vida), desenvolvido pelo matemático britânico John Horton Conway que simula vida artificial com base em quatro regras simples:

1. Se uma célula tem menos de duas células vizinhas, ela morre de solidão
2. Se uma célula tem mais de 3 células vizinhas, ela morre de superpopulação
3. Se uma célula viva tem 2 ou 3 vizinhas, ela continua viva
4. Se uma célula morta tem exatamente 3 vizinhas, ela vive

A partir da criação de uma matriz quadrada que contém os seres vivos e uma interface que permite que o usuário clique na tela para matar ou reviver uma célula, bem como escolher um padrão já determinado de disposição de seres.

[model.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/JogodaVida/model.py): É o programa que processa os dados do funcionamento da grade de células. Construindo uma matriz quadrada 100 x 100, cria uma grade de 10000 células, inicialmente mortas. 

[root.py](https://github.com/DaviNakamuraCardoso/Use-a-Cabeca-Aprenda-a-Programar/blob/master/Code/JogodaVida/root.py): A partir do módulo Tkinter, cria uma Interface Gráfica de Usuário (*Graphical User Interface*, em inglês) com as células. O usuário pode optar por três opções de grade inicial: Random (aleatória), Glider e Glider Gun. Ou também pode clicar na tela e criar a sua própria. Uma vez que o botão Start é pressionado, começa a interação, que é processada pelo módulo importado *root.py*, e é possível Pausar essa interação. Também há como reiniciar a grade, clicando no botão Clear.



#### Capítulo 12: Hotel para Cachorros com Objetos

Criando classes de objetos, primeiramente a superclasse *Dog* (Cachorro) e posteriormente as subclasses, *Service Dog* (Cão guia), sendo que o método *bark* da classe *Dog* foi sobrescrito na para os cães-guia, para que eles não latissem em serviço, *Frisbee Dog* (Cão de Frisbee), criamos uma classe Hotel, operada por *Dog Walkers*, que herdam suas características da classe *Person* (pessoa). Esse hotel aceita apenas membros da classe *Dog*, e têm certos métodos, como a hora de latir e a hora de passear.

