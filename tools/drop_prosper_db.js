var dbs = db.getMongo().getDBNames()
for(var i in dbs){
    db = db.getMongo().getDB( dbs[i] );
    if (db.getName() == 'prosper-cr') {
    	print( "dropping db " + db.getName() );
    	db.dropDatabase();
	}
}
