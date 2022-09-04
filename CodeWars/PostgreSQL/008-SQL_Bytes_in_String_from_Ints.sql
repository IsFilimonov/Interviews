SELECT octet_length(number1::text) AS octnum1,
       octet_length(number2::text) AS octnum2,
       octet_length(number3::text) AS octnum3,
       octet_length(number4::text) AS octnum4,
       octet_length(number5::text) AS octnum5
FROM numbers;