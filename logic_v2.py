import random
import streamlit as st
import time

# 1. 核心视觉架构
st.set_page_config(page_title="SASK_CORE_TERMINAL_V7", layout="wide", initial_sidebar_state="collapsed")

# 初始化状态机
if 'mode' not in st.session_state: st.session_state.mode = "init"
if 'lang' not in st.session_state: st.session_state.lang = "CN"
if 'hack_step' not in st.session_state: st.session_state.hack_step = 0

# 注入 CSS：十字准星 + 震动自毁特效
st.markdown("""
    <style>
    .stApp { background-color: #020202; color: #00FF41; font-family: 'Consolas', monospace; }

    /* 十字准星鼠标指针 */
    html, body, .stApp { 
        cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 2v20M2 12h20" stroke="%2300FF41" stroke-width="1" opacity="0.8"/></svg>') 12 12, auto !important; 
    }
    button, input, a { cursor: pointer !important; }

    /* 自毁闪烁特效 */
    @keyframes destruct { 0% { background-color: #000; } 50% { background-color: #600; } 100% { background-color: #000; } }
    .self-destruct { animation: destruct 0.2s infinite; }

    .stButton>button { border: 1px solid #00FF41 !important; background: transparent !important; color: #00FF41 !important; border-radius: 0px !important; height: 50px; font-weight: bold; width: 100%; }
    .stButton>button:hover { background: #00FF41 !important; color: #000 !important; box-shadow: 0 0 20px #00FF41 !important; }
    .stTextInput>div>div>input { background: #000 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; border-radius: 0; }

    header {visibility: hidden;} footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 2. 语言包
TEXTS = {
    "CN": {
        "auth_title": ">> 核心安全验证 (SECURITY_SHIELD)",
        "pwd_label": "请输入访问密钥 (ROOT_KEY):",
        "auth_btn": "执行权限申请",
        "warn": "⚠️ 发现自动防御拦截！",
        "bypass": "手动绕过防火墙",
        "report": "成功截获服务器节点数据：",
        "destruct_msg": "🚨 密钥错误！触发安全自毁程序..."
    },
    "EN": {
        "auth_title": ">> CORE_SECURITY_AUTHENTICATION",
        "pwd_label": "ENTER ROOT_ACCESS_KEY:",
        "auth_btn": "EXECUTE_ACCESS_REQUEST",
        "warn": "⚠️ AUTOMATED DEFENSE DETECTED!",
        "bypass": "BYPASS_MANUALLY",
        "report": "SERVER_NODE_DATA_EXTRACTED:",
        "destruct_msg": "🚨 WRONG KEY! SELF-DESTRUCT SEQUENCE INITIATED..."
    }
}
L = TEXTS[st.session_state.lang]

# --- 路由逻辑 ---

# [1. 语言选择]
if st.session_state.mode == "init":
    st.markdown("<h1 style='text-align:center; margin-top:10%; letter-spacing:15px;'>SASK_CORE_LINK</h1>",
                unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("SET_PROTOCOL: ZH_CN"):
            st.session_state.lang, st.session_state.mode = "CN", "auth";
            st.rerun()
    with c2:
        if st.button("SET_PROTOCOL: EN_US"):
            st.session_state.lang, st.session_state.mode = "EN", "auth";
            st.rerun()

# [2. 身份验证前置]
elif st.session_state.mode == "auth":
    st.markdown(f"### {L['auth_title']}")
    st.write("---")
    pwd = st.text_input(L['pwd_label'], type="password")
    if st.button(L['auth_btn']):
        if pwd.strip() == "prairie_yyl.py":
            st.session_state.mode = "boot"
            st.rerun()
        elif pwd != "":
            st.session_state.mode = "destruct"
            st.rerun()

# [3. 自毁程序]
elif st.session_state.mode == "destruct":
    st.markdown("<style>.stApp { animation: destruct 0.2s infinite; }</style>", unsafe_allow_html=True)
    st.error(L['destruct_msg'])
    destruct_box = st.empty()
    logs = ""
    for i in range(10):
        logs += f"> Wiping sector {hex(random.randint(0x1000, 0xFFFF))}... [OVERWRITTEN]\n"
        destruct_box.code(logs)
        time.sleep(0.15)
    st.session_state.mode = "init"
    st.rerun()

# [4. BIOS 加载]
elif st.session_state.mode == "boot":
    st.markdown("### [ KERNEL_INITIALIZING ]")
    log_area = st.empty()
    boot_log = ""
    steps = ["MEM_CHECK...", "SAT_LINK_SYNC...", "GHOST_SHELL_LOAD...", "SYSTEM_READY."]
    for step in steps:
        boot_log += f"> {step} [OK]\n"
        log_area.code(boot_log)
        time.sleep(0.4)
    st.session_state.mode = "cracking"
    st.rerun()

# [5. 互动破解]
elif st.session_state.mode == "cracking":
    st.markdown(f"### ⚙️ PENETRATING_SASK_VAULT: {st.session_state.hack_step}%")
    col_l, col_r = st.columns([2, 1])
    with col_l:
        log_box = st.empty()
        log_box.code("\n".join(
            [f"[ {time.strftime('%H:%M:%S')} ] SCAN: {hex(random.randint(0x111111, 0x999999))}" for _ in range(8)]))
        if st.session_state.hack_step in [40, 80]:
            st.warning(L['warn'])
            if st.button(L['bypass']):
                st.session_state.hack_step += 1
                st.rerun()
            else:
                st.stop()
    with col_r:
        st.write("### PROGRESS")
        st.progress(st.session_state.hack_step / 100)
        if st.session_state.hack_step < 100:
            st.session_state.hack_step += 1
            time.sleep(0.04)
            st.rerun()
        else:
            if st.button(">> FINAL_DECRYPTION"):
                st.session_state.mode = "report";
                st.rerun()

# [6. 战果报告]
elif st.session_state.mode == "report":
    st.markdown(f"## 📁 {L['report']}")
    st.json({"NODE_ID": "MOOSE-JAW-SRV-01", "IP": "10.0.0.1", "STATUS": "UNLOCKED", "PAYLOAD": "INJECTED"})
    if st.button(">> ENTER_SYSTEM"):
        st.session_state.mode = "cool";
        st.rerun()

# [7. 终极挂机屏保 (含动态数值浮动)]
elif st.session_state.mode == "cool":
    # 顶部监控列
    header_cols = st.columns(4)
    m1 = header_cols[0].empty()
    m2 = header_cols[1].empty()
    m3 = header_cols[2].empty()
    with header_cols[3]:
        if st.button("CONSOLE"): st.session_state.mode = "main_menu"; st.rerun()

    st.write("---")
    hex_area = st.empty()

    # 核心跳动循环
    while True:
        # 1. 计算浮动数值
        current_ping = random.randint(18, 35)  # Ping 值在 18-35ms 波动
        cpu_load = random.uniform(88.2, 99.1)  # CPU 负载在 88-99% 波动

        # 2. 更新仪表盘
        m1.metric("STATUS", "STEALTH", delta="SECURE")
        m2.metric("PING", f"{current_ping}ms", delta=f"{random.choice(['+', '-'])}{random.randint(1, 3)}ms")
        m3.metric("CPU_LOAD", f"{cpu_load:.1f}%", delta=f"{random.choice(['+', '-'])}{random.uniform(0.1, 0.5):.1f}%")

        # 3. 更新 16 进制流
        lines = "\n".join(["".join([random.choice("0123456789ABCDEF") for _ in range(50)]) for _ in range(12)])
        hex_area.code(lines)

        time.sleep(0.4)  # 刷新频率控制，既有跳动感又不会闪瞎眼

# [主菜单]
elif st.session_state.mode == "main_menu":
    st.success("SUCCESS: YOU ARE IN CONTROL.")
    if st.button("LOGOUT"):
        st.session_state.mode = "init"
        st.session_state.hack_step = 0
        st.rerun()
