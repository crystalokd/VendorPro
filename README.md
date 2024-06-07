# VendorPro - Vendor Management System Assessment

## Setup Instructions

### Getting Started

To set up VendorPro and start using its features, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd VendorPro
   ```

3. Install dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database by running migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser account to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the admin panel at `http://127.0.0.1:8000/admin` and log in with the superuser credentials created in step 5.

### Setting up Celery

To set up Celery for periodic task execution in VendorPro, follow these additional steps:

1. Install Celery and a message broker such as Redis:

   ```bash
   pip install celery redis
   ```

2. Configure Celery in your settings file (`settings.py`):

   ```python
   # settings.py
   
   CELERY_BROKER_URL = 'redis://localhost:6379'  # Replace with your message broker URL
   CELERY_RESULT_BACKEND = 'redis://localhost:6379'
   CELERY_ACCEPT_CONTENT = ["application/json"]
   CELERY_TASK_SERIALIZER = "json"
   CELERY_RESULT_SERIALIZER = "json"
   
   CELERY_IMPORTS = (
       'vendors.tasks',  # The module containing your Celery tasks
   )
   ```

3. Define Celery tasks in a separate module (`tasks.py`) and configure periodic tasks as needed.

4. Start the Celery worker:

   ```bash
   celery -A VendorPro worker --loglevel=info
   ```

5. Schedule periodic tasks using Celery Beat:

   ```bash
   celery -A VendorPro beat --loglevel=info
   ```

With Celery configured, periodic tasks such as updating historical performance data will be executed automatically according to the specified schedule.



### Using the API Endpoints with Swagger Documentation

1. **Vendor Management:**

   - **Create a New Vendor:** `POST /api/vendors/`
   - **List All Vendors:** `GET /api/vendors/`
   - **Retrieve a Specific Vendor's Details:** `GET /api/vendors/{vendor_id}/`
   - **Update a Vendor's Details:** `PUT /api/vendors/{vendor_id}/`
   - **Delete a Vendor:** `DELETE /api/vendors/{vendor_id}/`

2. **Purchase Order Management:**

   - **Create a New Purchase Order:** `POST /api/purchase-orders/`
   - **List All Purchase Orders:** `GET /api/purchase-orders/`
   - **Retrieve a Specific Purchase Order's Details:** `GET /api/purchase-orders/{order_id}/`
   - **Update a Purchase Order's Details:** `PUT /api/purchase-orders/{order_id}/`
   - **Delete a Purchase Order:** `DELETE /api/purchase-orders/{order_id}/`

3. **Vendor Performance Metrics:**

   - **Retrieve Vendor Performance Metrics:** `GET /api/vendors/{vendor_id}/performance/`

### Accessing Swagger Documentation

To explore and interact with the API endpoints using Swagger documentation, access the `/docs` path in your browser. For example:

```
http://127.0.0.1:8000/docs/
```

Swagger UI provides a user-friendly interface to browse the API endpoints, execute requests, and view responses. It also includes detailed descriptions and examples for each endpoint, making it easy to understand and utilize the VendorPro API.
