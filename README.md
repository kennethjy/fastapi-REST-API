# Database Stucture:
![image](https://github.com/kennethjy/fastapi-REST-API/assets/114073455/c3087704-8f0a-40eb-8623-b3a2c3aa776d)

# API Design

## Endpoints
![image](https://github.com/kennethjy/fastapi-REST-API/assets/114073455/dafdd4d9-1540-4221-831d-2ee1962aadcc)

- GET / => returns a default value, no use
- GET /gettodoforuser/{uid} => returns all todo items for a given user
- GET /gettodo/{id} => returns the todo item specified by the item id
- POST /newtodo/{uid} => creates a new todo item for the current user, returns the unique id for the created item
- DELETE /deletetodo/{id} => deletes the todo item
- PUT /checktodo/{id} => toggles the check status of the todo item
- PUT /changedesc/{id}/{desc} => changes the description of the todo item

## Request & Response Format

- Request => JSON
- Response => JSON

## Authentication

None
