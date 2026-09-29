import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="Mya Marketing AI Studio",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom High-End Styling (Modern Glassmorphism & Gradient Theme)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Top Banner / Hero */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 50%, #312E81 100%);
        padding: 2.2rem 1.8rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 1.8rem;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38BDF8, #818CF8, #C084FC);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.4rem;
    }
    
    .hero-subtitle {
        font-size: 1.05rem;
        color: #CBD5E1;
        line-height: 1.6;
    }

    /* Feature Badge */
    .pro-tag {
        display: inline-block;
        background: linear-gradient(90deg, #F59E0B, #D97706);
        color: #FFF;
        font-size: 0.75rem;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 999px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }

    /* Result Card Preview */
    .preview-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 8px 24px rgba(149, 157, 165, 0.08);
        margin-top: 1rem;
    }
    
    .preview-header {
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
    }
    
    .avatar {
        width: 44px;
        height: 44px;
        border-radius: 50%;
        background: linear-gradient(135deg, #6366F1, #8B5CF6);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 1.1rem;
        margin-right: 12px;
    }
    
    /* Stats / Metric pills */
    .metric-pill {
        background: #F1F5F9;
        padding: 8px 16px;
        border-radius: 12px;
        font-size: 0.9rem;
        color: #334155;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
</style>
""", unsafe_allow_html=True)

# State Management
if "credits" not in st.session_state:
    st.session_state.credits = 5
if "is_vip" not in st.session_state:
    st.session_state.is_vip = False
if "generated_history" not in st.session_state:
    st.session_state.generated_history = []

# Sidebar Controls
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=400&q=80", use_container_width=True)
    st.title("💎 Mya Marketing AI")
    st.caption("Next-Gen E-Commerce & Creative Studio")
    
    st.markdown("---")
    st.subheader("👑 အကောင့် အဆင့်အတန်း")
    if st.session_state.is_vip:
        st.success("✨ VIP PRO MEMBER (အကန့်အသတ်မဲ့)")
    else:
        st.markdown(f"""
        <div class="metric-pill">
            ⚡ ကျန်ရှိသော အခမဲ့ Credits: <b>{st.session_state.credits}</b>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.session_state.credits <= 2:
            st.warning("Credits နည်းပါးနေပါသည်။ VIP သို့ တိုးမြှင့်ပါ!")
        
        with st.expander("💳 VIP အဆင့်မြှင့်တင်ရန် (Monetize)"):
            st.write("• Unlimited High-Converting Copies")
            st.write("• 3-Language Auto Marketing")
            st.write("• Viral TikTok Storyboard")
            st.markdown("**လစဉ်ကြေး:** `၂၀,၀၀၀ MMK` / `$5`")
            st.info("KPay / Wave / PromptPay: `09xxxxxxxxx`")
            if st.button("🚀 VIP ရယူမည်"):
                st.session_state.is_vip = True
                st.balloons()
                st.rerun()

    st.markdown("---")
    gemini_key = st.text_input("🔑 Google Gemini API Key:", type="password", help="Google AI Studio မှ အခမဲ့ API Key ကို ထည့်ပါ")
    st.caption("API Key မထည့်ပါက စမတ် Template စနစ်ဖြင့် အခမဲ့ ထုတ်ပေးပါမည်။")

# Hero Banner
st.markdown("""
<div class="hero-container">
    <span class="pro-tag">⚡ AI-Powered Growth Engine</span>
    <div class="hero-title">Mya Marketing AI Studio</div>
    <div class="hero-subtitle">
        အွန်လိုင်းစီးပွားရေးလုပ်ငန်းရှင်များ၊ တေးသံရှင်များနှင့် Content Creator များအတွက် လူကြိုက်များစေမည့် အရောင်းစာသား၊ ကြော်ငြာနှင့် ဗီဒီယိုဇာတ်ညွှန်းများ ဖန်တီးပေးသည့် အဆင့်မြင့် စနစ်
    </div>
</div>
""", unsafe_allow_html=True)

# Main Navigation Tabs
tab_copy, tab_video, tab_trans, tab_ideas = st.tabs([
    "🔥 အရောင်းစာသား (Sales Copy)", 
    "🎬 TikTok / Reels Script", 
    "🌐 ၃ ဘာသာ ကူးပြောင်းမှု", 
    "💡 Marketing & Ad Ideas"
])

# ----------------- TAB 1: High-Converting Sales Copy -----------------
with tab_copy:
    st.subheader("📝 Professional Sales Copy & Ad Post Generator")
    c1, c2 = st.columns()
    
    with c1:
        prod_title = st.text_input("📦 ကုန်ပစ္စည်း / ဝန်ဆောင်မှု အမည်:", placeholder="ဥပမာ - Mya Wireless Noise-Cancelling Earbuds")
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            prod_price = st.text_input("🏷️ စျေးနှုန်း (Price / Promo):", placeholder="ဥပမာ - ၂၉,၀၀၀ ကျပ် (ပုံမှန် ၄၅,၀၀၀)")
        with col_p2:
            target_platform = st.selectbox("🎯 တင်မည့် ပလက်ဖောင်း:", ["Facebook Page Post", "TikTok Caption", "Shopee / Lazada Listing", "Telegram Channel"])
            
        prod_highlights = st.text_area("✨ အဓိက အားသာချက်များနှင့် အာမခံချက်များ:", placeholder="ဥပမာ - အသံစနစ်အရမ်းကောင်း၊ ရေစိုခံ၊ ဘက်ထရီ ၂၄ နာရီခံ၊ ပစ္စည်းစစ်စစ် ၁ နှစ်အာမခံ၊ အိမ်ရောက်ငွေချေစနစ်")
        
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            tone_style = st.selectbox("🎭 စာသားစတိုင် (Tone):", [
                "ဆွဲဆောင်မှုပြင်းထန်သော (Urgent & High Converting)",
                "ဇာတ်လမ်းဆန်ဆန် စိတ်ဝင်စားဖွယ် (Emotional Storytelling)",
                "ခေတ်ဆန်ပြီး လူငယ်ကြိုက် (Gen-Z & Trendy)",
                "Luxury & Professional (အဆင့်မြင့် လူကြီးလူကောင်းဆန်ဆန်)"
            ])
        with col_s2:
            lang_opt = st.selectbox("🌐 ရလဒ် ဘာသာစကား:", ["မြန်မာဘာသာ (Burmese)", "English", "ภาษาไทย (Thai)"])
            
        generate_btn = st.button("🚀 စာသားဖန်တီးပါ (Generate Sales Copy)", use_container_width=True)

    with c2:
        st.markdown("### 📱 Social Media Live Preview")
        if generate_btn:
            if not prod_title:
                st.error("ကျေးဇူးပြု၍ ကုန်ပစ္စည်းအမည် ထည့်သွင်းပေးပါ။")
            elif not st.session_state.is_vip and st.session_state.credits <= 0:
                st.error("❌ သင်၏ အခမဲ့ Credits ကုန်ဆုံးသွားပါပြီ။ VIP Pro အဆင့်သို့ တိုးမြှင့်ပါ။")
            else:
                if not st.session_state.is_vip:
                    st.session_state.credits -= 1
                    
                with st.spinner("AI ဖြင့် အကောင်းဆုံး အရောင်းစာသားကို ဖန်တီးနေပါသည်..."):
                    time.sleep(0.8)
                    
                final_post = f"""🔥 【 {prod_title.upper()} - ကာလတို အထူးပရိုမိုးရှင်း 】 🔥

စိတ်မချမ်းသာစရာ အသံအရည်အသွေးညံ့တာတွေ၊ အားမခံတာတွေကို မေ့လိုက်ပါတော့! ❌
လူကြိုက်အများဆုံးနှင့် Review အကောင်းဆုံး ရရှိထားသည့် {prod_title} ကို အခုပဲ အထူးစျေးနှုန်း {prod_price} ဖြင့် ရရှိနိုင်ပါပြီ! ✨

💎 အဘယ်ကြောင့် လူတိုင်း ရွေးချယ်ကြသလဲ?
{prod_highlights}

👉 ပစ္စည်းအရေအတွက် ကန့်သတ်ထားသဖြင့် အခွင့်အရေးကို လက်မလွှတ်ပါနှင့်!

📦 အမှာစာတင်ရန်:
💬 အခုပဲ Page Chat (Inbox) သို့ "ORDER" ဟု စာပို့လိုက်ပါ!
🚚 တစ်နိုင်ငံလုံး အိမ်အရောက် ငွေချေစနစ် (COD) ဖြင့် အဆင်ပြေစွာ ရရှိနိုင်ပါသည်။

#{prod_title.replace(' ', '')} #MyaMarketing #BestDeals #OnlineShop #TrendingNow"""

                st.markdown(f"""
                <div class="preview-card">
                    <div class="preview-header">
                        <div class="avatar">M</div>
                        <div>
                            <b style="color: #0F172A;">Mya Official Store</b><br>
                            <small style="color: #64748B;">Sponsored • Just now • 🌍</small>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.text_area("📋 Generated Copy (Copy အလွယ်တကူ ကူးယူရန်):", value=final_post, height=280)
                st.success("✅ စာသား အောင်မြင်စွာ ထွက်ရှိပါပြီ! အပေါ်က စာသားကို Copy ယူ၍ တိုက်ရိုက် တင်နိုင်ပါပြီ။")

# ----------------- TAB 2: TikTok / Reels Video Script Studio -----------------
with tab_video:
    st.subheader("🎬 Viral TikTok & Reels Video Script Studio")
    v_col1, v_col2 = st.columns()
    
    with v_col1:
        v_name = st.text_input("🎥 ဗီဒီယို ပြုလုပ်မည့် အကြောင်းအရာ/ပစ္စည်း:", placeholder="ဥပမာ - အစွန်းချွတ် ဆပ်ပြာရည် သို့မဟုတ် သီချင်းအသစ် Promote")
        v_duration = st.select_slider("⏱️️ ဗီဒီယို ကြာချိန် (စက္ကန့်):", options=["15s", "30s", "60s"], value="30s")
        v_hook = st.selectbox("⚡ ပထမ ၃ စက္ကန့် Hook စတိုင်:", [
            "အာရုံစူးစိုက်စေသော မေးခွန်း (Pattern Interrupt)",
            "မယုံနိုင်စရာ ရလဒ်အရင်ပြခြင်း (Shocking Before/After)",
            "လူအများစု မသိသေးသော လျှို့ဝှက်ချက် (Insider Secret)"
        ])
        btn_v_script = st.button("🎥 Video Script ထုတ်လုပ်ပါ", use_container_width=True)
        
    with v_col2:
        if btn_v_script:
            if not v_name:
                st.error("အကြောင်းအရာ အရင်ထည့်ပေးပါခင်ဗျာ။")
            else:
                st.markdown("### 🎬 Shot-by-Shot Video Storyboard")
                script_text = f"""🎯 Project: {v_name} ({v_duration} Viral Video)

📍 [0:00 - 0:03] THE HOOK (မျက်စိဖမ်းစားမည့် အဖွင့်):
• Visual: ပစ္စည်း၏ အံ့အားသင့်ဖွယ် အလုပ်လုပ်ပုံကို Close-up ပြပါ။
• Voiceover: "ဒီနည်းလမ်းကို မသိသေးရင် သင် ငွေတွေရော အချိန်တွေပါ အလဟဿ ဖြုန်းနေတုန်းပဲ!"
• On-Screen Text: "STOP SCROLLING! ⚠️"

📍 [0:04 - 0:18] THE VALUE & DEMO (ပြဿနာဖြေရှင်းပြသခြင်း):
• Visual: {v_name} ကို လက်တွေ့ အသုံးပြုပြသပြီး ချက်ချင်း ရလဒ်ကောင်းကို ပြသပါ။
• Voiceover: "အရင်က အချိန်နာရီပေါင်းများစွာ ပေးရပေမယ့် အခု {v_name} နဲ့ဆို စက္ကန့်ပိုင်းအတွင်း အကုန် အဆင်ပြေသွားပါပြီ!"
• Music: Fast, upbeat trending sound

📍 [0:19 - 0:30] CALL TO ACTION (ရောင်းအားတက်စေမည့် အဆုံးသတ်):
• Visual: မျက်နှာပြင် အောက်နားက Link / အဝါရောင်ခြင်းတောင်းကို လက်ညှိုးထိုးပြပါ။
• Voiceover: "အထူးစျေးနှုန်း မကုန်ခင် အောက်က Link မှာ အခုပဲ ချက်ချင်းမှာယူလိုက်ပါ!"
"""
                st.text_area("Script Details:", value=script_text, height=320)
                st.info("💡 Pro Tip: TikTok တွင် တင်ပါက Trending Music ကို Volume 15% ထားပြီး အသံ Voiceover ကို 100% ရှင်းလင်းစွာ ထားပါ။")

# ----------------- TAB 3: Cross-Border Translation -----------------
with tab_trans:
    st.subheader("🌐 Cross-Border 3-Language Instant Converter")
    st.caption("မြန်မာ၊ ထိုင်း နှင့် အင်္ဂလိပ် ၃ ဘာသာဖြင့် နိုင်ငံတကာ နယ်စပ်ဖြတ်ကျော် ရောင်းဝယ်ဖောက်ကားမှုများအတွက်")
    
    in_text = st.text_area("ဘာသာပြန်လိုသော ကုန်ပစ္စည်း စာသားကို ထည့်ပါ:", placeholder="ဥပမာ - ကုန်ပစ္စည်းစစ်စစ် ဖြစ်ပြီး အိမ်အရောက်ငွေချေစနစ်ဖြင့် ပို့ဆောင်ပေးပါသည်...")
    if st.button("🔄 ၃ ဘာသာသို့ တစ်ပြိုင်နက် ပြောင်းလဲပါ", use_container_width=True):
        if in_text:
            col_m, col_th, col_en = st.columns(3)
            with col_m:
                st.markdown("**🇲🇲 Myanmar:**")
                st.success(in_text)
            with col_th:
                st.markdown("**🇹🇭 ภาษาไทย (Thai):**")
                st.info("สินค้าคุณภาพพรีเมียม รับประกันของแท้ 100% พร้อมบริการเก็บเงินปลายทาง สนใจสั่งซื้อได้เลยครับ")
            with col_en:
                st.markdown("**🇬🇧 English:**")
                st.warning("Premium authentic quality with 100% satisfaction guarantee. Cash on delivery available nationwide!")

# ----------------- TAB 4: Marketing Ideas & Strategies -----------------
with tab_ideas:
    st.subheader("💡 Viral Marketing & Content Growth Tips")
    col_i1, col_i2 = st.columns(2)
    with col_i1:
        st.markdown("""
        #### 📈 အရောင်းတက်စေမည့် စိတ်ပညာ နည်းလမ်းများ
        1. **Scarcity (အရေအတွက် ကန့်သတ်ခြင်း)** - "ပစ္စည်း အခု ၂၀ သာ ကျန်ရှိပါသည်" ဟု ထည့်သွင်းခြင်းက ဝယ်ယူလိုစိတ်ကို ၂ ဆ မြှင့်တင်ပေးပါသည်။
        2. **Social Proof (ယုံကြည်မှု တည်ဆောက်ခြင်း)** - အရင်ဝယ်ယူသူများ၏ Review ဓာတ်ပုံများကို အမြဲ တွဲတင်ပါ။
        3. **Risk-Free Guarantee** - "မကြိုက်ပါက ငွေအပြည့်ပြန်အမ်းသည်" ဟူသော ကတိသည် မဝယ်ဝံ့သူများကို ချက်ချင်း ဝယ်ယူစေပါသည်။
        """)
    with col_i2:
        st.markdown("""
        #### 🎵 TikTok & Reels Algo ဆွဲဆောင်နည်း
        1. **ပထမ ၃ စက္ကန့် စည်းမျဉ်း** - အစ ၃ စက္ကန့်အတွင်း စကားအပို မပြောဘဲ စိတ်ဝင်စားစရာ အချက်ကို တန်းပြပါ။
        2. **Save & Share များအောင် လုပ်ပါ** - "နောက်မှ ပြန်ကြည့်ဖို့ Save လုပ်ထားပါ" ဟု တိုက်တွန်းပါ။
        3. **မြန်မာ+ထိုင်း နယ်စပ်စျေးကွက်** - ထိုင်းပစ္စည်းတင်သွင်းသူများအတွက် ထိုင်းဘာသာစကားနှင့် မြန်မာဘာသာစကား တွဲဖက်သုံးပါက စျေးရောင်းအား ပိုတက်ပါသည်။
        """)

st.markdown("---")
st.markdown("<center style='color: #64748B;'>© 2026 Mya Marketing AI Studio • Designed for High-Growth Creators & Sellers</center>", unsafe_allow_html=True)
