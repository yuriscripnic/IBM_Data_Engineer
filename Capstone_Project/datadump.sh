#!/bin/bash

mysqldump --host=172.21.18.194 --port=3306 --user=root \
    --password=aOqGTOC5Uk4Am4FyaCNzGpRv \
    sales sales_data > sales_data.sql