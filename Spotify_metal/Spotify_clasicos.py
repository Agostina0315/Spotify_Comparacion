import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import pandas as pd

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="eb2c0e4deb1a4de49e0c8a6e387d056c",
    client_secret="af65bac381f04ed5bc13476d9d6a5cd2"
)) 

num_batches = 8
batch_size = 50

for batch in range(num_batches):
    offset = batch * batch_size 
    results = sp.search(q='genre:classical', type='artist', limit=batch_size, offset=offset)
    artistas = results['artists']['items']

    datos = []
    for artist in artistas:
        artist_id = artist['id']

        
        albums = sp.artist_albums(artist_id, album_type='album', limit=50)
        album_ids = set()
        for album in albums['items']:
            album_ids.add(album['id'])
        cantidad_albumes = len(album_ids)

       
        top_tracks = sp.artist_top_tracks(artist_id, country='AR')
        if top_tracks['tracks']:
            mejor_pista = top_tracks['tracks'][0]
            nombre_pista = mejor_pista['name']
            album_pista = mejor_pista['album']['name']
            fecha_pista = mejor_pista['album']['release_date']
        else:
            nombre_pista = ''
            album_pista = ''
            fecha_pista = ''

        for genero in artist['genres']:
            datos.append({
                'nombre': artist['name'],
                'popularidad': artist['popularity'],
                'genero': genero,
                #'url': artist['external_urls']['spotify'],
                'cantidad_albumes': cantidad_albumes,
                'mejor_pista': nombre_pista,
                'album_mejor_pista': album_pista,
                'año_mejor_pista': fecha_pista[:4]  
            })

    df = pd.DataFrame(datos)
    filename = f"classical_batch{batch+1}.csv"
    df.to_csv(filename, index=False)
    print(f"✅ Archivo guardado: {filename}")