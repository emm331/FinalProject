# this is the AppleMusicToSpotify/web_app/routes/convert_routes.py file...

from flask import Blueprint, request, render_template, redirect, flash

from app.tajMusic import get_username, create_playlist, add_songs_to_playlist, add_song_ids, add_to_playlist, song_list_generator, artist_list_generator, album_list_generator #get_missing_track_id

convert_routes = Blueprint("convert_routes", __name__)

@convert_routes.route("/convert/playlist", methods=["POST"])
def convert_playlist():
    request_data = dict(request.form)

    name = request_data.get("name") or "Taj on Aux"
    username = request_data.get("username")
    XML = request.files["XML"].filename

    try:
        song_l = song_list_generator(XML)
        artist_l = artist_list_generator(XML)
        album_l = album_list_generator(XML)
        track_id = []

        playlist_id = create_playlist(username, name)
        track_id = add_to_playlist(song_l, artist_l, album_l, username, playlist_id, track_id)

        return render_template("playlist.html",
            username=username, name=name)
  
    except Exception as err:
          print("Oops")
          return redirect("/convert")