### 16homework - Django Web Framework



```sqlite
CREATE TABLE friends(id INTEGER, name TEXT, location TEXT);

INSERT INTO friends(id, name, location) VALUES (1, "Justin","Seoul");
INSERT INTO friends(id, name, location) VALUES (2, "Simon","New York");  
INSERT INTO friends(id, name, location) VALUES (3, "Chang","Las Vegas");    
INSERT INTO friends(id, name, location) VALUES (4, "John","Sydney");

ALTER TABLE friends ADD married INTEGER;

UPDATE friends SET married=1 WHERE id=1;
UPDATE friends SET married=0 WHERE id=2;                           UPDATE friends SET married=0 WHERE id=3;
UPDATE friends SET married=1 WHERE id=4;

DELETE FROM friends WHERE married=0;

DROP TABLE friends;
```

