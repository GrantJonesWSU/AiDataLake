-- SQLite
-- Use this to fill the TrainingCorpus table with useful examples to train GPT-3 for SQL output

-- query 1
INSERT INTO TrainingCorpus (inputText, outputText)
VALUES ("Find customers who have returned items more than 20% more often than the average customer returns for a store in TN in 2001.", "WITH customer_total_return 
     AS (SELECT sr_customer_sk     AS ctr_customer_sk, 
                sr_store_sk        AS ctr_store_sk, 
                Sum(sr_return_amt) AS ctr_total_return 
         FROM   store_returns, 
                date_dim 
         WHERE  sr_returned_date_sk = d_date_sk 
                AND d_year = 2001 
         GROUP  BY sr_customer_sk, 
                   sr_store_sk) 
SELECT c_customer_id 
FROM   customer_total_return ctr1, 
       store, 
       customer 
WHERE  ctr1.ctr_total_return > (SELECT Avg(ctr_total_return) * 1.2 
                                FROM   customer_total_return ctr2 
                                WHERE  ctr1.ctr_store_sk = ctr2.ctr_store_sk) 
       AND s_store_sk = ctr1.ctr_store_sk 
       AND s_state = 'TN' 
       AND ctr1.ctr_customer_sk = c_customer_sk 
ORDER  BY c_customer_id
LIMIT 100;");

-- query 6
INSERT INTO TrainingCorpus (inputText, outputText)
VALUES("List all the states with at least 10 customers who during the month of July 1998 bought items with the price tag at least 20% higher than the average price of items in the same category.", "SELECT a.ca_state state, 
               Count(*)   cnt 
FROM   customer_address a, 
       customer c, 
       store_sales s, 
       date_dim d, 
       item i 
WHERE  a.ca_address_sk = c.c_current_addr_sk 
       AND c.c_customer_sk = s.ss_customer_sk 
       AND s.ss_sold_date_sk = d.d_date_sk 
       AND s.ss_item_sk = i.i_item_sk 
       AND d.d_month_seq = (SELECT DISTINCT ( d_month_seq ) 
                            FROM   date_dim 
                            WHERE  d_year = 1998 
                                   AND d_moy = 7) 
       AND i.i_current_price > 1.2 * (SELECT Avg(j.i_current_price) 
                                      FROM   item j 
                                      WHERE  j.i_category = i.i_category) 
GROUP  BY a.ca_state 
HAVING Count(*) >= 10 
ORDER  BY cnt
LIMIT 100;");