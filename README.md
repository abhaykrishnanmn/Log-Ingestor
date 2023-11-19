

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<div align="center">

<h3 align="center">Log Ingestor</h3>


</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![logo](https://github.com/abhaykrishnanmn/Log-Ingestor/assets/75512915/a021ea06-ad50-4653-82b3-7f725dd958c0)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Python
* Django
* PostgreSQL
* SQLite3


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The project can be run using a local SQLite database.

### Prerequisites

- Python 3.10 or higher


### Installation


1. Create virtual environment
   ```sh
   python -m venv .env
   ```
2. Activate the environment
   ```sh
   source .env/bin/activate
   ```

3. Install requirements
   ```sh
    pip install -r requirements.txt
   ```

4. Run migrations
   ```sh
    python manage.py migrate
    ```

5. Run the server
   ```sh
    ./LogIngestor.sh
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Access the server at `localhost:3000`

Endpoints:
- '/': Home page
  Query interface is accessible here

- '/logs/': Ingest point for logs
  POST request to add individual logs to the database

- '/logsearch/': Search endpoint for logs
  Query interface accesses this endpoint to search for logs

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## System Design

![db_diagram](https://github.com/abhaykrishnanmn/Log-Ingestor/assets/75512915/85df4936-ad51-49a1-9107-ae8f0106d2c1)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features Implemented

**Ingestor:**

Develop a mechanism to ingest logs in the provided format.
Ensure scalability to handle high volumes of logs efficiently.
Mitigate potential bottlenecks such as I/O operations, database write speeds, etc.
Make sure that the logs are ingested via an HTTP server, which runs on port `3000` by default.

**Query Interface:**

Offer a user interface (Web UI or CLI) for full-text search across logs.
Include filters based on:
    - level
    - message
    - resourceId
    - timestamp
    - traceId
    - spanId
    - commit
    - metadata.parentResourceId
Aim for efficient and quick search results.
Allow combining multiple filters.
Provide real-time log ingestion and searching capabilities.
Distributed systems or cloud-based solutions can ensure robust scalability.
