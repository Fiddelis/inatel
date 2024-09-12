from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

def get_engineer(tx):
    query = """
        MATCH(n:Engenheiro) RETURN n.nome AS engineer;
    """
    try:
        result = tx.run(query)
        return [row['engineer'] for row in result]

    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

def get_father_from(tx, entity):
    query = """
        MATCH ({nome:"$entity"})-[:PAI_DE]->(p) RETURN p.nome As father_from;
    """
    try:
        result = tx.run(query.replace("$entity", entity))
        return [row['father_from'] for row in result]

    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

def get_husband_since(tx, entity):
    query = """
        MATCH ({nome:"$entity"})-[e:ESPOSO_DE]->(p)
        RETURN e.desde AS data, p.nome AS nome;
    """
    try:
        result = tx.run(query.replace("$entity", entity))
        return [f"O esposo de {entity} é {row['nome']} desde {row['data']}" for row in result]

    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise


uri = ""
user = ""
password = ""

driver = GraphDatabase.driver(uri, auth=(user, password))

while True:
    print("\n1 - Quem é o Engenheiro?")
    print("2 - É pai de quem?")
    print("3 - É casado com quem? desde quando?")
    x = input()

    if x == '1':
        with driver.session() as session:
            result = session.execute_read(get_engineer)
            print(result)
    elif x == '2':
        entity = input("Nome do pai: ")
        with driver.session() as session:
            result = session.execute_read(get_father_from, entity)
            print(result)
    elif x == '3':
        entity = input("Nome da pessoa: ")
        with driver.session() as session:
            result = session.execute_read(get_husband_since, entity)
            print(result)
    else:
        break

driver.close()