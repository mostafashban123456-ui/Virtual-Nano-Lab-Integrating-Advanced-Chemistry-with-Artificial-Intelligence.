import streamlit as st
import py3Dmol
from st_py3dmol import showmol

# إعدادات الصفحة
st.set_page_config(page_title="المختبر النانوي الافتراضي", layout="wide")

# القائمة الجانبية للتنقل بين الصور
st.sidebar.title("🧪 مراحل المشروع")
page = st.sidebar.slider("انتقل بين الصفحات", 1, 10, 1)
st.sidebar.image(f"{page}.png", caption=f"تعرض الآن الصفحة رقم {page}")

# عرض الجزيئات ثلاثية الأبعاد
st.title("🔬 مختبر الكيمياء التفاعلي 3D")
mol_choice = st.selectbox("اختر الجزيء للعرض:", ["Caffeine", "Aspirin", "Water"])

# كود المحاكاة
view = py3Dmol.view(query=f'cid:{297 if mol_choice=="Caffeine" else 2244 if mol_choice=="Aspirin" else 962}', width=800, height=400)
view.setStyle({'stick': {'colorscheme': 'cyanCarbon'}})
view.spin(True)
showmol(view, height=400)

# قسم الذكاء الاصطناعي والمراجع
st.sidebar.markdown("---")
st.sidebar.subheader("📚 المراجع العلمية")
st.sidebar.info("1. تقنية النانو - جامعة القاهرة\n2. أبحاث Nature العالمية")

question = st.text_input("اسأل المساعد الذكي عن هذا الجزيء:")
if question:
    st.write(f"🔍 الإجابة (بناءً على المراجع): جزيء {mol_choice} المدروس يعد أساسياً في تطبيقات النانو...")

