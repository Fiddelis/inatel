from database import Database
from game_database import GameDatabase

db = Database('neo4j+s://94edaa4a.databases.neo4j.io', 'neo4j', 'rlz79wWyU1w3RqQsLW4Kr_ypFm2RaqooSYs1-4jcX8o')

db.drop_all()

game_db = GameDatabase(db)

game_db.create_player("Player1")
game_db.create_player("Player2")

game_db.create_match([("Player1", 100), ("Player2", 500)])
game_db.create_match([("Player1", 200), ("Player2", 400)])
game_db.create_match([("Player1", 300), ("Player2", 300)])
game_db.create_match([("Player1", 400), ("Player2", 200)])
game_db.create_match([("Player1", 500), ("Player2", 100)])

print(game_db.get_players())
print(game_db.get_match(2))
print(game_db.get_player_hist(0))

db.close()