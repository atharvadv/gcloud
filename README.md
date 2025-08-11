# gcloud
Code to deploy Hello World App in GCP 
Process 
Create an account on Google App Engine
-----

# **Deploying a Python App to Google App Engine**

This guide outlines the steps to deploy a Python application to the Google Cloud Platform (GCP) using App Engine.

## **1. Project Setup in GCP**

First, set up your project environment in the Google Cloud Console.

  - **Create a New Project**: Go to the GCP Console and create a new project.
  - **Enable APIs**: Navigate to `APIs & Services` \> `Library` and enable the **App Engine Admin API**.
  - **Create App Engine Application**: Search for "App Engine" in the console and click **Create application**. Choose a region when prompted.

## **2. Prepare Your Code**

Your application needs a few specific files to work with App Engine.

  - **`main.py`**: Your main Python application file (e.g., a simple Flask app).

  - **`requirements.txt`**: A file listing your project's Python dependencies.

  - **`app.yaml`**: The configuration file that tells App Engine how to run your application.

    ```yaml
    # app.yaml
    runtime: python312 # Or your desired Python version
    entrypoint: gunicorn -b :$PORT main:app # Example for a Flask/Django app
    ```

## **3. Deployment via Cloud Shell**

The easiest way to deploy is by using the built-in Google Cloud Shell.

1.  **Activate Cloud Shell**: Click the `>` icon in the top-right of the GCP Console to open the Cloud Shell.

2.  **Upload Your Code**: Use the Cloud Shell editor to upload or create your `main.py`, `requirements.txt`, and `app.yaml` files.

3.  **Navigate to Project Directory**: In the terminal, change to the directory containing your code.

    ```bash
    cd your-project-folder
    ```

4.  **Deploy the Application**: Run the `gcloud` deploy command. The tool will automatically use your current project's configuration.

    ```bash
    gcloud app deploy
    ```

    Follow the prompts to confirm the deployment.

## **4. View Your Application**

Once the deployment is complete, you can view your live app.

1.  **Get the URL**: Run the `browse` command to get your application's public URL and open it in a new tab.
    ```bash
    gcloud app browse
    ```

-----
