"""
StockGenie Backend - FastAPI Application Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from datetime import datetime

# Create FastAPI app
app = FastAPI(
    title="StockGenie API",
    description="AI-Powered KSE100 Stock Intelligence Platform",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS configuration
origins = [
    "http://localhost:3000",  # Next.js frontend
    "http://frontend:3000",   # Docker internal
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint - API information"""
    return {
        "name": "StockGenie API",
        "version": "0.1.0",
        "status": "operational",
        "docs": "/docs",
        "environment": os.getenv("ENVIRONMENT", "development"),
    }


@app.get("/api/v1/health")
async def health_check():
    """Health check endpoint for container orchestration"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "stockgenie-backend",
        "environment": os.getenv("ENVIRONMENT", "development"),
    }


# Include routers
from app.api.v1.index import router as index_router
app.include_router(index_router, prefix="/api/v1")


@app.get("/api/v1/ping")
async def ping():
    """Simple ping endpoint"""
    return {"message": "pong"}


# Exception handlers
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Not Found",
            "message": f"The endpoint {request.url.path} does not exist",
            "docs": "/docs",
        },
    )


@app.exception_handler(500)
async def internal_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected error occurred. Please try again later.",
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )

