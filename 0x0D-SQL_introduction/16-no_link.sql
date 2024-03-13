-- Lists all records of the table `second_table` of the database hbtn_0c_0
-- Rows without a `name` value will not be listed
-- Results will be displayed by `score` and `name`, in that order
-- Records will be listed in descending order of `score`
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
