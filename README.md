# 🍕 Pizza Restaurant API Challenge

A simple RESTful API for managing restaurants, pizzas, and their relationships, following the MVC pattern using Flask, SQLAlchemy, and Flask-Migrate.

---

## 🧰 Setup Instructions

1. **Clone the repository and navigate to the project folder:**
   ```bash
   git clone <your-repo-url>
   cd pizza-api-challenge
   ```

2. **Install dependencies and activate the virtual environment:**
   ```bash
   pipenv install flask flask_sqlalchemy flask_migrate
   pipenv shell
   ```

3. **Set the Flask app environment variable:**
   ```bash
   export FLASK_APP=server/app.py
   ```

4. **Run database migrations:**
   ```bash
   flask db init           # Only needed the first time
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Seed the database:**
   ```bash
   python server/seed.py
   ```

---

## 🗂️ Project Structure (MVC)

```
server/
  app.py                # App setup
  config.py             # DB config
  models/               # SQLAlchemy models
    restaurant.py
    pizza.py
    restaurant_pizza.py
  controllers/          # Route handlers
    restaurant_controller.py
    pizza_controller.py
    restaurant_pizza_controller.py
  seed.py               # Seed data
migrations/             # DB migrations
challenge-1-pizzas.postman_collection.json
README.md
```

---

## 🧩 Models

- **Restaurant**: `id`, `name`, `address` (has many RestaurantPizzas)
- **Pizza**: `id`, `name`, `ingredients` (has many RestaurantPizzas)
- **RestaurantPizza**: `id`, `price` (1-30), `restaurant_id`, `pizza_id` (join table)
  - Validation: `price` must be between 1 and 30
  - Cascading deletes: Deleting a restaurant removes related RestaurantPizzas

---

## 🛠️ Routes

### GET `/restaurants`
Returns a list of all restaurants.

**Response:**
```json
[
  { "id": 1, "name": "Mario's Pizza", "address": "address1" },
  ...
]
```

---

### GET `/restaurants/<id>`
Returns details of a single restaurant and its pizzas.

**Success:**
```json
{
  "id": 3,
  "name": "Kiki's Pizza",
  "address": "address3",
  "pizzas": [
    { "id": 1, "name": "Emma", "ingredients": "Dough, Tomato Sauce, Cheese" }
  ]
}
```
**Not found:**
```json
{ "error": "Restaurant not found" }
```

---

### DELETE `/restaurants/<id>`
Deletes a restaurant and all related RestaurantPizzas.

- **Success:** 204 No Content
- **Not found:**
```json
{ "error": "Restaurant not found" }
```

---

### GET `/pizzas`
Returns a list of pizzas.

**Response:**
```json
[
  { "id": 1, "name": "Emma", "ingredients": "Dough, Tomato Sauce, Cheese" },
  ...
]
```

---

### POST `/restaurant_pizzas`
Creates a new RestaurantPizza.

**Request:**
```json
{ "price": 5, "pizza_id": 1, "restaurant_id": 3 }
```
**Success:**
```json
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": { "id": 1, "name": "Emma", "ingredients": "Dough, Tomato Sauce, Cheese" },
  "restaurant": { "id": 3, "name": "Kiki's Pizza", "address": "address3" }
}
```
**Error:**
```json
{ "errors": ["Price must be between 1 and 30"] }
```

---

## 🧾 Validation Rules
- `price` in `RestaurantPizza` must be between 1 and 30 (inclusive).
- `pizza_id` and `restaurant_id` must reference existing records.

---

## 🔎 Testing with Postman
1. Open Postman.
2. Click **Import** → Upload `challenge-1-pizzas.postman_collection.json`.
3. Test each route using the provided requests.

---

## ✅ Submission Checklist
- [x] MVC folder structure
- [x] Models with validations and relationships
- [x] All routes implemented
- [x] Postman tests passing
- [x] Well-written README.md

---

## 📞 Questions?
Open an issue or contact the maintainer.
