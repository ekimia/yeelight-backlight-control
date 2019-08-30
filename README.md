# Yeelight Ambilight Control

## What does this do?
It's a tiny Flask app to control the ambilight on Yeelights that have them.

## Why?
I love Yeelight. I especially love their ceiling lights which I have 4 of. What I dont like is how I cant control the background light via any sort of integration - especially Google Assistant and Alexa.

## So how do I use this?
Numerous ways, but ill explain how I use it with Google Assistant:
* Get a computer on your network to act as the middle man, and install [ngrok](https://ngrok.com/) on it. It's free.
* Once ngrok is setup, configure it to point to your computer at port 5000
* start your ngrok tunnel
* Set fixed IPs for your Yeelight(s), and modify the code with them.
* run `flask run`
* Setup an [IFTT](https://ifttt.com/google_assistant) account

### Turning On the Lights
* Connect your Google Assistant account
* Create a new applet. Call it turn on the lights
* Add a That trigger to point to `NGROK_HOSTNAMEyeelight-control/turn-on`
* You did it! Just tell Google Assistant that phrase and it will turn on your ambilighgs

### Turning off the Lights
* Repeat the above steps after creating and linking a Google Assistant app, but change the end of the endpoint to `turn-off`

## But why is this code so bad?
Because im hoping Yeelight realizes that having full control of both the primary and background lights is an enormous draw to their products, and that it's clearly doable.

If this does turn into a well written piece of open source software like the [Yeelight Python Library](https://yeelight.readthedocs.io/en/latest/) I will be severely disappointed.

And Yeelight - if you're reading this - feel free to add an issue to this repo so I can help you do it!
