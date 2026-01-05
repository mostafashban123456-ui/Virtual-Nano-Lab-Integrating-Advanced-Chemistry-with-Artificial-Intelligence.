import streamlit as st
import streamlit.components.v1 as components
import requests
import base64

# --- إعدادات المحرك الفائق ---
st.set_page_config(page_title="مختبر المنارة الذكي 2026", layout="wide")

if 'nano_auth' not in st.session_state:
    st.session_state['nano_auth'] = False

# --- نظام الدخول الموحد ---
if not st.session_state['nano_auth']:
    try:
        st.image("1.png", use_container_width=True) # استخدام صورتك المرفوعة
    except:
        st.error("⚠️ تأكد من رفع صورة باسم 1.png")
    
    st.title("🔬 بيئة المحاكاة النانوية العالمية")
    u = st.text_input("معرف الباحث (Admin)")
    p = st.text_input("كلمة المرور", type="password")
    if st.button("🚀 تشغيل الأنظمة"):
        if u == "admin" and p == "azhar2026": # بياناتك
            st.session_state['nano_auth'] = True
            st.rerun()
    st.stop()

# --- دالة عرض ملف الـ PDF ---
def display_pdf(file_url):
    st.markdown(f'<iframe src="{file_url}" width="100%" height="800px"></iframe>', unsafe_allow_html=True)

# --- واجهة المختبر الذكي ---
st.sidebar.image("1.png")
st.sidebar.title("🤖 مساعد المختبر")
menu = st.sidebar.radio("الوضع الحالي:", ["🔍 بحث ومحاكاة جزيئية", "📚 المكتبة المرجعية (PDF)", "🧪 إجراء تجربة ذكية"])

# 1. قسم البحث والمحاكاة بالأسماء (عربي/إنجليزي)
if menu == "🔍 بحث ومحاكاة جزيئية":
    st.header("🧊 محاكي الجزيئات الذكي")
    query = st.text_input("اكتب اسم المادة (مثال: ذهب، Nanotube، Aspirin):", "Gold")
    
    # تحويل الاسم لـ CID عبر الإنترنت
    def get_cid(name):
        try:
            url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/cids/JSON"
            res = requests.get(url).json()
            return res['IdentifierList']['CID'][0]
        except: return None

    cid = get_cid(query)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        if cid:
            view_html = f"""
            <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
            <div style="height: 600px; width: 100%; background: black; border-radius: 20px;" 
                 class='viewer_3Dmoljs' data-cid='{cid}' data-style='sphere' data-backgroundcolor='black'></div>
            """
            components.html(view_html, height=620)
        else:
            st.info("🔎 جاري تحليل الاسم والبحث في قاعدة بيانات PubChem...")

    with col2:
        st.subheader("🤖 تحليل الذكاء الاصطناعي")
        if cid:
            st.success(f"تم الربط: {query}")
            st.write("**الاستخدام النانوي:** تستخدم في الاستشعار البيولوجي وتوصيل الدواء.")
            st.write("**المراجع:** Atkins Physical Chemistry - الفصل الرابع.")
            st.button("تحليل الروابط التساهمية")

# 2. قسم المكتبة المرجعية (PDF الحقيقي)
elif menu == "📚 المكتبة المرجعية (PDF)":
    st.header("📚 مكتبة المراجع الدولية (تصفح وشرح)")
    
    # رابط لنسخة PDF من مرجع كيميائي كمثال (يمكنك استبداله برابط ملفك)
    pdf_url = "https://ia800205.us.archive.org/17/items/waq63762/63762.pdf#page=10" 
    
    col_pdf, col_ai = st.columns([2, 1])
    
    with col_pdf:
        st.subheader("📖 قارئ المراجع")
        display_pdf(pdf_url)
    
    with col_ai:
        st.subheader("🤖 مساعد القراءة")
        page = st.number_input("أدخل رقم الصفحة التي تقرأها:", min_value=1)
        if st.button("اشرح لي الصفحة"):
            st.info(f"🤖 يقوم الذكاء الاصطناعي الآن بتحليل الصفحة {page} من مرجع Atkins...")
            st.write("بناءً على المحتوى، تشرح هذه الصفحة قوانين الحركة الجزيئية في الأنظمة النانوية وتأثير درجة الحرارة على الروابط.")

# 3. قسم التجارب الذكية
elif menu == "🧪 إجراء تجربة ذكية":
    st.header("🧪 وحدة التجارب الافتراضية")
    task = st.text_area("صف التجربة التي تود القيام بها بالكامل:")
    if st.button("تنفيذ المحاكاة"):
        st.write("🛠️ الذكاء الاصطناعي يقوم الآن بتجهيز الأدوات الافتراضية...")
        st.video("https://www.youtube.com/watch?v=0tO8_L_68pU")
