---------------------DataBase Creation--------------
CREATE DATABASE StockAnalysis
GO

USE  StockAnalysis;
GO
---------------------Microsoft Table Creation--------------------
CREATE TABLE dbo.Microsoft
(
   [Date]		Date,
   [Open]		Float,
   [High]		Float,
   [Low]		Float,
   [Close]		Float,
   [Adj Close]  Decimal(12,5),
   [Volume]     Bigint
);


---------------------Pfizer Table Creation--------------------
CREATE TABLE dbo.PFE
(
   [Date]		Date,
   [Open]		Float,
   [High]		Float,
   [Low]		Float,
   [Close]		Float,
   [Adj Close]  Decimal(12,5),
   [Volume]     Bigint
);



---------------------Intel Table Creation--------------------
CREATE TABLE dbo.INTC
(
   [Date]		Date,
   [Open]		Float,
   [High]		Float,
   [Low]		Float,
   [Close]		Float,
   [Adj Close]  Decimal(12,5),
   [Volume]     Bigint
);



---------------------  AdvancedMD Table Creation--------------------
CREATE TABLE dbo.AMD
(
   [Date]		Date,
   [Open]		Float,
   [High]		Float,
   [Low]		Float,
   [Close]		Float,
   [Adj Close]  Decimal(12,5),
   [Volume]     Bigint
);


---------------------  GeneralMotors Table Creation--------------------
CREATE TABLE dbo.GM
(
   [Date]		Date,
   [Open]		Float,
   [High]		Float,
   [Low]		Float,
   [Close]		Float,
   [Adj Close]  Decimal(12,5),
   [Volume]     Bigint
);



---------------------  Nvidia Table Creation--------------------
CREATE TABLE dbo.NVDA
(
   [Date]		Date,
   [Open]		Float,
   [High]		Float,
   [Low]		Float,
   [Close]		Float,
   [Adj Close]  Decimal(12,5),
   [Volume]     Bigint
);



---------------------  Tesla Table Creation--------------------
CREATE TABLE dbo.TSLA
(
   [Date]		Date,
   [Open]		Float,
   [High]		Float,
   [Low]		Float,
   [Close]		Float,
   [Adj Close]  Decimal(12,5),
   [Volume]     Bigint
);


---------------------  Amazon Table Creation--------------------
CREATE TABLE dbo.AMZN
(
   [Date]		Date,
   [Open]		Float,
   [High]		Float,
   [Low]		Float,
   [Close]		Float,
   [Adj Close]  Decimal(12,5),
   [Volume]     Bigint
);



---------------------  Apple Table Creation--------------------
CREATE TABLE dbo.AAPL
(
   [Date]		Date,
   [Open]		Float,
   [High]		Float,
   [Low]		Float,
   [Close]		Float,
   [Adj Close]  Decimal(12,5),
   [Volume]     Bigint
);

---------------------  Google Table Creation--------------------
CREATE TABLE dbo.GOOGL
(
   [Date]		Date,
   [Open]		Float,
   [High]		Float,
   [Low]		Float,
   [Close]		Float,
   [Adj Close]  Decimal(12,5),
   [Volume]     Bigint
);
-----------------------------------------------------------------

----INSERT INTO dbo.Microsoft  VALUES ('1/3/2012','26.549999','26.959999','26.389999','26.77','21.321213',64731500);