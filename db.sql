CREATE TABLE shukofukurou_streamdata.links (
	id int(10) NOT NULL auto_increment,
	titleid int(10) NOT NULL,
	url varchar(500),
	siteid int(10) NOT NULL,
	regionid int(10) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE shukofukurou_streamdata.region (
	id int(10) NOT NULL auto_increment,
	regionname text(65535) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE shukofukurou_streamdata.sites (
	id int(10) NOT NULL auto_increment,
	sitename text(65535) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE shukofukurou_streamdata.staging (
	id int(10) NOT NULL auto_increment,
	title varchar(500),
	streamsitetitle varchar(100),
	streamsiteurl varchar(500),
	region varchar(3),
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE shukofukurou_streamdata.titles (
	titleid int(10) NOT NULL auto_increment,
	title varchar(500),
	mal_id int(10),
	PRIMARY KEY (titleid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;