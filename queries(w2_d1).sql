# Single JOIN example
SELECT 
    title, title_id
FROM
    titles AS title
        LEFT JOIN
    titleauthor AS author ON title_id = title_id;
    
# Books with author but title is duplicated due to JOIN
SELECT 
    t.title, t.title_id, a.au_id, CONCAT(au.au_fname, ' ', au.au_lname) as completename
FROM
    titles AS t
	LEFT JOIN titleauthor AS a
		ON t.title_id = a.title_id
    LEFT JOIN authors AS au
		ON a.au_id = au.au_id;
    
# Books with complete author names and year, title duplication is removed with GROUP BY
SELECT 
		title, 
        year(max(pubdate)) as "year",
        count(titleauthor.title_id) as numautores,
        group_concat(concat(authors.au_fname,' ', authors.au_lname))
	FROM titles
	LEFT JOIN titleauthor
		ON titles.title_id = titleauthor.title_id
	LEFT JOIN authors
		ON authors.au_id = titleauthor.au_id
    GROUP BY titles.title
    ORDER BY numautores DESC;


