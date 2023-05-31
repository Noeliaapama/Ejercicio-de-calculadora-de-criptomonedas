CREATE TABLE "mov_criptos" (
	"id"	INTEGER,
	"date"	TEXT NOT NULL,
	"time"	TEXT NOT NULL,
	"mfrom"	TEXT NOT NULL,
	"quantity_from"	REAL NOT NULL,
	"mto"	TEXT NOT NULL,
	"quantity_to"	REAL NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)