# this is a baidu baike spider
this result will save to mysql db

# 1.prerequire
please install relative python packages

# 2.mysql db datatable

CREATE TABLE `spider`.`baidu_baike` (
  `id` int(11) NOT NULL,
  `title` varchar(500) NOT NULL,
  `url` varchar(300) NOT NULL,
  `tags` varchar(500) NOT NULL,
  `attrs` varchar(2000) NOT NULL,
  `content` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# 3.run scripts

python3 ./main.py
