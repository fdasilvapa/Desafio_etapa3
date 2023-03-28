"""
-Após executar "desafio3.py", este é o script responsável
por fazer requisições.
-A variável BASE deve ser atualizada de acordo com o método
de execução escolhido para os testes:
1. Se estiver executando "desafio3.py" pelo prompt de comando
(recomendável), o link provavelmente será o que já está atribuído
à variável BASE, não necessitando mudanças;
2. Se estiver executando "desafio3.py" diretamente na ide,
o link provavelmente será http://127.0.0.1:5000 .
"""

import requests

BASE = "http://127.0.0.1:5000/"

"""
-A variável "data" recebe o que será adicionado usando a requisição put
-Está armazenado nela só para ficar mais fácil e organizado
-Basicamente ela já contém todos os argumentos necessários para esse 
tipo de requisição, seus valores podem ser alterados livremente, desde
que respeite a forma como estão dispostos e estejam em formato string,
já que são os parâmetros que o método no script "desafio3.py" aceita.
-Os 5 parâmetros nela contidos ('name', 'description', 'image_link',
'program' e 'animator') são obrigatórios para qualquer criação de 
personagem
"""
data = {"name":"felipe", "description":"a mage",
         "image_link":"imagelink.com", "program":"aseprite",
         "animator":"felipe"}


"""
-A requisição put adiciona informações a um id
- Como parâmetros devem ser passados a url do servidor + "characters/<id>" + 
informações a serem preenchidas
-O modelo da requisição está comentado abaixo, podendo ser adicionado
utilizando qualquer id e quaisquer informações, seguindo as regras citadas
anteriormente
-Para que sejam exibidas na tela, a conversão para o formato .json é necessária
"""
#response = requests.put(BASE + "characters/0", data)
#print(response.json())


"""
-A requisição get retorna as informações contidas em determinado
id, desde que elas existam na base de dados onde são salvas
-Como parâmetros devem ser passados a url + "characters/<id>"
-Segue abaixo o modelo
"""
#response = requests.get(BASE + "characters/0")
#print(response.json())


"""
-A requisição patch atualiza informações contidas em determinado id
-Os parâmetros a serem passados são url + "characters/<id>" , informação
modificada, seguindo o modelo abaixo
"""
#response = requests.patch(BASE + "characters/0", {"name":"lucas"})
#print(response.json())

"""
-A requisição delete apaga informações contidas em determinado id
-Os parâmetros a serem passados são os mesmos da requisição get, segue
abaixo o modelo
"""
#response = requests.delete(BASE + "characters/0")
#print(response)
