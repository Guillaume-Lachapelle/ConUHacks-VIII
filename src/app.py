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
    
    ng_feux_pietons = 0
    nb_signal_sonore = 0
    # Add points from the dataframe to the map using circle markers
    for index, row in df.iterrows():
        if row['audio_cue']:
            nb_signal_sonore += 1
        else:
            ng_feux_pietons += 1
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
    return str(ng_feux_pietons) + ',' + str(nb_signal_sonore)


@app.route('/generate_map2')
def generate_map2():
    # Load the two CSV files
    df = pd.read_csv('assets/collisions_routieres.csv')


    # Create a map centered around Montreal
    map_montreal = folium.Map(location=[45.5017, -73.5673], zoom_start=12)

    nb_collisions_yellow = 0
    nb_collisions_orange = 0
    nb_collisions_red = 0
    # Add points from the dataframe to the map using circle markers
    for index, row in df.iterrows():
    
        if row['NB_VICTIMES_PIETON'] > 0:
            if row['NB_VICTIMES_PIETON'] == 1:
                color = '#e3e344'
                nb_collisions_yellow += 1
            elif row['NB_VICTIMES_PIETON'] == 2:
                color = '#fc9c0a'
                nb_collisions_orange += 1
            else:
                color = 'red'
                nb_collisions_red += 1
            
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
    return str(nb_collisions_yellow) + ',' + str(nb_collisions_orange) + ',' + str(nb_collisions_red)

@app.route('/generate_map3')
def generate_map3():
    # Load the two CSV files
    df1 = pd.read_csv('assets/collisions_routieres.csv')
    df2 = pd.read_csv('assets/traverses-pietonnes-signal-sonore.csv')

    # Create a map centered around Montreal
    map_montreal = folium.Map(location=[45.5017, -73.5673], zoom_start=12)

    pedestrian_collisions = 0
    # Add points from the dataframe to the map using circle markers
    for index, row in df1.iterrows():
        if row['NB_VICTIMES_PIETON'] >= 2:
         
            pedestrian_collisions += 1
            folium.CircleMarker(
                location=[row['LOC_LAT'], row['LOC_LONG']],
                radius=6,  # Adjust the size of the circle markers here
                color = 'red',
                fill=True,
            ).add_to(map_montreal)
            
    audio_signal_count = 0
    for index, row in df2.iterrows():
        audio_signal_count += 1
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
    return str(pedestrian_collisions) + ',' + str(audio_signal_count)

if __name__ == '__main__':
    app.run()