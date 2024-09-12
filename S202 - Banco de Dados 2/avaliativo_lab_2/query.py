from database import Database

db = Database('neo4j+s://94edaa4a.databases.neo4j.io', 'neo4j', 'rlz79wWyU1w3RqQsLW4Kr_ypFm2RaqooSYs1-4jcX8o')
db.reset_db()


query = 'MATCH (t:Teacher {name: $name}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf;'
parameters = {"name": "Renzo"}
resutls = db.execute_query(query, parameters)

ano_nasc, cpf = resutls[0]['ano_nasc'], resutls[0]['cpf']

print('Questão 01\n')
print(f'{query}')
print(f'\tano_nasc: {ano_nasc}')
print(f'\tcpf: {cpf}')

query = 'MATCH (t:Teacher) WHERE t.name STARTS WITH "M" RETURN t.name AS name, t.cpf AS cpf;'
results = [
    {
        'name': row['name'],
        'cpf': row['cpf']
    }
    for row in db.execute_query(query)
]

print(f'{query}')
for row in results:
    for key, value in row.items():
        print(f'\t{key}: {value}')

query = 'MATCH (c:City) RETURN c.name AS name;'
results = [r['name'] for r in db.execute_query(query)]

print(f'{query}')
for i in results:
    print(f'\t{i}')

query = 'MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS name, s.address AS address;'
results = [
    {
        'name': row['name'],
        'address': row['address']
    }
    for row in db.execute_query(query)
]

print(f'{query}')
for row in results:
    for key, value in row.items():
        print(f'\t{key}: {value}')

print('\n\nQuestão 02')

query = 'MATCH (t:Teacher) RETURN min(t.ano_nasc) AS velho_ano_nasc, max(t.ano_nasc) AS novo_ano_nasc;'
velho_ano_nasc, novo_ano_nasc = db.execute_query(query)[0]['velho_ano_nasc'], db.execute_query(query)[0]['novo_ano_nasc']

print(f'{query}')
print(f'\tMais jovem: {"novo_ano_nasc"}')
print(f'\tMais velho: {"velho_ano_nasc"}')

query = 'MATCH (c:City) RETURN avg(c.population) as media_pop;'
result = db.execute_query(query)[0]['media_pop']

print(f'{query}')
print(f'\tMédia: {result}')

query = 'MATCH (c:City {cep: "37540-000"}) RETURN replace(c.name, "a", "A") AS name_replaced;'
result = db.execute_query(query)[0]['name_replaced']

print(f'{query}')
print(f'\t{result}')

query = 'MATCH (n:Teacher) RETURN substring(n.name, 3, 1) AS letra_3;'
results = [result['letra_3'] for result in db.execute_query(query)]

print(f'{query}')
for result in results:
    print(f' {result}')
