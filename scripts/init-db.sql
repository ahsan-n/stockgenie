-- StockGenie Database Initialization Script
-- This runs automatically when PostgreSQL container is first created

-- Enable TimescaleDB extension
CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Create initial database (if not exists)
-- Note: Main database is created via POSTGRES_DB env var

-- Grant necessary permissions
GRANT ALL PRIVILEGES ON DATABASE stockgenie_db TO stockgenie;

-- Create schema for organizing tables (optional)
-- CREATE SCHEMA IF NOT EXISTS market_data;
-- CREATE SCHEMA IF NOT EXISTS financial_statements;

-- Success message
DO $$
BEGIN
    RAISE NOTICE 'StockGenie database initialized successfully';
END $$;

