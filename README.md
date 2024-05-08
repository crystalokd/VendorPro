# VendorPro - Vendor Management System Assessment

## Core Feature: Historical Performance

### Implementation Using Celery
To enhance the efficiency of the Historical Performance feature, we have integrated Celery into VendorPro. Celery, a distributed task queue, facilitates asynchronous task execution, making it ideal for recurring tasks like updating historical performance data. By leveraging Celery, we ensure that the Historical Performance database is regularly updated with the latest vendor performance metrics. Specifically, we schedule this update to occur daily at midnight. 

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