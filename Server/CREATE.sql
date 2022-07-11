
CREATE TABLE Area_code(
    code int not null,
    name varchar(12) not null,
    primary key(code)
);
DROP TABLE Area_code;

CREATE TABLE info(
    Dt date not null,
    P_Code integer not null,
    C_Code integer not null,
    confirmed int not null,
    suspected int not null,
    cured int not null,
    dead int not null,
    id bigserial,
    primary key (id)
);

DROP TABLE sde.info;
