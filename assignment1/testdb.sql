CREATE TABLE US30(symbol char(20), price double precision, total_share double precision, p_e_ratio double precision, market_value double precision, total_profit double precision, PRIMARY KEY(symbol));


INSERT INTO US30(symbol, price, total_share, p_e_ratio)
VALUES
('MMM', 219.52, 5.97e+008, 27.68),
('AXP', 93.28, 9.15e+008, 31.41),
('AAPL', 167.78, 5.082e+009, 18.22),
('BA', 327.88, 5.96e+008, 24.41),
('CAT', 147.38, 5.91e+008, 116.97),
('CVX', 114.04, 1.899e+009, 23.51),
('CSCO', 42.89, 4.818e+009, 22.57),
('KO', 43.43, 4.264e+009, 149.76),
('DWDP', 63.71, 2.326e+009, 70.01),
('XOM', 74.61, 4.237e+009, 16.11),
('GE', 13.48, 8.846e+009, 11.52),
('GS', 251.86, 3.98e+008, 27.95),
('HD', 178.24, 1.157e+009, 24.45),
('IBM', 153.43, 9.66e+008, 24.99),
('INTC', 52.08, 4.68e+009, 26.17),
('JNJ', 128.15, 2.684e+009, 272.66),
('JPM', 109.97, 3.47e+009, 17.43),
('MCD', 156.38, 7.97e+008, 24.55),
('MRK', 54.47, 2.696e+009, 62.61),
('MSFT', 91.27, 7.715e+009, 33.68),
('NKE', 66.44, 1.627e+009, 26.47),
('PFE', 35.49, 5.961e+009, 10.08),
('PG', 79.28, 2.556e+009, 14.18),
('TRV', 138.86, 2.84e+008, 18.94),
('UNH', 214, 9.68e+008, 19.96),
('UTX', 125.82, 8.23e+008, 22.07),
('VZ', 47.82, 4.15e+009, 6.5),
('V', 119.62, 2.061e+009, 20.31),
('WMT', 88.97, 2.987e+009, 20.31),
('DIS', 100.44, 1.51e+009, 17.65);

UPDATE US30 SET market_value = price * total_share WHERE symbol IN (SELECT symbol FROM US30);

UPDATE US30 SET total_profit = market_value / p_e_ratio WHERE symbol IN (SELECT symbol FROM US30);

SELECT * FROM US30 ORDER BY market_value ASC;

SELECT * FROM US30 ORDER BY total_profit DESC;

SELECT * FROM US30 ORDER BY p_e_ratio DESC LIMIT 3;




SELECT SUM(price) FROM US30;

3500.59 / 0.145235;


CREATE FUNCTION DJIA(dow double precision)
RETURNS double precision AS $djia$
declare
	djia double precision;
BEGIN
	SELECT SUM(price)/dow INTO djia FROM US30;
	RETURN djia;
END;
$djia$ LANGUAGE plpgsql;


MSFT->GOOG

p_e_ratio = price / earning per share

UPDATE US30 SET symbol = 'GOOG', price = 1037.14, total_share = 6.87e+008, p_e_ratio = 56.95
WHERE symbol = 'MSFT';

UPDATE US30 SET market_value = price * total_share WHERE symbol = 'GOOG';

UPDATE US30 SET total_profit = market_value / p_e_ratio WHERE symbol = 'GOOG';

SELECT DJIA(0.145235);










