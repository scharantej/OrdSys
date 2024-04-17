## Flask Application Design for an Order System

### HTML Files

- **index.html:** This is the main HTML file that displays the order form. It contains input fields for customer information, product details, and a submit button.
- **confirmation.html:** This HTML file is displayed after the order is successfully submitted. It shows the order details and a confirmation message.

### Routes

- **@app.route('/')**: This route handles the display of the order form (index.html). It renders the index.html template.
- **@app.route('/order', methods=['POST'])**: This route handles the submission of the order form. It processes the form data, validates the input, and saves the order details to a database or other persistent storage. Upon successful submission, it redirects to the confirmation page.
- **@app.route('/confirmation')**: This route handles the display of the confirmation page (confirmation.html). It renders the confirmation.html template, displaying the order details.

### Additional Notes

- The specific database or persistent storage mechanism used for saving the order details will depend on the requirements of your application. Flask supports various database integrations, such as SQLAlchemy, which can be utilized for this purpose.
- The input validation can be implemented using the Flask-WTF extension, which provides robust form validation capabilities.
- Additional routes may be required based on the specific requirements of your order system, such as routes for managing orders, tracking their status, etc.