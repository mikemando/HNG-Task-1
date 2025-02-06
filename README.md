# Number Classification API

## Overview
This API takes a number as input and returns interesting mathematical properties about it, along with a fun fact retrieved from the Numbers API.

## Features
- Checks if a number is **prime**.
- Determines if a number is a **perfect number**.
- Classifies numbers as **Armstrong, odd, or even**.
- Computes the **sum of digits** of the number.
- Fetches a **fun fact** about the number from [Numbers API](http://numbersapi.com/).

## API Endpoint
### **GET /api/classify-number?number={integer}**

### **Response Format**
#### **Success Response (200 OK)**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### **Error Response (400 Bad Request)**
```json
{
    "number": "alphabet",
    "error": true
}
```

## Technology Stack
- **Python**
- **Django REST Framework (DRF)**


## Installation & Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/account_name/repository_name.git
cd repository_name
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Start the Server**
```bash
python manage.py runserver
```

The API will be accessible at:
```
http://127.0.0.1:8000/api/classify-number?number=371
```

