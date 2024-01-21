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
            color='blue' if row['audio_cue'] else 'red',
            fill=True,
            # fill_color='blue' if row['audio_cue'] else 'red',
            tooltip=f"Street: {row['RUE_1']} / {row['RUE_2']}",  # This will display when you hover over the marker
        ).add_to(map_montreal)
        
    # Add a legend to the map
    legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; 
                right: 50px; 
                width: auto; 
                height: auto; 
                border:2px solid grey; 
                z-index:9999; 
                font-size:14px;
                background-color: white;">
    <b>Legend</b><br>
    <i class="fa fa-circle fa-1x" style="color:blue"></i> With Audio Cue<br>
    <i class="fa fa-circle fa-1x" style="color:red"></i> Without Audio Cue
    </div>
    '''
    map_montreal.get_root().html.add_child(folium.Element(legend_html))

    # Save the map to an HTML file
    html_file = 'assets/AudioCUEMap.html'
    map_montreal.save(html_file)
    return send_file(html_file, mimetype='text/html')

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
                color = 'yellow'
            elif row['NB_VICTIMES_PIETON'] == 2:
                color = 'orange'
            else:
                color = 'red'
            
            folium.CircleMarker(
                location=[row['LOC_LAT'], row['LOC_LONG']],
                radius=6,  # Adjust the size of the circle markers here
                color=color,
                fill=True,
            ).add_to(map_montreal)
        
    # Add a legend to the map
    legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; 
                right: 50px; 
                width: auto; 
                height: auto; 
                border:2px solid grey; 
                z-index:9999; 
                font-size:14px;
                background-color: white;">
    <b>Legend</b><br>
    <i class="fa fa-circle fa-1x" style="color:yellow"></i> 1 person<br>
    <i class="fa fa-circle fa-1x" style="color:orange"></i> 2 people<br>
    <i class="fa fa-circle fa-1x" style="color:red"></i> 3+ people
    </div>
    '''
    map_montreal.get_root().html.add_child(folium.Element(legend_html))

    # Save the map to an HTML file
    html_file = 'assets/montreal_map2.html'
    map_montreal.save(html_file)
    return send_file(html_file, mimetype='text/html')

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
            color = 'red'
            
            folium.CircleMarker(
                location=[row['LOC_LAT'], row['LOC_LONG']],
                radius=6,  # Adjust the size of the circle markers here
                color=color,
                fill=True,
            ).add_to(map_montreal)
            
    for index, row in df2.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=6,  # Adjust the size of the circle markers here
            color='blue',
            fill=True,
        ).add_to(map_montreal)
        
    # Add a legend to the map
    legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; 
                right: 50px; 
                width: auto; 
                height: auto; 
                border:2px solid grey; 
                z-index:9999; 
                font-size:14px;
                background-color: white;">
    <b>Legend</b><br>
    <i class="fa fa-circle fa-1x" style="color:red"></i> Collisions with 2 or more pedestrians<br>
    <i class="fa fa-circle fa-1x" style="color:blue"></i> Pedestrian crossings with audible signals
    </div>
    '''
    map_montreal.get_root().html.add_child(folium.Element(legend_html))

    # Save the map to an HTML file
    html_file = 'assets/montreal_map3.html'
    map_montreal.save(html_file)
    return send_file(html_file, mimetype='text/html')

if __name__ == '__main__':
    app.run()