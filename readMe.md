
# 🚗 Car Wash API Documentation

Sistem Informasi Car Wash Sederhana berbasis Django REST Framework dengan JWT Authentication dan fitur upload bukti pembayaran.

Base URL: `http://localhost:8000/api/`

---

## 🔐 Authentication

### Get Token (Login)
**POST** `/auth/token/`

#### Request Body
```json
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

#### Response
```json
{
  "access": "<jwt-access-token>",
  "refresh": "<jwt-refresh-token>"
}
```

### Refresh Token
**POST** `/auth/token/refresh/`

#### Request Body
```json
{
  "refresh": "<jwt-refresh-token>"
}
```

#### Response
```json
{
  "access": "<new-access-token>"
}
```

---

## 📦 Endpoints

### 🔧 Services
Endpoint untuk menampilkan dan mengelola jenis layanan seperti cuci mobil, ganti oli, dll.

**URL:** `/services/`

| Method | Auth Required | Description             |
|--------|---------------|-------------------------|
| GET    | ✅ Yes         | Menampilkan semua service |
| POST   | ✅ Yes         | Menambahkan service baru |
| PUT    | ✅ Yes         | Update service (by ID) |
| DELETE | ✅ Yes         | Hapus service (by ID)  |

#### Contoh POST `/services/`
```json
{
  "name": "Cuci Mobil",
  "description": "Pencucian mobil standar",
  "price": 50000
}
```

---

### 📅 Bookings
Endpoint untuk membuat dan melihat booking layanan cuci.

**URL:** `/bookings/`

| Method | Auth Required | Description                |
|--------|---------------|----------------------------|
| GET    | ✅ Yes         | Menampilkan semua booking  |
| POST   | ✅ Yes         | Buat booking baru          |
| PUT    | ✅ Yes         | Update booking (by ID)     |
| DELETE | ✅ Yes         | Hapus booking (by ID)      |

#### Contoh POST `/bookings/`
```json
{
  "customer_name": "Budi",
  "vehicle_plate": "B1234XYZ",
  "service": 1,
  "booking_date": "2025-07-01T10:00:00Z"
}
```

---

### 💳 Payments (dengan Upload Bukti)
Endpoint untuk mencatat pembayaran booking dan mengunggah bukti pembayaran (gambar).

**URL:** `/payments/`

| Method | Auth Required | Description                        |
|--------|---------------|------------------------------------|
| GET    | ✅ Yes         | Menampilkan semua pembayaran       |
| POST   | ✅ Yes         | Buat data pembayaran + bukti upload|
| PUT    | ✅ Yes         | Update pembayaran (by ID)          |
| DELETE | ✅ Yes         | Hapus pembayaran (by ID)           |

#### Contoh POST `/payments/` (form-data)
Gunakan `Content-Type: multipart/form-data`

| Key       | Value              |
|-----------|--------------------|
| booking   | 1                  |
| method    | cash / transfer    |
| is_paid   | true               |
| proof     | *(upload file)*    |

#### Contoh Response:
```json
{
  "id": 1,
  "booking": 1,
  "method": "cash",
  "is_paid": true,
  "proof": "http://localhost:8000/media/payment_proofs/bukti123.jpg"
}
```

---

## 📝 Note
- Semua endpoint (kecuali token login/refresh) **wajib menggunakan JWT token** di header:
  ```http
  Authorization: Bearer <access-token>
  ```

- Format waktu menggunakan **ISO 8601** (`YYYY-MM-DDTHH:MM:SSZ`)
- File bukti pembayaran disimpan di `media/payment_proofs/`

---

## 🚀 Quickstart Pengujian
1. Buat superuser:
   ```bash
   python manage.py createsuperuser
   ```

2. Login & dapatkan token:
   ```http
   POST /api/auth/token/
   ```

3. Gunakan token untuk akses endpoint lain.

---