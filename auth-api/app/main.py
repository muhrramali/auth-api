from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from .routes import auth, public, protected

app = FastAPI(
    title="Secure Supabase Auth API",
    description="Authentication API using Supabase Auth and JWT bearer tokens.",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(public.router)
app.include_router(protected.router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    schema["components"]["securitySchemes"] = {
        "BearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    }
    for path in schema["paths"]:
        if path.startswith("/protected") or path == "/auth/logout":
            for method in schema["paths"][path]:
                schema["paths"][path][method]["security"] = [{"BearerAuth": []}]
    app.openapi_schema = schema
    return schema

app.openapi = custom_openapi

@app.get("/", tags=["Health"])
def health():
    return {"message": "Server running and connected to Supabase"}
