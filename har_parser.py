import json

# Load the HAR file
with open("exactspace.har", "r", encoding="utf-8") as file:
    har_data = json.load(file)

# Get all the request entries
entries = har_data.get("log", {}).get("entries", [])

# Track valid requests by status code categories
status_counts = {
    "1XX": 0,
    "2XX": 0,
    "3XX": 0,
    "4XX": 0,
    "5XX": 0
}

valid_request_count = 0
skipped_requests = 0

# Go through each entry and count valid status codes
for entry in entries:
    status = entry.get("response", {}).get("status", 0)

    if not isinstance(status, int):
        skipped_requests += 1
        continue

    if 100 <= status < 200:
        status_counts["1XX"] += 1
        valid_request_count += 1
    elif 200 <= status < 300:
        status_counts["2XX"] += 1
        valid_request_count += 1
    elif 300 <= status < 400:
        status_counts["3XX"] += 1
        valid_request_count += 1
    elif 400 <= status < 500:
        status_counts["4XX"] += 1
        valid_request_count += 1
    elif 500 <= status < 600:
   
        status_counts["5XX"] += 1
        valid_request_count += 1
    else:
        skipped_requests += 1

# Create the summary list
status_summary = []
for category, count in status_counts.items():
    percentage = (count / valid_request_count * 100) if valid_request_count else 0
    status_summary.append({
        "category": category,
        "count": count,
        "percentage": round(percentage, 2)
    })

# Final result dictionary
result = {
    "total_requests": valid_request_count,
    "status_summary": status_summary
}

# Save the result to a JSON file
with open("network_summary.json", "w", encoding="utf-8") as output_file:
    json.dump(result, output_file, indent=4)

print(" 'network_summary.json' created.")
