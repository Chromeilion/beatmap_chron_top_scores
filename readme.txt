This is the backend server for osu! rewind.

This server software provides services that osu! rewind relies on to function.

While the intention is to use it with the osu! rewind web client, its basically
just an api, so use it with anything you want really.

Setup:

Create a .env file in /src and set API_KEY, HOST and PORT accordingly.

- API_KEY is an osu api v1 key.
- HOST is the url the server is running at. Can also be localhost if you want
  to use a reverse proxy.
- PORT is the port the webserver is running on.

You need python 3.10 installed and all requirements from requirements.txt
must be satisfied.

Then just run main.py to start the web server.

Refer to the API documentation on how to use the server.
