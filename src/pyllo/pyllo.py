import requests
from enum import Enum
import json


class LabelColor(Enum):
    YELLOW = 'yellow'
    PURPLE = 'purple'
    BLUE = 'blue'
    RED = 'red'
    GREEN = 'green'
    ORANGE = 'orange'
    BLACK = 'black'
    SKY = 'sky'
    PINK = 'pink'
    LIME = 'lime'


class Pyllo(object):
    URL_BASE = 'https://api.trello.com/1{}'

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def create_board(self, name):
        return requests.post(self.URL_BASE.format('/boards'),
                             params={
                                 'name': name,
                                 'key': self.key,
                                 'token': self.token,
                                 'defaultLists': 'false'
                             })

    def create_board_from_template(self, name, template_name):
        return json.loads(requests.post(self.URL_BASE.format('/boards'),
                          params={
                              'name': name,
                              'idBoardSource': self.get_board_id(template_name),
                              'key': self.key,
                              'token': self.token,
                              'defaultLists': 'false',
                              'defaultLabels': 'false'
                          }).text)['id']

    def create_list(self, board_id, name, index):
        return requests.post(self.URL_BASE.format('/boards/{}/lists?name={}').format(board_id, name),
                             params={
                                 'key': self.key,
                                 'token': self.token,
                                 'pos': index
                             })

    def create_card(self, list_id, title, labels=''):
        return requests.post(self.URL_BASE.format('/cards'),
                             params={
                                 'key': self.key,
                                 'token': self.token,
                                 'idList': list_id,
                                 'name': title,
                                 'pos': 'bottom',
                                 'idLabels': labels
                             })

    def create_label(self, name, board_id, label_color):
        return requests.post(self.URL_BASE.format('/labels'),
                             params={
                                 'key': self.key,
                                 'token': self.token,
                                 'name': name,
                                 'color': label_color.value,
                                 'idBoard': board_id
                             })

    def get_labels(self, board_id):
        labels = json.loads(requests.get(self.URL_BASE.format('/boards/{}/labels'.format(board_id)),
                                         params={
                                             'key': self.key,
                                             'token': self.token,
                                             'fields': 'name'
                                         }).text)
        return {label['name']: label['id'] for label in labels}

    def remove_labels(self, card_id):
        labels = json.loads(requests.get(self.URL_BASE.format('/cards/{}/labels'.format(card_id)),
                            params={
                                'key': self.key,
                                'token': self.token
                            }).text)
        return [
            requests.delete(self.URL_BASE.format('/cards/{}/idLabels/{}'.format(card_id, label['id'])),
                            params={
                                'key': self.key,
                                'token': self.token
                            })
            for label in labels
            ]

    def get_lists(self, board_name):
        response = json.loads(requests.get(self.URL_BASE.format('/members/me/boards?fields=id,name&lists=all'),
                                           params={
                                               'key': self.key,
                                               'token': self.token
                                           }).text)

        return [board['lists'] for board in response if board['name'] == board_name][0]

    def get_list_id(self, board_id, list_name):
        response = json.loads(requests.get(self.URL_BASE.format('/boards/{}/lists?fields=id,name'.format(board_id)),
                                           params={
                                               'key': self.key,
                                               'token': self.token
                                           }).text)
        return [a_list['id'] for a_list in response if a_list['name'] == list_name]

    def get_board_id(self, name):
        response = json.loads(requests.get(self.URL_BASE.format('/members/me/boards?fields=id,name'),
                                           params={
                                               'key': self.key,
                                               'token': self.token
                                           }).text)
        return [board['id'] for board in response if board['name'] == name][0]

    def get_cards(self, list_id):
        return json.loads(
            requests.get(self.URL_BASE.format('/lists/{}/cards?&fields=id,name,labels'.format(list_id)),
                         params={
                             'key': self.key,
                             'token': self.token
                         }).text
        )

    def delete_card(self, card_id):
        return json.loads(
            requests.delete(self.URL_BASE.format('/cards/{}'.format(card_id)),
                            params={
                                'key': self.key,
                                'token': self.token
                            }).text
        )
