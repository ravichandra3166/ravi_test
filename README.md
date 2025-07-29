# FastAPI Microservice

A modern, production-ready Python microservice built with FastAPI, featuring user and item management with full CRUD operations.

## Features

- 🚀 **FastAPI**: High-performance, modern Python web framework
- 🗃️ **SQLAlchemy**: Database ORM with PostgreSQL and SQLite support
- 🔐 **Pydantic**: Data validation and serialization
- 🐳 **Docker**: Containerized deployment with docker-compose
- 📊 **Database Admin**: Adminer for database management
- 🧪 **Testing**: Ready for testing with pytest
- 🔒 **Security**: Password hashing with bcrypt
- 📖 **Auto Documentation**: Interactive API docs with Swagger UI

## Project Structure

```
├── app/
│   ├── api/                 # API route definitions
│   │   ├── users.py        # User CRUD endpoints
│   │   └── items.py        # Item CRUD endpoints
│   ├── core/               # Core configuration
│   │   ├── config.py       # Settings and configuration
│   │   └── database.py     # Database connection
│   ├── models/             # SQLAlchemy models
│   │   ├── user.py         # User database model
│   │   └── item.py         # Item database model
│   ├── schemas/            # Pydantic schemas
│   │   ├── user.py         # User validation schemas
│   │   └── item.py         # Item validation schemas
│   ├── services/           # Business logic
│   │   ├── user.py         # User service functions
│   │   └── item.py         # Item service functions
│   └── main.py             # FastAPI application entry point
├── tests/                  # Test directory
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker image definition
├── docker-compose.yml     # Multi-container setup
└── .env.example           # Environment variables template
```

## Quick Start

### 1. Clone and Setup

```bash
git clone <repository-url>
cd fastapi-microservice
```

### 2. Environment Configuration

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 3. Run with Docker (Recommended)

```bash
# Start all services (FastAPI + PostgreSQL + Adminer)
docker-compose up -d

# View logs
docker-compose logs -f fastapi-app
```

### 4. Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

### Core Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /docs` - Interactive API documentation

### User Management

- `POST /api/v1/users/` - Create user
- `GET /api/v1/users/` - List users
- `GET /api/v1/users/{user_id}` - Get user by ID
- `PUT /api/v1/users/{user_id}` - Update user
- `DELETE /api/v1/users/{user_id}` - Delete user

### Item Management

- `POST /api/v1/items/` - Create item
- `GET /api/v1/items/` - List items
- `GET /api/v1/items/{item_id}` - Get item by ID
- `GET /api/v1/items/user/{owner_id}` - Get items by owner
- `PUT /api/v1/items/{item_id}` - Update item
- `DELETE /api/v1/items/{item_id}` - Delete item

## API Documentation

Access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Database Management

Access Adminer (database admin interface):
- **URL**: http://localhost:8080
- **System**: PostgreSQL
- **Server**: db
- **Username**: postgres
- **Password**: password
- **Database**: fastapi_db

## Example Usage

### Create a User

```bash
curl -X POST "http://localhost:8000/api/v1/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "johndoe",
    "password": "securepassword123"
  }'
```

### Create an Item

```bash
curl -X POST "http://localhost:8000/api/v1/items/?owner_id=1" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Sample Item",
    "description": "This is a sample item"
  }'
```

### Get All Users

```bash
curl "http://localhost:8000/api/v1/users/"
```

## Development

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Tests

```bash
pytest
```

### Run with Hot Reload

```bash
uvicorn app.main:app --reload
```

## Configuration

Key environment variables (see `.env.example`):

- `DATABASE_URL`: Database connection string
- `SECRET_KEY`: Secret key for security
- `DEBUG`: Enable debug mode
- `API_V1_PREFIX`: API version prefix

## Docker Commands

```bash
# Build and start services
docker-compose up --build

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild specific service
docker-compose build fastapi-app
```

## Production Deployment

1. Set secure environment variables
2. Use a production database (PostgreSQL recommended)
3. Set `DEBUG=false`
4. Use a reverse proxy (nginx recommended)
5. Enable SSL/TLS

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License.
