from src.ressie.unit import Unit as U
import json


class Ingredient(object):

    def __init__(self, name, amount, unit):
        self._name = name
        self._amount = amount
        self._unit = unit

    def to_dict(self):
        return {
            'name': self._name.value,
            'amount': self._amount,
            'unit': self._unit.value
        }

    @property
    def name(self):
        return self._name

    @property
    def amount(self):
        return self._amount

    @property
    def unit(self):
        return self._unit

    @staticmethod
    def from_dict(ingredient_dict):
        return Ingredient(ingredient_dict['name'], ingredient_dict['amount'], U(ingredient_dict['unit']))

    def __repr__(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return '{} {} of {}'.format(self._amount, self._unit.value, self._name)

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
