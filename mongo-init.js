// Switch to the grant-writer database (this will create it)
db = db.getSiblingDB('documents');

// Create collections
db.createCollection('benefits');
db.createCollection('scraper_configs');
db.createCollection('pages');
