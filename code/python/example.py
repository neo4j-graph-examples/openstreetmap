# pip3 install neo4j
# python3 example.py

from neo4j import GraphDatabase, basic_auth

cypher_query = '''
MATCH (p1:PointOfInterest {type:$type}), (p2:PointOfInterest)
WHERE p1<>p2 AND distance(p1.location,p2.location) < 200
RETURN p2.name as name
'''

with GraphDatabase.driver(
    "neo4j://<HOST>:<BOLTPORT>",
    auth=("<USERNAME>", "<PASSWORD>")
) as driver:
    result = driver.execute_query(
        cypher_query,
        type="clock",
        database_="neo4j")
    for record in result.records:
        print(record['name'])
