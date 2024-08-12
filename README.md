# FastAPI Inventory Microservice

## Overview

This is a FastAPI microservice for managing orders in an inventory system. The microservice interacts with a Redis database to store and manage order data. It features endpoints for creating and retrieving orders, and it uses background tasks to handle order processing asynchronously.

## Features

- **Create Orders**: Allows the creation of new orders.
- **Retrieve Orders**: Fetches details of an existing order by its ID.
- **Background Processing**: Updates order status asynchronously after a delay.
- **Redis Streams**: Utilizes Redis streams to manage order completion events and refunds.

## Technologies

- **FastAPI**: Web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **Redis**: In-memory data structure store used for caching and messaging.
- **Pydantic**: Data validation and settings management library.
- **Uvicorn**: ASGI server for running the FastAPI application.

## Setup

### Prerequisites

- **Python 3.7+**
- **Redis**: Running Redis instance (e.g., via Docker, local installation, or cloud provider).

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/kaayce/ecommerce-microservice.git
    cd ecommerce-microservice
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Redis**

    Update the `redis` connection parameters in `main.py` with your Redis server details.

### Running the Application

1. **Start the FastAPI Application**

    ```bash
    uvicorn main:app --reload
    ```

2. **Access the API**

    The application will be accessible at `http://localhost:8000`. You can interact with the API using Swagger UI at `http://localhost:8000/docs`.

## API Endpoints

### Create an Order

- **Endpoint**: `POST /orders`
- **Description**: Creates a new order and processes it in the background.
- **Request Body**:

    ```json
    {
      "id": "product_id",
      "quantity": 2
    }
    ```

- **Responses**:
  - **200 OK**: Returns the created order.

### Retrieve an Order

- **Endpoint**: `GET /orders/{pk}`
- **Description**: Fetches details of an existing order by its ID.
- **Parameters**:
  - `pk` (path parameter): The ID of the order.
- **Responses**:
  - **200 OK**: Returns the order details.
  - **404 Not Found**: If the order does not exist.

## Background Processing

The application uses background tasks to update the status of orders. After an order is created, its status will be updated to "completed" after a 5-second delay.

## Error Handling

- **500 Internal Server Error**: If an error occurs during order processing or Redis operations, an error message will be logged.

## Redis Streams

The application uses Redis streams to manage order completion events and handle refunds:

- **Stream**: `order_completed`
- **Stream**: `refund_order`

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. For major changes, please open an issue first to discuss the changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [Patrick Nzediegwu](mailto:pat.nzediegwu@gmail.com).
