# interactive html map from zipcode list, requires lookup table from csv
import pandas as pd
import folium
from folium import plugins


# Read the zipcode lookup table
zip_lookup_df = pd.read_csv('USA_zipcode_to_lat_long.csv')

# Clean and prepare the data
zip_lookup_df = zip_lookup_df.dropna()
# Convert zip_code to string to ensure matching works correctly
zip_lookup_df['zip_code'] = zip_lookup_df['zip_code'].astype(str)

# Print data info
print("Lookup table info:")
print(zip_lookup_df.info())
print("\nSample of lookup table:")
print(zip_lookup_df.head())

# Example input list of zipcodes
zipcodes_to_plot = [
"90008",
 "90010",
 "90011",
 "90012",
 "90013",
 "90014",
 "90015",
 "90016",
 "90017",
 "90018",
 "90019",
 "90020",
 "90021",
 "90022",
 "90023",
 "90024",
 "90025",
 "90026",
 "90027",
 "90028",
 "90029",
 "90031",
 "90032",
 "90033",
 "90034",
 "90035",
 "90036",
 "90037",
 "90038",
 "90039",
 "90040",
 "90041",
 "90042",
]  # Replace with your zipcodes

# Filter the lookup table for our zipcodes and check if we got matches
plot_locations = zip_lookup_df[zip_lookup_df['zip_code'].isin(zipcodes_to_plot)]

print("\nNumber of matches found:", len(plot_locations))
print("\nMatched locations:")
print(plot_locations)

# Check if we have any data to plot
if len(plot_locations) == 0:
    print("No matching zipcodes found in the lookup table!")
else:
    # Option 1: Using Folium (Interactive, works well in Jupyter)
    def create_folium_map(locations_df):
        # Verify data before creating map
        print("\nCreating map with:")
        print(locations_df[['zip_code', 'latitude', 'longitude']])
        
        # Create a map centered on the mean lat/long
        center_lat = locations_df['latitude'].mean()
        center_lng = locations_df['longitude'].mean()
        
        m = folium.Map(location=[center_lat, center_lng], zoom_start=4)
        
        # Add markers for each location
        for idx, row in locations_df.iterrows():
            folium.Marker(
                [float(row['latitude']), float(row['longitude'])],  # Ensure floating point
                popup=f"Zip: {row['zip_code']}"
            ).add_to(m)
        
        return m

    try:
        # Create and display the map
        folium_map = create_folium_map(plot_locations)
        folium_map.save('zipcode_map.html')
        print("\nMap saved successfully as 'zipcode_map.html'")
    except Exception as e:
        print(f"\nError creating map: {str(e)}")

    # Let's also print the actual values we're trying to plot
    print("\nAttempting to plot these coordinates:")
    for _, row in plot_locations.iterrows():
        print(f"Zip: {row['zip_code']}, Lat: {row['latitude']}, Long: {row['longitude']}")
