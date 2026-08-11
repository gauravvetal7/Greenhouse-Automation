


#include <Arduino.h>
#include <DHT.h>

#include <WiFi.h>
#include <HTTPClient.h>



// --- Pin Configurations ---
#define DHTPIN 23
#define DHTTYPE DHT11

#define SOIL_MOISTURE_PIN 34  // Analog pin for soil sensor
#define LDR_PIN 35           // Analog pin for light sensor

#define RELAY_PUMP_PIN 18
#define RELAY_FAN_PIN 19
#define RELAY_LIGHTS_PIN 21

// ---------- Wi-Fi Credentials ----------
const char* ssid = "Gaurav";
const char* password = "12345678";

// Flask API URL
const char* serverURL = "http://10.126.217.28:5000/update";
// --- Automation Thresholds ---
const float TEMP_THRESHOLD_HIGH = 30.0; // Turn fan on above 30°C
const int SOIL_THRESHOLD_LOW    = 40;   // Turn pump on below 40%
const int LIGHT_THRESHOLD_LOW   = 30;   // Turn lights on below 30% percentage

// --- Timing Constants ---
const unsigned long POLLING_INTERVAL = 2000; // Poll sensors every 2 seconds
unsigned long lastPollTime = 0;

DHT dht(DHTPIN, DHTTYPE);

// --- Function Declarations ---
void readSensors(float &temp, float &humidity, int &soilMoisture, int &lightIntensity);
void executeAutomationLogic(float temp, int soilMoisture, int lightIntensity);
void sendDataToServer(float temp, float humidity, int soil, int light);

void setup() {
    Serial.begin(115200);

    WiFi.begin(ssid, password);

    Serial.print("Connecting to WiFi");

    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }

Serial.println();
Serial.println("WiFi Connected!");
Serial.print("ESP32 IP Address: ");
Serial.println(WiFi.localIP());
    
    // Initialize Sensor
    dht.begin();
    
    // Initialize Actuator Pins as Output
    pinMode(RELAY_PUMP_PIN, OUTPUT);
    pinMode(RELAY_FAN_PIN, OUTPUT);
    pinMode(RELAY_LIGHTS_PIN, OUTPUT);
    
    //  all actuators are OFF initially
    digitalWrite(RELAY_PUMP_PIN, HIGH);
    digitalWrite(RELAY_FAN_PIN, HIGH);
    digitalWrite(RELAY_LIGHTS_PIN, HIGH);

    Serial.println("Greenhouse Automation System Initialized Successfully.");
}

void loop() {
    unsigned long currentMillis = millis();
    
    
    if (currentMillis - lastPollTime >= POLLING_INTERVAL) {
        lastPollTime = currentMillis;
        
        float temperature = 0.0;
        float humidity = 0.0;
        int soilMoisture = 0;
        int lightIntensity = 0;
        
        readSensors(temperature, humidity, soilMoisture, lightIntensity);
        executeAutomationLogic(temperature, soilMoisture, lightIntensity);
        if (!isnan(temperature) && !isnan(humidity)){
            
    sendDataToServer(
        temperature,
        humidity,
        soilMoisture,
        lightIntensity
    );
}
else
{
    Serial.println("DHT read failed. Skipping HTTP request.");
}
    }
}

/**
 * @brief Reads data from environmental sensors and maps analog values to percentages.
 */
void readSensors(float &temp, float &humidity, int &soilMoisture, int &lightIntensity) {
    temp = dht.readTemperature();
    humidity = dht.readHumidity();
    
    // Read and map Soil Moisture (0-4095 on ESP32 ADC) -> 0% to 100%
    // Note: Calibrate 3500 (dry) and 1500 (wet) values based on your specific sensor hardware
    int rawSoil = analogRead(SOIL_MOISTURE_PIN);
    soilMoisture = map(rawSoil, 4095, 1200, 0, 100); 
    soilMoisture = constrain(soilMoisture, 0, 100);

    // Read and map Ambient Light
    int rawLDR = analogRead(LDR_PIN);
    lightIntensity = map(rawLDR, 0, 4095, 0, 100);
    
    // Error Checking
    if (isnan(temp) || isnan(humidity)) {
        Serial.println("Warning: Failed to read from DHT sensor!");
    }
}

/**
 * @brief Implements automation control loop using active-low relay logic.
 */
void executeAutomationLogic(float temp, int soilMoisture, int lightIntensity) {
    Serial.printf("\n--- Telemetry: Temp: %.1f°C | Soil: %d%% | Light: %d%% ---\n", temp, soilMoisture, lightIntensity);

    // 1. Ventilation Control (Fan)
    if (temp > TEMP_THRESHOLD_HIGH) {
        digitalWrite(RELAY_FAN_PIN, LOW); // Turn ON Fan
        Serial.println("[ACTUATOR] High Temperature Detected! Fan turned ON.");
    } else {
        digitalWrite(RELAY_FAN_PIN, HIGH); // Turn OFF Fan
    }

    // 2. Irrigation Control (Water Pump)
    if (soilMoisture < SOIL_THRESHOLD_LOW) {
        digitalWrite(RELAY_PUMP_PIN, LOW); // Turn ON Pump
        Serial.println("[ACTUATOR] Low Soil Moisture Detected! Irrigation Loop Active.");
    } else {
        digitalWrite(RELAY_PUMP_PIN, HIGH); // Turn OFF Pump
    }

    // 3. Lighting Control (Grow Lights)
    if (lightIntensity < LIGHT_THRESHOLD_LOW) {
        digitalWrite(RELAY_LIGHTS_PIN, LOW); // Turn ON Artificial Lights
        Serial.println("[ACTUATOR] Low Ambient Light Detected! Lighting System Active.");
    } else {
        digitalWrite(RELAY_LIGHTS_PIN, HIGH); // Turn OFF Lights
    }
}

void sendDataToServer(float temp, float humidity, int soil, int light)
{
    if (WiFi.status() == WL_CONNECTED)
    {
        HTTPClient http;

        http.begin(serverURL);

        http.addHeader("Content-Type", "application/json");

        String jsonData = "{";
        jsonData += "\"temperature\":" + String(temp, 1) + ",";
        jsonData += "\"humidity\":" + String(humidity, 1) + ",";
        jsonData += "\"soil\":" + String(soil) + ",";
        jsonData += "\"light\":" + String(light);
        jsonData += "}";


        Serial.println("Sending JSON:");
        Serial.println(jsonData);

        int httpResponseCode = http.POST(jsonData);

        Serial.print("HTTP Response: ");
        Serial.println(httpResponseCode);

        http.end();
    }
    else
    {
        Serial.println("WiFi Disconnected");
    }
}