# geeglee_backend_test

## Purpose

Create a web app to get infos from customer data through an API

## Technical Stack

- Python 3.6
- Django 2.2
- Django Rest Framework
- sqlite3

## Additionnal features
- Creation of a Django Custom command script to fill the 3 tables
- Custom create function for the API entries to ensure datas format (small caps and email)

## Tests
Done on Postman for all endpoints:
- Return response 200 (passed)
- Time response less than than 600ms (passed)
- Time response less than than 200ms (failed)
(I couldn't share tests as I have only free version)
