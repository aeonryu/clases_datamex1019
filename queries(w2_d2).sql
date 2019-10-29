

select stores.stor_name as store,
count(distinct(ord_num)) as orders,
count(title_id) as items, sum(qty) as qty
from publications.sales sales 
inner join publications.stores stores
on stores.stor_id=sales.stor_id
group by store;




























