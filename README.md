# Flask Boilerplate
```
Flask APIs for the fetching the product info
```

## Project Description
```
To set up this project on local Please follow the steps mention below:
1. First clone the Repository from the git lab.
2. Create a Python 3.6 virtual environment using command "virtualenv virt_name --python=python3.6".
3. Now activate the virtual env using command "source virt_name/bin/activate".
4. Now install the library requirements using the command "pip install -r requirement.txt"
4. Now change the database path from the .env.example file and use the command "source .env.example".
5. Now upgrade the database using command "alembic upgrade head".
6. Repository setup completed.
7. Start the server using command "python app.py"
```

## alembic commands to run migrations
```
1. Initiate the alembic -> alembic init alembic
2. For creating the revision -> alembic revision -m "your message"
3. automatic detects model changes and generate commit file -> alembic revision --autogenerate -m "your message"
4. create tables with basic data in your DB -> alembic upgrade head

```

### How to run the crawlers
```
Run the Following command to run the crawlers
1. python krannich.py 
2. python memodo.py
This will run the both the crawlers and store the data to the database.
```

### API endpoint to check the product details
```
Product List API:-
http://localhost:5009/api/product
http://localhost:5009/api/product/?product_id=1

For admin UI:-
http://localhost:5009/admin

```
