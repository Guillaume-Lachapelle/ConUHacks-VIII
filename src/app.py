from flask import Flask, send_file
import pandas as pd
import folium
import os

app = Flask(__name__)

@app.route('/generate_map')
def generate_map():
    # Load the two CSV files
    df1 = pd.read_csv('assets/feux-pietons.csv')
    df2 = pd.read_csv('assets/traverses-pietonnes-signal-sonore.csv')

    # Add a new column to df1 that indicates whether each intersection has an audio queue
    df1['audio_cue'] = df1['INT_NO'].isin(df2['INT_NO'])

    # Save the merged dataframe to a new CSV file
    df1.to_csv('assets/merged_file.csv', index=False)
    
    # Load the CSV file
    df = pd.read_csv('assets/merged_file.csv')

    # Create a map centered around Montreal
    map_montreal = folium.Map(location=[45.5017, -73.5673], zoom_start=12)
    
    # Add points from the dataframe to the map using circle markers
    for index, row in df.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=6,  # Adjust the size of the circle markers here
            color='#104a1c' if row['audio_cue'] else '#cf13bc',
            fill=True,
            # fill_color='#338f4c' if row['audio_cue'] else '#822b3d',
            tooltip=f"Street: {row['RUE_1']} / {row['RUE_2']}",  # This will display when you hover over the marker
        ).add_to(map_montreal)      

    # Save the map to an HTML file
    html_file = 'assets/AudioCUEMap.html'
    map_montreal.save(html_file)
    html_file_dark = 'assets/darkAudioCUEMap.html'
    dark_mode = map_montreal
    folium.TileLayer('cartodbdark_matter').add_to(dark_mode)
    dark_mode.save(html_file_dark)
    return 'Map generated!'


@app.route('/generate_map2')
def generate_map2():
    # Load the two CSV files
    df = pd.read_csv('assets/collisions_routieres.csv')


    # Create a map centered around Montreal
    map_montreal = folium.Map(location=[45.5017, -73.5673], zoom_start=12)

    # Add points from the dataframe to the map using circle markers
    for index, row in df.iterrows():
    
        if row['NB_VICTIMES_PIETON'] > 0:
            if row['NB_VICTIMES_PIETON'] == 1:
                color = '#e3e344'
            elif row['NB_VICTIMES_PIETON'] == 2:
                color = '#fc9c0a'
            else:
                color = 'red'
            
            folium.CircleMarker(
                location=[row['LOC_LAT'], row['LOC_LONG']],
                radius=6,  # Adjust the size of the circle markers here
                color=color,
                fill=True,
            ).add_to(map_montreal)
        

    # Save the map to an HTML file
    html_file = 'assets/montreal_map2.html'
    map_montreal.save(html_file)
    html_file_dark = 'assets/dark_montreal_map2.html'
    dark_mode = map_montreal
    folium.TileLayer('cartodbdark_matter').add_to(dark_mode)
    dark_mode.save(html_file_dark)
    return 'Map generated!'

@app.route('/generate_map3')
def generate_map3():
    # Load the two CSV files
    df1 = pd.read_csv('assets/collisions_routieres.csv')
    df2 = pd.read_csv('assets/traverses-pietonnes-signal-sonore.csv')

    # Create a map centered around Montreal
    map_montreal = folium.Map(location=[45.5017, -73.5673], zoom_start=12)

    # Add points from the dataframe to the map using circle markers
    for index, row in df1.iterrows():
        if row['NB_VICTIMES_PIETON'] >= 2:
         
            
            folium.CircleMarker(
                location=[row['LOC_LAT'], row['LOC_LONG']],
                radius=6,  # Adjust the size of the circle markers here
                color = 'red',
                fill=True,
            ).add_to(map_montreal)
            
    for index, row in df2.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=6,  # Adjust the size of the circle markers here
            color='blue',
            fill=True,
        ).add_to(map_montreal)
        

    # Save the map to an HTML file
    html_file = 'assets/montreal_map3.html'
    map_montreal.save(html_file)
    html_file_dark = 'assets/dark_montreal_map3.html'
    dark_mode = map_montreal
    folium.TileLayer('cartodbdark_matter').add_to(dark_mode)
    dark_mode.save(html_file_dark)
    return 'Map generated!'

if __name__ == '__main__':
    app.run()