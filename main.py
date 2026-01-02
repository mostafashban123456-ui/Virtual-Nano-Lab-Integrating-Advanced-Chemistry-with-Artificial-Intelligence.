import streamlit as st

# إعدادات الواجهة الاحترافية
st.set_page_config(page_title="Virtual Nano-Lab", layout="wide")

# القائمة الجانبية للتنقل
st.sidebar.title("🧪 مراحل المشروع")
page = st.sidebar.slider("انتقل بين الصفحات", 1, 10, 1)

# عرض الصورة
st.image(f"{page}.png", use_container_width=True)

st.sidebar.info(f"أنت الآن تعرض الصفحة رقم {page} من أصل 10")
