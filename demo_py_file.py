import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col, avg
from datetime import datetime

def main(session: snowpark.Session):
    """
    Snowflake Snowpark Pipeline for Smart Agro Telemetry
    Connects with active Snowflake session and ingests AI-driven crop telemetry data.
    """
    # Print active session details for debugging
    current_db = session.get_current_database()
    current_schema = session.get_current_schema()
    print(f"Connected to Snowflake Database: {current_db}, Schema: {current_schema}")

    # Sample Smart Agro Telemetry Data Structure
    telemetry_data = [
        {"sensor_id": "DRONE-01", "temperature": 28.5, "humidity": 75.2, "soil_moisture": 42.0, "timestamp": datetime.now()},
        {"sensor_id": "DRONE-02", "temperature": 29.1, "humidity": 72.8, "soil_moisture": 40.5, "timestamp": datetime.now()},
        {"sensor_id": "IOT-FIELD-A", "temperature": 27.8, "humidity": 78.0, "soil_moisture": 45.1, "timestamp": datetime.now()}
    ]

    # Convert Python dictionary list to Snowflake Dataframe
    df = session.create_dataframe(telemetry_data)
    
    # Save/Append to Snowflake Table
    table_name = "AGRO_TELEMETRY_LOGS"
    df.write.mode("append").save_as_table(table_name)
    
    # Fetch and aggregate average telemetry metrics
    summary_df = session.table(table_name).group_by("sensor_id").agg(
        avg(col("temperature")).alias("AVG_TEMP"),
        avg(col("humidity")).alias("AVG_HUMIDITY")
    )

    return summary_df

# Entry point for Snowflake Python Worksheets
if __name__ == "__main__":
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
    result = main(session)
    result.show()
