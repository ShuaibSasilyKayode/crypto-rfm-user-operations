-- Core Users Profile Table
CREATE TABLE users (
    user_id VARCHAR(64) PRIMARY KEY,
    registration_date TIMESTAMP NOT NULL,
    country_code VARCHAR(3) NOT NULL,
    kyc_status VARCHAR(20) DEFAULT 'Unverified'
);

-- High-Frequency Transaction Ledger
CREATE TABLE user_transactions (
    transaction_id VARCHAR(64) PRIMARY KEY,
    user_id VARCHAR(64) REFERENCES users(user_id),
    block_time TIMESTAMP NOT NULL,
    order_type VARCHAR(30) NOT NULL,
    asset_symbol VARCHAR(10) NOT NULL,
    amount NUMERIC(28, 8) NOT NULL,
    volume_usd NUMERIC(18, 2) NOT NULL
);

-- Optimization Layer for Analytics Telemetry
CREATE INDEX idx_transactions_user_time ON user_transactions (user_id, block_time DESC);
