# NEXUS ARENA — Python Backend Completed

This package removes the Firebase runtime dependency and connects the dashboard, bookings,
orders, rewards/daily spin, and birthday verification/gift flows to a Flask + SQLite API.

## 1. Install

Windows PowerShell:

```powershell
cd nexus-arena\backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## 2. Configure

Copy `.env.example` to `.env` and set a strong `NEXUS_JWT_SECRET` for production.
For local testing the app has a development fallback secret.

## 3. Run

```powershell
python app.py
```

Open:

```text
http://127.0.0.1:5000/
```

The Flask server serves the existing frontend, so the frontend API base automatically points
at port 5000 when you use Live Server or another frontend server.

## 4. API health

Open:

```text
http://127.0.0.1:5000/api/health
```

Expected:

```json
{"ok":true,"service":"NEXUS ARENA API"}
```

## Backend-connected features

- Authentication: register, login, `/api/auth/me`, logout
- Dashboard profile/statistics
- Booking list + booking creation
- Seat availability validation during booking
- Order list + order creation
- Daily reward spin with 24-hour server-side cooldown
- Server-side XP and reward points
- Birthday verification
- Birthday gift claim with one-claim-per-year protection
- SQLite persistence
- Password hashing
- JWT authentication
- Basic API validation and error responses
- Firebase runtime removed

## Important

The old Firebase configuration file is intentionally removed from `js/`.
The browser no longer depends on Firebase Authentication or Firestore.

For production, use HTTPS, a strong secret, restricted CORS origins, CSRF-aware cookie
sessions or a secure token strategy, rate limiting, and a real payment provider rather
than the demo payment-method selection used by the existing UI.

## New backend-backed features

- Tournament catalog at `/api/tournaments`
- Authenticated tournament registration at `/api/tournaments/<id>/register`
- Player roster capture (captain + up to 4 additional players)
- Bracket data at `/api/tournaments/<id>/bracket`
- User registration history at `/api/tournaments/my`
- Database-backed leaderboard at `/api/leaderboard`
- Nexus AI response endpoint at `/api/chat`
- Café checkout now creates a persisted order
- Store product pages share the Pro Store cart via `nexusStoreCart`
- Order totals are validated on the server before persistence

## Verification performed

- All JavaScript files pass `node --check`.
- `backend/app.py` passes `python -m py_compile`.
- Required frontend/backend files and new API routes were checked for integrity.
- A Chromium headless smoke-test attempt was made; complete API runtime testing cannot be truthfully claimed until the Python dependencies are installed and the server is running.

Run the backend before testing authenticated features:
```powershell
cd nexus-arena\backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```
