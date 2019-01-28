### 16workshop - Django Web Framework



```sqlite
CREATE TABLE bands(id INTEGER, name TEXT, debut INTEGER);
INSERT INTO bands(id, name, debut)
   ...> VALUES(1, "Queen", 1973);
INSERT INTO bands(id, name, debut) VALUES (2,"Coldplay",1998);
INSERT INTO bands(id, name, debut) VALUES (3,"MCR",2001);
SELECT * FROM bands;

ALTER TABLE bands ADD members INTEGER;
UPDATE bands SET members=4 WHERE id=1;
UPDATE bands SET members=5 WHERE id=2;
UPDATE bands SET members=9 WHERE id=3;

UPDATE bands SET members=5 WHERE id=3;
DELETE FROM bands WHERE id=2;
```

