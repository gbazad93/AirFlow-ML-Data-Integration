# API Connection Setup: OpenWeather API

This guide provides step-by-step instructions to create an API key on OpenWeather and integrate it into Airflow for weather data retrieval. Follow these steps to configure your API connection securely and effectively.

---

## Steps to Obtain and Configure the API Key

### 1. Sign Up on OpenWeather
1. Visit the [OpenWeather website](https://openweathermap.org).
2. Click **Sign Up** in the top-right corner of the homepage.
3. Fill in the required details (username, email, and password) to register.
4. Complete the registration process by confirming your email address via the verification link sent to your inbox.

---

### 2. Log In to Your Account
1. After verifying your email, log in to your OpenWeather account using your credentials.

---

### 3. Navigate to the API Section
1. Once logged in, locate the **API** section in the main navigation bar.
2. For this project, we are using the **Current Weather API**. Click on its documentation link to view details.
3. You will see the API call format:

   ```
   https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
   ```

4. Review the documentation for parameter details such as `lat` (latitude), `lon` (longitude), and `appid` (your API key).

---

### 4. Generate an API Key
1. Go to your account dashboard and find the **API Keys** section (under **My API Keys**).
2. Click **Create Key** and provide a descriptive name for your key (e.g., `My Weather App`).
3. Copy the generated API key for later use.

---

### 5. Choose a Free API Plan
1. OpenWeather offers a free tier for basic usage, suitable for this project.
2. Ensure that your API key is set up for the free plan.
3. Review the [pricing page](https://openweathermap.org/price) to confirm the limits of the free plan (e.g., number of API calls per minute).

---

## Adding the API Key to Airflow

### 1. Activate the Airflow Environment
Before configuring the API connection, activate your Airflow virtual environment:

```bash
source ~/airflow_env/bin/activate
```

---

### 2. Add the API Key to Airflow Connections
1. Log in to the Airflow UI at [http://localhost:8080](http://localhost:8080).
2. Navigate to **Admin → Connections**.
3. Click the **plus (+)** button to create a new connection.
4. Fill out the connection details as follows:
   - **Conn Id**: `openweather_api_key`
   - **Conn Type**: HTTP
   - **Host**: `https://api.openweathermap.org/data/2.5/weather`
   - **Extra**: Add the API key in JSON format:
     ```
     {
         "api_key": "YOUR_API_KEY"
     }
     ```

5. Click **Save** to store the connection securely in Airflow.

---

### 3. Using the API Connection in the Project DAG
In this project, the DAG code references the connection created above using the **Conn Id** (`openweather_api_key`). This ensures secure and seamless integration with the OpenWeather API.

---

## Notes
- Keep your API key secure and avoid hardcoding it into your scripts.
- Monitor your API usage to ensure it stays within the tier limits.
