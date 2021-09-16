1. Import data from data.json into sqlite db
2. Create API to fetch records from db by field 'id'
3. Create API for record deletion by field 'id'
4. Create API that will:
    a. update record if record with given id exists
    b. create new record if there is no record with the given id
5. Use authentication

Usage:
spec-tile.txt contains instruction to build conda virtual environment.
Create conda virtual environment: conda create --name myenv --file spec-file.txt
Activate it: conda activate myenv
Navigate to the folder with code and run: python main.py


OR if you have docker then:
run: sudo docker build -t fast_api .
run: sudo docker run -d -p 8000:8000 fast_api

navigete to port http://<IP_ADDRESS>:8000 
