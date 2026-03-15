import streamlit as st
import pandas as pd
import pickle
import ast

st.title("🏠 Property Recommendation System")

st.write("Select a property to find similar projects based on amenities")

st.title("🏢 Facility Based Recommendation")

df_top = pd.read_csv("df_top.csv")

#----------------------------------------------

def parse_facilities(x):
    try:
        if isinstance(x, str):
            return ast.literal_eval(x)
        else:
            return []
    except:
        return []

df_top['TopFacilities'] = df_top['TopFacilities'].apply(parse_facilities)


#--------------------------------------



similarity = pickle.load(open("similarity.pkl", "rb"))


#----------------------------------------

def recommend(property_name):

    idx = df_top[df_top['PropertyName'] == property_name].index[0]

    scores = list(enumerate(similarity[idx]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    results = []

    for i, score in scores:

        results.append({
            "PropertyName": df_top.iloc[i]['PropertyName'],
            "score": score,
            "Link": df_top.iloc[i]['Link']
        })

    return results


#--------------------------------------------

property_list = sorted(df_top['PropertyName'].unique())

selected_property = st.selectbox(
    "Select Property",
    property_list
)


#------------------------------------------------------------


if st.button("Recommend Similar Properties"):

    recommendations = recommend(selected_property)

    st.success("Top Similar Properties")

    for item in recommendations:

        prop = item["PropertyName"]
        score = round(item["score"],2)

        st.subheader(prop)

        st.write(f"Similarity Score: {score}")

        st.markdown(f"[🔗 View Property]({item['Link']})")

        st.divider()


#--------------------------------------------

st.caption("Built by **Prince Kumar** · Data Scientist · [LinkedIn](https://www.linkedin.com/in/prince-datascientist) · [GitHub](https://github.com/prince-kumar-ds)")