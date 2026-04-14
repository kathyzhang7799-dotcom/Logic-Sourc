import streamlit as st
import time

# =========================================
# 1. 初始化核心引擎
# =========================================
st.set_page_config(page_title="Code: Credits", layout="centered")

if 'game_step' not in st.session_state: st.session_state.game_step = "lang_selection"
if 'points_mine' not in st.session_state: st.session_state.points_mine = 50
if 'lang' not in st.session_state: st.session_state.lang = None

def check_death():
    if st.session_state.points_mine <= 0 and st.session_state.lang:
        msg = "💀 系统判定：该个体学分归零，判定为“无培养价值”。" if st.session_state.lang == "cn" else "💀 System Verdict: Credits Zero. Classified as 'Unproductive'."
        st.error(msg)
        st.write("你的档案被碎纸机搅碎，班主任冷漠地指了指校门口。" if st.session_state.lang == "cn" else "Your records are shredded. The teacher points coldly to the exit.")
        if st.button("重启人生 / Restart"): st.session_state.clear(); st.rerun()
        st.stop()

# =========================================
# 2. 语言分流
# =========================================
if st.session_state.game_step == "lang_selection":
    st.title("--- [ CODE: CREDITS ] ---")
    st.markdown("### 选择你的生存语言 / Choose your language")
    c1, c2 = st.columns(2)
    if c1.button("中文版本 (全剧情扩张)"):
        st.session_state.lang = "cn"; st.session_state.game_step = "intro_cn"; st.rerun()
    if c2.button("English Version (Full Expansion)"):
        st.session_state.lang = "en"; st.session_state.game_step = "intro_en"; st.rerun()

if st.session_state.lang:
    label = "剩余学分" if st.session_state.lang == "cn" else "Credits"
    st.sidebar.metric(label, st.session_state.points_mine)

check_death()

# =========================================
# 3. 中文全线剧情 (CN Route)
# =========================================
if st.session_state.lang == "cn":

    # --- 1. 教室：询问与氛围 ---
    if st.session_state.game_step == "intro_cn":
        st.write("教室内死寂一片，只有签字笔划过纸张的沙沙声，像是无数蚕食梦想的幼虫。")
        st.write("你坐下时，旁边的同桌正疯狂地填着练习册，他眼眶深陷，笔尖因过度用力而发出刺耳的摩擦声。")
        choice = st.radio("你的行动：", ["请选择...", "1. 保持沉默，假装一切正常", "2. 轻轻敲他的桌子，低声问他在忙什么"], index=0)
        if st.button("确定") and choice != "请选择...":
            if "2." in choice: st.session_state.game_step = "ask_teammate_cn"
            else: st.session_state.game_step = "exam_cn"
            st.rerun()

    elif st.session_state.game_step == "ask_teammate_cn":
        st.write("同桌像被针扎了一样猛地颤抖，他死死护住卷子，认清是你后才松了口气。")
        st.info("“我昨天在寝室偷偷带泡面被抓了。”他声音低得几乎听不见，“王老师罚我写500字检讨，早自习下课必须交。少一个字扣1学分……这学分就是我们的命啊。”")
        if st.button("转过身，王老师走进了教室..."):
            st.session_state.game_step = "exam_cn"; st.rerun()

    # --- 2. 摸底考试 (原题还原) ---
    elif st.session_state.game_step == "exam_cn":
        st.subheader("📝 突击测试")
        st.write("班主任王老师拍了拍讲台：“2分钟，决定你们今天的定级。别想作弊，我的眼睛盯着你们呢。”")
        q1 = st.radio("第一道题：在这种环境下，你决定赌一把，选哪个？", ["...", "a", "b", "c"], key="q1_cn")
        q2 = st.radio("第二道题：逻辑序列依然是 a, b, c...", ["...", "a", "b", "c"], key="q2_cn")
        if st.button("交卷"):
            if q1 == "a": st.session_state.points_mine += 1
            if q2 == "c": st.session_state.points_mine += 1
            st.session_state.game_step = "collision_cn"; st.rerun()

    # --- 3. 撞人：不分青红皂白 (顺序调整) ---
    elif st.session_state.game_step == "collision_cn":
        st.write("下课铃响起，楼道瞬间拥挤得让人窒息。你急着去食堂。")
        st.write("转角处，年级第一的“优等生”突然停步，你刹车不及撞了上去。王老师就像预谋好了一样，瞬间从阴影里冲出。")
        st.error("“你在干什么？！”他一把推开你，小心翼翼地检查优等生的胳膊，“你这种差生要是撞坏了他的手，让他写不了字，你赔得起他的前途吗？！”")
        st.write("你刚想辩解，王老师便咆哮道：“闭嘴！解释就是推卸责任！明天叫你家长来办公室！”")
        st.write("---")
        st.write("次日办公室，父母唯唯诺诺地向王老师鞠躬，他们的旧衬衫上还有没洗掉的泥点，在整洁的办公室里显得格格不入。")
        st.info("王老师嫌弃地扇着鼻子前的空气，仿佛那里有一股恶臭：“一股穷酸味。带坏优等生，扣10学分！带回去管好，别让他再害人。”")
        if st.button("心碎地回到寝室"):
            with st.status("🌙 屈辱在夜晚蔓延..."): time.sleep(1.5)
            st.session_state.points_mine -= 10
            st.session_state.game_step = "dorm_night_cn"; st.rerun()

    # --- 4. 寝室冲突：恶意 ---
    elif st.session_state.game_step == "dorm_night_cn":
        st.write("推开402寝室，原本的谈笑声瞬间熄灭。张国伟坐在床头，手里摆弄着他的名牌球鞋。")
        st.error("“哟，大孝子回来了？”他阴阳怪气地抬眼，“听说你妈今天在办公室求饶的样子，跟路边收废品的一模一样啊？哈哈哈哈！”")
        st.write("周围的室友也跟着哄笑。那种嘲讽像刀一样割在你脸上。")
        choice = st.radio("你的反应：", ["1. 爆发质问", "2. 保持沉默", "3. 躲进被窝"])
        if st.button("做出抉择"):
            with st.status("🕐 第二天食堂..."): time.sleep(1.5)
            st.session_state.game_step = "cafeteria_cn"; st.rerun()

    # --- 5. 食堂冲突：收废品论 ---
    elif st.session_state.game_step == "cafeteria_cn":
        st.write("食堂里，你拿着冰冷的塑料餐盘排队。张国伟故意经过你身边，猛地撞了一下。")
        st.warning("“哎呀，不好意思。反正你这校服跟你爸妈那身收废品的衣服一样脏，多点菜汤也没关系吧？”")
        if st.button("忍住，为了学分..."):
            with st.status("💡 入夜，黑暗降临。"): time.sleep(1)
            st.session_state.points_mine -= 2
            st.session_state.game_step = "phone_crisis_cn"; st.rerun()

    # --- 6. 手机搜查：背叛 ---
    elif st.session_state.game_step == "phone_crisis_cn":
        st.write("深夜，走廊里传来沉重的皮鞋声。王老师推开寝室门，手电筒的光柱极其刺眼。")
        st.error("“举报违规奖励 120学分。只要举报属实，这学期你就能换到单间宿舍。”")
        st.write("你兜里的手机滚烫，那是你和外界唯一的联系。你看到张国伟的眼神正死死锁定在你的枕头下。")
        hide = st.radio("藏在哪？", ["1. 裤兜里", "2. 扔到楼下", "3. 塞进张国伟臭鞋里", "4. 暖气片后"])
        if st.button("生死抉择"):
            st.session_state.points_mine -= 15
            st.error("手机最终还是被王老师搜了出来。他露出了那个令人不寒而栗的微笑。")
            if st.button("查看最终的真相"): st.session_state.game_step = "reveal_truth_cn"; st.rerun()

    elif st.session_state.game_step == "reveal_truth_cn":
        st.markdown('<div style="background-color:#ededed;padding:15px;border-radius:10px;color:black;"><b>张国伟:</b> 老师，那举报的120学分什么时候到账？<br><b>王老师:</b> 表现不错，明天早操奖励你。</div>', unsafe_allow_html=True)
        st.error("背叛。价值120学分的“友谊”。")
        if st.button("第一章 完"): st.balloons(); st.stop()

# =========================================
# 4. 英文全线剧情 (EN Route - Full Expansion)
# =========================================
elif st.session_state.lang == "en":

    if st.session_state.game_step == "intro_en":
        st.write("The classroom is dead silent. Only the scratching of pens echoes like insects devouring dreams.")
        st.write("Your seatmate is writing frantically, his eyes sunken and his pen trembling with exhaustion.")
        choice = st.radio("Your action:", ["Choose...", "1. Stay silent", "2. Ask him what he's doing"], index=0)
        if st.button("Confirm") and choice != "Choose...":
            if "2." in choice: st.session_state.game_step = "ask_teammate_en"
            else: st.session_state.game_step = "exam_en"
            st.rerun()

    elif st.session_state.game_step == "ask_teammate_en":
        st.info("'They caught me with instant noodles last night,' he whispers. 'Mr. Wang ordered a 500-word reflection by 8 AM. Every missing word is 1 credit lost. Credits are our lives here.'")
        if st.button("The teacher enters..."): st.session_state.game_step = "exam_en"; st.rerun()

    elif st.session_state.game_step == "exam_en":
        st.subheader("📝 Surprise Test")
        st.write("Mr. Wang slams the podium: '2 minutes. This defines your credit tier for today. No cheating.'")
        q1 = st.radio("Q1: You decide to gamble. Pick one:", ["...", "a", "b", "c"], key="q1_en")
        q2 = st.radio("Q2: Sequence continues a, b, c...", ["...", "a", "b", "c"], key="q2_en")
        if st.button("Submit"):
            if q1 == "a": st.session_state.points_mine += 1
            if q2 == "c": st.session_state.points_mine += 1
            st.session_state.game_step = "collision_en"; st.rerun()

    elif st.session_state.game_step == "collision_en":
        st.write("The bell rings. The hallway is suffocating. You are rushing to the cafeteria.")
        st.error("'What are you doing?!' Mr. Wang screams as you bump into the 'Top Student'. He doesn't listen to you.")
        st.write("'A failure like you bumping into a genius? You can't pay for his future!'")
        st.write("---")
        st.write("In the office, your parents bow low. Their worn-out clothes look pathetic in the sterile room.")
        st.info("Wang fans the air in front of his nose: 'Smells like poverty. -10 Credits!'")
        if st.button("Back to the dorm"):
            with st.status("🌙 Night falls..."): time.sleep(1.5)
            st.session_state.points_mine -= 10
            st.session_state.game_step = "dorm_night_en"; st.rerun()

    elif st.session_state.game_step == "dorm_night_en":
        st.write("You open the door to Dorm 402. The laughter stops. Zhang sits on his bunk.")
        st.error("'The filial son is back?' he mocks. 'I heard your mom begging today. She looked just like a trash collector on the street! Hahaha!'")
        if st.button("Continue"):
            with st.status("🕐 Tomorrow at the cafeteria..."): time.sleep(1.5)
            st.session_state.game_step = "cafeteria_en"; st.rerun()

    elif st.session_state.game_step == "cafeteria_en":
        st.write("Zhang bumps your tray on purpose, spilling soup on your sleeve.")
        st.warning("'Oops. Well, your uniform is as dirty as your parents' trash-collecting rags anyway, right?'")
        if st.button("Endure"):
            with st.status("💡 Night arrives."): time.sleep(1)
            st.session_state.points_mine -= 2
            st.session_state.game_step = "phone_en"; st.rerun()

    elif st.session_state.game_step == "phone_en":
        st.write("Late at night, Wang enters: '120 credits for reporting contraband electronics.'")
        st.write("Zhang is staring at your pillow with hungry eyes.")
        hide = st.radio("Hide phone:", ["Pocket", "Window", "Zhang's Shoe", "Radiator"])
        if st.button("Confirm"):
            st.session_state.points_mine -= 15
            st.error("The phone is seized. Wang smiles cruelly.")
            if st.button("The Truth"): st.session_state.game_step = "reveal_en"; st.rerun()

    elif st.session_state.game_step == "reveal_en":
        st.markdown('<div style="background-color:#ededed;padding:15px;border-radius:10px;color:black;"><b>Zhang:</b> Sir, where are my 120 snitching credits?<br><b>Wang:</b> Tomorrow morning. Good job.</div>', unsafe_allow_html=True)
        st.error("Betrayal. Your 'friend' sold you for 120 credits.")
        if st.button("End Chapter 1"): st.balloons(); st.stop()