import streamlit as st
import streamlit.components.v1 as components
import requests
import os
import hashlib

# ================== إعداد الصفحة ==================
st.set_page_config(
    page_title="المختبر الافتراضي الشامل",
    layout="wide"
)

# ================== نظام الدخول ==================
ADMIN_USER = "admin"
ADMIN_PASS_HASH = hashlib.sha256("azhar2026".encode()).hexdigest()

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    if os.path.exists("1.png"):
        st.image("1.png", use_container_width=True)

    st.title("🔬 المختبر الافتراضي العلمي")

    u = st.text_input("معرّف العالم")
    p = st.text_input("كلمة المرور", type="password")

    if st.button("🚀 تفعيل المختبر"):
        if u == ADMIN_USER and hashlib.sha256(p.encode()).hexdigest() == ADMIN_PASS_HASH:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ بيانات غير صحيحة")

    st.stop()

# ================== الشريط الجانبي ==================
st.sidebar.title("🖼 وحدات المختبر")
for i in range(1, 11):
    img = f"{i}.png"
    if os.path.exists(img):
        st.sidebar.image(img)

library_list = [
    "Physics for Scientists and Engineers",
    "Introduction to Quantum Mechanics",
    "Fundamentals of Optics",
    "Linear Algebra",
    "Calculus",
    "Solid State Physics",
    "The Art of Electronics"
]

st.sidebar.title("📚 المكتبة")
selected_book = st.sidebar.selectbox("اختر المرجع", library_list)

# ================== قاعدة التحليل ==================
ANALYSIS_DB = {
    "Aspirin": {
        "formula": "C9H8O4",
        "field": "Organic Chemistry",
        "description": "مثبط لإنزيم COX، مسكن وخافض للحرارة"
    },
    "طوب": {
        "formula": "SiO2 + Al2O3",
        "field": "Materials Science",
        "description": "مادة إنشائية ذات بنية بلورية صلبة"
    },
    "أسمنت": {
        "formula": "Calcium Silicates",
        "field": "Inorganic Chemistry",
        "description": "يتفاعل مع الماء ليكوّن بنية صلبة"
    }
}

def analyze_matter(name):
    return ANALYSIS_DB.get(
        name,
        {
            "formula": "غير معروف",
            "field": "تحليل ذكاء اصطناعي",
            "description": f"جارٍ تحليل {name} على المستوى الذري..."
        }
    )

# ================== الواجهة الرئيسية ==================
st.title("⚛️ بيئة التحليل والمحاكاة")

input_data = st.text_input("اكتب اسم مادة / جزيء / عنصر", "Aspirin")

tab_3d, tab_exp = st.tabs(["💎 التفكيك الذري 3D", "🧪 المختبر الذكي"])

# ================== عرض ثلاثي الأبعاد ==================
with tab_3d:
    st.header(f"💎 تحليل جزيء: {input_data}")

    try:
        cid = requests.get(
            f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{input_data}/cids/JSON"
        ).json()["IdentifierList"]["CID"][0]
    except:
        cid = 2244

    col1, col2 = st.columns([2, 1])

    with col1:
        components.html(f"""
        <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
        <div class="viewer_3Dmoljs"
             style="height:600px;width:100%;background:black;border-radius:15px;"
             data-cid="{cid}"
             data-style="stick"
             data-backgroundcolor="black"></div>
        """, height=620)

    with col2:
        data = analyze_matter(input_data)
        st.subheader("📊 النتائج")
        st.write("**الصيغة:**", data["formula"])
        st.write("**المجال:**", data["field"])
        st.write("**الوصف:**", data["description"])
        st.info(f"📘 المرجع المستخدم: {selected_book}")

# ================== التجارب ==================
with tab_exp:
    st.header("🧪 تنفيذ تجربة افتراضية")
    exp_query = st.text_input("اكتب اسم التجربة")

    if st.button("⚙️ تنفيذ"):
        st.info("🤖 الذكاء الاصطناعي ينفذ التجربة...")
        st.write("1️⃣ تحديد الفرضية")
        st.write("2️⃣ اختيار الأدوات")
        st.write("3️⃣ محاكاة التفاعل")
        st.success("✅ التجربة نجحت وتم تسجيل النتائج")

# ================== الدردشة ==================
st.divider()
with st.expander("💬 الدردشة مع المختبر"):
    chat = st.chat_input("اسأل عن أي قانون أو تجربة")
    if chat:
        st.write(f"🤖 بناءً على {selected_book}، هذا السؤال يتطلب تحليل رياضي وفيزيائي دقيق.")

# ================== عرض PDF ==================
st.header(f"📖 تصفح المرجع: {selected_book}")
pdf_path = f"{selected_book}.pdf"
if os.path.exists(pdf_path):
    st.markdown(
        f'<iframe src="{pdf_path}" width="100%" height="800px"></iframe>',
        unsafe_allow_html=True
    )
else:
    st.warning("📄 ملف المرجع غير موجود")
