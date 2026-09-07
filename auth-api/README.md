# Secure Supabase Auth API

A FastAPI authentication API built for the Auth Login & Protect assignment.

## Features

- Supabase Auth signup and login
- JWT bearer-token authentication
- Reusable FastAPI dependency for protected routes
- Protected profile and dashboard endpoints
- Logout endpoint
- Swagger UI with Bearer Authorization
- Environment variables protected by `.gitignore`

## 1. Setup

Install Python 3.10+.

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your Supabase Project URL and Anon Key.

## 2. Run

```bash
uvicorn app.main:app --reload --port 8000
```

Open Swagger:

http://localhost:8000/docs

## API Reference

| Method | Endpoint | Authentication |
|---|---|---|
| POST | /auth/signup | No |
| POST | /auth/login | No |
| POST | /auth/logout | Bearer JWT |
| GET | /protected/profile | Bearer JWT |
| GET | /protected/dashboard | Bearer JWT |
| GET | /public/info | No |

## Required assignment status codes

- 201: successful signup
- 200: successful login/read
- 204: successful logout
- 400: invalid/missing input
- 401: missing or invalid token / invalid credentials

## Testing

Public endpoint:

```bash
curl http://localhost:8000/public/info
```

Protected endpoint without a token:

```bash
curl -i http://localhost:8000/protected/profile
```

After login, copy `access_token`, then use Swagger's Authorize button or:

```bash
curl -i http://localhost:8000/protected/profile -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Git commits

Recommended commits:

1. `Stage 0: setup server and supabase client`
2. `Stage 1: signup and login routes working`
3. `Stage 2: public route and unverified protected route`
4. `Stage 3: profile route token verification`
5. `Stage 4: auth middleware and logout endpoint`
6. `Stage 5: Swagger UI documentation with bearer auth`
7. `Stage 6: publish to GitHub and write README`

## Security

Never commit `.env`. Use your own Supabase project credentials.
