# README.md
## Setup

Create and activate a virtual environment:

```sh
conda create -n playlist-env python=3.8

conda activate playlist-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

### Export Apple Music playlists to XML File
The first step is to select the playlist you want to import over and export it as an XML file. 
This is done by going to Apple Music, selecting File -> Library -> Export Playlist. 
Save the resuting file in the same directory as where you cloned this repository.
Note: the playlist much be greater than 1 song.

### Create a Spotify app 
Create a Spotify app at the [spotify developer dashboard](https://developer.spotify.com/dashboard/applications) and select redirect url to `http://localhost:8888/callback`
- Create WebApp
- Edit Settings
- Redirect URIs -> http://localhost:8888/callback -> Add -> Save
- Go to .env file and securely set Client ID and Client Secret from your newly created app 

```sh
# this is the ".env" file...

client_id="_________"
client_secret="__________"
```


###
After running the web app (instructions below), log on to your Spotify account, and enjoy your newly created playlist!

### Web App

Run the web app (then view in the browser at http://localhost:5000):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testing

Run test:
```sh
pytest
```

## To Do

https://taj-converter.herokuapp.com/
^This link displays the web app and runs it; however, it hangs and fails when it runs for longer than 30 seconds. Something that we will further investigate is trying to fix this problem and helping the public web app run quicker

Another to do item is adding more dynamic testing options in the taj_test.py file. This testing would include ways to test for successful playlist creation on the Spotify side of things

Also, our code climat score is an F right now. One thing we will explore is raising this score and helping our code become more efficient

In regards to Dev Process, we had an issue on 12/9 after a series of revisions where we could not obtain older commits. Our solution was to create a new repository from scratch, which was submitted. Our old repository (https://github.com/emm331/AppleMusicToSpotify) is a more accurate representation of our process, as we utilized branching and forking through a series of commits from each group member.
