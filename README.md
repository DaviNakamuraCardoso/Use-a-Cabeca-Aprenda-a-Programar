# Use a Cabeca-Aprenda a Programar
 Programas gerados durante o aprendizado de programação com base no livro *Use a Cabeça! Aprenda a Programar*.
 Esse repositório contém todos os exercícios em Python organizados nos capítulos de 1 a 12. 

Os capítulos estão nomeados de acordo com o projeto de cada capítulos, desde os mais simples, como o 'Hello World' do capítulo 1 até o complexo 'Jogo da Vida' do capítulo 11. 

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



### Listas, iteração, loop for, *bubble sort* e funções

 #### Capítulo 4: Listas e iteração

Do aprendizado deste capítulo destacam-se os conceitos de **listas**, listas paralelas e a **iteração** com base no *loop* **for**.  Também foi aprendido como se referir a determinados itens da lista. Na segunda parte do capítulo, aprendi o funcionamento do **bubble sort** e, ao fim, da função **sort**, já incorporada no **Python**.



#### Capítulo 5: Funções 

Nesse capítulo aprendi a refatorar códigos com o uso de **funções**, bem como o escopo de variáveis globais e locais, o que são **parâmetros**, entre outras coisas. 



#### Capítulo 6: Índice de legibilidade Flesch

Para reunir todos os conceitos dos capítulos anteriores, desenvolveu-se um programa que analisa o [Índice de Legibilidade Flesch-Kincaid](https://pt.wikipedia.org/wiki/Legibilidade_de_Flesch) de um texto e seu respectivo grau de entendimento para pessoas de certa escolaridade. Resumidamente, esse Índice calcula a facilidade de leitura de um texto e se esse texto poderia ser entendido por alunos de 11 anos que cursam o 7º ano do Ensino Fundamental ou se é um texto que só poderia ser compreendido por alunos da Graduados.



### Objetos, recursão e dicionários

#### Capítulo 7: A corrida de Turtles

Com uma introdução aos **objetos**, seus atributos e métodos, o capítulo se utilizou das  turtles do Python para criar uma corrida de tartarugas, na qual tartarugas de várias cores distintas correm em uma pista.



#### Capítulo 8: Fibonacci e Fractais

Nesse capítulo aprendi a usar o **método recursivo**, criando um caso base e um caso recursivo para a resolução de problemas como  o cálculo da sequência de Fibonacci. Contudo, para que isso fosse possível, também foi preciso aprender a utilizar **dicionários** para armazenar valores e tornar o programa exponencialmente mais eficiente.



#### Capítulo 9: Crazy Libs

Aprendendo a utilizar as funções open() e close() do Python, bem como a ler e a escrever em arquivos, seja a partir de seu path absoluto ou relativo, criei um jogo que  lê um arquivo com um texto e, com base no input fornecido pelo usuário, gera um novo arquivo de texto com frases absurdas e muito engraçadas.



### Web API, GUI e Classes de objetos

#### Capítulo 10: Mapa da ISS

Utilizando dos conceitos de API e com o uso do JSON, captei as informações referentes à localização da Estação Espacial Internacional (ISS, em inglês), criando uma janela com turtles que indica, precisamente, a posição da ISS.



#### Capítulo 11: Jogo da Vida

Nesse capítulo criei uma interface de usuário que contém o [Jogo da Vida](https://pt.wikipedia.org/wiki/Jogo_da_vida), desenvolvido pelo matemático britânico John Horton Conway que simula vida artificial com base em quatro regras simples:

1. Se uma célula tem menos de duas células vizinhas, ela morre de solidão
2. Se uma célula tem mais de 3 células vizinhas, ela morre de superpopulação
3. Se uma célula viva tem 2 ou 3 vizinhas, ela continua viva
4. Se uma célula morta tem exatamente 3 vizinhas, ela vive

A partir da criação de uma matriz quadrada que contém os seres vivos e uma interface que permite que o usuário clique na tela para matar ou reviver uma célula, bem como escolher um padrão já determinado de disposição de seres.



#### Capítulo 12: Hotel para Cachorros com Objetos

Criando classes de objetos, primeiramente a superclasse *Dog* (Cachorro) e posteriormente as subclasses, *Service Dog* (Cão guia), sendo que o método *bark* da classe *Dog* foi sobrescrito na para os cães-guia, para que eles não latissem em serviço, *Frisbee Dog* (Cão de Frisbee), criamos uma classe Hotel, operada por *Dog Walkers*, que herdam suas características da classe *Person* (pessoa). Esse hotel aceita apenas membros da classe *Dog*, e têm certos métodos, como a hora de latir e a hora de passear.

