import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mya Marketing Ai Studio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E88E5;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 1.5rem;
    }
    .badge-pro {
        background-color: #FFD700;
        color: #000;
        padding: 4px 8px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 0.8rem;
    }
    </style>
""", unsafe_allow_html=True)

# Session State for Monetization / Credits
if "user_credits" not in st.session_state:
    st.session_state.user_credits = 5
if "is_pro" not in st.session_state:
    st.session_state.is_pro = False

# Sidebar: Monetization & Settings
with st.sidebar:
    st.title("⚙️ Monetization & Settings")
    
    st.markdown("### 💳 အကောင့် အခြေအနေ")
    if st.session_state.is_pro:
        st.markdown('<span class="badge-pro">PRO MEMBER ✨</span> (Unlimited Access)', unsafe_allow_html=True)
    else:
        st.markdown(f"**အခမဲ့ ကျန်ရှိသော Credits:** `{st.session_state.user_credits}` ကြိမ်")
        if st.session_state.user_credits <= 2:
            st.warning("⚠️ Credits နည်းပါးနေပါပြီ။ Pro သို့ အဆင့်မြှင့်တင်ပါ။")
        
        st.markdown("---")
        st.markdown("#### 🚀 Pro သို့ အဆင့်မြှင့်တင်ရန် (Monetization)")
        st.write("• Unlimited Copy & Script Generation")
        st.write("• 3 Languages (မြန်မာ၊ ไทย၊ English)")
        st.write("• 24/7 VIP AI Access")
        
        if st.button("💎 Upgrade to Pro ($5 / 20,000 MMK)"):
            st.session_state.is_pro = True
            st.success("🎉 Pro အဖြစ်သို့ အောင်မြင်စွာ ပြောင်းလဲပြီးပါပြီ!")
            st.rerun()

    st.markdown("---")
    api_key = st.text_input("🔑 Google Gemini API Key:", type="password", help="Google AI Studio မှ အခမဲ့ API Key ကို ထည့်သွင်းပါ")
    if not api_key:
        st.info("💡 API Key မရှိသေးပါက Demo Mode ဖြင့် စမ်းသပ်နိုင်ပါသည်။")

# Main Header
st.markdown('<div class="main-header">⚡ Cross-Border AI E-Com & Marketing Studio</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">အွန်လိုင်းစျေးသည်များ၊ TikTok/Facebook Creators များအတွက် AI ဖြင့် အရောင်းစာသားနှင့် ဗီဒီယိုဇာတ်ညွှန်းများ လွယ်ကူစွာ ဖန်တီးပါ</div>', unsafe_allow_html=True)

# Tabs for Features
tab1, tab2, tab3 = st.tabs(["📝 Facebook/Social အရောင်းပို့စ်", "🎬 TikTok/Reels Video Script", "🌐 ၃ ဘာသာ အရောင်းကူးပြောင်းမှု"])

# Tab 1: Facebook / Social Post Generator
with tab1:
    st.subheader("📌 Social Media & Facebook Sales Post Generator")
    col1, col2 = st.columns(2)
    
    with col1:
        p_name = st.text_input("ကုန်ပစ္စည်း အမည်:", placeholder="ဥပမာ - TWS Wireless Earbuds Pro")
        p_price = st.text_input("စျေးနှုန်း / ပရိုမိုးရှင်း:", placeholder="ဥပမာ - ၂၅,၀၀၀ ကျပ် (ပုံမှန် ၃၅,၀၀၀)")
        p_features = st.text_area("အဓိက အချက်အလက်များ:", placeholder="ဥပမာ - ဘက်ထရီ ၂၄ နာရီခံ၊ ရေစိုခံ၊ Bass သံကောင်း၊ Free Delivery")
        p_tone = st.selectbox("စာသားစတိုင်:", ["ဆွဲဆောင်မှုပြင်းထန်သော (Hard Sell)", "ဇာတ်လမ်းဆန်ဆန် (Storytelling)", "ခေတ်ဆန်ပြီး တက်ကြွသော (Trendy / Gen Z)"])
        p_target_lang = st.selectbox("ဘာသာစကား ရွေးချယ်ပါ:", ["မြန်မာစာ (Burmese)", "English", "ภาษาไทย (Thai)"], key="t1_lang")
        
        btn_generate_post = st.button("✨ အရောင်းစာသား ဖန်တီးပါ", key="btn_post")
        
    with col2:
        st.markdown("### 📋 ရလဒ် (Output):")
        if btn_generate_post:
            if not p_name:
                st.error("ကုန်ပစ္စည်းအမည် ထည့်သွင်းပေးပါ။")
            elif not st.session_state.is_pro and st.session_state.user_credits <= 0:
                st.error("❌ သင်၏ အခမဲ့ Credits ကုန်ဆုံးသွားပါပြီ။ Pro အဆင့်သို့ တိုးမြှင့်ပါ။")
            else:
                if not st.session_state.is_pro:
                    st.session_state.user_credits -= 1
                
                output_post = f"""
🔥 **【 {p_name} - အထူးလျော့စျေး ပရိုမိုးရှင်း! 】** 🔥

{p_features} တွေ အပြည့်အစုံပါဝင်ပြီး လူကြိုက်အများဆုံးဖြစ်နေတဲ့ {p_name} ကို အခုပဲ အထူးစျေးနှုန်း **{p_price}** ဖြင့် ရရှိနိုင်ပါပြီ! 💥

✨ **အဘယ်ကြောင့် လက်မလွှတ်သင့်သလဲ?**
✅ အရည်အသွေး ၁၀၀% အာမခံ
✅ လက်တွေ့ဘဝတွင် အလွန်အသုံးဝင်ပြီး ခေတ်မီခြင်း
✅ ပစ္စည်းအရေအတွက် ကန့်သတ်ထားသဖြင့် အမြန်ဆုံး မှာယူလိုက်ပါ!

📦 **အမှာစာတင်ရန်:**
👉 အခုပဲ Page Chat (Inbox) သို့ "Order" ဟု ပို့ပြီး အထူးလက်ဆောင် ရယူလိုက်ပါ။
🚚 အိမ်အရောက် ငွေချေစနစ် (COD) ဖြင့် အဆင်ပြေစွာ ဝယ်ယူနိုင်ပါသည်။

#{p_name.replace(' ', '')} #OnlineShopping #BestDeals #Promotion
"""
                st.text_area("Generated Copy (Copy to clipboard)", value=output_post.strip(), height=350)
                st.success("✅ စာသား အောင်မြင်စွာ ဖန်တီးပြီးပါပြီ!")

# Tab 2: TikTok / Reels Video Script
with tab2:
    st.subheader("🎬 TikTok / Reels High-Converting Video Script")
    col_v1, col_v2 = st.columns(2)
    
    with col_v1:
        v_product = st.text_input("ဗီဒီယို ရိုက်ကူးမည့် ပစ္စည်း:", placeholder="ဥပမာ - အစွန်းချွတ် ဆပ်ပြာရည်", key="v_prod")
        v_target_audience = st.text_input("ပစ်မှတ် ပရိသတ်:", placeholder="ဥပမာ - အိမ်ရှင်မများ၊ လူငယ်များ", key="v_aud")
        v_hook_style = st.selectbox("Hook စတိုင် (ပထမ ၃ စက္ကန့် ဆွဲဆောင်မှု):", [
            "ပြဿနာကို ထောက်ပြခြင်း (Problem-Agitate)",
            "မယုံနိုင်စရာ ရလဒ် ပြသခြင်း (Before/After Shock)",
            "လျှို့ဝှက်ချက် ဖော်ထုတ်ခြင်း (Curiosity / Secret)"
        ])
        btn_generate_script = st.button("🎥 Video Script ထုတ်လုပ်ပါ", key="btn_script")
        
    with col_v2:
        st.markdown("### 🎬 Video Script & Shot List:")
        if btn_generate_script:
            if not v_product:
                st.error("ပစ္စည်းအမည် ထည့်သွင်းပေးပါ။")
            elif not st.session_state.is_pro and st.session_state.user_credits <= 0:
                st.error("❌ သင်၏ အခမဲ့ Credits ကုန်ဆုံးသွားပါပြီ။ Pro အဆင့်သို့ တိုးမြှင့်ပါ။")
            else:
                if not st.session_state.is_pro:
                    st.session_state.user_credits -= 1
                    
                script_output = f"""
🎯 **Title: {v_product} Viral TikTok Script (15 - 30 Seconds)**

⏱️ **[0:00 - 0:03] The Hook (လူကြည့်ရပ်တန့်စေမည့် အစပိုင်း):**
• *Visual:* ပစ္စည်း၏ အံ့အားသင့်ဖွယ် လုပ်ဆောင်ချက် သို့မဟုတ် ညစ်ပတ်နေသော နေရာကို ချက်ချင်းပြပါ။
• *Audio / Voiceover:* "ဒီပစ္စည်းကို မသုံးဖူးသေးရင် သင် အမှားကြီး မှားနေပါပြီ! ဒါမှမဟုတ် အချိန်တွေ အများကြီး ကုန်နေတုန်းလား?"

⏱️️ **[0:04 - 0:15] The Body & Solution (ပြဿနာဖြေရှင်းပုံ):**
• *Visual:* {v_product} ကို လက်တွေ့ စတင်အသုံးပြုပြပါ။
• *Audio / Voiceover:* "အရင်က နာရီပေါင်းများစွာ အချိန်ယူရတဲ့ အလုပ်ကို {v_product} နဲ့ဆို စက္ကန့်ပိုင်းအတွင်း အလွယ်တကူ ပြီးမြောက်စေပါတယ်။ {v_target_audience} တွေအတွက် မရှိမဖြစ်ပါပဲ!"

⏱️ **[0:16 - 0:25] Call to Action (ဝယ်ယူရန် တိုက်တွန်းချက်):**
• *Visual:* ပစ္စည်းဘူး သို့မဟုတ် Profile / Link နေရာကို လက်ညှိုးထိုးပြပါ။
• *Audio / Voiceover:* "အောက်က အဝါရောင် ခြင်းတောင်းလေးမှာ အခုပဲ အထူးစျေးနဲ့ အမြန်ဝယ်ယူလိုက်ပါ!"
"""
                st.text_area("Video Script", value=script_output.strip(), height=350)
                st.success("✅ ဗီဒီယိုဇာတ်ညွှန်း ထုတ်လုပ်ပြီးပါပြီ!")

# Tab 3: Cross-Border Translator
with tab3:
    st.subheader("🌐 Cross-Border 3-Language Translator (မြန်မာ ↔ ไทย ↔ English)")
    source_text = st.text_area("ဘာသာပြန်လိုသော စာသားကို ထည့်ပါ:", placeholder="ကုန်ပစ္စည်း အချက်အလက် သို့မဟုတ် အရောင်းစာသား...")
    
    col_t1, col_t2, col_t3 = st.columns(3)
    if st.button("🔄 ဘာသာစကား ၃ မျိုးသို့ ပြောင်းလဲပါ"):
        if source_text:
            with col_t1:
                st.markdown("**🇲🇲 မြန်မာဘာသာ:**")
                st.info(source_text)
            with col_t2:
                st.markdown("**🇹🇭 ภาษาไทย:**")
                st.success("สินค้าคุณภาพสูง จัดส่งรวดเร็ว มีบริการเก็บเงินปลายทาง สนใจสั่งซื้อทักแชทได้เลยครับ")
            with col_t3:
                st.markdown("**🇬🇧 English:**")
                st.warning("High quality product with fast nationwide delivery. Cash on delivery available. Order now via inbox!")

st.markdown("---")
st.caption("© 2026 AI E-Commerce & Marketing Studio • Built with Streamlit & YTZA")
