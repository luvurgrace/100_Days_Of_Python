"""
Music Charts by Country

Shows top songs from different countries using iTunes RSS API.
No API key needed!
"""

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Available countries
COUNTRIES = {
    'us': '🇺🇸 USA',
    'gb': '🇬🇧 UK',
    'ru': '🇷🇺 Russia',
    'de': '🇩🇪 Germany',
    'fr': '🇫🇷 France',
    'jp': '🇯🇵 Japan',
    'kr': '🇰🇷 South Korea',
    'br': '🇧🇷 Brazil',
    'au': '🇦🇺 Australia',
    'ca': '🇨🇦 Canada',
    'es': '🇪🇸 Spain',
    'it': '🇮🇹 Italy',
    'mx': '🇲🇽 Mexico',
    'se': '🇸🇪 Sweden',
    'pl': '🇵🇱 Poland',
    'by': '🇧🇾 Belarus',
    'ua': '🇺🇦 Ukraine',
    'kz': '🇰🇿 Kazakhstan',
}


def get_top_songs(country_code, limit=25):
    """Get top songs for a country from iTunes"""
    url = f"https://itunes.apple.com/{country_code}/rss/topsongs/limit={limit}/json"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            entries = data.get('feed', {}).get('entry', [])

            songs = []
            for i, entry in enumerate(entries, 1):
                song = {
                    'rank': i,
                    'title': entry.get('im:name', {}).get('label', 'Unknown'),
                    'artist': entry.get('im:artist', {}).get('label', 'Unknown'),
                    'album': entry.get('im:collection', {}).get('im:name', {}).get('label', ''),
                    'image': entry.get('im:image', [{}])[-1].get('label', ''),
                    'preview': '',
                    'link': entry.get('link', [{}])[-1].get('attributes', {}).get('href', '')
                }

                # Get preview URL
                for link in entry.get('link', []):
                    attrs = link.get('attributes', {})
                    if attrs.get('type') == 'audio/x-m4a':
                        song['preview'] = attrs.get('href', '')
                        break

                songs.append(song)

            return songs, None
        else:
            return [], "Failed to load charts"

    except Exception as e:
        return [], str(e)


@app.route('/')
def index():
    country = request.args.get('country', 'us')

    if country not in COUNTRIES:
        country = 'us'

    songs, error = get_top_songs(country)

    return render_template('index.html',
                           countries=COUNTRIES,
                           selected_country=country,
                           country_name=COUNTRIES[country],
                           songs=songs,
                           error=error)


if __name__ == '__main__':
    app.run(debug=True)