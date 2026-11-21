import streamlit as st
import requests




st.title("Mushaf Web App")
st.write("A Quaranic Project")


surahs_Data=requests.get("https://api.alquran.cloud/v1/surah").json()["data"]


surahs=[]
for i in surahs_Data:

    surahs.append(f"{i['number']}  | {i['name']} |  {i['englishNameTranslation']}")




selectedsurah =st.selectbox("Select the Surah",surahs)


surahNum=selectedsurah.split(" | ")[0]


#st.write(surahNum)


fullofsurah=requests.get(f"https://api.alquran.cloud/v1/surah/{surahNum}/ar.abdurrahmaansudais").json()["data"]["ayahs"]




for a in fullofsurah:

    st.success(a["numberInSurah"])
    st.write(a["text"])
    st.audio(a["audio"])