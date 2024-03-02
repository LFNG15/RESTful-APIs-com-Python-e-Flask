from flask_restful import Resource, reqparse

hoteis = [
        {
            'hotel_id': 'alpha',
            'nome': 'Alpha Hotel',
            'estrelas': 3.2,
            'diaria': 220.30,
            'cidade': 'Seoul'
        },
        {
            'hotel_id': 'beta',
            'nome': 'Beta Hotel',
            'estrelas': 4.2,
            'diaria': 720.30,
            'cidade': 'Toquio'
        },
        {
            'hotel_id': 'LF',
            'nome': 'LF Hotel',
            'estrelas': 5,
            'diaria': 950.50,
            'cidade': 'Toquio'
        }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
    
class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
            return {'message': 'Hotel not found.'}, 404 #not found

    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')

        dados = argumentos.parse_args()

        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']
        }

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass