create schema stock_analysis;

create table stock_analysis.stock(
 ticker             varchar(50),
 trading_date       date,
 open_price         numeric(12,7),
 high_price         numeric(12,7),
 low_price          numeric(12,7),
 close_price        numeric(12,7),
 adj_close_price    varchar(50),
 volume             bigint
);