$request_uri="https://99xoxbk3x1.execute-api.eu-central-1.amazonaws.com/api/"

$json_response = Invoke-WebRequest -UseBasicParsing -URI $request_uri`
$response=ConvertFrom-Json $json_response

$streaming_url=$response.StreamingURL

Start-Process -FilePath "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -ArgumentList "$streaming_url", "--new-window", "--app"