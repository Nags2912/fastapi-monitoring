# fastapi-monitoring
![WhatsApp Image 2025-03-12 at 03 23 24_3db5be76](https://github.com/user-attachments/assets/7eec086d-bd3c-43c2-a3b3-33f83e253fe0)

# FastAPI Monitoring with PostgreSQL & Grafana

## 📌 Overview

This project is a FastAPI-based web service that stores monitoring data in PostgreSQL and visualizes it using Grafana. Prometheus is used as a data source for Grafana to monitor web server metrics.

## 🏗️ Project Components

- **FastAPI**: REST API framework for handling monitoring data.
- **PostgreSQL**: Database for storing monitoring data.
- **Prometheus**: Collects and exposes metrics.
- **Grafana**: Visualizes PostgreSQL and Prometheus metrics.
- **Docker Compose**: Containerizes the services for easy deployment.

---

## 🚀 Setup & Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/YOUR_USERNAME/fastapi-monitoring.git
cd fastapi-monitoring
```

### 2️⃣ Configure Environment Variables

Create a `.env` file and specify the database password:

```
DB_PASSWORD=yourpassword
```

### 3️⃣ Start the Services (Docker Compose)

```sh
docker-compose up -d
```

### 4️⃣ Verify Running Containers

```sh
docker ps
```

Ensure all containers (FastAPI, PostgreSQL, Prometheus, Grafana) are running.

---

## 🎯 API Endpoints

| Method | Endpoint   | Description                    |
| ------ | ---------- | ------------------------------ |
| POST   | `/report`  | Submits monitoring data        |
| GET    | `/metrics` | Exposes metrics for Prometheus |
| GET    | `/health`  | Health check for FastAPI       |

Example to send data:

```sh
curl -X POST "http://localhost:8080/report" -H "Content-Type: application/json" -d '{"message": "Hello World"}'
```

---

## 📊 Visualizing Data in Grafana

### 1️⃣ Access Grafana

Open Grafana in your browser:

```
http://localhost:3000
```

(Default login: `admin` / `admin`)

### 2️⃣ Configure Data Sources

- **PostgreSQL**: Connect using `postgres://postgres:yourpassword@db:5432/postgres`
- **Prometheus**: Use `http://prometheus:9090`

###

---

```sh
while true; do curl -X POST "http://localhost:8080/report" -H "Content-Type: application/json" -d '{"message": "Hello World"}'; sleep 1; done
```

---

## 🔧 Stopping & Cleaning Up

To stop and remove containers:

```sh
docker-compose down
```

To remove volumes and clear database data:

```sh
docker-compose down -v
```

---




