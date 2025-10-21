from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Datos de ejemplo
usuarios = [
    {"id": 1, "nombre": "Juan Pérez", "email": "juan@example.com"},
    {"id": 2, "nombre": "Ana Gómez", "email": "ana@example.com"}
]

class Usuario(Resource):
    def get(self, usuario_id):
        usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
        if usuario:
            return jsonify(usuario)
        return {"mensaje": "Usuario no encontrado"}, 404

    def put(self, usuario_id):
        usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
        if usuario:
            data = request.get_json()
            usuario.update(data)
            return jsonify(usuario)
        return {"mensaje": "Usuario no encontrado"}, 404

    def delete(self, usuario_id):
        global usuarios
        usuarios = [u for u in usuarios if u["id"] != usuario_id]
        return {"mensaje": "Usuario eliminado"}

class UsuarioLista(Resource):
    def get(self):
        return jsonify(usuarios)

    def post(self):
        data = request.get_json()
        nuevo_id = max(u["id"] for u in usuarios) + 1 if usuarios else 1
        nuevo_usuario = {"id": nuevo_id, **data}
        usuarios.append(nuevo_usuario)
        return jsonify(nuevo_usuario)

api.add_resource(UsuarioLista, "/usuarios")
api.add_resource(Usuario, "/usuarios/<int:usuario_id>")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
