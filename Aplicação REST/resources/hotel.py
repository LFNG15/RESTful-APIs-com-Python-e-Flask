from flask_restful import Resource, reqparse
from models.hotel import HotelModel

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

class HotelModel:
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return{
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'diaria': self.diaria,
            'cidade': self.cidade
        }

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome')
    atributos.add_argument('estrelas')
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return False

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Hotel not found.'}, 404

    def post(self, hotel_id):
        dados = Hotel.atributos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        #novo_hotel =    {'hotel_id': hotel_id, **dados}
        hoteis.append(novo_hotel)
        return novo_hotel, 201
    
    def put(self, hotel_id):
        dados = Hotel.atributos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        #novo_hotel =    {'hotel_id': hotel_id, **dados}
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted.'}
