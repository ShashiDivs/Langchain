from dotenv import load_dotenv
import os
import json
import datetime
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Load environment variables
load_dotenv()

# Fetch API key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=GEMINI_API_KEY)

# Output parser for JSON validation
json_parser = JsonOutputParser()

# First template to generate network data with anomalies
template1 = PromptTemplate(
    template="""
    Generate network monitoring data with the following specifications:
    - Start time: {start_time}
    - End time: {end_time}
    - Interval: {interval} minutes
    - Include fields: timestamp, error_count, value, anomaly

    Anomaly Instructions:
    {anomaly_pattern}

    Return the data as a valid JSON array. Each data point should have this format:
    {{
      "timestamp": "ISO8601 format with Z suffix",
      "error_count": integer (0-100),
      "value": float (0-100),
      "anomaly": boolean (true/false)
    }}
    """,
    input_variables=["start_time", "end_time", "interval", "anomaly_pattern"]
)

# Second template to validate and fix the data
template2 = PromptTemplate(
    template="""
    The following is network monitoring data that may contain formatting issues:
    
    {raw_data}
    
    Validate and fix any issues with this data. Ensure:
    1. All timestamps follow ISO8601 format with Z suffix
    2. All timestamps are exactly {interval} minutes apart
    3. error_count is an integer between 0-100
    4. value is a float between 0-100
    5. anomaly is a boolean (true/false)
    6. Anomalies follow this pattern: {anomaly_pattern}
    
    Return only the fixed data as a valid JSON array.
    """,
    input_variables=["raw_data", "interval", "anomaly_pattern"]
)

# Generate timestamps in ISO8601 format
start_time = datetime.datetime.utcnow().replace(microsecond=0, second=0).isoformat() + "Z"
end_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=2)).replace(microsecond=0, second=0).isoformat() + "Z"
interval = 5
anomaly_pattern = "Inject anomalies every 5 minutes with significantly higher error counts"

try:
    # Generate raw network data with anomalies
    raw_data_response = model.invoke(template1.format(
        start_time=start_time,
        end_time=end_time,
        interval=interval,
        anomaly_pattern=anomaly_pattern
    ))

    # Extract content from AIMessage (if applicable)
    raw_data_text = raw_data_response.content if hasattr(raw_data_response, "content") else str(raw_data_response)

    # Parse raw JSON response
    raw_data = json_parser.parse(raw_data_text)

    # Validate and fix the generated data
    validated_data_response = model.invoke(template2.format(
        raw_data=json.dumps(raw_data, indent=2),
        interval=interval,
        anomaly_pattern=anomaly_pattern
    ))

    # Extract content from AIMessage
    validated_data_text = validated_data_response.content if hasattr(validated_data_response, "content") else str(validated_data_response)

    # Parse the validated JSON response
    validated_data = json_parser.parse(validated_data_text)

    # Save validated data to a JSON file
    with open("network_anomalies.json", "w") as f:
        json.dump(validated_data, f, indent=2)

    # Print results
    print(f"Generated {len(validated_data)} data points")
    print("First two data points:")
    print(json.dumps(validated_data[:2], indent=2))

except Exception as e:
    print(f"Error occurred: {str(e)}")
