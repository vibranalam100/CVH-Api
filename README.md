# Commercial Vehicle Health Monitoring API

A layered Flask REST API for monitoring commercial vehicle health using SQL Server, SQLAlchemy, DTOs, services, repositories, and rule-based diagnostic logic. The application stores vehicle and sensor data in a SQL Server database and evaluates key operating parameters such as engine temperature, oil pressure, battery voltage, and brake wear to detect abnormal vehicle conditions.

This project demonstrates REST API development, backend architecture, SQL Server integration, request validation, service-layer business logic, and basic diagnostic decision-making for commercial vehicle systems.

## Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* SQL Server Express
* PyODBC
* DTOs
* Service Layer
* Repository Pattern
* Postman

## Features

* Register commercial vehicles
* Store vehicle sensor data in SQL Server
* Analyze latest sensor readings
* Detect abnormal operating conditions
* Generate vehicle health status: Healthy, Warning, or Critical
* Provide maintenance recommendations
* Clean layered backend architecture

## API Endpoints

### Home

```http
GET /
```

Returns basic API information.

---

### Create Vehicle

```http
POST /vehicles
```

Sample request body:

```json
{
  "vehicle_number": "TRUCK-101",
  "vehicle_type": "Heavy Truck",
  "manufacturer": "MAN",
  "model": "TGX",
  "mileage_km": 180000
}
```

---

### Get All Vehicles

```http
GET /vehicles
```

Returns all registered vehicles from the SQL Server database.

---

### Add Sensor Data

```http
POST /sensor-data
```

Sample request body:

```json
{
  "vehicle_id": 1,
  "engine_temperature": 110,
  "oil_pressure": 18,
  "battery_voltage": 12.1,
  "brake_wear": 85
}
```

---

### Get Vehicle Health Report

```http
GET /vehicle-health/{vehicle_id}
```

Example:

```http
GET /vehicle-health/1
```

Sample response:

```json
{
  "vehicle": {
    "id": 1,
    "vehicle_number": "TRUCK-101",
    "vehicle_type": "Heavy Truck",
    "manufacturer": "MAN",
    "model": "TGX",
    "mileage_km": 180000
  },
  "status": "Critical",
  "issues": [
    "Engine temperature is too high",
    "Oil pressure is too low",
    "Brake wear is too high"
  ],
  "recommendation": "Immediate inspection required"
}
```

## Diagnostic Rules

The API checks the latest sensor data using simple rule-based diagnostics:

* Engine temperature above 105°C → Warning
* Oil pressure below 20 psi → Critical
* Battery voltage below 11.8 V → Warning
* Brake wear above 80% → Critical

## Project Architecture

```text
app.py
↓
routes.py
↓
DTOs
↓
Services
↓
Repository
↓
Models
↓
SQL Server Database
```

## Purpose

The goal of this project is to connect backend software development with commercial vehicle technology. It simulates a basic vehicle health monitoring system that could be used to support fleet diagnostics, maintenance planning, and early detection of vehicle faults.
