# Quering Data in NoSQL Databases
## Scenario
You are a data engineer at an e-commerce company. Your company needs you to design a data platform that uses MongoDB as a NoSQL database. You will be using MongoDB to store the e-commerce catalog data.

### Exercise 1 - Check the lab environment
Check if you have the ‘mongoimport’ and ‘mongoexport’ installed on the lab, otherwise install them.
Download the catalog.json file from [here](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json).

### Exercise 2 - Working with MongoDB
#### Task 1 - Import ‘catalog.json’ into mongodb server into a database named ‘catalog’ and a collection named ‘electronics’
- Name the screenshot as mongoimport.jpg. (images can be saved with either .jpg or .png extension)

 ```bash
mongoimport  \
    --authenticationDatabase=admin \
    --db=catalog --collection=electronics \
    --uri=mongodb://root:ymE2KMpkumRj1jM9940rqoJL@172.21.51.24:27017 \
    --file=catalog.json
 ```

#### Task 2 - List out all the databases
- Name the screenshot as list-dbs.jpg. (images can be saved with either .jpg or .png extension)
```js
show databases;
```

#### Task 3 - List out all the collections in the database catalog.
-Name the screenshot as list-collections.jpg. (images can be saved with either .jpg or .png extension)
```js
use catalog
show collections
```

#### Task 4 - Create an index on the field “type”
- Name the screenshot as create-index.jpg. (images can be saved with either .jpg or .png extension)
```js
db.electronics.createIndex({type:1})
```

#### Task 5 - Write a query to find the count of laptops
- Name the screenshot as mongo-query-laptops.jpg. (images can be saved with either .jpg or .png extension)
```js
db.electronics.aggregate([
    {$match:{type:"laptop"}},
    {$count:"count"}
])
```

#### Task 6 - Write a query to find the number of smart phones with screen size of 6 inches.
- Name the screenshot as mongo-query-mobiles1.jpg. (images can be saved with either .jpg or .png extension)
```js
db.electronics.aggregate([
    {
        $match:{
            $and: [{type:"smart phone"},{"screen size":6}]
        }
    },
    {$count:"count"}
])
```

#### Task 7. Write a query to find out the average screen size of smart phones.
- Name the screenshot as mongo-query-mobiles2.jpg. (images can be saved with either .jpg or .png extension)
```js
db.electronics.aggregate([
    {
        $match: { type: "smart phone" }
    },
    {
        $group: {
            _id: null,
            averageScreenSize: { $avg: "$screen size" }
        }
    }
])
```

#### Task 8 - Export the fields _id, “type”, “model”, from the ‘electronics’ collection into a file named electronics.csv
- Name the screenshot as mongoexport.jpg. (images can be saved with either .jpg or .png extension)

 ```bash
mongoexport \
    --authenticationDatabase=admin \
    --db=catalog --collection=electronics \
    --uri=mongodb://root:ymE2KMpkumRj1jM9940rqoJL@172.21.51.24:27017 \
    --type=csv \
    --fields=_id,type,model \
    --out=electronics.csv
 ```
