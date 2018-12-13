--
-- Check Table schema, auto-increment id, index
--

USE `database_name`;

SHOW tables;

DESC `table_name`;

SHOW CREATE TABLE `table_name` \G;

--
-- Create temp table based on one month data
--
CREATE TABLE `month_1705` as
  select sender, receiver, content, receiver_time from `table_name`
    where  receiver_time >= '2017-05-01 00:00:01' and receiver_time < '2017-06-01 00:00:01';

