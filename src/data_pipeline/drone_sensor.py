import time
import random
import json

def generate_drone_telemetry():
    """
    Simulates live drone telemetry data for the Snowflake Smart Agro pipeline.
    Captures crop health indices, soil moisture levels, and location mapping.
    """
    crop_diseases = ["None", "Leaf Blast", "Brown Spot", "Sheath Blight"]
    
    telemetry_data = {
        "timestamp": int(time.time()),
        "drone_id": "DRONE-AGRO-09",
        "gps_coordinates": {
            "latitude": round(random.uniform(25.84, 26.10), 6),  # Simulating Thakurgaon region bounds
            "longitude": round(random.uniform(88.35, 88.55), 6)
        },
        "soil_metrics": {
            "moisture_content_percentage": round(random.uniform(35.5, 78.2), 2),
            "soil_temperature_celsius": round(random.uniform(22.0, 31.5), 1),
            "nitrogen_level_ppm": random.randint(20, 50)
        },
        "crop_health_diagnostics": {
            "ndvi_index": round(random.uniform(0.4, 0.9), 2),  # Normalized Difference Vegetation Index
            "detected_anomaly": random.choice(crop_diseases),
            "infestation_risk": random.choice(["Low", "Medium", "High"])
        }
    }
    return telemetry_data

if __name__ == "__main__":
    print("--- Starting Live Snowflake CoCo Agro Ingestion Pipeline ---")
    # Simulate 3 frames of live data ingestion
    for i in range(3):
        sample_feed = generate_drone_telemetry()
        print(json.dumps(sample_feed, indent=4))
        time.sleep(1)
