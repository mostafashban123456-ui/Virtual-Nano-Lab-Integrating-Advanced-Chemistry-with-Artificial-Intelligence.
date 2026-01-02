import streamlit as st
import py3Dmol
from st_py3dmol import showmol

# إعدادات الصفحة
st.set_page_config(page_title="المختبر النانوي الافتراضي", layout="wide")

# القائمة الجانبية للتنقل بين الصور
st.sidebar.title
page = st.sidebar.slider
st.sidebar.image(f"{page}.png", caption=f {page}

# عرض الجزيئات ثلاثية الأبعاد
st.title
mol_choice = st.selectbox , ["Caffeine", "Aspirin", "Water"])

# كود المحاكاة
view = py3Dmol.view(query=f'cid:{297 if mol_choice=="Caffeine" else 2244 if mol_choice=="Aspirin" else 962}', width=800, height=400)
view.setStyle({'stick': {'colorscheme': 'cyanCarbon'}})
view.spin(True)
showmol(view, height=400)

# قسم الذكاء الاصطناعي والمراجع
st.sidebar.markdown("---")
st.sidebar.subheader
st.sidebar.info

question = st.text_input
if question:
    st.write

