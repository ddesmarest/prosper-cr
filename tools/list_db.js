var dbs = db.getMongo().getDBNames()
for(var i in dbs){
    db = db.getMongo().getDB( dbs[i] );
    if (db.getName() != 'admin') {
    	print( db.getName() );
	}
}
