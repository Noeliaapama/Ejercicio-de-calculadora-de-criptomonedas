CREATE TABLE "mov_criptos" (
	"id"	INTEGER,
	"date"	TEXT NOT NULL,
	"time"	TEXT NOT NULL,
	"from"	TEXT NOT NULL,
	"quantity_from"	REAL NOT NULL,
	"to"	TEXT NOT NULL,
	"quantity_to"	REAL NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)