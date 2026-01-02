import streamlit as st

# إعدادات الواجهة الاحترافية
st.set_page_config(page_title="Virtual Nano-Lab", layout="wide")

# القائمة الجانبية للتنقل
st.sidebar.title("🧪 مراحل المشروع")
page = st.sidebar.slider("انتقل بين الصفحات", 1, 10, 1)

# عرض الصورة
st.image(f"{page}.png", use_container_width=True)

st.sidebar.info(f"أنت الآن تعرض الصفحة رقم {page} من أصل 10")
import streamlit as st
import py3Dmol
from st_py3dmol import showmol

st.title("🔬 مختبر النانو كيمياء التفاعلي")

# إضافة قائمة لاختيار الجزيء
molecule_choice = st.sidebar.selectbox(
    "اختر الجزيء المراد عرضه:",
    ["Caffeine", "Aspirin", "Ethanol"]
)

# كود لعرض الجزيء ثلاثي الأبعاد
def display_molecule(molecule_name):
    # هنا نستخدم معرفات الجزيئات من قاعدة بيانات PubChem
    search_query = f'cid:{297 if molecule_name == "Caffeine" else 2244 if molecule_name == "Aspirin" else 702}'
    
    view = py3Dmol.view(query=search_query, width=800, height=400)
    view.setStyle({'stick': {}}) # شكل الروابط (عصا)
    view.setBackgroundColor('#1e1e1e') # لون الخلفية
    view.spin(True) # جعل الجزيء يدور تلقائياً
    
    showmol(view, height=400, width=800)

# استدعاء دالة العرض
st.subheader(f"عرض جزيء {molecule_choice} ثلاثي الأبعاد")
display_molecule(molecule_choice)

st.info("💡 يمكنك استخدام الماوس لتدوير الجزيء أو تكبيره داخل المختبر.")
st.sidebar.markdown("---")
st.sidebar.subheader("📚 المراجع العلمية")
st.sidebar.write("1. مقدمة في تقنية النانو - جامعة القاهرة")
st.sidebar.write("2. أبحاث في تفاعلات الجزيئات - مجلة Nature")

# إضافة خانة لسؤال الذكاء الاصطناعي
question = st.text_input("اسأل الذكاء الاصطناعي حول هذه الجزيئات (بناءً على المراجع):")
if question:
    st.write(f"🔍 جاري البحث في المراجع عن إجابة لـ: {question}")
    # هنا مستقبلاً سنربط الـ API الخاص بـ OpenAI أو Gemini
    st.success("الرد (تجريبي): بناءً على المرجع الأول، فإن هذا الجزيء يتفاعل عند درجة حرارة 25 مئوية.")
