 # Model Description


[SILERO] Text TO SPEECH MODEL


# How API works

The api takes two payloads namely:

1. text (your text message to be converted)

    ```python
        headers = {'content-type': 'application/json'}
        response = requests.post('localhost/api/v1/convert', data={
        'text': 'your text'
        }, headers=headers)

    ```


# System Requirements
| RAM | GPU|
| :-: | :-: |
| 8G| Not required|

