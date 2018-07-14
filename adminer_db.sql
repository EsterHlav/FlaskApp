-- Adminer 4.6.3-dev PostgreSQL dump

\connect "d3155lq25v3f2b";

DROP TABLE IF EXISTS "comments";
DROP SEQUENCE IF EXISTS comments_id_seq;
CREATE SEQUENCE comments_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."comments" (
    "id" integer DEFAULT nextval('comments_id_seq') NOT NULL,
    "idlocation" integer NOT NULL,
    "location" character varying NOT NULL,
    "userid" integer NOT NULL,
    "comment" character varying NOT NULL,
    CONSTRAINT "comments_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "userlogin";
DROP SEQUENCE IF EXISTS userlogin_id_seq;
CREATE SEQUENCE userlogin_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."userlogin" (
    "id" integer DEFAULT nextval('userlogin_id_seq') NOT NULL,
    "name" character varying NOT NULL,
    "password" character varying NOT NULL,
    CONSTRAINT "userlogin_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "zips";
DROP SEQUENCE IF EXISTS zips_id_seq;
CREATE SEQUENCE zips_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."zips" (
    "id" integer DEFAULT nextval('zips_id_seq') NOT NULL,
    "zipcode" character varying NOT NULL,
    "city" character varying NOT NULL,
    "state" character varying NOT NULL,
    "latitude" double precision NOT NULL,
    "longtitude" double precision NOT NULL,
    "population" integer NOT NULL,
    "checkins" integer DEFAULT '0' NOT NULL,
    CONSTRAINT "zips_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


-- 2018-07-14 21:50:27.475809+00
