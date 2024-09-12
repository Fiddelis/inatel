from pokedex import Pokedex
from database import Database
from write_a_json import write_a_json

db = Database(database="pokedex", collection="pokemons")
pokedex = Pokedex(db)

db.resetDatabase()

name = "Dragonite"
pokedex.get_pokemon_by_name(name)

types = ["Psychic"]
pokedex.get_pokemons_by_types(types)

weaknesses = ["Ice", "Dragon", "Fairy"]
pokedex.get_pokemons_weaknesses_against(weaknesses)

pokedex.get_pokemons_with_two_weaknesses()

pokedex.get_pokemons_with_no_evolutions()