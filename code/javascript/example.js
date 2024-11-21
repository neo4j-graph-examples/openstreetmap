// npm install --save neo4j-driver
// node example.js
const neo4j = require('neo4j-driver');
const driver = neo4j.driver('neo4j://<HOST>:<BOLTPORT>',
                  neo4j.auth.basic('<USERNAME>', '<PASSWORD>'), 
                  {/* encrypted: 'ENCRYPTION_OFF' */});

const query =
  `
  MATCH (p1:PointOfInterest {type:$type}), (p2:PointOfInterest)
  WHERE p1<>p2 AND distance(p1.location,p2.location) < 200
  RETURN p2.name as name
  `;

const params = {"type": "clock"};

const session = driver.session({database:"neo4j"});

session.run(query, params)
  .then((result) => {
    result.records.forEach((record) => {
        console.log(record.get('name'));
    });
    session.close();
    driver.close();
  })
  .catch((error) => {
    console.error(error);
  });
