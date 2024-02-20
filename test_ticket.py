class Item:
    _prix: int
    nom: str

    def __init__(self, prix: int, nom: str) -> None:
        self.prix = prix
        self.nom = nom

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, value):
        if value <= 0:
            raise ValueError("prix doit être supérieur à 0")
        self._prix = value




class Ticket:
    def __init__(self) -> None:
        self.items = []

    @property
    def total(self):
        total = 0
        for item in self.items:
            total += item.prix
        return total

    def add(self, item: Item):
        self.items.append(item)

 
    # def test_remove_bad_item_index(self):
    #     tck = Ticket()
    #     item = Item(prix=1, nom="red bull")
    #     tck.add(item)
    #     assert tck.total == 1
    #     tck.remove(10)
    #     assert tck.total == 1
    def remove(self, item_index: int):
        #   [a, b, c, d, e, f] => len == 6
        #    0  1  2  3  4  5
        #   remove(6)                CASSE
        #   remove(0) ... remove(5)  OK
        if item_index < 0:
            raise ValueError("item index must be ...")
        if len(self.items) > 0 and item_index < len(self.items):
            self.items.pop(item_index)
        
        

import unittest

class TestTicket(unittest.TestCase):

    def test_add_one_item(self):
        tck = Ticket()
        item = Item(prix=1, nom="red bull")
        tck.add(item)

        assert len(tck.items) == 1
        assert tck.total == 1

    def test_add_two_items(self):
        tck = Ticket()
        item = Item(prix=1, nom="red bull")
        item2 = Item(prix=1, nom="monster")
        tck.add(item)
        tck.add(item2)
        assert len(tck.items) == 2
        assert tck.total == 2
    
    def test_remove_item(self):
        tck = Ticket()
        item = Item(prix=1, nom="red bull")
        tck.add(item)
        assert len(tck.items) == 1
        assert tck.items.pop(0) == item
        assert len(tck.items) == 0
        assert tck.total == 0
    
    def test_remove_item_not_init(self):
        tck = Ticket()
        assert len(tck.items) == 0
        tck.remove(0) # n’échoue pas même si la liste d’items est vide
        assert tck.total == 0
    
    def test_remove_item_init(self):
        tck = Ticket()
        item = Item(prix=1, nom="red bull")
        tck.add(item)
        assert tck.total == 1
        tck.remove(0)
        assert tck.total == 0

    def test_remove_negative_item(self):
        tck = Ticket()
        item = Item(prix=1, nom="red bull")
        tck.add(item)
        assert tck.total == 1
        with self.assertRaises(ValueError):
            tck.remove(-1)
        assert tck.total == 1
    
    def test_remove_bad_item_index(self):
        tck = Ticket()
        item = Item(prix=1, nom="red bull")
        tck.add(item)
        assert tck.total == 1
        tck.remove(10)
        assert tck.total == 1