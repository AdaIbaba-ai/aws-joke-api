README.md (Vorlage für Doku)
markdown
Copy
Edit
# AWS Joke API (Serverless Project)

## Projektziel

Erstellung einer eigenen Mini-REST-API mit AWS Lambda und API Gateway. Die Funktion ruft bei jedem HTTP-Aufruf einen zufälligen Witz von der öffentlichen JokeAPI ab und liefert ihn als JSON zurück.

## Verwendete AWS-Services

- **AWS Lambda** – Hauptfunktion zum Abrufen des Witzes
- **API Gateway** – HTTP-Zugriff auf die Lambda-Funktion
- **CloudWatch Logs** – zur Fehleranalyse und Überprüfung

## Architektur

Client (Browser) → API Gateway → Lambda → JokeAPI → Antwort zurück

markdown
Copy
Edit

## Ablauf

1. Der Benutzer sendet einen HTTP GET-Request an die API-URL
2. Die Lambda-Funktion wird ausgelöst
3. Sie ruft `https://v2.jokeapi.dev/joke/Any` auf
4. Die Antwort wird verarbeitet und zurückgesendet

## Screenshots

Siehe Ordner `screenshots/` für:

- Lambda-Code
- API-Antwort
- Logs

##  Beispielantwort

```json
{
  "joke": "Why do they call it hyper terminal? - Too much Java."
}