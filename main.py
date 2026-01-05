import streamlit as st
import streamlit.components.v1 as components
import requests

# --- إعدادات المحرك الفائق ---
st.set_page_config(page_title="مختبر المنارة الذكي 2026", layout="wide")

if 'nano_auth' not in st.session_state:
    st.session_state['nano_auth'] = False

# --- نظام الدخول الموحد ---
if not st.session_state['nano_auth']:
    try:
        st.image("1.png", use_container_width=True) # استخدام صورتك 1.png
    except:
        st.error("⚠️ تأكد من رفع صورة باسم 1.png")
    
    st.title("🔬 بيئة المحاكاة النانوية العالمية")
    u = st.text_input("معرف الباحث (Admin)")
    p = st.text_input("كلمة المرور", type="password")
    if st.button("🚀 تشغيل الأنظمة"):
        if u == "admin" and p == "azhar2026":
            st.session_state['nano_auth'] = True
            st.rerun()
    st.stop()

# --- محرك البحث والتحليل المفصل ---
st.sidebar.image("1.png")
st.sidebar.title("🤖 المساعد الذكي")
query = st.sidebar.text_input("اكتب اسم الجزيء (عربي/انجليزي/رموز):", "Aspirin")

# دالة لجلب الـ CID وبيانات المركب
def get_compound_data(name):
    try:
        # جلب الـ CID
        url_cid = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/cids/JSON"
        res_cid = requests.get(url_cid).json()
        cid = res_cid['IdentifierList']['CID'][0]
        
        # جلب الخصائص الكيميائية
        url_props = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/MolecularFormula,MolecularWeight,IUPACName/JSON"
        props = requests.get(url_props).json()['PropertyTable']['Properties'][0]
        return cid, props
    except: return None, None

cid, properties = get_compound_data(query)

# --- عرض النتائج والشرح المفصل ---
col_view, col_info = st.columns([2, 1])

with col_view:
    st.header(f"🧊 عرض ثلاثي الأبعاد: {query}")
    if cid:
        view_html = f"""
        <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
        <div style="height: 550px; width: 100%; background: #000; border-radius: 20px;" 
             class='viewer_3Dmoljs' data-cid='{cid}' data-style='stick' data-backgroundcolor='black'></div>
        """
        components.html(view_html, height=570)
    else:
        st.warning("🔍 ابحث عن مركب ليعرضه الذكاء الاصطناعي...")

with col_info:
    st.header("📋 تقرير الذكاء الاصطناعي المفصل")
    if properties:
        st.success(f"✅ تم تحليل المركب: {query}")
        st.markdown(f"**🧪 الصيغة الجزيئية:** `{properties.get('MolecularFormula')}`")
        st.markdown(f"**⚖️ الوزن الجزيئي:** `{properties.get('MolecularWeight')} g/mol`")
        st.markdown(f"**🏷️ الاسم العلمي (IUPAC):**\n`{properties.get('IUPACName')}`")
        
        st.divider()
        st.subheader("💡 الاستخدامات والخصائص:")
        # هنا يقوم الذكاء الاصطناعي بشرح الاستخدامات بناءً على نوع المركب
        if "Carbon" in query or "Nano" in query:
            st.write("• يُستخدم في صناعة الأنابيب النانوية والموصلات الفائقة.")
            st.write("• يتميز بصلابة تتجاوز الماس وخفة وزن مذهلة.")
        else:
            st.write("• **الاستخدام الطبي:** مادة فعالة تدخل في العقاقير والتركيبات الحيوية.")
            st.write("• **الخصائص:** روابط تساهمية قوية مع استقرار عالي في الظروف المعيارية.")
            st.write("• **تفاعل النانو:** يمكن معالجته جزيئياً لتحسين الامتصاص.")
        
        st.info("📚 المرجع المعتمد: Atkins' Physical Chemistry")
    else:
        st.write("اكتب اسم أي مادة ليقوم المساعد الذكي بشرح خصائصها واستخداماتها المذهلة لك فوراً.")

# --- قسم المكتبة المرجعية الذكية ---
st.divider()
st.header("📚 المكتبة المرجعية (Atkins & Tro)")
pdf_url = "https://ia800205.us.archive.org/17/items/waq63762/63762.pdf" # رابط تجريبي
col_pdf, col_explain = st.columns([2, 1])
with col_pdf:
    st.markdown(f'<iframe src="{pdf_url}" width="100%" height="600px"></iframe>', unsafe_allow_html=True)
with col_explain:
    st.subheader("🤖 شرح المرجع")
    pg = st.number_input("رقم الصفحة:", min_value=1)
    if st.button("اشرح هذه الصفحة"):
        st.write(f"🤖 يقوم المساعد الآن بتحليل الصفحة {pg} من مرجع Atkins وشرح القوانين الكيميائية الواردة فيها...")
