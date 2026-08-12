### To find circular dependencies in a pg database

```SQL
WITH temp AS (
	SELECT 
		conname,
		conrelid::regclass AS table_name,
		confrelid::regclass AS referenced_table 
	FROM pg_constraint 
	WHERE contype = 'f'
)

SELECT * FROM temp AS t 
WHERE EXISTS (
	SELECT 1
	FROM temp AS tt
	WHERE
		tt.table_name = t.referenced_table
		AND tt.referenced_table = t.table_name
);
```

