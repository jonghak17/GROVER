import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="GROVER: NL2SQL 프로젝트",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ---- fonts & theme ---- */
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Noto+Sans+KR:wght@400;500;700&family=Noto+Serif+KR:wght@600;700&display=swap');

:root {
    --bg: #f3ede2;
    --bg-soft: #f8f4ec;
    --surface: rgba(252, 249, 242, 0.9);
    --surface-strong: #fcfaf5;
    --ink: #1f2625;
    --muted: #5f6866;
    --line: #d6cdbf;
    --accent: #7b4c3a;
    --accent-soft: rgba(123, 76, 58, 0.14);
    --accent-cool: #315a59;
    --accent-cool-soft: rgba(49, 90, 89, 0.1);
    --accent-olive: #6c7557;
    --accent-olive-soft: rgba(108, 117, 87, 0.11);
    --accent-gold: #a17343;
    --accent-gold-soft: rgba(161, 115, 67, 0.11);
    --accent-plum: #6d586d;
    --accent-plum-soft: rgba(109, 88, 109, 0.1);
    --danger: #a95a58;
    --danger-soft: rgba(169, 90, 88, 0.1);
    --shadow: 0 12px 28px rgba(34, 31, 28, 0.06);
}

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
    color: var(--ink);
}

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main {
    background:
        linear-gradient(rgba(123, 76, 58, 0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(123, 76, 58, 0.04) 1px, transparent 1px),
        linear-gradient(180deg, var(--bg) 0%, var(--bg-soft) 100%);
    background-size: 28px 28px, 28px 28px, auto;
}

.main .block-container {
    max-width: 1200px;
    padding-top: 2.2rem;
    padding-bottom: 4rem;
}

h1, h2, h3, h4,
.section-header,
.subsection-header,
.hero-title {
    font-family: 'Noto Serif KR', serif;
    letter-spacing: -0.02em;
}

code,
pre,
.formula-box,
.hero-meta-value,
.stage-code,
.score-card-value,
.score-vector {
    font-family: 'IBM Plex Mono', monospace;
}

/* ---- sidebar ---- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #27231f 0%, #181512 100%);
    border-right: 1px solid rgba(239, 229, 214, 0.14);
}
[data-testid="stSidebar"] * {
    color: #efe5d6 !important;
}
[data-testid="stSidebar"] .block-container {
    padding-top: 1.45rem;
}
[data-testid="stSidebar"] .stRadio label {
    padding: 8px 12px;
    border: 1px solid transparent;
    border-radius: 0;
    transition: background 0.2s, border-color 0.2s;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,0.04);
    border-color: rgba(239, 229, 214, 0.18);
}

/* ---- hero banner ---- */
.hero {
    background: linear-gradient(180deg, rgba(252, 249, 242, 0.96) 0%, rgba(245, 237, 226, 0.92) 100%);
    border: 1px solid var(--line);
    border-radius: 0;
    padding: 42px 42px 36px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow);
}
.hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        linear-gradient(180deg, rgba(49, 90, 89, 0.08) 0%, transparent 40%),
        linear-gradient(90deg, transparent 0%, transparent 58%, rgba(49, 90, 89, 0.08) 58%, rgba(49, 90, 89, 0.08) 59%, transparent 59%);
    pointer-events: none;
}
.hero::after {
    content: "";
    position: absolute;
    right: 28px;
    top: 22px;
    width: 190px;
    height: 190px;
    border-radius: 50%;
    border: 1px solid rgba(49, 90, 89, 0.16);
    opacity: 0.9;
}
.hero-grid {
    display: grid;
    grid-template-columns: minmax(0, 2.1fr) minmax(250px, 1fr);
    gap: 24px;
    position: relative;
    z-index: 1;
}
.hero-title {
    font-size: 3rem;
    font-weight: 700;
    color: var(--ink);
    line-height: 1.08;
    margin-bottom: 12px;
}
.hero-subtitle {
    font-size: 1rem;
    color: var(--muted);
    max-width: 720px;
    line-height: 1.75;
}
.hero-badge {
    display: inline-block;
    background: transparent;
    color: var(--accent);
    border: 1px solid var(--accent-soft);
    border-radius: 999px;
    padding: 5px 14px;
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    margin-bottom: 18px;
    text-transform: uppercase;
}
.hero-panel {
    background: rgba(31, 38, 37, 0.03);
    border: 1px solid rgba(31, 38, 37, 0.1);
    padding: 18px 20px;
    align-self: start;
}
.hero-panel-label {
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--accent);
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 10px;
}
.hero-panel-copy {
    color: var(--ink);
    font-size: 0.92rem;
    line-height: 1.75;
}
.hero-meta {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    margin-top: 22px;
}
.hero-meta-item {
    padding: 12px 14px;
    border-top: 1px solid var(--line);
    background: rgba(252, 249, 242, 0.8);
}
.hero-meta-label {
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--muted);
    letter-spacing: 0.12em;
    text-transform: uppercase;
}
.hero-meta-value {
    margin-top: 7px;
    font-size: 0.8rem;
    line-height: 1.6;
    color: var(--ink);
}

/* ---- section headers ---- */
.section-header {
    position: relative;
    font-size: 1.42rem;
    font-weight: 700;
    color: var(--ink);
    padding: 0 0 12px 16px;
    border-bottom: 1px solid var(--line);
    margin: 10px 0 24px;
}
.section-header::before {
    content: "";
    position: absolute;
    left: 0;
    top: 4px;
    bottom: 12px;
    width: 4px;
    background: var(--accent-cool);
}
.subsection-header {
    position: relative;
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--ink);
    margin-top: 30px;
    margin-bottom: 12px;
    padding-left: 14px;
}
.subsection-header::before {
    content: "";
    position: absolute;
    left: 0;
    top: 4px;
    bottom: 4px;
    width: 3px;
    background: var(--accent);
}

/* ---- info / highlight cards ---- */
.card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 0;
    padding: 22px 24px;
    margin-bottom: 18px;
    box-shadow: var(--shadow);
}
.card-blue {
    background: linear-gradient(180deg, rgba(49, 90, 89, 0.06), rgba(252, 249, 242, 0.94));
    border-left: 4px solid var(--accent-cool);
}
.card-green {
    background: linear-gradient(180deg, rgba(108, 117, 87, 0.08), rgba(252, 249, 242, 0.94));
    border-left: 4px solid var(--accent-olive);
}
.card-purple {
    background: linear-gradient(180deg, rgba(109, 88, 109, 0.08), rgba(252, 249, 242, 0.94));
    border-left: 4px solid var(--accent-plum);
}
.card-orange {
    background: linear-gradient(180deg, rgba(161, 115, 67, 0.08), rgba(252, 249, 242, 0.94));
    border-left: 4px solid var(--accent-gold);
}
.card-red {
    background: linear-gradient(180deg, rgba(169, 90, 88, 0.08), rgba(252, 249, 242, 0.94));
    border-left: 4px solid var(--danger);
}

/* ---- pipeline / stage cards ---- */
.pipeline-step {
    display: flex;
    align-items: flex-start;
    gap: 18px;
    padding: 18px 20px;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 0;
    margin-bottom: 12px;
    box-shadow: var(--shadow);
}
.step-number {
    min-width: 38px;
    height: 38px;
    background: var(--accent-cool);
    color: #f4ede0;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.95rem;
}
.step-content h4 {
    margin: 0 0 4px;
    color: var(--ink);
    font-size: 0.98rem;
    font-weight: 700;
}
.step-content p {
    margin: 0;
    color: var(--muted);
    font-size: 0.9rem;
    line-height: 1.65;
}
.stage-card {
    min-height: 148px;
    padding: 18px 16px;
    background: var(--surface);
    border: 1px solid var(--line);
    border-top: 3px solid var(--accent-cool);
    box-shadow: var(--shadow);
}
.stage-index {
    font-size: 0.74rem;
    font-weight: 700;
    color: var(--accent);
    letter-spacing: 0.14em;
    text-transform: uppercase;
}
.stage-title {
    font-size: 0.94rem;
    font-weight: 700;
    color: var(--ink);
    margin: 10px 0 6px;
    line-height: 1.4;
}
.stage-code {
    display: inline-block;
    font-size: 0.75rem;
    color: var(--accent-cool);
    background: var(--accent-cool-soft);
    padding: 4px 8px;
    margin-bottom: 10px;
}
.stage-copy {
    color: var(--muted);
    font-size: 0.82rem;
    line-height: 1.55;
}

/* ---- metric level cards ---- */
.metric-level {
    border-radius: 0;
    padding: 22px 24px;
    margin-bottom: 20px;
    border: 1px solid var(--line);
    border-left: 5px solid;
    box-shadow: var(--shadow);
}
.level-sql {
    background: linear-gradient(180deg, rgba(49, 90, 89, 0.07), rgba(252, 249, 242, 0.92));
    border-color: var(--accent-cool);
}
.level-db {
    background: linear-gradient(180deg, rgba(108, 117, 87, 0.08), rgba(252, 249, 242, 0.92));
    border-color: var(--accent-olive);
}
.level-insight {
    background: linear-gradient(180deg, rgba(109, 88, 109, 0.08), rgba(252, 249, 242, 0.92));
    border-color: var(--accent-plum);
}
.metric-level h3 {
    margin: 0 0 8px;
    font-size: 1.08rem;
    font-weight: 700;
}
.metric-level p {
    margin: 0;
    color: var(--muted);
    font-size: 0.9rem;
    line-height: 1.7;
}

/* ---- formula box ---- */
.formula-box {
    background: #232826;
    border-left: 4px solid var(--accent-gold);
    border-radius: 0;
    padding: 16px 20px;
    margin: 12px 0;
    color: #efe5d6;
    font-size: 0.9rem;
    line-height: 1.75;
}

/* ---- example box ---- */
.example-box {
    background: rgba(252, 249, 242, 0.9);
    border: 1px solid var(--line);
    border-left: 4px solid var(--accent-gold);
    border-radius: 0;
    padding: 18px 20px;
    margin: 14px 0;
}
.example-label {
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--accent-gold);
    text-transform: uppercase;
    letter-spacing: 0.14em;
    margin-bottom: 8px;
}

/* ---- contribution cards ---- */
.contribution {
    background: var(--surface);
    border: 1px solid var(--line);
    border-left: 4px solid var(--accent-cool);
    border-radius: 0;
    padding: 18px 22px;
    margin-bottom: 14px;
    box-shadow: var(--shadow);
}
.contribution-tag {
    display: inline-block;
    background: transparent;
    color: var(--accent);
    border: 1px solid var(--accent-soft);
    border-radius: 999px;
    padding: 2px 10px;
    font-size: 0.72rem;
    font-weight: 700;
    margin-bottom: 8px;
    letter-spacing: 0.12em;
}

/* ---- score cards ---- */
.score-card {
    min-height: 168px;
    padding: 20px 18px;
    background: var(--surface);
    border: 1px solid var(--line);
    border-top: 4px solid;
    box-shadow: var(--shadow);
}
.score-card-label {
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--muted);
    letter-spacing: 0.14em;
    text-transform: uppercase;
}
.score-card-value {
    font-size: 1.15rem;
    color: var(--ink);
    margin: 12px 0 8px;
}
.score-card-body {
    color: var(--muted);
    font-size: 0.84rem;
    line-height: 1.6;
}
.score-card.sql { border-top-color: var(--accent-cool); }
.score-card.db { border-top-color: var(--accent-olive); }
.score-card.insight { border-top-color: var(--accent-plum); }
.score-vector {
    text-align: center;
    margin-top: 16px;
    padding: 16px 18px;
    background: var(--surface);
    border: 1px solid var(--line);
    color: var(--ink);
    font-size: 1rem;
}
.score-vector-panel {
    padding: 28px 32px;
    background: #23211f;
    border-top: 4px solid var(--accent-gold);
    box-shadow: var(--shadow);
    text-align: center;
}
.score-vector-panel-label {
    color: #bba995;
    font-size: 0.72rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
}
.score-vector-panel-main {
    color: #f2e8da;
    font-size: 1.35rem;
    margin: 14px 0 16px;
}
.score-vector-panel-sub {
    color: #d8c8b5;
    font-size: 0.9rem;
}
.score-vector-panel-note {
    color: #a59785;
    font-size: 0.82rem;
    margin-top: 12px;
    line-height: 1.65;
}

/* ---- table styling ---- */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 0.9rem;
    background: rgba(252, 249, 242, 0.82);
    border: 1px solid var(--line);
}
th {
    background: #23211f;
    color: #efe5d6;
    padding: 11px 14px;
    text-align: left;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-size: 0.76rem;
}
td {
    padding: 10px 14px;
    border-bottom: 1px solid rgba(214, 205, 191, 0.9);
    color: #33403f;
}
tr:nth-child(even) td { background: rgba(31, 38, 37, 0.02); }
tr:hover td { background: rgba(49, 90, 89, 0.08); }

/* ---- divider ---- */
.fancy-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent 0%, rgba(49, 90, 89, 0.45) 50%, transparent 100%);
    margin: 34px 0;
}

/* ---- claim type badge ---- */
.badge {
    display: inline-block;
    border-radius: 999px;
    padding: 3px 10px;
    font-size: 0.74rem;
    font-weight: 700;
    margin: 3px;
    letter-spacing: 0.04em;
}
.badge-numeric { background: var(--accent-cool-soft); color: var(--accent-cool); }
.badge-comparison { background: var(--accent-olive-soft); color: var(--accent-olive); }
.badge-ranking { background: var(--accent-gold-soft); color: var(--accent-gold); }
.badge-diagnostic { background: var(--accent-plum-soft); color: var(--accent-plum); }

/* ---- score weight table ---- */
.weight-row {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 10px 0;
    border-bottom: 1px solid rgba(214, 205, 191, 0.7);
}
.weight-label { min-width: 130px; font-weight: 500; color: #33403f; font-size: 0.9rem; }
.weight-bar-bg { flex: 1; height: 10px; background: rgba(31, 38, 37, 0.08); border-radius: 999px; }
.weight-bar-fill { height: 10px; border-radius: 999px; }
.weight-pct { min-width: 40px; text-align: right; font-weight: 700; font-size: 0.9rem; color: var(--ink); }

/* ---- streamlit controls ---- */
div[data-baseweb="tab-list"] {
    gap: 6px;
    margin-bottom: 18px;
}
button[data-baseweb="tab"] {
    border: 1px solid var(--line);
    border-radius: 0;
    background: rgba(252, 249, 242, 0.75);
    color: var(--ink);
    padding: 10px 14px;
}
button[data-baseweb="tab"][aria-selected="true"] {
    background: #23211f;
    color: #efe5d6;
    border-color: #23211f;
}
div[data-testid="stExpander"] {
    border: 1px solid var(--line);
    background: rgba(252, 249, 242, 0.78);
}
div[data-testid="stExpander"] details summary {
    background: rgba(31, 38, 37, 0.03);
}

@media (max-width: 900px) {
    .hero {
        padding: 30px 24px 26px;
    }
    .hero-grid,
    .hero-meta {
        grid-template-columns: 1fr;
    }
    .hero-title {
        font-size: 2.35rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar Navigation ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### GROVER")
    st.markdown("<small style='color:#cbbca7;'>Research Interface for End-to-End NL2SQL Reporting</small>", unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio(
        "페이지 선택",
        [
            "Overview",
            "Introduction",
            "Methodology",
            "Experimental",
            "References",
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("""
    <small style='color:#b8ac9a;line-height:1.7'>
    <b style='color:#efe5d6;letter-spacing:0.08em'>GROVER</b><br>
    Generative Reasoning and<br>
    Objective Verification for<br>
    End-to-end Reporting
    </small>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
if page == "Overview":
    st.markdown("""
    <div class='hero'>
        <div class='hero-grid'>
            <div>
                <div class='hero-badge'>Research Framework</div>
                <div class='hero-title'>GROVER</div>
                <div class='hero-subtitle'>
                    Generative Reasoning and Objective Verification for End-to-end Reporting<br>
                    자연어 질문에서 SQL 생성과 결과 해석, 최종 리포트 생성까지 이어지는 전체 흐름을
                    하나의 평가 단위로 다루는 NL2SQL 연구 프레임워크입니다.
                </div>
                <div class='hero-meta'>
                    <div class='hero-meta-item'>
                        <div class='hero-meta-label'>Problem Shift</div>
                        <div class='hero-meta-value'>SQL correctness → analysis reliability</div>
                    </div>
                    <div class='hero-meta-item'>
                        <div class='hero-meta-label'>Evidence Unit</div>
                        <div class='hero-meta-value'>main SQL + support SQL bundle</div>
                    </div>
                    <div class='hero-meta-item'>
                        <div class='hero-meta-label'>Core Output</div>
                        <div class='hero-meta-value'>table-grounded report with verifiable claims</div>
                    </div>
                </div>
            </div>
            <div class='hero-panel'>
                <div class='hero-panel-label'>Research Thesis</div>
                <div class='hero-panel-copy'>
                    핵심은 더 정교한 SQL 하나를 만드는 것이 아니라, 질문을 설명할 수 있는 evidence를
                    충분히 수집하고 그 근거를 바탕으로 검증 가능한 report를 생성하는 데 있습니다.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 핵심 문제 의식
    st.markdown("<div class='section-header'>Core Problem</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card card-red'>
            <h4 style='color:#b91c1c;margin:0 0 10px'>❌ 기존 NL2SQL의 한계</h4>
            <ul style='color:#374151;margin:0;padding-left:18px;line-height:1.8;font-size:0.92rem'>
                <li>"SQL이 문법적으로 맞는가?"만 평가</li>
                <li>실행 결과 테이블을 어떻게 해석할지는 다루지 않음</li>
                <li>단일 SQL 하나로 복잡한 비즈니스 질문에 답하려 함</li>
                <li>최종 사용자에게 의미 있는 인사이트 제공 여부 미평가</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card card-green'>
            <h4 style='color:#15803d;margin:0 0 10px'>✅ GROVER의 접근</h4>
            <ul style='color:#374151;margin:0;padding-left:18px;line-height:1.8;font-size:0.92rem'>
                <li>SQL + 결과 해석 + 리포트 생성을 통합 평가</li>
                <li>Main SQL + Support SQL <b>bundle</b>로 근거 확보</li>
                <li>3단계 평가 프레임워크(SQL / DB / Insight Level)</li>
                <li>숫자 정확성, 커버리지, 의도 정렬까지 측정</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

    # 핵심 파이프라인 개요
    st.markdown("<div class='section-header'>Pipeline Shift</div>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color:#475569;margin-bottom:20px'>
    기존 NL2SQL이 <b>q → z₀</b> (질문 → SQL 하나)에 집중했다면, GROVER는 다음 전체 흐름을 다룹니다.
    </p>
    """, unsafe_allow_html=True)

    cols = st.columns(5)
    steps = [
        ("01", "Question", "q", "사용자 질문의 의도와 분석 단위를 파악"),
        ("02", "SQL Bundle", "Z = {z₀, z₁, …, zₖ}", "main query와 support query를 함께 생성"),
        ("03", "Execution", "R = {r₀, r₁, …, rₖ}", "실행 결과를 검증하고 유효한 evidence 확보"),
        ("04", "Interpretation", "table analysis", "결과 테이블을 claim 단위로 해석"),
        ("05", "Reporting", "y", "최종 답변과 caveat를 구조화해 제시"),
    ]
    for i, (idx, label, sub, desc) in enumerate(steps):
        with cols[i]:
            st.markdown(f"""
            <div class='stage-card'>
                <div class='stage-index'>Stage {idx}</div>
                <div class='stage-title'>{label}</div>
                <div class='stage-code'>{sub}</div>
                <div class='stage-copy'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

    # 4대 Contribution
    st.markdown("<div class='section-header'>Contributions</div>", unsafe_allow_html=True)

    contributions = [
        ("C1", "End-to-End Problem Reformulation",
         "NL2SQL을 단일 SQL 생성 문제가 아니라 SQL 생성 → 실행 → 리포팅으로 이어지는 end-to-end pipeline으로 재정의합니다."),
        ("C2", "Evidence-Bundled NL2SQL Pipeline",
         "단일 SQL 대신 Main SQL + Support SQL bundle을 생성하여, 복잡한 비즈니스 질문에 필요한 근거를 충분히 확보합니다."),
        ("C3", "GROVER Evaluation Framework",
         "SQL-Level · DB-Level · Insight-Level의 3계층 평가 체계를 제안합니다. 특히 Insight-Level은 TG-F1, NumAcc, Coverage, Intent Alignment를 포함하는 새로운 메트릭입니다."),
        ("C4", "Human-Verified Evaluation Protocol",
         "자동 메트릭의 한계를 보완하기 위해 150~200개 규모의 GROVER-Bridge 검증 셋을 구축하고, human judgment와의 상관도를 검증합니다."),
    ]
    for tag, title, desc in contributions:
        st.markdown(f"""
        <div class='contribution'>
            <span class='contribution-tag'>{tag}</span>
            <h4 style='margin:0 0 6px;color:#1e293b;font-size:1rem'>{title}</h4>
            <p style='margin:0;color:#475569;font-size:0.9rem;line-height:1.6'>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    # GROVER Score Vector
    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>Score Vector</div>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color:#475569;margin-bottom:16px'>
    GROVER는 단일 점수 대신 세 축의 <b>score vector</b>를 기본 출력으로 사용합니다.
    단일 점수로 순위를 매기면 "어디서 잘하고 어디서 실패하는지"를 숨기게 됩니다.
    </p>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class='score-card sql'>
            <div class='score-card-label'>Baseline Layer</div>
            <div class='score-card-value'>S_sql</div>
            <div class='score-card-body'>
                SQL-Level Score<br>
                문법 정확도와 semantic execution correctness를 측정합니다.
            </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class='score-card db'>
            <div class='score-card-label'>System Layer</div>
            <div class='score-card-value'>S_db</div>
            <div class='score-card-body'>
                DB-Level Score<br>
                실행 시간, retry 수, DB call efficiency를 함께 봅니다.
            </div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class='score-card insight'>
            <div class='score-card-label'>User-Facing Layer</div>
            <div class='score-card-value'>S_insight</div>
            <div class='score-card-body'>
                Insight-Level Score<br>
                groundedness, numeric correctness, coverage를 포함합니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class='score-vector'>
        G = (S<sub>sql</sub>, S<sub>db</sub>, S<sub>insight</sub>)
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: INTRODUCTION
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Introduction":
    st.markdown("<div class='section-header'>Introduction</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card card-blue'>
        <h4 style='color:#1d4ed8;margin:0 0 10px'>NL2SQL이란?</h4>
        <p style='color:#374151;margin:0;line-height:1.7;font-size:0.93rem'>
        자연어 질문(Natural Language)을 SQL 쿼리로 자동 변환하여, 비전문가도 데이터베이스에 접근할 수 있게 하는 기술입니다.
        예를 들어 "지난 분기 매출이 가장 높은 지역은 어디인가요?"라는 질문을 
        <code>SELECT region, SUM(revenue) FROM sales WHERE quarter='Q3' GROUP BY region ORDER BY 2 DESC LIMIT 1</code>
        같은 SQL로 자동 변환합니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 1.1 연구 배경
    st.markdown("<div class='subsection-header'>1.1 NL2SQL의 최근 흐름</div>", unsafe_allow_html=True)

    benchmarks = [
        ("WikiSQL / Spider", "초기", "#6b7280", "단순 text-to-SQL 대중화. 문법 정확도 중심의 평가."),
        ("BIRD", "2023", "#3b82f6", "실제 DB 환경 강조. Database values, external knowledge, SQL efficiency 평가."),
        ("Spider 2.0", "2025", "#8b5cf6", "632개 실제 enterprise workflow 문제. 1,000개 이상의 컬럼, multi-query, metadata search 요구."),
        ("BIRD-INTERACT", "2025", "#06b6d4", "clarification, knowledge retrieval, 실행 오류 복구까지 포함하는 대화형 benchmark."),
    ]
    for name, year, color, desc in benchmarks:
        st.markdown(f"""
        <div style='display:flex;gap:14px;align-items:flex-start;padding:14px 18px;background:white;
                    border-radius:10px;border:1px solid #e2e8f0;margin-bottom:10px;
                    border-left:4px solid {color}'>
            <div style='min-width:90px'>
                <div style='font-weight:700;color:#1e293b;font-size:0.95rem'>{name}</div>
                <div style='font-size:0.78rem;color:{color};font-weight:600'>{year}</div>
            </div>
            <div style='color:#475569;font-size:0.88rem;line-height:1.6'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class='example-box'>
        <div class='example-label'>💡 핵심 인사이트</div>
        <p style='margin:0;color:#374151;line-height:1.7;font-size:0.92rem'>
        오늘날 NL2SQL은 더 이상 <b>"질문 하나에 SQL 하나를 정확히 생성하는 문제"</b>로만 볼 수 없습니다.
        실제 비즈니스에서 사용자가 원하는 것은 SQL 그 자체가 아니라, <b>질문에 대한 신뢰할 수 있는 답변과 인사이트</b>입니다.
        문제의 중심이 <b>SQL correctness</b>에서 <b>end-to-end analysis reliability</b>로 이동하고 있습니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

    # 1.2 기존 한계
    st.markdown("<div class='subsection-header'>1.2 기존 연구의 세 가지 한계</div>", unsafe_allow_html=True)

    limits = [
        ("⚠️", "한계 1: SQL 평가에 머무름",
         "EX, EM, Test Suite 등 기존 메트릭은 'SQL이 맞는가?'에는 답하지만, '그 결과가 유용하고 신뢰할 수 있는가?'에는 직접 답하지 못합니다.",
         "#fef3c7", "#d97706"),
        ("⚠️", "한계 2: SQL 실행 이후 테이블 해석 부재",
         "BI-Bench, CORGI, MT-RAIG, T2R-bench 등 최근 연구는 테이블 결과를 해석하고 리포트를 생성하는 것이 별도의 핵심 문제임을 보여주지만, NL2SQL 연구와 분리되어 있습니다.",
         "#fce7f3", "#be185d"),
        ("⚠️", "한계 3: Benchmark 자체의 신뢰성 문제",
         "SpotIt은 static DB 기반 실행 평가가 semantic equivalence를 과대평가한다고 지적했고, BIRD와 Spider 2.0-Snow에 상당한 annotation error가 있다고 보고되었습니다(CIDR 2026).",
         "#f0fdf4", "#15803d"),
    ]
    for icon, title, desc, bg, color in limits:
        st.markdown(f"""
        <div style='padding:18px 22px;background:{bg};border-radius:12px;
                    border:1px solid {color}30;margin-bottom:12px'>
            <h4 style='color:{color};margin:0 0 8px;font-size:1rem'>{icon} {title}</h4>
            <p style='color:#374151;margin:0;font-size:0.9rem;line-height:1.6'>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

    # 1.3 연구 질문
    st.markdown("<div class='subsection-header'>1.3 이 프로젝트의 핵심 질문 3가지</div>", unsafe_allow_html=True)

    rqs = [
        ("RQ1", "Algorithm", "SQL 자체만 생성하는 것이 아니라, 최종 리포트 생성에 필요한 evidence를 더 잘 수집하는 SQL generation 전략은 무엇인가?"),
        ("RQ2", "Table Analysis", "실행 결과를 바탕으로 LLM이 신뢰할 수 있는 자연어 인사이트를 생성하도록 만들려면 어떤 intermediate representation과 리포팅 템플릿이 필요한가?"),
        ("RQ3", "Evaluation", "SQL correctness와 DB execution efficiency를 넘어, 최종 리포트의 충실성·유용성·groundedness를 어떻게 정량적으로 평가할 수 있는가?"),
    ]
    for tag, area, question in rqs:
        col_a, col_b = st.columns([1, 6])
        with col_a:
            st.markdown(f"""
            <div style='text-align:center;padding:16px 8px;background:linear-gradient(135deg,#3b82f6,#1d4ed8);
                        border-radius:12px;color:white'>
                <div style='font-weight:700;font-size:1.1rem'>{tag}</div>
                <div style='font-size:0.72rem;opacity:0.85;margin-top:4px'>{area}</div>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown(f"""
            <div style='padding:16px 20px;background:#f8fafc;border-radius:12px;
                        border:1px solid #e2e8f0;height:100%'>
                <p style='margin:0;color:#374151;font-size:0.92rem;line-height:1.65'>{question}</p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: METHODOLOGY
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Methodology":
    st.markdown("<div class='section-header'>Methodology</div>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color:#475569;margin-bottom:24px;font-size:0.95rem;line-height:1.7'>
    Methodology는 크게 4개의 Part로 구성됩니다.
    SQL bundle 생성 전략부터, 결과 해석 방법, 평가 메트릭 설계, 그리고 인간 검증 프로토콜까지 다룹니다.
    </p>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "2.1 문제 정의",
        "2.2 전체 파이프라인",
        "2.3 SQL Bundle",
        "2.4 테이블 분석",
        "2.5 GROVER Metric",
        "2.6 인간 평가",
    ])

    # ── Tab 1: 문제 정의 ─────────────────────────────────────────────────────
    with tabs[0]:
        st.markdown("<div class='subsection-header'>2.1 문제 정의와 기본 표기</div>", unsafe_allow_html=True)

        st.markdown("""
        <p style='color:#475569;line-height:1.7'>
        GROVER가 다루는 문제를 수식으로 명확하게 정의합니다.
        </p>
        """, unsafe_allow_html=True)

        # 표기 정의 표
        st.markdown("""
        <table>
        <tr><th>기호</th><th>의미</th><th>예시</th></tr>
        <tr><td><code>q</code></td><td>자연어 질문</td><td>"지난 분기 매출이 왜 감소했는가?"</td></tr>
        <tr><td><code>D</code></td><td>데이터베이스</td><td>sales_db (실제 DB 파일)</td></tr>
        <tr><td><code>S</code></td><td>스키마 정보</td><td>테이블명, 컬럼명, 타입 등</td></tr>
        <tr><td><code>Z = {z₀, z₁, …, zₖ}</code></td><td>SQL Bundle (z₀=main, z₁…=support)</td><td>메인 쿼리 + 보조 쿼리들</td></tr>
        <tr><td><code>R = {r₀, r₁, …, rₖ}</code></td><td>각 SQL 실행 결과 테이블</td><td>결과 데이터프레임들</td></tr>
        <tr><td><code>y</code></td><td>최종 자연어 리포트</td><td>"북미 지역 매출이 18% 감소했습니다..."</td></tr>
        <tr><td><code>C*</code></td><td>Gold claim set (정답 주장 목록)</td><td>사람이 검증한 정답 statements</td></tr>
        <tr><td><code>Ĉ</code></td><td>예측 claim set (생성된 주장 목록)</td><td>모델이 생성한 리포트에서 추출</td></tr>
        </table>
        """, unsafe_allow_html=True)

        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style='padding:20px;background:#fef2f2;border-radius:14px;border:1px solid #fecdd3'>
                <h4 style='color:#dc2626;margin:0 0 10px'>❌ 기존 NL2SQL 목표</h4>
                <div style='text-align:center;font-size:1.3rem;font-family:monospace;
                            padding:16px;background:white;border-radius:8px;color:#374151;
                            border:1px solid #fecdd3'>
                    q → z₀
                </div>
                <p style='color:#6b7280;font-size:0.85rem;margin:12px 0 0;text-align:center'>
                    질문 하나 → SQL 하나
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style='padding:20px;background:#f0fdf4;border-radius:14px;border:1px solid #bbf7d0'>
                <h4 style='color:#15803d;margin:0 0 10px'>✅ GROVER 목표</h4>
                <div style='text-align:center;font-size:1.1rem;font-family:monospace;
                            padding:16px;background:white;border-radius:8px;color:#374151;
                            border:1px solid #bbf7d0'>
                    q → Z → R → y
                </div>
                <p style='color:#6b7280;font-size:0.85rem;margin:12px 0 0;text-align:center'>
                    질문 → SQL Bundle → 실행 결과 → 최종 리포트
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class='example-box' style='margin-top:20px'>
            <div class='example-label'>📝 구체적인 예시로 이해하기</div>
            <p style='color:#374151;margin:0;line-height:1.7;font-size:0.92rem'>
            <b>질문 q</b>: "지난 분기 북미 매출이 왜 감소했나요?"<br><br>
            <b>기존 방식</b>: <code>SELECT SUM(revenue) FROM sales WHERE region='NA' AND quarter='Q3'</code> 한 줄만 생성. 숫자만 나오고 "왜?"에 대한 답은 없음.<br><br>
            <b>GROVER 방식</b>: <br>
            &nbsp;&nbsp;• z₀ (main): 전체 매출 감소량 집계<br>
            &nbsp;&nbsp;• z₁ (support): 시간별 추세 쿼리<br>
            &nbsp;&nbsp;• z₂ (support): 세그먼트별 분해 (enterprise vs SMB)<br>
            &nbsp;&nbsp;• z₃ (support): 가장 큰 감소 요인 (top negative driver)<br>
            → 이 결과들을 종합해 "북미 매출 18% 감소, 그중 enterprise 고객이 절반 이상 차지"라는 신뢰할 수 있는 리포트 y 생성
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ── Tab 2: 전체 파이프라인 ───────────────────────────────────────────────
    with tabs[1]:
        st.markdown("<div class='subsection-header'>2.2 GROVER 6단계 파이프라인</div>", unsafe_allow_html=True)

        pipeline_steps = [
            ("1", "Question Typing", "질문 유형 분류",
             "질문을 <b>Descriptive</b>(사실 요약) 또는 <b>Diagnostic</b>(원인 분석)으로 분류합니다. "
             "첫 버전에서는 predictive와 prescriptive는 제외하고, 이 두 유형에 집중합니다.",
             "Q: '지난 분기 매출 총액은?' → Descriptive<br>Q: '왜 매출이 감소했나?' → Diagnostic"),
            ("2", "Schema / Value Retrieval", "관련 스키마·값 검색",
             "질문과 관련된 <b>테이블, 컬럼, 실제 값</b>을 검색하여 대규모 스키마에서 필요한 부분만 추립니다(pruning). "
             "최신 text-to-SQL 연구에서 가장 중요한 병목 중 하나입니다.",
             "1,000개 컬럼이 있는 DB에서 질문 관련 컬럼 20개만 선택 → LLM 입력 토큰 절약"),
            ("3", "SQL Bundle Generation", "SQL 묶음 생성",
             "Main SQL 하나만 아니라 <b>Support SQL을 함께 생성</b>합니다. "
             "Diagnostic 질문이면 trend query, breakdown query, driver query를 자동 생성합니다.",
             "Diagnostic 질문의 경우: trend(추세) + segment(분해) + driver(요인) 쿼리 자동 생성"),
            ("4", "Execution and Verification", "실행 및 검증",
             "생성된 SQL bundle을 실제 DB에서 실행하고, <b>syntax error, empty result, trivial result</b>를 점검합니다. "
             "문제가 있으면 retry 또는 candidate 교체를 수행합니다.",
             "빈 결과 반환 → 다른 candidate SQL로 교체 후 재실행"),
            ("5", "Structured Report Generation", "구조화된 리포트 생성",
             "실행 결과를 바탕으로 <b>Direct Answer, Supporting Claims, Caveat</b>를 포함한 "
             "구조화된 리포트를 생성합니다. 자유로운 장문 생성 대신 atomic claim 중심으로 구조화합니다.",
             "직접 답변 + 근거 claim 3개 + 한계 명시 형식으로 출력"),
            ("6", "Report-aware Selection / Verification", "리포트 품질 기반 선택",
             "여러 SQL bundle candidate 중 <b>최종 리포트 품질을 가장 높이는 bundle을 선택</b>합니다. "
             "기존 selector가 SQL 자체를 선택했다면, GROVER는 report quality를 기준으로 선택합니다.",
             "SQL 정확도는 비슷하지만 더 완전한 인사이트를 제공하는 bundle 선택"),
        ]

        for num, title, subtitle, desc, ex in pipeline_steps:
            with st.expander(f"Step {num}: {title} — {subtitle}", expanded=(num == "1")):
                col_a, col_b = st.columns([3, 2])
                with col_a:
                    st.markdown(f"""
                    <p style='color:#374151;font-size:0.93rem;line-height:1.7;margin:0 0 12px'>{desc}</p>
                    """, unsafe_allow_html=True)
                with col_b:
                    st.markdown(f"""
                    <div class='example-box'>
                        <div class='example-label'>예시</div>
                        <p style='font-size:0.85rem;color:#374151;margin:0;line-height:1.6'>{ex}</p>
                    </div>
                    """, unsafe_allow_html=True)

    # ── Tab 3: SQL Bundle ────────────────────────────────────────────────────
    with tabs[2]:
        st.markdown("<div class='subsection-header'>2.3 Part I: Evidence-Bundled NL2SQL Algorithm</div>", unsafe_allow_html=True)

        # 왜 bundle인가
        st.markdown("""
        <div class='card card-orange'>
            <h4 style='color:#b45309;margin:0 0 10px'>❓ 왜 Single SQL이 아니라 SQL Bundle인가?</h4>
            <p style='color:#374151;margin:0;line-height:1.7;font-size:0.92rem'>
            실제 사용자가 "지난 분기 매출이 왜 감소했는가?"라고 묻는다면,
            단일 aggregate query 하나만으로는 충분하지 않습니다. 이 질문에 답하려면 보통 다음 정보가 모두 필요합니다.
            </p>
        </div>
        """, unsafe_allow_html=True)

        info_needed = [
            ("📈", "전체 추세(Trend)", "시간 흐름에 따른 매출 변화"),
            ("🔍", "세그먼트별 분해(Breakdown)", "지역·제품·고객군별 기여도"),
            ("🎯", "주요 요인(Driver)", "가장 큰 감소를 일으킨 원인"),
        ]
        cols = st.columns(3)
        for i, (icon, title, desc) in enumerate(info_needed):
            with cols[i]:
                st.markdown(f"""
                <div style='text-align:center;padding:20px 12px;background:white;border-radius:14px;
                            border:1px solid #e2e8f0;height:140px'>
                    <div style='font-size:1.8rem'>{icon}</div>
                    <div style='font-weight:600;color:#1e293b;font-size:0.9rem;margin:8px 0 6px'>{title}</div>
                    <div style='color:#64748b;font-size:0.82rem'>{desc}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

        # Bundle 구조
        st.markdown("<div class='subsection-header'>SQL Bundle 생성 전략 — 질문 유형별 차이</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style='padding:22px;background:#eff6ff;border-radius:16px;border:1px solid #bfdbfe'>
                <h4 style='color:#1d4ed8;margin:0 0 16px'>📋 Descriptive Query</h4>
                <div style='background:white;border-radius:10px;padding:14px 16px;margin-bottom:10px;
                            border-left:3px solid #3b82f6'>
                    <div style='font-size:0.75rem;font-weight:700;color:#3b82f6;margin-bottom:4px'>MAIN SQL</div>
                    <div style='font-size:0.88rem;color:#374151'>direct answer query<br>
                    <code style='font-size:0.8rem'>SELECT SUM(revenue) ...</code></div>
                </div>
                <div style='background:white;border-radius:10px;padding:14px 16px;
                            border-left:3px solid #93c5fd'>
                    <div style='font-size:0.75rem;font-weight:700;color:#60a5fa;margin-bottom:4px'>SUPPORT SQL (optional)</div>
                    <div style='font-size:0.88rem;color:#374151'>granularity check 또는 top-k evidence query</div>
                </div>
                <div class='example-box' style='margin-top:14px'>
                    <div class='example-label'>예시 질문</div>
                    <p style='font-size:0.85rem;color:#374151;margin:0'>"지난 분기 전체 매출은 얼마인가?"</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style='padding:22px;background:#faf5ff;border-radius:16px;border:1px solid #ddd6fe'>
                <h4 style='color:#7e22ce;margin:0 0 16px'>🔬 Diagnostic Query</h4>
                <div style='background:white;border-radius:10px;padding:14px 16px;margin-bottom:8px;
                            border-left:3px solid #a855f7'>
                    <div style='font-size:0.75rem;font-weight:700;color:#a855f7;margin-bottom:4px'>MAIN SQL</div>
                    <div style='font-size:0.88rem;color:#374151'>target KPI difference query</div>
                </div>
                <div style='background:white;border-radius:10px;padding:14px 16px;margin-bottom:8px;
                            border-left:3px solid #c084fc'>
                    <div style='font-size:0.75rem;font-weight:700;color:#c084fc;margin-bottom:4px'>SUPPORT SQL 1</div>
                    <div style='font-size:0.88rem;color:#374151'>time trend query (시간 추세)</div>
                </div>
                <div style='background:white;border-radius:10px;padding:14px 16px;margin-bottom:8px;
                            border-left:3px solid #e9d5ff'>
                    <div style='font-size:0.75rem;font-weight:700;color:#d8b4fe;margin-bottom:4px'>SUPPORT SQL 2</div>
                    <div style='font-size:0.88rem;color:#374151'>segment breakdown query (세그먼트 분해)</div>
                </div>
                <div style='background:white;border-radius:10px;padding:14px 16px;
                            border-left:3px solid #f3e8ff'>
                    <div style='font-size:0.75rem;font-weight:700;color:#e9d5ff;margin-bottom:4px'>SUPPORT SQL 3</div>
                    <div style='font-size:0.88rem;color:#374151'>top positive/negative driver query (요인 분석)</div>
                </div>
                <div class='example-box' style='margin-top:14px'>
                    <div class='example-label'>예시 질문</div>
                    <p style='font-size:0.85rem;color:#374151;margin:0'>"지난 분기 매출이 왜 감소했는가?"</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

        # Candidate selection
        st.markdown("<div class='subsection-header'>Candidate 생성 및 Report-aware Selection</div>", unsafe_allow_html=True)
        st.markdown("""
        <p style='color:#475569;font-size:0.92rem;line-height:1.7;margin-bottom:16px'>
        하나의 질문에 대해 여러 SQL bundle candidate를 생성하고, 최종적으로 <b>리포트 품질을 기준</b>으로 가장 좋은 것을 선택합니다.
        이것이 기존 CHASE-SQL의 candidate selection과의 핵심 차이점입니다.
        </p>
        """, unsafe_allow_html=True)

        st.markdown("""
        <table>
        <tr><th>다양성 확보 방법</th><th>설명</th></tr>
        <tr><td>Prompt Variation</td><td>같은 질문을 다른 프롬프트로 여러 번 물어봄</td></tr>
        <tr><td>Decomposition Variation</td><td>질문을 다른 방식으로 분해하여 각각 SQL 생성</td></tr>
        <tr><td>Retrieval Variation</td><td>다른 스키마/값 검색 전략으로 다양한 컨텍스트 제공</td></tr>
        </table>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style='padding:18px;background:#fef2f2;border-radius:12px;border:1px solid #fecdd3'>
                <h4 style='color:#dc2626;margin:0 0 8px;font-size:0.95rem'>❌ 기존 SQL-only Selector</h4>
                <p style='color:#374151;font-size:0.87rem;margin:0;line-height:1.6'>
                후보 중 SQL 정확도 점수가 가장 높은 것을 선택.<br>
                → SQL은 맞지만 리포트에 필요한 정보가 부족할 수 있음.
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style='padding:18px;background:#f0fdf4;border-radius:12px;border:1px solid #bbf7d0'>
                <h4 style='color:#15803d;margin:0 0 8px;font-size:0.95rem'>✅ GROVER Report-aware Selector</h4>
                <p style='color:#374151;font-size:0.87rem;margin:0;line-height:1.6'>
                후보 중 생성 가능한 리포트의 품질이 가장 높은 것을 선택.<br>
                → SQL 정확도 + 인사이트 완성도를 모두 고려.
                </p>
            </div>
            """, unsafe_allow_html=True)

    # ── Tab 4: 테이블 분석 ───────────────────────────────────────────────────
    with tabs[3]:
        st.markdown("<div class='subsection-header'>2.4 Part II: NL2SQL 이후 LLM의 Table Data Analysis</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='card card-blue'>
            <h4 style='color:#1d4ed8;margin:0 0 10px'>왜 별도 모듈인가?</h4>
            <p style='color:#374151;margin:0;line-height:1.7;font-size:0.92rem'>
            기존 NL2SQL 시스템은 SQL 실행 후 결과 테이블을 그냥 사용자에게 보여줬습니다.
            하지만 실제 사용자 관점에서는 <b>테이블 그 자체보다 해석된 의미</b>가 더 중요합니다.
            BI-Bench, MT-RAIG, T2R-bench는 SQL 이후의 테이블 해석과 리포트 생성이
            <b>별도의 핵심 연구 문제</b>임을 보여줍니다.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

        # Structured Report Format
        st.markdown("<div class='subsection-header'>구조화된 리포트 포맷</div>", unsafe_allow_html=True)
        st.markdown("""
        <p style='color:#475569;font-size:0.92rem;line-height:1.7;margin-bottom:16px'>
        리포트 평가를 가능하게 하려면 출력 포맷이 어느 정도 구조화되어야 합니다.
        자유로운 장문 생성 대신 아래 4개의 필드로 구성된 리포트를 생성합니다.
        </p>
        """, unsafe_allow_html=True)

        report_fields = [
            ("Direct Answer", "질문에 대한 1~2문장 요약 답변", "#3b82f6",
             "북미 지역의 enterprise segment 부진이 지난 분기 매출 감소의 주된 원인입니다."),
            ("Supporting Claims", "최대 3개의 atomic claim (검증 가능한 단위 주장)", "#8b5cf6",
             "Claim 1: 북미 매출 전분기 대비 18% 감소\nClaim 2: Enterprise 고객군 감소가 전체의 절반 이상\nClaim 3: 전 지역 중 북미 감소폭 최대"),
            ("Evidence Mapping", "각 claim이 어떤 result table에 근거하는지 표시", "#06b6d4",
             "Claim 1 → r₀ (매출 집계 테이블)\nClaim 2 → r₂ (세그먼트 분해 테이블)\nClaim 3 → r₁ (지역별 추세 테이블)"),
            ("Caveat / Limitation", "데이터 또는 해석의 한계가 있으면 명시", "#f59e0b",
             "프로모션 종료 효과와 가격 정책 변화는 현재 테이블만으로 직접 검증되지 않습니다."),
        ]

        for field, desc, color, ex in report_fields:
            with st.expander(f"📌 {field}", expanded=(field == "Direct Answer")):
                col_a, col_b = st.columns([2, 3])
                with col_a:
                    st.markdown(f"""
                    <div style='padding:16px;background:{color}10;border-radius:10px;border:1px solid {color}30'>
                        <p style='color:#374151;margin:0;font-size:0.92rem;line-height:1.65'>{desc}</p>
                    </div>
                    """, unsafe_allow_html=True)
                with col_b:
                    st.markdown(f"""
                    <div class='example-box'>
                        <div class='example-label'>예시</div>
                        <pre style='font-size:0.83rem;color:#374151;margin:0;white-space:pre-wrap;
                                    font-family:Inter,sans-serif;line-height:1.6'>{ex}</pre>
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

        # Claim 유형
        st.markdown("<div class='subsection-header'>Atomic Claim 4가지 유형</div>", unsafe_allow_html=True)
        st.markdown("""
        <p style='color:#475569;font-size:0.92rem;line-height:1.7;margin-bottom:16px'>
        리포트의 각 문장을 <b>claim 단위</b>로 분해합니다. 유형마다 검증 방법이 달라집니다.
        </p>
        """, unsafe_allow_html=True)

        claims = [
            ("numeric claim", "badge-numeric", "값, 비율, 증감률", "결과 테이블로 deterministic check 가능",
             '"북미 매출이 18% 감소했습니다."'),
            ("comparison claim", "badge-comparison", "A > B, 증가/감소 비교", "결과 테이블로 deterministic check 가능",
             '"Enterprise 감소폭이 SMB보다 큽니다."'),
            ("ranking claim", "badge-ranking", "top-1, highest, lowest", "결과 테이블로 deterministic check 가능",
             '"전 지역 중 북미 감소폭이 가장 큽니다."'),
            ("diagnostic claim", "badge-diagnostic", "원인, 패턴, 설명", "LLM-as-a-judge + human audit 필요",
             '"프로모션 종료가 enterprise 이탈을 가속화했을 가능성이 있습니다."'),
        ]

        for name, badge, desc, verify, ex in claims:
            st.markdown(f"""
            <div style='padding:16px 20px;background:white;border-radius:12px;border:1px solid #e2e8f0;
                        margin-bottom:10px;display:flex;gap:16px;align-items:flex-start'>
                <div style='min-width:140px'>
                    <span class='badge {badge}'>{name}</span>
                    <div style='font-size:0.8rem;color:#64748b;margin-top:6px'>{desc}</div>
                </div>
                <div style='flex:1;border-left:1px solid #e2e8f0;padding-left:16px'>
                    <div style='font-size:0.82rem;color:#475569;margin-bottom:6px'>
                        <b>검증:</b> {verify}
                    </div>
                    <div style='font-size:0.85rem;color:#1e293b;background:#f8fafc;
                                padding:6px 12px;border-radius:6px;font-style:italic'>"{ex[1:-1]}"</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card card-green' style='margin-top:8px'>
            <h4 style='color:#15803d;margin:0 0 8px'>💡 Hybrid 검증 구조의 장점</h4>
            <p style='color:#374151;margin:0;font-size:0.9rem;line-height:1.65'>
            numeric / comparison / ranking claim은 결과 테이블로 <b>자동 검증</b>이 가능하고,
            diagnostic claim만 LLM-as-a-judge + human audit를 사용합니다.
            이 hybrid 구조가 pure judge metric보다 <b>더 안정적이고 신뢰할 수 있습니다.</b>
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ── Tab 5: GROVER Metric ─────────────────────────────────────────────────
    with tabs[4]:
        st.markdown("<div class='subsection-header'>2.5 Part III: GROVER Metric 설계</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='card card-purple'>
            <h4 style='color:#7e22ce;margin:0 0 10px'>설계 5원칙</h4>
            <ol style='color:#374151;margin:0;padding-left:20px;line-height:1.9;font-size:0.92rem'>
                <li>SQL correctness만 보지 않는다</li>
                <li>judge-only metric에 의존하지 않는다</li>
                <li><b>table-grounded verification</b>을 우선한다</li>
                <li>질문 유형에 따라 요구되는 인사이트를 다르게 평가한다</li>
                <li>human judgment와의 정렬을 반드시 검증한다</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

        # Level 1
        st.markdown("""
        <div class='metric-level level-sql'>
            <h3 style='color:#1d4ed8'>🔷 Level 1: SQL-Level</h3>
            <p>기존 text-to-SQL 평가 메트릭을 그대로 활용합니다. "SQL이 맞는가?"를 평가하는 baseline layer입니다.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <table>
        <tr><th>메트릭</th><th>설명</th><th>역할</th></tr>
        <tr><td><b>EX</b> (Execution Accuracy)</td><td>예측 SQL의 실행 결과가 정답과 일치하는가</td><td>핵심 메트릭</td></tr>
        <tr><td><b>TS</b> (Test Suite Accuracy)</td><td>다양한 test condition에서 semantic equivalence를 만족하는가</td><td>핵심 메트릭</td></tr>
        <tr><td><b>SF1</b> (Soft F1)</td><td>execution result 기반의 부드러운 유사도 측정</td><td>핵심 메트릭</td></tr>
        <tr><td><b>EM</b> (Exact Match)</td><td>SQL 문자열이 완전히 일치하는가</td><td>디버깅용 보조 메트릭</td></tr>
        </table>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='formula-box'>
        S<sub>sql</sub> = α₁ · EX + α₂ · TS + α₃ · SF1
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <p style='color:#64748b;font-size:0.85rem;margin:4px 0 0'>
        EM은 semantic equivalence를 제대로 반영하지 못하기 때문에 main score에서 제외하고 보조 지표로 사용합니다.
        </p>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

        # Level 2
        st.markdown("""
        <div class='metric-level level-db'>
            <h3 style='color:#15803d'>🟢 Level 2: DB-Level</h3>
            <p>"실행되느냐"를 넘어 <b>"얼마나 효율적으로 실행되느냐"</b>를 평가합니다. agentic pipeline의 효율을 보여줍니다.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <table>
        <tr><th>측정 항목</th><th>설명</th></tr>
        <tr><td>Normalized execution time</td><td>실행 시간을 정규화한 값</td></tr>
        <tr><td>R-VES (valid efficiency score)</td><td>BIRD에서 제안한 효율성 메트릭 계열</td></tr>
        <tr><td>Retry count</td><td>SQL 실패 후 재시도 횟수 (적을수록 좋음)</td></tr>
        <tr><td>DB call count</td><td>총 DB 호출 횟수 (적을수록 효율적)</td></tr>
        <tr><td>Memory usage (optional)</td><td>환경 노이즈가 크므로 appendix로 처리</td></tr>
        </table>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='formula-box'>
        S<sub>db</sub> = β₁ · R̃VES + β₂ · (1 − R̃etry) + β₃ · (1 − C̃alls)
        <br><br>
        <span style='color:#94a3b8;font-size:0.82rem'>※ R̃VES, R̃etry, C̃alls 모두 [0,1] 범위로 정규화한 값</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

        # Level 3
        st.markdown("""
        <div class='metric-level level-insight'>
            <h3 style='color:#7e22ce'>🔮 Level 3: Insight-Level (핵심 Contribution)</h3>
            <p>최종 리포트가 <b>질문 의도에 맞고, 결과 테이블에 근거하며, 숫자적으로 정확하고, 핵심 요소를 빠짐없이 포함하는지</b>를 평가합니다.</p>
        </div>
        """, unsafe_allow_html=True)

        insight_metrics = [
            ("(1) Table-Grounded F1 (TG-F1)", "#a855f7",
             "생성된 리포트의 claim이 실제 실행 결과 테이블로 뒷받침되는지 평가합니다. "
             "Ragas Faithfulness의 철학을 계승하지만, retrieved text가 아닌 <b>executed result tables</b>를 근거로 사용합니다.",
             """TG-P = Σ(c∈Ĉ) 𝟙[c ⊢ R] / |Ĉ|         ← 생성 claim 중 테이블로 지지되는 비율
TG-R = Σ(c*∈C*) 𝟙[c* covered by y] / |C*|   ← gold claim 중 리포트에 포함된 비율
TG-F1 = 2 · TG-P · TG-R / (TG-P + TG-R)""",
             '"북미 매출 18% 감소"라는 claim → r₀ 테이블에서 직접 계산 가능 → ✅ supported',
             0.35),
            ("(2) Numeric Consistency (NumAcc)", "#3b82f6",
             "리포트에 포함된 수치 claim의 정확성을 측정합니다. "
             "숫자 하나만 틀려도 전체 리포트의 신뢰성이 크게 떨어지기 때문에 별도로 측정합니다.",
             "NumAcc = #correct numerical claims / #all numerical claims",
             '"18%"라고 했는데 실제는 "17.8%" → 허용 오차 내면 correct로 처리',
             0.30),
            ("(3) Question Coverage (Cov)", "#06b6d4",
             "질문 유형마다 반드시 포함되어야 하는 analytical slot이 모두 채워졌는지 평가합니다. "
             "'말은 자연스럽지만 중요한 요소를 빠뜨린 답변'을 페널티할 수 있습니다.",
             """Cov = #required slots addressed / #required slots

Descriptive: [직접 답변, 핵심 값, 관련 세분화]
Diagnostic:  [직접 답변, 추세, 세그먼트, 요인, 한계]""",
             'Diagnostic 질문에서 driver(요인) 설명이 없으면 Cov 점수 감소',
             0.20),
            ("(4) Intent Alignment (IA)", "#f59e0b",
             "질문 의도에 맞는 답변이 생성되었는지 평가합니다. "
             "Descriptive 질문인데 불필요한 recommendation을 길게 생성하거나, "
             "Diagnostic 질문인데 단순 집계값만 나열하면 낮은 점수를 받습니다.",
             "IA ∈ [0,1]  ←  question type별 rubric으로 judge model이 점수 부여",
             '"왜 감소했나?" (Diagnostic)인데 "매출 총액은 100억원" (Descriptive 답변)만 하면 낮은 IA 점수',
             0.15),
        ]

        for metric_name, color, desc, formula, ex, weight in insight_metrics:
            with st.expander(f"{'🔮 ' if 'TG' in metric_name else '📊 '}{metric_name} (가중치: {int(weight*100)}%)", expanded=(metric_name.startswith("(1)"))):
                col_a, col_b = st.columns([3, 2])
                with col_a:
                    st.markdown(f"<p style='color:#374151;font-size:0.92rem;line-height:1.7'>{desc}</p>",
                                unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class='formula-box' style='font-size:0.82rem'>{formula}</div>
                    """, unsafe_allow_html=True)
                with col_b:
                    st.markdown(f"""
                    <div class='example-box'>
                        <div class='example-label'>예시</div>
                        <p style='font-size:0.83rem;color:#374151;margin:0;line-height:1.6'>{ex}</p>
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

        # 종합 점수
        st.markdown("<div class='subsection-header'>Insight-Level 종합 Score</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='formula-box'>
        S<sub>insight</sub> = γ₁ · TG-F1 + γ₂ · NumAcc + γ₃ · Cov + γ₄ · IA
        <br><br>
        γ₁ + γ₂ + γ₃ + γ₄ = 1
        </div>
        """, unsafe_allow_html=True)

        weights = [("TG-F1 (근거 충실성)", 35, "#a855f7"),
                   ("NumAcc (숫자 정확성)", 30, "#3b82f6"),
                   ("Coverage (커버리지)", 20, "#06b6d4"),
                   ("Intent Align (의도 정렬)", 15, "#f59e0b")]

        st.markdown("<p style='color:#475569;font-size:0.88rem;margin:12px 0 8px'>초기 가중치 설정 (groundedness와 numeric correctness를 가장 중요하게)</p>", unsafe_allow_html=True)
        for label, pct, color in weights:
            st.markdown(f"""
            <div class='weight-row'>
                <span class='weight-label'>{label}</span>
                <div class='weight-bar-bg'>
                    <div class='weight-bar-fill' style='width:{pct}%;background:{color}'></div>
                </div>
                <span class='weight-pct' style='color:{color}'>{pct}%</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

        # 최종 G
        st.markdown("""
        <div class='score-vector-panel'>
            <div class='score-vector-panel-label'>GROVER Final Score Vector</div>
            <div class='score-vector-panel-main'>
                G = (S<sub>sql</sub>, S<sub>db</sub>, S<sub>insight</sub>)
            </div>
            <div class='score-vector-panel-sub'>
                단일 leaderboard 점수가 필요하면:
            </div>
            <div class='score-vector-panel-main' style='font-size:1.08rem;margin-top:8px;margin-bottom:0'>
                Ḡ = λ₁ · S<sub>sql</sub> + λ₂ · S<sub>db</sub> + λ₃ · S<sub>insight</sub>
            </div>
            <div class='score-vector-panel-note'>
                ※ 연구 논문에서는 vector form을 유지하는 것이 권장됩니다.<br>
                그래야 시스템이 어디서 잘하고 어디서 실패하는지를 분명하게 보여줄 수 있습니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Tab 6: 인간 평가 ─────────────────────────────────────────────────────
    with tabs[5]:
        st.markdown("<div class='subsection-header'>2.6 Part IV: Human-verified Evaluation Protocol</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='card card-orange'>
            <h4 style='color:#b45309;margin:0 0 10px'>⚠️ 왜 인간 평가가 필요한가?</h4>
            <p style='color:#374151;margin:0;line-height:1.7;font-size:0.92rem'>
            최근 benchmark noise 문제가 크게 제기되고 있습니다 (SpotIt, CIDR 2026).
            자동 메트릭만으로 논문을 구성하는 것은 위험합니다.
            GROVER-Bridge라는 소규모 human-verified subset을 구축하여, 자동 메트릭이 실제로 인간의 판단과 
            얼마나 잘 일치하는지 검증합니다.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style='padding:20px;background:white;border-radius:14px;border:1px solid #e2e8f0'>
                <h4 style='color:#1e293b;margin:0 0 14px'>📋 GROVER-Bridge Annotation 항목</h4>
                <ul style='color:#374151;margin:0;padding-left:18px;line-height:2;font-size:0.9rem'>
                    <li>질문 유형 (descriptive / diagnostic)</li>
                    <li>허용 가능한 SQL family 목록</li>
                    <li>gold support evidence</li>
                    <li><b>gold atomic claim set</b></li>
                    <li>required analytical slots</li>
                    <li>ambiguity / abstention label</li>
                </ul>
                <div style='margin-top:16px;padding:12px;background:#f8fafc;border-radius:8px;
                            text-align:center;border:1px dashed #cbd5e1'>
                    <div style='font-size:1.4rem;font-weight:700;color:#3b82f6'>150~200</div>
                    <div style='font-size:0.85rem;color:#64748b'>권장 예시 수 (BIRD/CORGI에서 샘플링)</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style='padding:20px;background:white;border-radius:14px;border:1px solid #e2e8f0'>
                <h4 style='color:#1e293b;margin:0 0 14px'>📏 인간 평가 3개 축</h4>
                <div style='padding:12px 14px;background:#eff6ff;border-radius:8px;margin-bottom:8px'>
                    <b style='color:#1d4ed8'>Factual Correctness</b>
                    <div style='font-size:0.85rem;color:#64748b;margin-top:4px'>사실적으로 맞는가? (1~5 Likert)</div>
                </div>
                <div style='padding:12px 14px;background:#f0fdf4;border-radius:8px;margin-bottom:8px'>
                    <b style='color:#15803d'>Usefulness</b>
                    <div style='font-size:0.85rem;color:#64748b;margin-top:4px'>실제로 유용한가? (1~5 Likert)</div>
                </div>
                <div style='padding:12px 14px;background:#faf5ff;border-radius:8px'>
                    <b style='color:#7e22ce'>Completeness</b>
                    <div style='font-size:0.85rem;color:#64748b;margin-top:4px'>필요한 내용이 다 있는가? (1~5 Likert)</div>
                </div>
                <div style='margin-top:14px;font-size:0.85rem;color:#475569'>
                    → 최종적으로 GROVER-Insight와의 <b>Spearman correlation</b> 측정
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card card-green' style='margin-top:16px'>
            <h4 style='color:#15803d;margin:0 0 8px'>이 subset으로 검증할 3가지</h4>
            <ol style='color:#374151;margin:0;padding-left:20px;line-height:1.9;font-size:0.9rem'>
                <li>GROVER-Insight와 human judgment의 correlation</li>
                <li>vanilla Ragas metric과의 비교 (왜 table-specific 재설계가 필요한가)</li>
                <li>SQL-level metric과 end-to-end usefulness 간의 괴리 확인</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: EXPERIMENTAL
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Experimental":
    st.markdown("<div class='section-header'>Experimental Design</div>", unsafe_allow_html=True)

    # Research Questions
    st.markdown("<div class='subsection-header'>3.1 연구 질문 & 가설</div>", unsafe_allow_html=True)

    rqs = [
        ("RQ1", "H1", "#3b82f6",
         "Evidence-bundled NL2SQL pipeline은 single-SQL baseline보다 더 높은 Insight-Level quality를 달성하는가?",
         "support SQL bundle과 report-aware selection을 사용하면 SQL accuracy가 비슷하더라도 Insight-Level score는 유의미하게 향상될 것이다."),
        ("RQ2", "H2", "#a855f7",
         "GROVER-Insight metric은 generic LLM judge나 vanilla Ragas보다 human judgment와 더 잘 정렬되는가?",
         "claim decomposition과 numeric verification을 포함한 GROVER-Insight가 더 높은 human correlation을 보일 것이다."),
        ("RQ3", "H3", "#f59e0b",
         "SQL-Level ranking과 end-to-end report ranking은 일치하는가?",
         "동일한 SQL-Level score를 가진 system들 사이에서도 Insight-Level score는 크게 다를 수 있다."),
    ]

    for rq, hyp, color, question, hypothesis in rqs:
        with st.expander(f"{rq}: {question[:60]}...", expanded=True):
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(f"""
                <div style='padding:14px 18px;background:{color}10;border-radius:10px;border-left:4px solid {color}'>
                    <div style='font-size:0.75rem;font-weight:700;color:{color};margin-bottom:6px'>{rq} (Research Question)</div>
                    <p style='color:#374151;margin:0;font-size:0.9rem;line-height:1.65'>{question}</p>
                </div>
                """, unsafe_allow_html=True)
            with col_b:
                st.markdown(f"""
                <div style='padding:14px 18px;background:#f0fdf4;border-radius:10px;border-left:4px solid #22c55e'>
                    <div style='font-size:0.75rem;font-weight:700;color:#15803d;margin-bottom:6px'>{hyp} (Hypothesis)</div>
                    <p style='color:#374151;margin:0;font-size:0.9rem;line-height:1.65'>{hypothesis}</p>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

    # Dataset
    st.markdown("<div class='subsection-header'>3.2 데이터셋 구성 전략</div>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color:#475569;font-size:0.92rem;line-height:1.7;margin-bottom:16px'>
    단일 benchmark로 모든 것을 해결하기보다, <b>역할이 다른 benchmark를 조합</b>합니다.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <table>
    <tr><th>Dataset</th><th>역할</th><th>추천 사용 방식</th></tr>
    <tr><td><b>BIRD Mini-Dev V2</b></td><td>빠른 개발 및 반복 실험</td><td>메인 development benchmark (780 instances)</td></tr>
    <tr><td><b>BIRD Dev / selected split</b></td><td>SQL correctness + efficiency 확인</td><td>최종 SQL/DB-level validation</td></tr>
    <tr><td><b>CORGI</b></td><td>business-domain high-order query 평가</td><td>Insight-Level 핵심 benchmark</td></tr>
    <tr><td><b>BI-Bench</b></td><td>query taxonomy와 BI framing 참고</td><td>보조 benchmark 또는 taxonomy source</td></tr>
    <tr><td><b>Spider 2.0-Lite</b></td><td>stress test</td><td>appendix 수준의 robustness 실험</td></tr>
    <tr><td><b>GROVER-Bridge</b></td><td>human alignment 평가</td><td>소규모 수작업 검증셋 (150~200개)</td></tr>
    </table>
    """, unsafe_allow_html=True)

    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

    # Models
    st.markdown("<div class='subsection-header'>3.3 모델 선택 (Google Colab 환경)</div>", unsafe_allow_html=True)

    models = [
        ("SQL Generator", "🔷", [
            ("Qwen2.5-Coder-7B-Instruct", "code generation 특화, SQL 생성에 최우선 추천"),
            ("Qwen2.5-7B-Instruct", "structured output과 table understanding에도 적합"),
        ], "#3b82f6"),
        ("Reporter / Judge", "🔮", [
            ("Gemma 3 4B IT", "long context와 reasoning에 적합, judge 모델로도 활용"),
            ("Phi-4-mini-instruct", "128K context 지원, 여러 테이블을 함께 처리할 때 유리"),
        ], "#a855f7"),
        ("Multilingual Baseline", "🌐", [
            ("Llama 3.1 8B Instruct", "multilingual 공식 지원, 한국어 질문 baseline으로 유용"),
        ], "#06b6d4"),
    ]

    cols = st.columns(3)
    for i, (role, icon, model_list, color) in enumerate(models):
        with cols[i]:
            items = "".join([f"<div style='padding:10px 12px;background:white;border-radius:8px;margin-bottom:8px;border:1px solid {color}20'>"
                             f"<div style='font-weight:600;color:#1e293b;font-size:0.85rem'>{name}</div>"
                             f"<div style='color:#64748b;font-size:0.78rem;margin-top:4px'>{desc}</div>"
                             f"</div>" for name, desc in model_list])
            st.markdown(f"""
            <div style='padding:18px;background:{color}08;border-radius:14px;border:1px solid {color}25;height:100%'>
                <div style='display:flex;align-items:center;gap:8px;margin-bottom:14px'>
                    <span style='font-size:1.3rem'>{icon}</span>
                    <span style='font-weight:700;color:#1e293b;font-size:0.95rem'>{role}</span>
                </div>
                {items}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card card-green' style='margin-top:16px'>
        <h4 style='color:#15803d;margin:0 0 10px'>💡 추천 조합 (Colab 기준)</h4>
        <div style='display:flex;gap:20px;flex-wrap:wrap'>
            <div><b>단일 모델:</b> Qwen2.5-7B-Instruct</div>
            <div><b>역할 분리:</b> Qwen2.5-Coder-7B + Phi-4-mini-instruct</div>
        </div>
        <p style='color:#374151;margin:8px 0 0;font-size:0.85rem'>
        모두 4-bit quantization으로 Google Colab에서 실행 가능합니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

    # Baselines
    st.markdown("<div class='subsection-header'>3.5 Baseline 설계</div>", unsafe_allow_html=True)

    baselines = [
        ("Baseline A", "One-shot NL2SQL + Direct Answer",
         "질문과 schema를 넣고 단일 SQL을 생성한 후, 그 결과를 그대로 자연어로 설명합니다.",
         "가장 단순한 baseline"),
        ("Baseline B", "Retrieval-pruned Single SQL",
         "schema/value retrieval로 관련 요소만 추린 뒤 SQL을 생성합니다.",
         "retrieval의 효과 측정"),
        ("Baseline C", "Multi-candidate SQL + SQL-only Selector",
         "여러 SQL candidate를 생성하지만, 최종 선택은 SQL correctness 기준으로만 합니다.",
         "bundle의 효과 측정"),
        ("Proposed", "GROVER-Agent",
         "main SQL + support SQL bundle을 생성하고, report-aware selection과 GROVER metric 기반 verification을 적용합니다.",
         "제안 시스템"),
    ]
    for tag, name, desc, role in baselines:
        color = "#3b82f6" if tag == "Proposed" else "#6b7280"
        bg = "#eff6ff" if tag == "Proposed" else "#f8fafc"
        st.markdown(f"""
        <div style='padding:16px 20px;background:{bg};border-radius:12px;border:1px solid {"#bfdbfe" if tag == "Proposed" else "#e2e8f0"};
                    margin-bottom:10px;border-left:4px solid {color}'>
            <div style='display:flex;justify-content:space-between;align-items:flex-start'>
                <div>
                    <span style='font-weight:700;color:{color}'>{tag}</span>
                    <span style='font-weight:600;color:#1e293b;margin-left:8px'>{name}</span>
                </div>
                <span style='font-size:0.78rem;color:{color};background:{color}15;
                             padding:3px 10px;border-radius:6px'>{role}</span>
            </div>
            <p style='color:#475569;margin:8px 0 0;font-size:0.88rem;line-height:1.6'>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class='example-box'>
        <div class='example-label'>💡 비교를 통해 검증할 것들</div>
        <ul style='color:#374151;margin:0;padding-left:18px;line-height:1.8;font-size:0.9rem'>
            <li>A vs B: retrieval-based pruning이 필요한가?</li>
            <li>B vs C: multi-candidate generation이 도움이 되는가?</li>
            <li>C vs Proposed: report-aware selection과 bundle이 필요한가?</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

    # Ablation
    st.markdown("<div class='subsection-header'>3.7 Ablation Study</div>", unsafe_allow_html=True)
    ablations = [
        "support SQL 제거",
        "report-aware selector 제거",
        "numeric checker 제거",
        "Coverage metric 제거",
        "diagnostic query를 descriptive로 축소",
        "human-verified subset 없이 기존 benchmark만 사용",
    ]
    for i, a in enumerate(ablations):
        st.markdown(f"""
        <div style='display:flex;align-items:center;gap:12px;padding:10px 14px;background:white;
                    border-radius:8px;border:1px solid #e2e8f0;margin-bottom:8px'>
            <span style='min-width:24px;height:24px;background:#f1f5f9;border-radius:50%;
                         display:flex;align-items:center;justify-content:center;
                         font-size:0.8rem;font-weight:600;color:#475569'>{i+1}</span>
            <span style='color:#374151;font-size:0.9rem'>{a}</span>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: REFERENCES
# ══════════════════════════════════════════════════════════════════════════════
elif page == "References":
    st.markdown("<div class='section-header'>References</div>", unsafe_allow_html=True)

    refs = [
        ("[1]", "BIRD", "Li et al., 2023",
         "Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs",
         "https://arxiv.org/abs/2305.03111", "#3b82f6"),
        ("[2]", "Spider 2.0", "Lei et al., ICLR 2025",
         "Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows",
         "https://openreview.net/forum?id=XmProj9cPs", "#8b5cf6"),
        ("[3]", "BIRD-INTERACT", "Huo et al., 2025",
         "BIRD-INTERACT: Re-imagining Text-to-SQL Evaluation for Large Language Models via Lens of Dynamic Interactions",
         "https://arxiv.org/abs/2510.05318", "#06b6d4"),
        ("[4]", "BI-Bench", "Gupta et al., ACL 2025",
         "BI-Bench: A Comprehensive Benchmark Dataset and Unsupervised Evaluation for BI Systems",
         "https://aclanthology.org/2025.acl-industry.90/", "#10b981"),
        ("[5]", "CORGI", "Li et al., 2025",
         "A New Text-to-SQL Benchmark for the Business Domain",
         "https://arxiv.org/abs/2510.07309", "#f59e0b"),
        ("[6]", "MT-RAIG", "Seo et al., ACL 2025",
         "MT-RAIG: Novel Benchmark and Evaluation Framework for Retrieval-Augmented Insight Generation over Multiple Tables",
         "https://aclanthology.org/2025.acl-long.1128/", "#ec4899"),
        ("[7]", "T2R-Bench", "Zhang et al., EMNLP 2025",
         "T2R-Bench: A Benchmark for Real World Table-to-Report Task",
         "https://aclanthology.org/2025.emnlp-main.1141/", "#ef4444"),
        ("[8]", "SpotIt", "Klopfenstein et al., 2025/2026",
         "SpotIt: Evaluating Text-to-SQL Evaluation with Formal Verification",
         "https://arxiv.org/abs/2510.26840", "#64748b"),
        ("[9]", "Benchmarks are Broken", "Jin et al., CIDR 2026",
         "Text-to-SQL Benchmarks are Broken: An In-Depth Analysis of BIRD and Spider 2.0-Snow",
         "https://www.vldb.org/cidrdb/papers/2026/p5-jin.pdf", "#dc2626"),
        ("[11]", "CHASE-SQL", "Pourreza et al., 2024",
         "CHASE-SQL: Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL",
         "https://arxiv.org/abs/2410.01943", "#0891b2"),
        ("[12]", "APEX-SQL", "Cao et al., 2026",
         "APEX-SQL: Talking to the Data via Agentic Exploration for Text-to-SQL",
         "https://arxiv.org/abs/2602.16720", "#7c3aed"),
    ]

    for num, name, authors, title, url, color in refs:
        st.markdown(f"""
        <div style='padding:16px 20px;background:white;border-radius:12px;border:1px solid #e2e8f0;
                    margin-bottom:10px;border-left:4px solid {color}'>
            <div style='display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:6px'>
                <div>
                    <span style='font-weight:700;color:{color};font-family:monospace'>{num}</span>
                    <span style='font-weight:700;color:#1e293b;margin-left:8px'>{name}</span>
                    <span style='color:#64748b;font-size:0.82rem;margin-left:8px'>— {authors}</span>
                </div>
            </div>
            <p style='color:#374151;margin:0 0 8px;font-size:0.88rem;line-height:1.5;font-style:italic'>{title}</p>
            <a href='{url}' target='_blank' style='font-size:0.8rem;color:{color};text-decoration:none'>
                🔗 {url}
            </a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0'>
        <div style='font-size:1.1rem;font-weight:700;color:#1e293b;margin-bottom:8px'>GROVER Project</div>
        <div style='color:#64748b;font-size:0.88rem'>
            Generative Reasoning and Objective Verification for End-to-end Reporting<br>
            NL2SQL end-to-end evaluation framework
        </div>
    </div>
    """, unsafe_allow_html=True)
