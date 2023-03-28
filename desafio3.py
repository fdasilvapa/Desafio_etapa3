"""
Código criado seguindo as instruções do vídeo:
https://www.youtube.com/watch?v=GMppyAPbLYk
"""
from flask import Flask
from flask_restful import Api,Resource,reqparse,abort,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask("__name__")
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Classe modelo do que deve estar contido em um personagem
class CharacterModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    image_link = db.Column(db.String(150), nullable=False)
    program = db.Column(db.String(30), nullable=False)
    animator = db.Column(db.String(30), nullable=False)

    # Método contendo o que será retornado na tela
    def __repr__(self):
        return f"Character(Name = {name}, Description = {description}," \
               f" Image link = {image_link}, Program = {program}," \
               f" Animator = {animator})"


# Método para criar o arquivo .db
"""
IMPORTANTE: só é executado uma vez,
quando o arquivo .db já existe não é mais necessário
"""
#db.create_all()

# Controlador dos argumentos que devem ser passados para o método put
charac_put_args = reqparse.RequestParser()
charac_put_args.add_argument("name", type=str, help="Name of the character is required", required=True)
charac_put_args.add_argument("description", type=str, help="Description of the character is required", required=True)
charac_put_args.add_argument("image_link", type=str, help="Link for image is required", required=True)
charac_put_args.add_argument("program", type=str, help="Used program is required", required=True)
charac_put_args.add_argument("animator", type=str, help="Name of the animator is required", required=True)

# Controlador dos argumentos para o método update
charac_update_args = reqparse.RequestParser()
charac_update_args.add_argument("name", type=str)
charac_update_args.add_argument("description", type=str)
charac_update_args.add_argument("image_link", type=str)
charac_update_args.add_argument("program", type=str)
charac_update_args.add_argument("animator", type=str)

# Definindo como os parâmetros devem ser serializados
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'image_link': fields.String,
    'program': fields.String,
    'animator': fields.String
}

# Classe contendo os métodos que realizam os requests
class Character(Resource):

    @marshal_with(resource_fields)
    def get(self, charac_id):
        # Procurando o id requisitado no comando get
        result = CharacterModel.query.filter_by(id=charac_id).first()
        # Caso não exista, retorna um erro para o usuário
        if not result:
            abort(404, message="Could not find character with this id...")
        # Caso exista, retorna as informações disponíveis
        return result

    @marshal_with(resource_fields)
    def put(self, charac_id):
        # Variável recebendo o método que analisa os argumentos passados
        args = charac_put_args.parse_args()
        # Novamente checando o id requisitado
        result = CharacterModel.query.filter_by(id=charac_id).first()
        # Se já existe um personagem criado com esse id, retorna um erro para o usuário
        if result:
            abort(409, message="A character with this id already exists...")
        # Parâmetros que devem ser passados
        character = CharacterModel(id=charac_id, name=args['name'], description=args['description'],
                                  image_link=args['image_link'], program=args['program'], animator=args['animator']
                                  )
        # Métodos semelhantes aos comandos add e commit do git
        # Add "coloca na fila"
        db.session.add(character)
        # Commit adiciona à base de dados
        db.session.commit()

        return character, 201

    @marshal_with(resource_fields)
    def patch(self, charac_id):
        args = charac_update_args.parse_args()
        result = CharacterModel.query.filter_by(id=charac_id).first()
        if not result:
            abort(404, message="Character doesn't exist, cannot update...")

        # Atualizando informações com os parâmetros passados
        """
        O usuário pode atualizar somente um parâmetro se quiser,
        por isso há uma verificação separada para cada um deles,
        por ser mais simples, optei por não colocar em um loop,
        assim como foi feito no vídeo.
        """
        if args['name']:
            result.name = args['name']
        if args['description']:
            result.description = args['description']
        if args['image_link']:
            result.image_link = args['image_link']
        if args['program']:
            result.program = args['program']
        if args['animator']:
            result.animator = args['animator']

        # Por já existir o personagem, não é necessário o add
        db.session.commit()

        return result

    def delete(self, charac_id):
        CharacterModel.query.filter_by(id=charac_id).delete()
        db.session.commit()
        return '', 204

api.add_resource(Character, "/characters/<int:charac_id>")

if __name__ == "__main__":
    app.run()
