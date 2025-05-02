DROP TABLE IF EXISTS public.MyFactSales;

CREATE TABLE public.MyFactSales(
    salesid INT NOT NULL, 
    productid INT NOT NULL, 
    segmentid INT NOT NULL, 
    dateid INT NOT NULL, 
    quantitysold INT NOT NULL, 
    priceperunit INT NOT NULL, 
    PRIMARY KEY (salesid)
);