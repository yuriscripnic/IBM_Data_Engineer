DROP TABLE IF EXISTS public.MyDimProduct;

CREATE TABLE public.MyDimProduct (
    productid integer NOT NULL,
    productname "char" NOT NULL,
    PRIMARY KEY (productid)
);