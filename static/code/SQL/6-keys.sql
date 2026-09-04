-- -------------------- Keys --------------------
 

-- Primary Key
--
-- It is a column (or a set of columns) in a table that uniquely identifies each row in that table. (a unique id)
-- There is only 1 primary key in a table and it should not be NULL.



-- Foreign Key
--
-- A foreign key is a column (or a set of columns) in a table tha refers to th eprimary key of another table.
-- There can be multiple Foreign keys in a table. These can be duplicate and NULL.



------------------------- Example -------------------------

--             students Table                                      city Table           
--
--   | id   |  name     | cityid |  city  |                  |  id    | city_name |
--   | ---- | --------- | ------ |  ----  |                  | ------ | --------- |
--   | 101  | soymadip  |   1    |  Pune  |                  |   1    |  Pune     |
--   | 102  | sonaii    |   1    |  Pune  |                  |   2    |  Delhi    |
--   | 103  | google    |   2    |  Delhi |                  |   3    |  Mumbai   |


-- In above tables,
-- cityid in students table is a foreign key that refers to primary key id in city table. 
-- This means that each student belongs to a city, and the cityid column in the students table is used to link each student to their corresponding city in the city table.

