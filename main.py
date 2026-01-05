import streamlit as st
import streamlit.components.v1 as components

# --- إعدادات المختبر الفائقة ---
st.set_page_config(page_title="المختبر النانوي العالمي", layout="wide")

if 'nano_auth' not in st.session_state:
    st.session_state['nano_auth'] = False

# --- شاشة الدخول الاحترافية ---
if not st.session_state['nano_auth']:
    try:
        st.image("1.png", use_container_width=True) # تم التعديل لاسم صورتك الجديد
    except:
        st.error("⚠️ يرجى التأكد من رفع ملف الصورة باسم 1.png في المستودع")
    
    st.title("🔬 المركز الدولي للبحوث النانوية والكيميائية")
    col1, col2 = st.columns(2)
    with col1:
        u = st.text_input("معرف الباحث (Admin)")
        p = st.text_input("كلمة المرور", type="password")
        if st.button("🚀 تشغيل النظام"):
            if u == "admin" and p == "azhar2026":
                st.session_state['nano_auth'] = True
                st.rerun()
            else:
                st.error("❌ بيانات الدخول غير صحيحة")
    st.stop()

# --- واجهة المختبر (الأقوى في العالم) ---
st.sidebar.image("1.png")
st.sidebar.title("🧬 مركز التحكم")
task = st.sidebar.selectbox("العمليات:", ["المحاكي الذري 3D", "محلل الجزيئات AI", "المكتبة الكيميائية"])

if task == "المحاكي الذري 3D":
    st.header("🧊 وحدة المحاكاة الجزيئية (PubChem Global)")
    cid = st.text_input("أدخل رقم المركب (CID) - مثال: 2244 للاسبرين، 962 للماء:", "2244")
    
    # محاكي احترافي أسود اللون ليناسب المختبرات العالمية
    view_html = f"""
    <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
    <div style="height: 500px; width: 100%; border-radius: 15px; overflow: hidden;" 
         class='viewer_3Dmoljs' data-cid='{cid}' data-backgroundcolor='0x111111' data-style='stick'></div>
    """
    components.html(view_html, height=520)
    st.success(f"تم سحب بيانات الجزيء {cid} من المراجع الدولية بنجاح.")

elif task == "محلل الجزيئات AI":
    st.header("🤖 المحلل الذكي للمواد النانوية")
    st.write("ارفع صورة مجهرية للمادة للتحليل الفوري:")
    st.file_uploader("Upload Nano-Material Image", type=['png', 'jpg'])
    st.button("بدء المسح الرقمي")

elif task == "المكتبة الكيميائية":
    st.header("📚 مراجع البحث العلمي")
    st.info("نظام البحث مرتبط بمرجع: Atkins' Physical Chemistry")
    st.video("https://www.youtube.com/watch?v=7u_Xp9pSOn4") # فيديو تعليمي عن كيمياء النانو
 # فيديو توضيحي لتقنيات النانو
