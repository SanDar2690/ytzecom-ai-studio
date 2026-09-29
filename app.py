import streamlit as st

st.set_page_config(
    page_title="Mya AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "credits" not in st.session_state:
    st.session_state.credits = 12
if "page" not in st.session_state:
    st.session_state.page = "ပင်မ"

st.markdown(r'''<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Myanmar:wght@400;500;600;700;800&display=swap');
html,body,[class*="css"]{font-family:'Noto Sans Myanmar',sans-serif}
.stApp{background:#f6fbf8}.block-container{max-width:1120px;padding:22px 18px 110px}
#MainMenu,footer,header{visibility:hidden}
.header{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}.brand{display:flex;align-items:center;gap:12px}
.logo{width:55px;height:55px;border-radius:18px;background:linear-gradient(135deg,#087d57,#25bd7c);display:flex;align-items:center;justify-content:center;color:#fff;font-size:28px;box-shadow:0 8px 22px #0a916233}.brand-title{font-size:27px;font-weight:800;color:#064d3b;line-height:1.1}.brand-sub{font-size:12px;color:#68827a}.icons{display:flex;gap:9px}.icon{width:43px;height:43px;border-radius:50%;background:#fff;border:1px solid #dceee7;display:flex;align-items:center;justify-content:center;font-size:19px}
.greeting h1{font-size:29px;color:#063f31;margin:16px 0 2px;font-weight:800}.greeting p{color:#607c74;margin:0 0 17px;font-size:14px}
.hero{position:relative;overflow:hidden;min-height:225px;border-radius:27px;padding:31px;background:linear-gradient(115deg,#087d57,#10a96e 55%,#8be2aa);color:white;box-shadow:0 14px 35px #087e561f}.hero h2{font-size:25px;line-height:1.45;max-width:650px;margin:0 0 8px;font-weight:800}.hero p{max-width:620px;font-size:14px;line-height:1.8;margin:0}.hero-btn{display:inline-block;margin-top:15px;background:#fff;color:#087d57;padding:11px 21px;border-radius:30px;font-weight:800}.robot{position:absolute;right:34px;bottom:-4px;font-size:112px;filter:drop-shadow(0 9px 12px #0002)}
.credit{margin-top:17px;background:#fff;border:1px solid #dcefe7;border-radius:22px;padding:17px 20px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 6px 20px #145a450d}.credit-left{display:flex;align-items:center;gap:13px}.credit-icon{width:54px;height:54px;border-radius:17px;background:#e4f8ef;display:flex;align-items:center;justify-content:center;font-size:27px}.small{font-size:12px;color:#668078}.num{font-size:28px;color:#087d57;font-weight:800}.reward{background:#e6f8ef;color:#087d57;border-radius:17px;padding:11px 17px;font-size:13px;font-weight:700}
.section{display:flex;justify-content:space-between;align-items:center;margin:27px 0 13px}.section h2{font-size:21px;color:#073f32;margin:0;font-weight:800}.link{color:#087d57;font-size:12px;font-weight:700}
.tool{background:#fff;border:1px solid #e1eee9;border-radius:20px;padding:18px 13px;min-height:145px;box-shadow:0 7px 22px #125b450f}.tool-icon{width:50px;height:50px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:24px;margin-bottom:11px}.green{background:#dff7eb}.blue{background:#e2efff}.orange{background:#fff0d7}.purple{background:#eee5ff}.red{background:#ffe4e7}.pink{background:#ffe4f4}.tool-name{font-size:14px;font-weight:800;color:#073f32}.tool-desc{font-size:10px;color:#78918b;line-height:1.6;margin-top:4px}
.recent{background:#fff;border:1px solid #e1eee9;border-radius:20px;padding:10px 16px}.row{display:flex;align-items:center;justify-content:space-between;padding:11px 2px;border-bottom:1px solid #edf3f0}.row:last-child{border-bottom:0}.row-left{display:flex;gap:11px;align-items:center}.ri{width:42px;height:42px;border-radius:13px;background:#e5f8ef;display:flex;align-items:center;justify-content:center}.rn{font-size:13px;font-weight:700;color:#214f43}.rt{font-size:10px;color:#91a49f}
.ad{margin-top:20px;padding:19px 22px;border-radius:22px;background:linear-gradient(110deg,#087d55,#19ae71);color:#fff;display:flex;align-items:center;justify-content:space-between;box-shadow:0 10px 28px #087d5528}.adt{font-size:15px;font-weight:800}.add{font-size:10px;opacity:.9;margin-top:4px}.adb{background:#fff;color:#087c55;border-radius:25px;padding:10px 15px;font-size:12px;font-weight:800}
.bottom{position:fixed;left:50%;bottom:9px;transform:translateX(-50%);width:min(1000px,94%);background:#fffffff7;border:1px solid #dcebe5;border-radius:24px;padding:9px 10px;display:flex;justify-content:space-around;box-shadow:0 10px 35px #00000020;z-index:999}.nav{text-align:center;color:#748c85;font-size:10px}.nav span{display:block;font-size:20px;margin-bottom:1px}.active{color:#087d57;font-weight:800}
@media(max-width:700px){.block-container{padding:12px 10px 100px}.brand-title{font-size:22px}.logo{width:47px;height:47px}.greeting h1{font-size:24px}.hero{padding:23px;min-height:250px}.hero h2{font-size:20px;max-width:80%}.hero p{font-size:11px;max-width:78%}.robot{font-size:78px;right:-4px}.credit{padding:14px}.reward{font-size:10px;padding:9px}.section h2{font-size:18px}.tool{min-height:138px;padding:14px 9px}.tool-name{font-size:12px}.tool-desc{font-size:9px}.ad{padding:16px}.adt{font-size:12px}.adb{font-size:10px;padding:8px 10px}}
</style>''', unsafe_allow_html=True)

# Header
st.markdown('''<div class="header"><div class="brand"><div class="logo">✦</div><div><div class="brand-title">Mya AI ✨</div><div class="brand-sub">သင့်ရဲ့ AI မိတ်ဆွေ</div></div></div><div class="icons"><div class="icon">🔔</div><div class="icon">👤</div></div></div>''', unsafe_allow_html=True)

st.markdown('''<div class="greeting"><h1>မင်္ဂလာပါ 👋</h1><p>ဒီနေ့ သင့်အတွက် AI နဲ့ ဘာလုပ်ပေးရမလဲ?</p></div>''', unsafe_allow_html=True)

st.markdown('''<div class="hero"><h2>AI နဲ့ စာရေး၊ ဒီဇိုင်း၊ ဈေးရောင်းတာတွေ အလွယ်တကူလုပ်မယ်!</h2><p>အွန်လိုင်းရောင်းချသူများ၊ Content ဖန်တီးသူများနဲ့ လုပ်ငန်းရှင်များအတွက် အသုံးဝင်တဲ့ AI ကိရိယာများကို လွယ်လွယ်ကူကူ အသုံးပြုနိုင်ပါတယ်။</p><div class="hero-btn">✨ စတင်အသုံးပြုမယ် →</div><div class="robot">🤖</div></div>''', unsafe_allow_html=True)

st.markdown(f'''<div class="credit"><div class="credit-left"><div class="credit-icon">🪙</div><div><div class="small">လက်ရှိ အသုံးပြုခွင့်</div><div class="num">{st.session_state.credits}</div></div></div><div class="reward">🎁 ကြော်ငြာကြည့်ပြီး<br>အသုံးပြုခွင့်ရယူမယ် →</div></div>''', unsafe_allow_html=True)

st.markdown('''<div class="section"><h2>▦ AI ကိရိယာများ</h2><div class="link">အားလုံးကြည့်ရန် →</div></div>''', unsafe_allow_html=True)

tools = [
    ("📝","green","AI စာရေးပေးမယ်","Post၊ Caption စာသားများ ရေးပေးမယ်"),
    ("♪","blue","TikTok / Reels","ဗီဒီယိုစာသားများ ဖန်တီးမယ်"),
    ("文","blue","ဘာသာပြန်","ဘာသာစကားများကို ပြန်ပေးမယ်"),
    ("📣","orange","Marketing အကြံပြုချက်","ရောင်းချရေးအတွက် အကြံများ"),
    ("🖼️","purple","AI ပုံဖန်တီးခြင်း","ပုံအကြံနှင့် Prompt ဖန်တီးမယ်"),
    ("▶","red","Video Script","ဗီဒီယိုအတွက် Script ရေးမယ်"),
    ("🎙️","green","အသံဖန်တီးခြင်း","စာသားမှ အသံပြောင်းမယ်"),
    ("✨","pink","Content အကြံများ","အကြောင်းအရာ အကြံများ ရယူမယ်"),
]
cols = st.columns(4)
for i,(icon,color,name,desc) in enumerate(tools):
    with cols[i%4]:
        st.markdown(f'''<div class="tool"><div class="tool-icon {color}">{icon}</div><div class="tool-name">{name}</div><div class="tool-desc">{desc}</div></div>''', unsafe_allow_html=True)

st.markdown('''<div class="section"><h2>◷ ယနေ့ အသုံးပြုမှုများ</h2><div class="link">အားလုံးကြည့်ရန် →</div></div>''', unsafe_allow_html=True)

items=[("📝","AI စာရေးပေးမယ်","5 ကြိမ်အသုံးပြု"),("♪","TikTok / Reels Script","3 ကြိမ်အသုံးပြု"),("💡","Marketing အကြံပြုချက်","5 ကြိမ်အသုံးပြု")]
st.markdown('<div class="recent">',unsafe_allow_html=True)
for icon,name,count in items:
    st.markdown(f'''<div class="row"><div class="row-left"><div class="ri">{icon}</div><div><div class="rn">{name}</div><div class="rt">{count}</div></div></div><div>›</div></div>''',unsafe_allow_html=True)
st.markdown('</div>',unsafe_allow_html=True)

st.markdown('''<div class="ad"><div><div class="adt">📣 ကြော်ငြာကြည့်ပြီး Credits ရယူပါ!</div><div class="add">ကြော်ငြာတစ်ခုကြည့်ရုံနဲ့ အသုံးပြုခွင့် ထပ်ရနိုင်ပါတယ်။</div></div><div class="adb">▶ ကြည့်မယ် →</div></div>''',unsafe_allow_html=True)

st.markdown('''<div class="bottom"><div class="nav active"><span>⌂</span>ပင်မ</div><div class="nav"><span>▤</span>ကိရိယာများ</div><div class="nav"><span>◷</span>မှတ်တမ်း</div><div class="nav"><span>🎁</span>ဆုလက်ဆောင်</div><div class="nav"><span>⚙</span>ဆက်တင်များ</div></div>''',unsafe_allow_html=True)
