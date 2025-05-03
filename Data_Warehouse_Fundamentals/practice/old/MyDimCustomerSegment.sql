DROP TABLE IF EXISTS public.MyDimCustomerSegment;

CREATE TABLE public.MyDimCustomerSegment(
    segmentid integer NOT NULL,
    segmentname "char" NOT NULL,
    PRIMARY KEY (segmentid)
);