import streamlit as st
import streamlit.components.v1 as components
import requests
import os

# --- إعدادات المحرك العالمي 2026 ---
st.set_page_config(page_title="مجمع المنارة العلمي - النسخة الفائقة", layout="wide")

if 'nano_auth' not in st.session_state:
    st.session_state['nano_auth'] = False

# --- نظام الدخول الموحد ---
if not st.session_state['nano_auth']:
    if os.path.exists("1.png"):
        st.image("1.png", use_container_width=True) #
    
    st.title("🔬 بيئة المحاكاة والتحليل الذري الشامل")
    u = st.text_input("معرف العالم (Admin)")
    p = st.text_input("كلمة المرور", type="password")
    if st.button("🚀 تشغيل المحرك الذري"):
        if u == "admin" and p == "azhar2026": #
            st.session_state['nano_auth'] = True
            st.rerun()
    st.stop()

# --- المكتبة (مطابقة لأسماء صورك تماماً) ---
library_list = [
    "Quantum Optics (Mark Fox)",
    "Chemistry of the Elements (Greenwood & Earnshaw)",
    "The Art of Electronics (Horowitz & Hill)",
    "ATKINS’ PHYSICAL CHEMISTRY",
    "The Elements (Visual Guide)",
    "Fundamentals of Optics (Jenkins & White)",
    "Introduction to Electrodynamics (David J. Griffiths)",
    "How to Prove It (Daniel J. Velleman)",
    "Modern Electrochemistry Vol 2A (Bockris)",
    "Eshbach’s Handbook of Engineering Fundamentals",
    "Battery Systems Engineering (Rahn & Wang)",
    "Introduction to Quantum Mechanics (David J. Griffiths)",
    "Electrical Machines & Power Systems (Wildi)",
    "Electrochemical Methods (Allen J. Bard)",
    "Physics for Scientists"
]

st.sidebar.image("1.png")
st.sidebar.title("📚 المكتبة المرجعية")
selected_book = st.sidebar.selectbox("اختر المرجع:", library_list)

# --- محرك التحليل الشامل (فحص وفصفصة أي مادة) ---
st.sidebar.title("🔍 المحلل الذري والفحص")
input_data = st.sidebar.text_input("اكتب أي شيء (طوب، دواء، أسمنت، جزيء):", "Aspirin")

def analyze_matter_pro(name):
    # محاكاة لفكر الذكاء الاصطناعي في تحليل المواد
    knowledge_base = {
        "طوب": "التحليل: يتكون من السيليكا (SiO2) بنسبة 50%، الألومينا (Al2O3) بنسبة 20-30%، وأكاسيد الحديد. البنية: شبكة بلورية صلبة ناتجة عن الحرق الحراري.",
        "أسمنت": "التحليل: كيميائياً هو مزيج من سيليكات الكالسيوم وألومينات الكالسيوم. عند إضافة الماء، تتكون روابط هيدروجينية قوية تخلق بنية صلبة جداً.",
        "Aspirin": "التحليل الصيدلاني: C9H8O4. مركب عضوي يحتوي على حلقة أروماتية. يستخدم لتثبيط إنزيمات الأكسدة الحلقية.",
        "الشقوق الحامضية": "التحليل المعملي: تتكون من أنيونات ناتجة عن أحماض. يتم الكشف عنها بتفاعلات الترسيب أو تصاعد الغازات المميزة."
    }
    return knowledge_base.get(name, f"جاري 'فصفصة' مكونات {name} ذرياً وكيميائياً بناءً على المراجع المتاحة...")

# --- نظام التجارب الذاتي (الذكاء الاصطناعي ينفذ التجربة) ---
def run_autonomous_experiment(exp_name):
    st.subheader(f"🧪 تجربة افتراضية ذاتية: {exp_query}")
    st.info("🤖 المساعد الذكي يقوم الآن بإجراء التجربة باستخدام الأدوات الافتراضية...")
    
    # خطوات التجربة تظهر تباعاً
    st.write("**1. فحص الشقوق:** عرض جميع الشقوق الحامضية الممكنة (كربونات، كبريتات، كلوريدات).")
    st.write("**2. إضافة الكاشف:** تم اختيار حمض الهيدروكلوريك (HCl) ككاشف أساسي.")
    st.write("**3. الملاحظة:** حدوث فوران وتصاعد غاز يعكر ماء الجير (تأكيد وجود الكربونات).")
    st.success("✅ التجربة اكتملت: المادة تحتوي على شق الكربونات الحامضي.")

# --- الواجهة الرئيسية (التفكيك والعرض) ---
tab_3d, tab_exp = st.tabs(["💎 التفكيك الذري 3D", "🧪 المختبر الذكي والتجارب"])

with tab_3d:
    st.header(f"💎 فصفصة جزيء: {input_data}")
    # البحث في قاعدة البيانات العالمية
    try:
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{input_data}/cids/JSON"
        cid = requests.get(url).json()['IdentifierList']['CID'][0]
    except:
        cid = 2244 # نموذج افتراضي (الأسبرين)

    col_view, col_desc = st.columns([2, 1])
    with col_view:
        # عرض شامل للجزيء (فصفصة كاملة للروابط)
        view_html = f"""
        <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
        <div style="height: 600px; width: 100%; background: black; border-radius: 20px;" 
             class='viewer_3Dmoljs' data-cid='{cid}' data-style='stick' data-backgroundcolor='black'></div>
        """
        components.html(view_html, height=620)
    
    with col_desc:
        st.subheader("🤖 نتائج الفحص الذري")
        st.write(analyze_matter_pro(input_data))
        st.warning(f"📍 تم تحليل هذه المادة وفقاً لمرجع: {selected_book}")

with tab_exp:
    st.header("🧪 وحدة التجارب الذكية")
    exp_query = st.text_input("اطلب أي تجربة (مثال: الكشف عن الشق الحامضي للكربونات):")
    if st.button("🚀 تنفيذ التجربة ذاتياً"):
        run_autonomous_experiment(exp_query)

# --- واجهة الدردشة (سهم الرفع) ---
st.divider()
with st.expander("⬆️ اسحب للأعلى للدردشة الفورية مع المختبر"):
    chat_input = st.chat_input("اسأل الذكاء الاصطناعي عن أي تفاعل...")
    if chat_input:
        st.write(f"🤖 المساعد: بناءً على مرجع {selected_book}، فإن '{chat_input}' يتطلب شروط تفاعل دقيقة...")

# --- قارئ الكتب PDF ---
st.header(f"📖 تصفح المرجع: {selected_book}")
pdf_path = f"{selected_book}.pdf"
st.markdown(f'<iframe src="{pdf_path}" width="100%" height="800px"></iframe>', unsafe_allow_html=True)
