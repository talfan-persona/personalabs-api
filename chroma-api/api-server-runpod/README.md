# PersonaLabs API 🚀

A comprehensive Product Recommendation API with testing tools and documentation.

## 🌐 Live Documentation

Visit our GitHub Pages site: [https://talfan-persona.github.io/personalabs-api/](https://talfan-persona.github.io/personalabs-api/)

## 📋 API Endpoints

### 1. Generate API Key
- **Endpoint**: `POST /generate_api_key`
- **Description**: Generate an authentication key for API access
- **Request**: `{"username": "your-username"}`
- **Response**: `{"api_key": "generated-key", "username": "your-username"}`

### 2. Query Products
- **Endpoint**: `POST /query`
- **Description**: Get product recommendations based on basket queries
- **Headers**: `X-API-Key: your-api-key`
- **Request**: `{"basket_query": "blue trucker hat\nblack snapback\nsummer sale"}`
- **Response**: `{"ids": [...], "basket_query": "..."}`

### 3. Send Data
- **Endpoint**: `POST /send`
- **Description**: Store arbitrary JSON data for logging and feedback
- **Headers**: `X-API-Key: your-api-key`
- **Request**: Any valid JSON object
- **Response**: `{"status": "stored"}`

## 🔧 Testing Script

Use our comprehensive Python testing script to validate all API endpoints:

```bash
# Download the script
wget https://talfan-persona.github.io/personalabs-api/test_api_docs.py

# Update the BASE_URL in the script to your API endpoint
# Then run:
python3 test_api_docs.py
```

### Features
- ✅ Tests all three API endpoints automatically
- 🔐 Handles API key generation and authentication
- 📊 Provides detailed success/failure reporting
- ⚡ Fast and reliable testing with proper error handling
- 🎯 Easy to customize for different environments

## 📁 Repository Structure

```
personalabs-api/
├── index.html          # GitHub Pages website
├── test_api_docs.py    # API testing script
└── README.md           # This file
```

## 🚀 Quick Start

1. **Visit the documentation**: Go to our [GitHub Pages site](https://talfan-persona.github.io/personalabs-api/)
2. **Download the test script**: Click the download button on the website
3. **Configure your endpoint**: Update the `BASE_URL` variable in the script
4. **Run tests**: Execute `python3 test_api_docs.py`

## 📖 Example Usage

```python
import requests

# 1. Generate API key
response = requests.post("https://your-api-endpoint.com/generate_api_key", 
                        json={"username": "test-user"})
api_key = response.json()["api_key"]

# 2. Query for recommendations
headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
response = requests.post("https://your-api-endpoint.com/query",
                        headers=headers,
                        json={"basket_query": "blue hat\nsummer sale"})
recommendations = response.json()

# 3. Send feedback data
feedback = {"rating": 5, "comment": "Great recommendations!"}
requests.post("https://your-api-endpoint.com/send",
              headers=headers,
              json=feedback)
```

## 🛠️ Requirements

- Python 3.6+
- `requests` library

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

**Built with ❤️ for developers by PersonaLabs** 