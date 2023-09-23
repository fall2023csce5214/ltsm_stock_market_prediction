create schema stock_analysis;

create table stock_analysis.stocks(
 trading_date       date,
 open_price         numeric(12,7),
 high_price         numeric(12,7),
 low_price          numeric(12,7),
 close_price        numeric(12,7),
 adj_close_price    varchar(50)
);