
CREATE DATABASE IF NOT EXISTS `test_selenium`;

USE `test_selenium`;

CREATE TABLE IF NOT EXISTS `senario` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(250)  NOT NULL default '',
  `passed`  int(11) NULL default 0,
  `failed` int(11)  NULL default 0,
  `skipped` int(11)  NULL default 0,
  `error` int(11)  NULL default 0,
  `xfailed` int(11)  NULL default 0,
  `xpassed` int(11)  NULL default 0,
  `num_tests` int(11)  NULL default 0,
  `duration` float(20,20)  NULL,
  `created_at` datetime NOT NULL,
   PRIMARY KEY  (`id`)
);

CREATE TABLE IF NOT EXISTS `test` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(250)  NOT NULL default '',
  `outcome` varchar(250)  NOT NULL default '',
  `duration` float(20,20)  NULL,
  `senario_id`  int(11) NOT NULL,
   PRIMARY KEY  (`id`),
   FOREIGN KEY (senario_id) REFERENCES senario(id)
);


