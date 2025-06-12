---
## 🧩 Modules & Classes (Pseudocode)
---

### 1. `input_reader.py`

```python
CLASS InputReader:
    METHOD read_from_console() -> dict:
        PROMPT user for:
            - name
            - age
            - email
            - phone
            - gender
            - country
            - dob
        RETURN dictionary of raw inputs
```

---

### 2. `data_processor.py`

```python
CLASS DataProcessor:
    METHOD preprocess(raw_data: dict) -> User:
        VALIDATE and CLEAN:
            - Trim and store name
            - Convert and validate age
            - Format and validate email using regex
            - Strip non-numeric from phone and validate length
            - Normalize gender (e.g., "m" → "Male")
            - Capitalize country name
            - Accept date of birth (dob)

        RETURN User object

    METHOD _normalize_gender(gender: str) -> str:
        CONVERT to lower, map values to "Male", "Female", or "Other"

    METHOD _capitalize(text: str) -> str:
        RETURN capitalized version of input
```

---

### 3. `user.py`

```python
CLASS User:
    CONTAINS attributes:
        - name
        - age
        - email
        - phone
        - gender
        - country
        - dob

    METHOD __init__(...):
        ASSIGN parameters to attributes
```

---

### 4. `database_handler.py`

```python
CLASS DatabaseHandler:
    METHOD __init__(host, user, password, db_name):
        CONNECT to MySQL server
        CALL _init_db()
        SWITCH to db_name
        CALL _init_table()

    METHOD _init_db():
        CHECK if database exists
        IF not:
            CREATE database

    METHOD _init_table():
        CHECK if users table exists
        IF not:
            CREATE table with schema

    METHOD insert_user(user: User):
        PREPARE insert SQL query
        EXECUTE insert with user fields

    METHOD close():
        CLOSE cursor and connection
```

---

### 5. `main.py`

```python
FUNCTION main():
    INITIALIZE InputReader
    raw_data = READ from console

    INITIALIZE DataProcessor
    user = PREPROCESS raw_data

    INITIALIZE DatabaseHandler
    INSERT user into database
    CLOSE database connection

IF script is main:
    CALL main()
```

---

## 🔁 Data Flow Summary

```text
User input (console)
    ↓
InputReader.read_from_console()
    ↓
Raw dict of user fields
    ↓
DataProcessor.preprocess()
    ↓
Structured and validated User object
    ↓
DatabaseHandler.insert_user(user)
    ↓
User data inserted into MySQL ✅
```
