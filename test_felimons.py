import pytest
from unittest.mock import Mock
from main import Felimon, Deck


def test_felimon_creation():
    f = Felimon("Ignis Leo", "Fogo", 10, 5)
    assert f.name == "Ignis"


def test_battle_damage():
    attacker = Felimon("Sparky", "Trovão", 15, 5)
    defender = Felimon("Shadow Paw", "Psíquico", 8, 10)
    assert attacker.attack_target(defender) == 5


def test_deck_get_strongest():
    deck = Deck(owner_name="Chrystian")  # CORRIGIDO
    f1 = Felimon("Weak Cat", "Normal", 2, 2)
    f2 = Felimon("Strong Cat", "Fogo", 20, 10)
    deck.add_card(f1)
    deck.add_card(f2)
    assert deck.get_strongest() == f2


def test_get_strongest_empty_deck():
    deck = Deck(owner_name="Vazio")
    assert deck.get_strongest() is None


def test_get_magical_name_success(mocker):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'name': 'Nebula Whiskers'}
    mocker.patch('requests.get', return_value=mock_response)

    deck = Deck(owner_name="Mestre")
    name = deck.fetch_magical_name()
    assert name == "Nebula Whiskers"


def test_get_magical_name_failure(mocker):
    mocker.patch('requests.get', side_effect=Exception)
    deck = Deck(owner_name="Offline")
    name = deck.fetch_magical_name()
    assert name == "Gato Misterioso"