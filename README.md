![image](https://github.com/AVK1206/LaptopRater/assets/134367028/9c9fe3a9-c12e-409a-8077-98f598752ca6)# LaptopRater
This project comprises a complete pipeline for scraping laptop product information from an online store, storing the data in MongoDB, and providing an API to access the scraped data.
The project is divided into three main parts:

1. Web Scraping Script: Extracts product details such as the title and rating of laptops listed on the Foxtrot website.
2. MongoDB Database Integration: Stores the scraped data in a MongoDB database.
3. FastAPI Application: Provides an API endpoint to retrieve laptop data from the MongoDB database.

# Prerequisites

- selenium
- beautifulsoup
- pymongo
- fastapi
- uvicorn

# Installation

1. Clone the repository:

    ```
    git clone https://github.com/AVK1206/LaptopRater.git
    ```

2. Create a virtual environment (optional but recommended):

    ```
    python -m venv venv
    ```

3. Activate the virtual environment:

   - On Windows:

        ```
        .\venv\Scripts\activate
        ```

   - On Unix or MacOS:

        ```
        source venv/bin/activate
        ```

4. Install the dependencies:

    ```
    pip install -r requirements.txt
    ```
 
# Local Usage

1. Connection to MongoDB
    
    ```
    Open MongoDBCompass and activate connection to database
    with URI "mongodb://localhost:27017"
    ```
2. Parse data and store the data in database
   - On Windows:

       ```
       python db/mondb.py
       ```
   - On Unix or MacOS:

       ```
       python3 db/mondb.py
       ```

3. Run server FastAPI
    ```
    uvicorn route:app --reload
    ```
    
# Automatically Usage
    
    ```
    Docker-compose up -d
    ```
    
