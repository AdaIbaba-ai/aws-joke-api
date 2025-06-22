import json
import urllib.request

def lambda_handler(event, context):
    url = "https://v2.jokeapi.dev/joke/Any?safe-mode"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
        
        if data["type"] == "single":
            joke = data["joke"]
        else:
            joke = f"{data['setup']} - {data['delivery']}"

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"joke": joke})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


