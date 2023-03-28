Desafio back end etapa 3\
Aluno: Felipe da Silva Pereira Alves\
Matrícula: 2310995\
Api para criar personagens\
Instruções:
1. O programa que utilizei foi o 
pycharm, não sei se as bibliotecas
 que estão nesta pasta serão carregadas
 corretamente, portanto, caso dê algum 
erro relacionado a elas, segue a lista
contendo as biblliotecas necessárias para
 rodar os programas:\
-flask\
-flask_restful\
-flask_sqlalchemy\
-requests
2. O primeiro programa a ser executado
 é o "desafio3.py". Ao rodá-lo, será 
iniciado um servidor local, ao qual podem
 ser feitas requisições utilizando o script
 "requests_here.py"
3. Ao iniciar o servidor, um link será 
gerado, este link deve ser atribuído à 
variável BASE contida no script "requests_here.py".
4. As requisições possíveis são:\
-Get: solicita informações de determinado id\
-Put: adiciona informações a um id\
-Patch: atualiza informações do id desejado\
-Delete: deleta informações do id requerido
5. Essas informações são salvas ou deletadas
do arquivo "database.db".
6. Mais informações sobre como fazer cada
 tipo de requisição estão em formato de
 comentário no script "requests_here.py".

OBS.1: Não consegui encontrar um método
de fazer as requisições de put, patch e 
delete diretamente do navegador. Para usar
 o get diretamente por lá, basta copiar a
 url do servidor local, colá-la no navegador,
 adicionar "/characters/" + número de id. Ex.: 
"http://127.0.0.1:5000/characters/0"

OBS.2: Em todos os meus testes o link 
padrão gerado foi "http://127.0.0.1:5000"
 então já deixei pré-estabelecido no script
 "requests_here.py".

OBS.3: Eu aconselho executar o arquivo 
"desafio3.py" diretamente do prompt de 
comando, já que o arquivo "requests_here.py"
 deverá ser executado em conjunto a ele.
Para isso, se estiver usando um windows,
 é só abrir a pasta com esses arquivos, 
clicar na barra onde fica o endereço dessa 
pasta, digitar "cmd" e dar um enter. Se já
 possuir o python instalado, é só executar
 o comando "python desafio.py", se não 
possuir, este vídeo pode ajudar https://www.youtube.com/watch?v=0pG4NrucQR4

