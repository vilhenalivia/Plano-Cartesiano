<h1>Verificador de Quadrantes Cartesianos</h1>

<h3>Descrição:</h3>

Este programa em Python tem como objetivo determinar em qual quadrante do plano cartesiano um ponto se encontra, dadas as coordenadas X e Y inseridas pelo usuário.
<br>
<br>
OBS: Exercício de prática do curso "Python: crie sua primeira aplicação" da plataforma Alura
<br>
<h3>Funcionalidades:</h3>
<b>Entrada:</b>  Solicita ao usuário os valores das coordenadas X e Y.
<br>
<br>
<b>Processamento:</b> Verifica as condições para cada quadrante e a origem.
<br>
<br>
<b>Saída:</b> Imprime na tela o quadrante em que o ponto está localizado ou indica que o ponto está sobre um dos eixos ou na origem.
<br>
<h3>Como usar:</h3>
<b>Executar o programa:</b> Execute o arquivo Python (por exemplo, verificador_quadrantes.py) em seu ambiente de desenvolvimento Python.
<br>
<br>
<b>Inserir coordenadas:</b> Digite os valores de X e Y quando solicitados.
<br>
<br>
<b>Verificar resultado:</b> O programa exibirá o quadrante correspondente ou a informação sobre a localização do ponto.

<h3>Explicação do código:</h3>

O código utiliza estruturas condicionais (if, elif, else) para verificar os sinais das coordenadas X e Y e determinar o quadrante correspondente.
<br>
<br>
<b>Primeiro quadrante:</b> X > 0 e Y > 0
<br>
<b>Segundo quadrante:</b> X < 0 e Y > 0
<br>
<b>Terceiro quadrante:</b> X < 0 e Y < 0
<br>
<b>Quarto quadrante:</b> X > 0 e Y < 0
<br>
<br>
<b>Eixos ou origem:</b> Se nenhuma das condições acima for verdadeira, o ponto está em um dos eixos ou na origem.

<h3>Observações:</h3>

<b>Tipos de dados:</b> As entradas são convertidas para números de ponto flutuante (float) para permitir valores decimais.
<br>
<br>
<b>Mensagens de saída:</b> As mensagens são claras e concisas, facilitando a compreensão do resultado.
