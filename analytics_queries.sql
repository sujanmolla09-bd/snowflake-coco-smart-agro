-- Snowflake CoCo Smart Agro Engine Analytics Queries
-- Target Schema: SMART_AGRO_DB.PUBLIC

-- 1. Create Telemetry Table if not exists
CREATE TABLE IF NOT EXISTS AGRO_TELEMETRY_LOGS (
    sensor_id VARCHAR(50),
    temperature FLOAT,
    humidity FLOAT,
    soil_moisture FLOAT,
    timestamp TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

-- 2. Query Average Temperature and Humidity across Field Sensors
SELECT 
    sensor_id,
    ROUND(AVG(temperature), 2) AS avg_temperature,
    ROUND(AVG(humidity), 2) AS avg_humidity,
    ROUND(AVG(soil_moisture), 2) AS avg_soil_moisture,
    COUNT(*) AS total_readings
FROM AGRO_TELEMETRY_LOGS
GROUP BY sensor_id
ORDER BY total_readings DESC;

-- 3. AI Crop Health Anomaly Detection Query
SELECT 
    sensor_id,
    temperature,
    humidity,
    soil_moisture,
    timestamp,
    CASE 
        WHEN soil_moisture < 35.0 THEN 'CRITICAL: Irrigation Needed'
        WHEN temperature > 32.0 THEN 'WARNING: High Heat Index'
        ELSE 'OPTIMAL: Normal Crop Status'
    END AS crop_health_status
FROM AGRO_TELEMETRY_LOGS
WHERE timestamp >= DATEADD('day', -7, CURRENT_TIMESTAMP())
ORDER BY timestamp DESC;
