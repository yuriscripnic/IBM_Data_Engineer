# MongoDB Cheat Sheet Basic commands
Connect to MongoDB: Different ways to connect using Mongoshell

```bash
mongosh "URI"
mongosh --host mongodb0.example.com --port 28015
mongosh "mongodb://mongodb0.example.com:28015" --username alice --authenticationDatabase admin
```

### Show databases
``` show dbs ```

### Switch database
```use <database_name>```

### Create a collection
```db.createCollection("<collection_name>")```

### Show collections in the current database
```show collections```

### Insert a document
```db.<collection_name>.insert({ field1: value1, field2: value2, ... })```

#### Insert multiple documents
```db.<collection_name>.insertMany([document1, document2, ...])```

### Find documents
```db.<collection_name>.find()```

### Querying
#### Filter documents with a query
```db.<collection_name>.find({ field: value })```
Equality query
```db.<collection_name>.find({ field: "value" })```
#### Range query
```
db.<collection_name>.find({ field: { $lt: value } })
db.<collection_name>.find({ field: { $gt: value } })
db.<collection_name>.find({ field: { $lt: value, $gt: value } })
```

#### AND query
```db.<collection_name>.find({ field1: value1, field2: value2 })```
#### OR query
```db.<collection_name>.find({ $or: [ { field1: value1 }, { field2: value2 } ] })```
#### Sort ascending
```db.<collection_name>.find().sort({ field: 1 })```
#### Sort descending
```db.<collection_name>.find().sort({ field: -1 })```

### Update and delete
#### Update documents
```
db.<collection_name>.updateOne({ field: value }, { $set: { new_field: new_value } })
db.<collection_name>.updateMany({ field: value }, { $set: { new_field: new_value } })
```

### Delete documents
```
db.<collection_name>.deleteOne({ field: value })
db.<collection_name>.deleteMany({ field: value })
```


### Aggregation
#### Aggregation pipeline

```
db.<collection_name>.aggregate([
{ $match: { field: value } },
{ $group: { _id: "$field", total: { $sum: 1 } } }
])
```

### Indexing
#### Create a single field index
```db.<collection_name>.createIndex({ field: 1 })```
#### Create a compound index
```db.<collection_name>.createIndex({ field: 1, another_field: 1 })```
#### List all indexes
```db.<collection_name>.getIndexes()```
### Export and import data
#### Export data to JSON
```mongoexport --db <database_name> --collection <collection_name> --out <output_file.json>```
#### Import data from JSON
```mongoimport --db <database_name> --collection <collection_name> --file <input_file.json>```