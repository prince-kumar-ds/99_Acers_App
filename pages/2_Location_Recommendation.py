import streamlit as st
import pandas as pd
import pickle

st.title("🏠 Property Recommendation System")
st.write("Find properties based on facilities or similar projects")

df_loc = pd.read_csv("df_loc.csv")


#-----------------------------------------------------------




import ast

def parse_dict(x):
    try:
        if isinstance(x, str):
            return ast.literal_eval(x)
        else:
            return {}
    except:
        return {}

df_loc['LocationAdvantages'] = df_loc['LocationAdvantages'].apply(parse_dict)



#---------------------------------------------------------------



def convert_distance(value):

    try:
        value = value.lower().strip()

        if 'km' in value:
            return float(value.replace('km','').strip())

        elif 'meter' in value:
            return float(value.replace('meter','').strip()) / 1000

        elif 'm' in value:
            return float(value.replace('m','').strip()) / 1000

        else:
            return float(value)

    except:
        return None



#-------------------------------------------------------------------


df_loc['LocationAdvantages'] = df_loc['LocationAdvantages'].apply(
    lambda d: {k: convert_distance(v) for k,v in d.items()} if isinstance(d, dict) else {}
)

df_loc['LocationAdvantages'] = df_loc['LocationAdvantages'].apply(
    lambda d: {k.lower(): v for k,v in d.items()} if isinstance(d, dict) else {}
)

#-----------------------------------------------------------------------


def search_properties(location, radius):

    results = []

    for _, row in df_loc.iterrows():

        loc_dict = row['LocationAdvantages']

        if location in loc_dict:

            dist = loc_dict[location]

            if dist <= radius:

                results.append({
                    "PropertyName": row['PropertyName'],
                    "distance": dist,
                    "Link": row['Link']
                })

    return pd.DataFrame(results)


#-----------------------------------------------------------------


unique_locations = set()

for loc_dict in df_loc['LocationAdvantages']:
    
    if isinstance(loc_dict, dict):
        unique_locations.update(loc_dict.keys())


#-------------------------------------------------------------------

import streamlit as st

st.title("📍 Location Based Recommendation")

selected_location = st.selectbox(
    "Select Nearby Location",
    [loc.title() for loc in unique_locations]
).lower()

radius = st.slider(
    "Select Radius (km)",
    0.4,
    20.0,
    5.0,
    0.1
)


#-------------------------------------------------------------------------


if st.button("Search Properties"):

    results = search_properties(selected_location, radius)

    if results.empty:

        st.warning(
            f"No properties found within {radius} km of {selected_location.title()}."
        )

        st.info("Try increasing the radius or selecting another location.")

    else:

        st.success(f"Found {len(results)} properties within {radius} km")

        for _, row in results.iterrows():

            st.subheader(row['PropertyName'])

            st.write(
                f"📏 {row['distance']} km from {selected_location.title()}"
            )

            st.markdown(
                f"[🔗 View Property]({row['Link']})"
            )

            st.divider()


#------------------------------------------------------------------------

st.caption("Built by **Prince Kumar** · Data Scientist · [LinkedIn](https://www.linkedin.com/in/prince-datascientist) · [GitHub](https://github.com/prince-kumar-ds)")