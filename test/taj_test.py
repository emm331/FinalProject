# this is the AppleMusicToSpotify/test/taj_test file...
from app.tajMusic import song_list_generator, artist_list_generator, album_list_generator
import os

xml_filepath = os.path.join(os.path.dirname(__file__), "..", "Music.xml")

def test_xml_parse_song():
    results = song_list_generator(xml_filepath)
   # breakpoint()
    assert results == ['Delicate', 'Look What You Made Me Do', 'I Did Something Bad', 'Don’t Blame Me', 'End Game (feat. Ed Sheeran & Future)', '...Ready For It?', 'Hope Will Lead Us On', 'Call It What You Want', 'Hold Up', 'New Year’s Day', 'Dress', 'This Is Why We Can’t Have Nice Things', 'King of My Heart', 'Dancing With Our Hands Tied', 'Gorgeous', 'Getaway Car', 'So It Goes...']

def test_xml_parse_artist():
    results = artist_list_generator(xml_filepath)
    #breakpoint()
    assert results == ['Taylor Swift', 'Taylor Swift', 'Taylor Swift', 'Taylor Swift', 'Taylor Swift', 'Taylor Swift', 'BarlowGirl', 'Taylor Swift', 'Beyoncé', 'Taylor Swift', 'Taylor Swift', 'Taylor Swift', 'Taylor Swift', 'Taylor Swift', 'Taylor Swift', 'Taylor Swift', 'Taylor Swift']

def test_xml_parse_album():
    results = album_list_generator(xml_filepath)
    #breakpoint()
    assert results == ['reputation', 'reputation', 'reputation', 'reputation', 'reputation', 'reputation', 'Christian', 'reputation', 'Lemonade', 'reputation', 'reputation', 'reputation', 'reputation', 'reputation', 'reputation', 'reputation', 'reputation']