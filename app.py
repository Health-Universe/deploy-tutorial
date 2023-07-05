from model import chads_vasc_score, df

import streamlit as st

# Text
st.markdown("## CHA₂DS₂-VASc Score for Atrial Fibrillation Stroke Risk 🫀")
st.divider()

# Inputs
cols = st.columns(2)

cols[0].markdown("#### Patient Information")
age = cols[0].number_input("Age", min_value=0, max_value=120, value=65)
sex = cols[0].radio("Sex", ["Male", "Female"], horizontal=True)

cols[1].markdown("#### Past Medical History")
chf = cols[1].checkbox("Congestive Heart Failure (CHF)")
hypertension = cols[1].checkbox("Hypertension")
stroke_tia = cols[1].checkbox("Stroke or Transient Ischemic Attack (TIA)")
vascular_disease = cols[1].checkbox("Vascular Disease")
diabetes = cols[1].checkbox("Diabetes")

# Output
score = chads_vasc_score(age=age, 
                female={"Male": False, "Female": True}[sex], 
                chf=chf, 
                hypertension=hypertension,
                stroke_tia=stroke_tia, 
                vascular_disease=vascular_disease, 
                diabetes=diabetes)
cols[0].info(f"CHA₂DS₂-VASc Score: {score}")

cols[1].markdown("See [MDCalc](https://www.mdcalc.com/) for details.")

st.divider()

# Plotting
frame_col, chart_col = st.columns(2)

frame_col.dataframe(df)

chart_col.line_chart(data=df, x="CHA₂DS₂-VASc Score", 
                y=["Risk of Ischemic Stroke", "Risk of Stroke/TIA/Systemic Embolism"])

chart_col.markdown("From [Friberg 2012](https://pubmed.ncbi.nlm.nih.gov/22246443/).")

st.divider()

st.markdown("App Created by [Health Universe](https://www.healthuniverse.com) 🛸")
