import streamlit as st
import py3Dmol
from st_py3dmol import showmol

# Page Configuration
st.set_page_config(page_title="Virtual Nano Lab", layout="wide")

st.title("🔬 Virtual Nano-Chemistry Lab")

# Sidebar for Images (Your 1.png to 10.png)
st.sidebar.title("Project Stages")
page = st.sidebar.slider("Navigate Pages", 1, 10, 1)
try:
    st.sidebar.image(f"{page}.png", caption=f"Showing Page {page}")
except:
    st.sidebar.error("Image not found. Please check file names.")

# 3D Molecule Simulation
st.subheader("Interactive 3D Molecular Visualization")
option = st.selectbox("Select Molecule:", ["Caffeine", "Aspirin", "Water"])

# Dictionary for PubChem IDs
mol_ids = {"Caffeine": 297, "Aspirin": 2244, "Water": 962}

# Visualization Code
view = py3Dmol.view(query=f'cid:{mol_ids[option]}', width=800, height=400)
view.setStyle({'stick': {'colorscheme': 'cyanCarbon'}})
view.spin(True)
showmol(view, height=400)

# AI & References Section
st.divider()
st.sidebar.markdown("---")
st.sidebar.subheader("📚 Scientific References")
st.sidebar.info("1. Nanotechnology Essentials\n2. Nature Journal Research")

user_input = st.text_input("Ask the AI Assistant about this molecule:")
if user_input:
    st.success(f"Based on the references, {option} is key in nano-systems.")
