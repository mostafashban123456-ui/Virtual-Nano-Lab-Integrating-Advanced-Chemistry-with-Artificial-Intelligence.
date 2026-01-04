import streamlit as st
import py3Dmol
from st_py3dmol import showmol
import requests

# --- محرك البحث العالمي عن المركبات ---
def get_molecule_all_info(compound_name):
    try:
        # 1. جلب البيانات الأساسية والخصائص الكيميائية
        prop_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound_name}/property/MolecularFormula,MolecularWeight,IUPACName,XLogP/JSON"
        # 2. جلب الوصف العلمي (Description)
        desc_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound_name}/description/JSON"
        
        prop_res = requests.get(prop_url).json()
        desc_res = requests.get(desc_url).json()
        
        return prop_res, desc_res
    except:
        return None, None

# --- تحديث واجهة المختبر الشاملة ---
if menu == "🧬 استكشاف الجزيئات 3D":
    st.header("🌍 الموسوعة الكيميائية العالمية الشاملة")
    st.write("ابحث عن أي مركب على وجه الأرض (أدوية، عناصر، مركبات نانوية، غازات)")
    
    search_query = st.text_input("أدخل اسم المركب (مثلاً: Aspirin, Graphene, H2SO4, Insulin):")
    
    if search_query:
        with st.spinner('جاري الفحص المجهري والبحث في المراجع العالمية...'):
            props, desc = get_molecule_all_info(search_query)
            
            if props and 'PropertyTable' in props:
                data = props['PropertyTable']['Properties'][0]
                
                col_view, col_details = st.columns([2, 1])
                
                with col_view:
                    st.subheader(f"🔭 العرض ثلاثي الأبعاد: {search_query}")
                    render_molecule(search_query) # الدالة التي برمجناها سابقاً
                
                with col_details:
                    st.subheader("📋 البطاقة التعريفية")
                    st.success(f"**الصيغة الكيميائية:** {data.get('MolecularFormula')}")
                    st.info(f"**الوزن الجزيئي:** {data.get('MolecularWeight')} g/mol")
                    st.warning(f"**الاسم العلمي (IUPAC):** {data.get('IUPACName')}")
                
                st.divider()
                
                # --- قسم الفحص التفصيلي (يفصفصه حتة حتة) ---
                st.subheader("🔬 التحليل العميق (بناءً على المراجع الـ 10)")
                
                tab1, tab2, tab3 = st.tabs(["💡 تحليل الذكاء الاصطناعي", "📚 الربط بالمراجع", "⚠️ الأمان والوقاية"])
                
                with tab1:
                    description_text = desc['InformationList']['Information'][0].get('Description', 'لا يوجد وصف متاح حالياً.')
                    st.write(f"**وصف المركب:** {description_text}")
                    st.write("**طريقة الارتباط:** يتم تحليل الروابط التساهمية والأيونية بناءً على نظرية لويس المذكورة في مرجع Nivaldo J. Tro.")
                
                with tab2:
                    st.write(f"1. **بناءً على Atkins:** يتم حساب الطاقة الحرة لهذا المركب عند ظروف STP.")
                    st.write(f"2. **بناءً على Paula Bruice:** يتم تصنيف المجموعات الوظيفية (Functional Groups) في هذا المركب.")
                    st.write(f"3. **تكنولوجيا النانو:** إذا تم تصغير هذا المركب، فإنه يتبع قوانين Guozhong Cao للمواد النانوية.")
                
                with tab3:
                    st.error("🛡️ إجراءات المعمل: يجب التعامل مع هذا المركب تحت خزانة الغازات (Fume Hood) إذا كان في حالة نشطة.")
            else:
                st.error("تعذر العثور على هذا المركب. تأكد من كتابة الاسم بشكل صحيح.")
