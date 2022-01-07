### Aşağıdaki sorgu senaryolarını dvdrental örnek veri tabanı üzerinden gerçekleştiriniz.

#### 1. film tablosunda bulunan ve film ismi (title) 'n' karakteri ile biten en uzun (length) 5 filmi sıralayınız.
#### 2. film tablosunda bulunan ve film ismi (title) 'n' karakteri ile biten en kısa (length) ikinci(6,7,8,9,10) 5 filmi(6,7,8,9,10) sıralayınız.
#### 3. customer tablosunda bulunan last_name sütununa göre azalan yapılan sıralamada store_id 1 olmak koşuluyla ilk 4 veriyi sıralayınız.

SELECT title FROM film WHERE title LIKE '%n' ORDER BY length(title) DESC LIMIT 5;

SELECT title FROM film WHERE title LIKE '%n' ORDER BY length(title) ASC LIMIT 5 OFFSET 5;

SELECT * FROM customer WHERE store_id = 1 ORDER BY last_name LIMIT 4;