##############################################################
# convert_zipcodes_to_geocode_latitude_longitude_in_pandas_df
##############################################################
"""
This assumes that the columns in your lookup-table are name:
    "zip_code"
    "latitude"
    "longitude"
    
    
This assumes that the last two columns in your df are:
    "latitude", "longitude"
in that order.
(spelling of the names is not needed, just being the last two columns.)

Exceptions caught below may include string values.

Use this for a notebook: (add the "!")
!wget("https://raw.githubusercontent.com/lineality/convert_zipcodes_to_geocode_latitude_longitude_in_pandas_df/main/USA_zipcode_to_lat_long.csv")

"""
import pandas as pd

# get lookup table
wget("https://raw.githubusercontent.com/lineality/convert_zipcodes_to_geocode_latitude_longitude_in_pandas_df/main/USA_zipcode_to_lat_long.csv")

# load lookup table
zip_df = pd.read_csv("USA_zipcode_to_lat_long.csv")

how_zipcode_is_named_in_your_csv = "Zip"

# iterate through df and make lat long
for index, value in df[how_zipcode_is_named_in_your_csv].iteritems():

    try:
        value = float(value)
        shape_number = df.shape[0]

        # inspection
        # print(f"index= {index}, value={value} (type:{type(value)}) out of {shape_number}")

        if len(zip_df[zip_df["zip_code"] == value]):

            # geolat
            df.iloc[index, -2] = zip_df[zip_df["zip_code"] == value]["latitude"].values[0]

            # geolong
            df.iloc[index, -1] = zip_df[zip_df["zip_code"] == value]["longitude"].values[0]

        # else: print("0")
        
    except:
        print(f"index= {index}, value={value} (type:{type(value)}) out of {shape_number}")

print("Done!")

# Make csv:
df.to_csv("NAME_YOU_WANT_v01.csv", index = False)
