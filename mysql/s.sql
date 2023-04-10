-- netstat -anp 发现3306开着，root，root若口令，但是不能远程登录，就没动

UPDATE admin SET user_pass = 'Metc1309' WHERE user_id = '1'
-- 无法更新，锁表了
DROP TABLE admin
-- 先删除
CREATE TABLE `admin` (
  `id` int(100) NOT NULL,
  `user_name` varchar(30) NOT NULL,
  `user_pass` varchar(50) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
INSERT INTO `admin` VALUES (1,'admin','Metc1309');
-- 再新建
LOCK TABLES `admin` WRITE;
-- 再锁上