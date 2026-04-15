import random
import streamlit as st
import time

# 1. 初始化设置
st.set_page_config(page_title="SASK-ENCRYPT-GATEWAY", layout="centered")

# 2. 状态初始化
if 'mode' not in st.session_state:
    st.session_state.mode = "lang_select"
if 'lang' not in st.session_state:
    st.session_state.lang = "CN"

# 3. 语言字典：加入更冷酷的军事化术语
TEXTS = {
    "CN": {
        "title": "SYSTEM BOOT: GMNEII_SASK_ROOT",
        "btn": "执行强制协议 (FORCE_AUTH)",
        "load": "同步萨省加密卫星节点...",
        "ready": "内核逻辑已注入 - [LOGIC SOURCE v4.0]",
        "system_status": "节点: MOOSE-JAW-SERVER | 加密: RSA-4096 | 状态: 幽灵模式"
    },
    "EN": {
        "title": "SYSTEM BOOT: GMNEII_SASK_ROOT",
        "btn": "EXECUTE FORCE_AUTH",
        "load": "SYNCING SASK-SATELLITE NODES...",
        "ready": "KERNEL INJECTED - [LOGIC SOURCE v4.0]",
        "system_status": "NODE: MOOSE-JAW-SERVER | ENC: RSA-4096 | STATUS: GHOST_MODE"
    }
}
L = TEXTS[st.session_state.lang]

# 4. 极致黑客视觉 (黑底绿字，去掉所有现代UI感)
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00FF41; font-family: 'Courier New', monospace; }
    .stButton>button { border: 1px solid #00FF41; background-color: #000000; color: #00FF41; border-radius: 0px; height: 50px; font-weight: bold;}
    .stButton>button:hover { background-color: #00FF41 !important; color: #000000 !important; box-shadow: 0 0 20px #00FF41; }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    /* 自定义代码块颜色 */
    code { color: #00FF41 !important; background-color: #111 !important; }
    </style>
""", unsafe_allow_html=True)

# 5. 路由逻辑
if st.session_state.mode == "lang_select":
    st.markdown("<h1 style='text-align: center;'>[ TERMINAL_BOOT_v4.0 ]</h1>", unsafe_allow_html=True)
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("PROTOCOL: ZH_CN"):
            st.session_state.lang, st.session_state.mode = "CN", "auth"
            st.rerun()
    with col2:
        if st.button("PROTOCOL: EN_US"):
            st.session_state.lang, st.session_state.mode = "EN", "auth"
            st.rerun()

elif st.session_state.mode == "auth":
    st.markdown(f"### {L['title']}")
    st.text(L['system_status'])
    st.write("---")
    pwd = st.text_input("ENTER ACCESS KEY (ROOT@GMNEII):", type="password")
    if st.button(L['btn']):
        if pwd == "prairie_gmneii.ca.py":
            st.session_state.mode = "cool"
            st.rerun()
        elif pwd != "":
            st.session_state.mode = "destruct"
            st.rerun()

elif st.session_state.mode == "cool":
    # 模拟多阶段破译，拉长时间线
    status_box = st.empty()
    bar = st.progress(0)

    stages = [
        "正在绕过萨省电力局防火墙...",
        "正在建立量子纠缠链路...",
        "正在伪造核心签名...",
        "正在劫持逻辑源节点..."
    ] if st.session_state.lang == "CN" else [
        "BYPASSING SASK-POWER FIREWALL...",
        "ESTABLISHING QUANTUM LINK...",
        "FORGING CORE SIGNATURE...",
        "HIJACKING LOGIC-SOURCE NODES..."
    ]

    for idx, stage in enumerate(stages):
        status_box.markdown(f"**>>> {stage}**")
        for p in range(25):
            time.sleep(0.04)  # 稍微慢一点，更有真实感
            bar.progress((idx * 25) + p + 1)
        st.toast(f"Phase {idx + 1} Complete", icon="✔")

    # 成功后的视觉冲击：不再蹦气球，而是满屏代码流
    st.success("ACCESS GRANTED. KERNEL BYPASS SUCCESSFUL.")
    time.sleep(0.5)

    with st.expander("VIEW SYSTEM LOGS (ROOT)", expanded=True):
        for _ in range(8):
            hex_dump = "".join([random.choice("0123456789ABCDEF") for _ in range(16)])
            st.text(f"MEM_DUMP: 0x{hex_dump} ... LOADED")
            time.sleep(0.1)

    st.markdown(f"## ⚡ {L['ready']}")

    if st.button("INITIALIZE: LOGIC_SOURCE"):
        st.warning("核心逻辑已挂载。正在等待指令...")
        time.sleep(2)
        st.session_state.mode = "lang_select"
        st.rerun()

elif st.session_state.mode == "destruct":
    # 背景爆红
    st.markdown("<style>.stApp { background-color: #880000; }</style>", unsafe_allow_html=True)
    st.error("🚨 CRITICAL: UNAUTHORIZED ACCESS DETECTED 🚨")

    # 模拟硬件损毁
    for i in range(5):
        st.markdown(f"**ERASING SECTOR 0x000{i}F ... [DATA_WIPED]**")
        time.sleep(0.3)

    # 倒计时
    t = st.empty()
    for i in range(5, 0, -1):
        t.markdown(f"<h1 style='text-align:center; font-size: 80px;'>{i}</h1>", unsafe_allow_html=True)
        time.sleep(1)

    st.error("HARDWARE PERMANENTLY LOCKED.")
    if st.button("REBOOT_EMERGENCY"):
        st.session_state.mode = "lang_select"
        st.rerun()

# 兜底逻辑
else:
    st.session_state.mode = "lang_select"
    st.rerun()
