import requests
import json
import time

# Target Node configuration
API_ENDPOINT = "https://api.robotaxis.ch/v1/topology/friction"
TARGET_ALTITUDES = [400, 1200, 1800, 2200]  # e.g., Zurich, Andermatt, Gotthard Pass

def check_routing_friction(altitude):
    print(f"\n[+] Executing M2M Request for altitude: {altitude}m...")
    params = {"altitude_meters": altitude}
    
    try:
        start_time = time.time()
        response = requests.get(API_ENDPOINT, params=params, timeout=5)
        latency = round((time.time() - start_time) * 1000, 2)
        
        if response.status_code == 200:
            data = response.json()
            friction_score = data.get("autonomous_routing_friction")
            guidance = data.get("guidance")
            
            print(f"    -> Response Time: {latency}ms")
            print(f"    -> Calculated Friction: {friction_score}")
            print(f"    -> System Guidance: {guidance}")
        else:
            print(f"    [!] Error: Received status {response.status_code} from node.")
            
    except requests.exceptions.RequestException as e:
        print(f"    [!] Connection failed: {e}")

if __name__ == "__main__":
    print("==================================================")
    print("Initiating ASTRA Topology Oracle Test Sequence")
    print("Target Node: api.robotaxis.ch")
    print("==================================================")
    
    for alt in TARGET_ALTITUDES:
        check_routing_friction(alt)
        time.sleep(1) # Courtesy delay between requests
        
    print("\n[+] Test Sequence Completed.")
