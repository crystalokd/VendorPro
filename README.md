# VendorPro - Vendor Management System Assessment

## Core Feature: Historical Performance

### Implementation Using Celery
To enhance the efficiency of the Historical Performance feature, I have integrated Celery into VendorPro. Celery, a distributed task queue, facilitates asynchronous task execution, making it ideal for recurring tasks like updating historical performance data. By leveraging Celery, we ensure that the Historical Performance database is regularly updated with the latest vendor performance metrics. Specifically, we schedule this update to occur daily at midnight. 

### Conclusion
The integration of Celery into VendorPro enhances the functionality and reliability of the Historical Performance feature. With Celery managing the periodic updates of historical performance data, users can confidently analyze trends and make informed decisions regarding vendor relationships.



## Easy to miss Feature: Metric calculations

### Fulfilment Rate:
One feature that might be overlooked by other developers is the calculation of the fulfilment rate upon any change in the Purchase Order (PO) status. This feature is critical for providing real-time insights into vendor performance. By calculating the fulfilment rate dynamically, developers ensure that the system always reflects the latest status of POs issued to vendors. The logic behind this calculation is straightforward: it involves dividing the number of successfully fulfilled POs (those with a status of 'completed' and without any issues) by the total number of POs issued to the vendor.

### Avoiding Oversight:
It's easy for developers to overlook this feature, especially if they only calculate metrics periodically or upon specific user actions. However, by not updating the fulfilment rate upon every change in PO status, developers risk providing outdated or inaccurate information to users. This oversight could lead to misinformed decisions and negatively impact vendor relationships and business operations.

### Average Response Time:
Similarly, another critical metric that might be missed is the calculation of the average response time. However, this calculation should only occur before the status of the PO changes to 'completed'. Average response time provides valuable insights into vendor responsiveness and efficiency in acknowledging POs. By calculating this metric dynamically and specifically before the completion of a PO, developers ensure that users have access to timely and relevant data for decision-making.

### Conclusion:
By implementing dynamic calculations for metrics such as fulfilment rate and average response time, developers can enhance the accuracy and usefulness of the Vendor Management System. By being mindful of these critical features and their timing, developers can provide users with up-to-date insights into vendor performance, ultimately improving operational efficiency and decision-making processes.







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
   CELERY_TIMEZONE = "Africa/Lagos"
   
   CELERY_IMPORTS = (
       'authentication.tasks',  # The module containing your Celery tasks
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