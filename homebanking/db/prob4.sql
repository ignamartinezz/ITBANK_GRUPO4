-- select count(customer_id)
-- from customer
--     left join sucursal on customer.branch_id = sucursal.branch_id
-- where sucursal.branch_name = 'tuvieja'
-- order by ;


-- Primer punto 
SELECT COUNT(customer_id) FROM cliente
    LEFT JOIN sucursal ON customer.branch_id = sucursal.branch_id
    WHERE sucursal.branch_name IS NOT NULL;
