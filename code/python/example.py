# pip3 install neo4j-driver
# python3 example.py

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "bolt://<HOST>:<BOLTPORT>",
  auth=basic_auth("<USERNAME>", "<PASSWORD>"))

cypher_query = '''
MATCH (p1:PointOfInterest {type:$type}), (p2:PointOfInterest)
WHERE p1<>p2 AND distance(p1.location,p2.location) < 200
RETURN p2.name as name
'''

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
                      type="clock").data())
  for record in results:
    print(record['name'])

driver.close()
