# FarmPure Made of Farmers For better Crop Management

FarmPure is a web application designed to connect local farmers with consumers, providing a platform for selling and purchasing fresh, natural produce directly from the farm. The project includes a multi-page website for user and farmer interactions, a database schema, and a machine learning model for predicting optimal product prices.

### Project Structure

The project is organized into the following key components:

-   **HTML Files**: The front-end of the application, consisting of multiple pages for user and farmer portals.
-   **CSS & JavaScript**: A stylesheet for consistent design and a script for specific functionalities like geolocation.
-   **Backend & Database**: A Flask-based Python server for routing and a MySQL database schema (`farmpure.sql`) for managing user, farmer, and product data.
-   **Pricing Model**: Python scripts for a machine learning model that analyzes market data to suggest optimal product prices for farmers.

### Getting Started

To run this project locally, you need to set up a few things:

1.  **File Organization**: Ensure your files are arranged in the correct folder structure:
    ```
    FarmPure/
    ├── app.py
    ├── index.html
    ├── login_signup.html
    ├── user_login.html
    ├── user_signup.html
    ├── farmer_login.html
    ├── farmer_signup.html
    ├── u_homepage.html
    ├── f_homepage.html
    ├── home.html
    ├── gps.html
    ├── style.css
    ├── your_script.js
    ├── farmpure.sql
    ├── image/
    │   ├── background1.jpg
    │   ├── logo.png
    │   └── ... (other images)
    └── graph/
        ├── dataset.py
        ├── dummy_data_with_predicted_prices.csv
        ├── evaluate_model.py
        └── plot_graph.py
    ```
2.  **Run the Backend Server**:
    The provided `app.py` file uses the Flask framework to handle routing. To start the server, navigate to the `FarmPure` directory in your terminal and run:

    ```bash
    pip install Flask
    python app.py
    ```
    
    Once the server is running, you can access the website by opening your web browser and navigating to `http://127.0.0.1:5000`.

3.  **Database Setup (Optional)**:
    If you want to set up the database, you can use the `farmpure.sql` file. You will need a MySQL server installed and configured.

4.  **Pricing Model (Optional)**:
    The Python scripts in the `graph` folder are for data analysis. You can run them independently to see the pricing model in action. You will need to install the required libraries:

    ```bash
    pip install pandas scikit-learn matplotlib
    ```
    Then, you can run each script to generate the data, plots, and evaluation metrics:

    ```bash
    python graph/dataset.py
    python graph/evaluate_model.py
    python graph/plot_graph.py
    ```

### Key Features

* **Role-Based Access**: Separate login and signup flows for Farmers and Users.
* **Intuitive Navigation**: Easy-to-use navigation bars on the user and farmer homepages.
* **Geolocation**: The `gps.html` page demonstrates how to get the user's current location using a JavaScript API.
* **Data-Driven Insights**: The pricing model scripts show how the platform could provide valuable data to farmers to help them set optimal prices.

