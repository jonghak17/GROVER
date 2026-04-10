from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="GROVER Explainer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# -----------------------------
# Data and helper functions
# -----------------------------


def inject_css() -> None:
    st.markdown(
        """
        <style>
        @import url('https://cdn.jsdelivr.net/npm/pretendard/dist/web/static/pretendard.css');

        :root {
            --bg-page: #f4f0e8;
            --bg-main: #f7f4ee;
            --surface: #ffffff;
            --surface-soft: #fcfaf6;
            --surface-muted: #f1ebe0;
            --line: #d8d0c2;
            --line-strong: #bfae97;
            --ink: #191714;
            --text: #38342e;
            --muted: #6e675e;
            --accent: #94633f;
            --accent-soft: #efe0cf;
            --accent-deep: #234f47;
            --accent-mist: #eef4f2;
            --danger: #a24636;
            --danger-bg: #fbf1ee;
            --success: #35624b;
            --success-bg: #f1f7f3;
            --shadow-lg: 0 22px 52px rgba(25, 23, 20, 0.08);
            --shadow-md: 0 14px 30px rgba(25, 23, 20, 0.06);
            --shadow-sm: 0 8px 18px rgba(25, 23, 20, 0.05);
            --radius-xl: 28px;
            --radius-lg: 20px;
            --radius-md: 16px;
            --radius-sm: 12px;
        }

        html, body {
            font-family: "Pretendard Variable", "Pretendard", -apple-system, BlinkMacSystemFont,
                         "Apple SD Gothic Neo", "Noto Sans KR", "Segoe UI", sans-serif;
        }

        .stApp {
            background: var(--bg-page);
            color: var(--text);
        }

        [data-testid="stAppViewContainer"] {
            background:
                radial-gradient(circle at top right, rgba(148, 99, 63, 0.07), transparent 28%),
                linear-gradient(180deg, #f7f4ee 0%, #f3eee6 100%);
        }

        [data-testid="stHeader"] {
            background: rgba(247, 244, 238, 0.82);
            border-bottom: 1px solid rgba(25, 23, 20, 0.06);
            backdrop-filter: blur(8px);
        }

        .main .block-container {
            max-width: 1240px;
            padding-top: 2.2rem;
            padding-bottom: 3.5rem;
        }

        .main * {
            font-family: "Pretendard Variable", "Pretendard", -apple-system, BlinkMacSystemFont,
                         "Apple SD Gothic Neo", "Noto Sans KR", "Segoe UI", sans-serif;
        }

        .main h1, .main h2, .main h3, .main h4 {
            color: var(--ink);
            letter-spacing: -0.02em;
        }

        .main h2 {
            margin-top: 0.3rem;
            margin-bottom: 1rem;
            padding-bottom: 0.8rem;
            border-bottom: 1px solid rgba(25, 23, 20, 0.08);
            font-size: 1.6rem;
        }

        .main h3 {
            margin-top: 1.8rem;
            margin-bottom: 0.8rem;
            font-size: 1.08rem;
        }

        .main p, .main li, .main label, .main .stCaption, .main .stMarkdown {
            color: var(--muted);
            line-height: 1.72;
        }

        [data-testid="stHorizontalBlock"] {
            gap: 1rem;
            align-items: stretch;
        }

        [data-testid="column"] {
            display: flex;
        }

        [data-testid="column"] > div {
            width: 100%;
            height: 100%;
        }

        .block-frame {
            display: flex;
            height: 100%;
            margin-bottom: 1rem;
        }

        .hero {
            position: relative;
            overflow: hidden;
            background:
                radial-gradient(circle at top right, rgba(148, 99, 63, 0.14), transparent 33%),
                linear-gradient(135deg, #fffaf3 0%, #ffffff 56%, #f1ebe0 100%);
            padding: 2.15rem 2rem 1.95rem 2rem;
            border-radius: var(--radius-xl);
            color: var(--ink);
            box-shadow: var(--shadow-lg);
            border: 1px solid rgba(25, 23, 20, 0.11);
        }
        .hero::after {
            content: "";
            position: absolute;
            right: -52px;
            top: -70px;
            width: 220px;
            height: 220px;
            border-radius: 999px;
            background: radial-gradient(circle, rgba(35, 79, 71, 0.16), rgba(35, 79, 71, 0) 68%);
            pointer-events: none;
        }
        .hero h1 {
            position: relative;
            z-index: 1;
            font-size: 2.35rem;
            margin: 0.25rem 0 0.78rem 0;
            line-height: 1.2;
            color: var(--ink);
            max-width: 860px;
        }
        .hero p {
            position: relative;
            z-index: 1;
            font-size: 1.01rem;
            line-height: 1.75;
            margin-bottom: 0.1rem;
            color: var(--text);
            max-width: 800px;
        }
        .eyebrow {
            display: inline-block;
            position: relative;
            z-index: 1;
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            padding: 0.45rem 0.76rem;
            border-radius: 999px;
            border: 1px solid rgba(25, 23, 20, 0.06);
            background: var(--ink);
            color: white;
            margin-bottom: 0.7rem;
        }
        .badge-row {
            margin: 0.9rem 0 0.1rem 0;
        }
        .badge {
            display: inline-block;
            padding: 0.36rem 0.76rem;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
            border-radius: 999px;
            background: var(--accent-soft);
            color: #4d3a2b;
            font-size: 0.81rem;
            font-weight: 600;
            border: 1px solid #dcc7af;
        }
        .section-card {
            position: relative;
            overflow: hidden;
            flex: 1;
            background: var(--surface);
            border-radius: var(--radius-lg);
            padding: 1.25rem 1.2rem 1.1rem 1.2rem;
            border: 1px solid var(--line);
            box-shadow: var(--shadow-md);
            height: 100%;
        }
        .section-card::before {
            content: "";
            position: absolute;
            left: 1.2rem;
            top: 0;
            width: 76px;
            height: 4px;
            border-radius: 999px;
            background: var(--accent);
        }
        .section-card h3 {
            margin-top: 0;
            margin-bottom: 0.7rem;
            font-size: 1.08rem;
            color: var(--ink);
        }
        .section-card p, .section-card li {
            color: var(--text);
            line-height: 1.72;
            font-size: 0.96rem;
        }
        .section-card ul {
            padding-left: 1.15rem;
            margin-bottom: 0;
        }
        .mini-card {
            flex: 1;
            background: linear-gradient(180deg, var(--surface) 0%, var(--surface-soft) 100%);
            border-radius: var(--radius-md);
            padding: 1rem 1.05rem;
            border: 1px solid rgba(191, 174, 151, 0.72);
            box-shadow: var(--shadow-sm);
            margin-bottom: 1rem;
            height: 100%;
        }
        .mini-card strong {
            color: var(--ink);
            display: block;
            font-size: 0.98rem;
            margin-bottom: 0.12rem;
        }
        .mini-card p {
            margin: 0.42rem 0 0 0;
            color: var(--text);
            line-height: 1.65;
            font-size: 0.94rem;
        }
        .callout {
            border-left: 6px solid var(--accent-deep);
            background: linear-gradient(135deg, var(--accent-mist) 0%, #ffffff 100%);
            padding: 1.05rem 1.15rem;
            border-radius: var(--radius-md);
            color: #1d3935;
            margin: 0.45rem 0 1rem 0;
            border: 1px solid rgba(35, 79, 71, 0.14);
            box-shadow: var(--shadow-sm);
        }
        .callout strong {
            color: #1d3935;
        }
        .step-card {
            flex: 1;
            background: linear-gradient(180deg, #ffffff 0%, #faf6ef 100%);
            border-radius: var(--radius-lg);
            padding: 1.1rem 1rem 1rem 1rem;
            border: 1px solid var(--line);
            box-shadow: var(--shadow-md);
            height: 100%;
        }
        .step-num {
            width: 38px;
            height: 38px;
            border-radius: 12px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: var(--ink);
            color: white;
            font-weight: 700;
            margin-bottom: 0.72rem;
            font-size: 0.95rem;
            box-shadow: 0 10px 20px rgba(25, 23, 20, 0.16);
        }
        .step-card h4 {
            margin: 0 0 0.4rem 0;
            color: var(--ink);
            font-size: 1rem;
        }
        .step-card p {
            margin: 0;
            color: var(--text);
            line-height: 1.65;
            font-size: 0.93rem;
        }
        .report-box {
            flex: 1;
            background: linear-gradient(180deg, #ffffff 0%, #fbf8f2 100%);
            border: 1px solid var(--line);
            border-radius: var(--radius-lg);
            padding: 1.2rem 1.3rem;
            box-shadow: var(--shadow-md);
        }
        .report-box h4 {
            margin-top: 0;
            color: var(--ink);
        }
        .report-pill {
            display: inline-block;
            padding: 0.3rem 0.66rem;
            border-radius: 999px;
            background: #eee6d8;
            color: #4b3b2d;
            border: 1px solid #dcccb5;
            font-size: 0.82rem;
            margin-right: 0.45rem;
            margin-bottom: 0.35rem;
            font-weight: 600;
        }
        .formula-box {
            background: rgba(25, 23, 20, 0.03);
            border: 1px solid rgba(25, 23, 20, 0.08);
            border-radius: var(--radius-md);
            padding: 0.9rem 1rem;
            margin-top: 0.7rem;
        }
        .danger-box {
            border-left: 6px solid var(--danger);
            background: var(--danger-bg);
            padding: 1rem 1.05rem;
            border-radius: var(--radius-md);
            color: #6f2d22;
            margin: 0.65rem 0;
            border: 1px solid rgba(162, 70, 54, 0.16);
            box-shadow: var(--shadow-sm);
        }
        .success-box {
            border-left: 6px solid var(--success);
            background: var(--success-bg);
            padding: 1rem 1.05rem;
            border-radius: var(--radius-md);
            color: #264a38;
            margin: 0.65rem 0;
            border: 1px solid rgba(53, 98, 75, 0.15);
            box-shadow: var(--shadow-sm);
        }
        .sidebar-brand {
            background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
            border-radius: 20px;
            padding: 1.1rem 1.05rem 1rem 1.05rem;
            border: 1px solid rgba(255,255,255,0.08);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
            margin-bottom: 1rem;
        }
        .sidebar-kicker {
            display: inline-block;
            color: #d6c6b1;
            font-size: 0.74rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 0.55rem;
        }
        .sidebar-brand h2 {
            margin: 0 0 0.5rem 0;
            font-size: 1.35rem;
            color: #faf7f2;
            letter-spacing: -0.03em;
        }
        .sidebar-brand p {
            margin: 0;
            color: rgba(255,255,255,0.7);
            font-size: 0.92rem;
            line-height: 1.65;
        }
        .sidebar-note {
            background: rgba(255,255,255,0.04);
            border-radius: 16px;
            padding: 0.9rem 1rem;
            border: 1px solid rgba(255,255,255,0.08);
            color: rgba(255,255,255,0.82);
        }
        .footer-note {
            color: var(--muted);
            font-size: 0.9rem;
            line-height: 1.6;
        }

        [data-testid="stSidebar"] {
            background:
                radial-gradient(circle at top left, rgba(148, 99, 63, 0.18), transparent 26%),
                linear-gradient(180deg, #111315 0%, #17191d 100%);
            border-right: 1px solid rgba(255,255,255,0.08);
        }

        [data-testid="stSidebar"] :where(
            p, span, label, li, a, div, button, input, textarea, select, summary, h1, h2, h3, h4, h5, h6
        ) {
            font-family: "Pretendard Variable", "Pretendard", -apple-system, BlinkMacSystemFont,
                         "Apple SD Gothic Neo", "Noto Sans KR", "Segoe UI", sans-serif;
        }

        .material-symbols-rounded,
        .material-symbols-outlined,
        .material-icons,
        .material-icons-round,
        [class^="material-symbols"],
        [class*=" material-symbols"] {
            font-family: "Material Symbols Rounded", "Material Symbols Outlined", sans-serif !important;
            font-weight: normal;
            font-style: normal;
            line-height: 1;
            letter-spacing: normal;
            text-transform: none;
            display: inline-block;
            white-space: nowrap;
            word-wrap: normal;
            direction: ltr;
            -webkit-font-smoothing: antialiased;
        }

        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] li,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] .stCaption {
            color: rgba(255,255,255,0.78);
        }

        [data-testid="stSidebar"] .stMarkdown h3 {
            color: #f6f3ef;
        }

        [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"] {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 14px;
            padding: 0.55rem 0.72rem;
            margin-bottom: 0.45rem;
            transition: background 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
        }

        [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"]:hover {
            background: rgba(255,255,255,0.06);
            border-color: rgba(255,255,255,0.16);
            transform: translateY(-1px);
        }

        [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {
            background: #f3ede2;
            border-color: #f3ede2;
        }

        [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) p,
        [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) span {
            color: #17191d !important;
            font-weight: 600;
        }

        [data-testid="stSidebar"] details {
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            background: rgba(255,255,255,0.03);
        }

        [data-testid="stSidebar"] details summary,
        [data-testid="stSidebar"] details summary * {
            color: #f6f3ef !important;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.5rem;
            padding: 0;
        }

        .stTabs [data-baseweb="tab"] {
            height: auto;
            padding: 0.55rem 0.92rem;
            border-radius: 999px;
            border: 1px solid var(--line);
            background: rgba(255,255,255,0.72);
            color: var(--text);
            font-weight: 600;
        }

        .stTabs [aria-selected="true"] {
            background: var(--ink);
            border-color: var(--ink);
            color: #ffffff;
        }

        .main [data-testid="stRadio"] div[role="radiogroup"] {
            gap: 0.45rem;
        }

        .main [data-testid="stRadio"] label[data-baseweb="radio"] {
            border: 1px solid var(--line);
            background: rgba(255,255,255,0.82);
            border-radius: 999px;
            padding: 0.38rem 0.74rem;
        }

        .main [data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {
            background: var(--ink);
            border-color: var(--ink);
        }

        .main [data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) p,
        .main [data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) span {
            color: #ffffff !important;
            font-weight: 600;
        }

        div[data-baseweb="select"] > div {
            border: 1px solid var(--line);
            border-radius: 14px;
            background: rgba(255,255,255,0.92);
            box-shadow: none;
        }

        [data-testid="stDataFrame"] {
            border: 1px solid var(--line);
            border-radius: 18px;
            overflow: hidden;
            background: rgba(255,255,255,0.94);
            box-shadow: var(--shadow-sm);
        }

        [data-testid="stMetric"] {
            background: rgba(255,255,255,0.95);
            border: 1px solid var(--line);
            border-radius: 18px;
            padding: 0.95rem 1rem 0.9rem 1rem;
            box-shadow: var(--shadow-sm);
        }

        [data-testid="stMetricValue"] {
            color: var(--ink);
        }

        [data-testid="stMetricLabel"] {
            color: var(--muted);
        }

        .stCodeBlock, pre {
            border-radius: 16px !important;
            border: 1px solid rgba(25, 23, 20, 0.10);
        }

        details[data-testid="stExpander"] {
            border: 1px solid var(--line);
            border-radius: 18px;
            background: rgba(255,255,255,0.82);
            box-shadow: var(--shadow-sm);
        }

        details[data-testid="stExpander"] summary {
            padding: 0.15rem 0.1rem;
        }

        @media (max-width: 960px) {
            .main .block-container {
                padding-top: 1.6rem;
                padding-bottom: 2.6rem;
            }
            .hero {
                padding: 1.7rem 1.35rem 1.55rem 1.35rem;
            }
            .hero h1 {
                font-size: 1.9rem;
            }
            .block-frame {
                margin-bottom: 0.85rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def badge_row(labels: List[str]) -> None:
    badges = "".join(f'<span class="badge">{label}</span>' for label in labels)
    st.markdown(f'<div class="badge-row">{badges}</div>', unsafe_allow_html=True)


def card(title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="block-frame">
            <div class="section-card">
                <h3>{title}</h3>
                {body}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def mini_card(title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="block-frame">
            <div class="mini-card">
                <strong>{title}</strong>
                <p>{body}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def step_box(num: int, title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="block-frame">
            <div class="step-card">
                <div class="step-num">{num}</div>
                <h4>{title}</h4>
                <p>{body}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def callout(text: str) -> None:
    st.markdown(f'<div class="callout">{text}</div>', unsafe_allow_html=True)


def success_box(text: str) -> None:
    st.markdown(f'<div class="success-box">{text}</div>', unsafe_allow_html=True)


def danger_box(text: str) -> None:
    st.markdown(f'<div class="danger-box">{text}</div>', unsafe_allow_html=True)


def report_box(direct_answer: str, claims: List[str], caveat: str) -> None:
    claim_html = "".join(f"<li>{claim}</li>" for claim in claims)
    st.markdown(
        f"""
        <div class="block-frame">
            <div class="report-box">
                <div>
                    <span class="report-pill">Direct Answer</span>
                    <span class="report-pill">Supporting Claims</span>
                    <span class="report-pill">Caveat</span>
                </div>
                <h4>예시 Structured Report</h4>
                <p><strong>Direct Answer</strong><br>{direct_answer}</p>
                <p><strong>Supporting Claims</strong></p>
                <ul>{claim_html}</ul>
                <p><strong>Caveat / Limitation</strong><br>{caveat}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def load_raw_document() -> str:
    candidates = [
        Path(__file__).with_name("project_grover.md"),
        Path.cwd() / "project_grover.md",
        Path(__file__).with_name("GROVER_NL2SQL_project_plan.md"),
        Path.cwd() / "GROVER_NL2SQL_project_plan.md",
        Path("/mnt/data/GROVER_NL2SQL_project_plan.md"),
    ]
    for path in candidates:
        if path.exists():
            try:
                return path.read_text(encoding="utf-8")
            except Exception:
                continue
    return ""


PIPELINE_STEPS: Dict[str, Dict[str, str]] = {
    "1. Question Typing": {
        "goal": "질문이 '무엇이 얼마인가'를 묻는지(descriptive), 아니면 '왜 그렇게 되었는가'를 묻는지(diagnostic)를 먼저 분류합니다.",
        "why": "질문 유형이 다르면 필요한 evidence도 달라집니다. '총매출' 질문에는 직접 답을 주는 SQL이 중요하지만, '왜 감소했는가' 질문에는 추세, 세그먼트 분해, driver 분석이 추가로 필요합니다.",
        "input": "자연어 질문 q",
        "output": "질문 유형 + 필요한 analytical slot 목록",
        "example": "'지난 분기 매출이 왜 감소했는가?' → diagnostic. 따라서 direct answer + trend + segment breakdown + driver + caveat가 필요합니다.",
        "analogy": "의사도 먼저 '열이 나는가'와 '왜 열이 나는가'를 구분합니다. 진단 질문은 검사 종류가 더 많아집니다.",
        "risk": "이 단계가 틀리면, 시스템이 사용자가 원하는 답의 깊이를 잘못 맞춥니다. 예를 들어 diagnostic 질문을 descriptive처럼 처리하면 숫자만 말하고 원인을 설명하지 못합니다.",
    },
    "2. Schema / Value Retrieval": {
        "goal": "큰 데이터베이스에서 실제로 관련 있는 테이블, 컬럼, 값만 골라서 문맥을 줄입니다.",
        "why": "현실 데이터베이스는 컬럼 수가 많습니다. 관련 없는 스키마를 모두 보여주면 모델이 헷갈리고, 쿼리도 길어지고, 실행 효율도 나빠집니다.",
        "input": "질문 q + 전체 스키마 S + 후보 값들",
        "output": "pruned schema + grounded value candidates",
        "example": "'매출 감소' 질문이라면 sales, region, customer_segment, order_date, revenue 같은 요소를 우선 회수하고, 인사 테이블 같은 비관련 스키마는 제외합니다.",
        "analogy": "도서관 전체를 뒤지지 않고, 먼저 해당 주제의 서가만 꺼내서 보는 과정과 같습니다.",
        "risk": "retrieval이 약하면 필요한 테이블을 놓치고, retrieval이 너무 넓으면 모델이 noise에 휩쓸립니다.",
    },
    "3. SQL Bundle Generation": {
        "goal": "main SQL 1개만 만들지 않고, 최종 설명에 필요한 support SQL까지 함께 생성합니다.",
        "why": "diagnostic 질문은 보통 하나의 aggregate SQL만으로는 충분하지 않습니다. 감소율은 알 수 있어도 왜 감소했는지는 별도 evidence가 필요합니다.",
        "input": "질문 유형 + pruned schema + retrieved values",
        "output": "SQL bundle Z = {main SQL, support SQLs}",
        "example": "main SQL은 분기별 KPI 차이를 구하고, support SQL은 시간 추세, 지역/세그먼트 breakdown, top driver를 계산합니다.",
        "analogy": "보고서를 쓸 때 본문 한 문장만 쓰는 것이 아니라, 표·그래프·근거 표본을 함께 모으는 것과 같습니다.",
        "risk": "support SQL이 없으면 결과 보고서가 얕고 취약해집니다. 반대로 support SQL이 너무 많으면 비용이 커집니다.",
    },
    "4. Execution and Verification": {
        "goal": "생성된 SQL bundle을 실제 DB에 실행하고, 문법 오류·빈 결과·사소한 결과를 점검합니다.",
        "why": "문법만 맞아도 실무적으로 쓸모없는 결과가 나올 수 있습니다. 예를 들어 빈 결과는 분석 근거가 되지 못하고, 한 행만 나오는 표로는 driver 분석이 불가능할 수 있습니다.",
        "input": "SQL bundle Z + 데이터베이스 D",
        "output": "실행 결과 R + 검증 상태",
        "example": "breakdown query가 빈 결과를 내면, 다른 grouping 기준으로 retry하거나 candidate를 교체합니다.",
        "analogy": "계산식을 적는 것과 실제로 계산해 검산하는 것은 다릅니다.",
        "risk": "실행은 되었지만 분석에 불충분한 'trivial result'를 놓치면 report가 과장되거나 공허해질 수 있습니다.",
    },
    "5. Structured Report Generation": {
        "goal": "결과 테이블을 그대로 던져주지 않고, direct answer + supporting claims + caveat 형태의 구조화된 보고서를 생성합니다.",
        "why": "자유로운 장문 응답은 평가하기 어렵습니다. claim 단위로 쪼개서 검증하려면 보고서 형식이 어느 정도 구조화되어야 합니다.",
        "input": "실행 결과 R",
        "output": "최종 report y",
        "example": "'주된 원인은 북미 enterprise segment의 부진'이라는 direct answer를 쓰고, 수치 근거 claim 2~3개와 caveat 1개를 덧붙입니다.",
        "analogy": "표를 읽어서 발표 슬라이드용 핵심 메시지로 번역하는 단계입니다.",
        "risk": "구조가 없으면 평가는 주관적으로 흐르고, 모델이 그럴듯한 과장을 하기 쉬워집니다.",
    },
    "6. Report-aware Selection / Verification": {
        "goal": "여러 candidate bundle 중에서 SQL만 잘 맞는 후보가 아니라, 최종 보고서 품질이 가장 좋은 후보를 선택합니다.",
        "why": "SQL-level score가 비슷해도 insight-level quality는 크게 다를 수 있습니다. 근거가 더 풍부한 후보가 좋은 보고서를 만듭니다.",
        "input": "candidate bundles + 각 bundle로부터 생성된 report",
        "output": "최종 선택된 bundle/report",
        "example": "Candidate A와 C가 둘 다 실행은 성공했지만, B만 trend와 segment evidence를 함께 제공한다면 B를 선택합니다.",
        "analogy": "정답처럼 보이는 계산식 여러 개 중, 실제 발표 자료로 가장 설득력 있는 버전을 고르는 과정입니다.",
        "risk": "selector가 SQL 정확도만 보면, 근거가 빈약한 답변을 뽑을 수 있습니다.",
    },
}


def get_example_tables() -> Dict[str, pd.DataFrame]:
    trend = pd.DataFrame(
        {
            "월": ["1월", "2월", "3월", "4월", "5월", "6월"],
            "매출(백만 달러)": [128, 125, 121, 118, 109, 103],
        }
    )

    breakdown = pd.DataFrame(
        {
            "지역": ["북미", "북미", "유럽", "APAC"],
            "세그먼트": ["Enterprise", "SMB", "Enterprise", "Enterprise"],
            "전분기 매출": [72, 31, 44, 37],
            "지난 분기 매출": [45, 29, 41, 35],
            "변화율": ["-37.5%", "-6.5%", "-6.8%", "-5.4%"],
        }
    )

    driver = pd.DataFrame(
        {
            "드라이버 후보": ["북미 Enterprise", "가격 인상 제품군 A", "유럽 SMB", "신규 고객 유입 감소"],
            "기여 감소액": [27, 8, 3, 2],
            "설명": [
                "전체 감소의 가장 큰 비중",
                "상위 제품군 매출 하락",
                "영향은 있으나 규모는 작음",
                "부가적인 요인 가능성",
            ],
        }
    )

    claims = pd.DataFrame(
        {
            "claim 유형": ["numeric", "comparison", "ranking", "diagnostic"],
            "예시": [
                "북미 매출은 전분기 대비 37.5% 감소했다.",
                "북미 감소폭이 유럽보다 더 크다.",
                "가장 큰 감소 요인은 북미 Enterprise이다.",
                "주된 원인은 북미 Enterprise 부진이다.",
            ],
            "검증 방식": [
                "표에서 수치를 직접 계산",
                "두 수치의 관계를 비교",
                "정렬 및 top-1 확인",
                "수치 evidence + judge/human audit 결합",
            ],
        }
    )

    candidate_table = pd.DataFrame(
        {
            "Candidate": ["A", "B", "C"],
            "구성": [
                "main SQL만 생성",
                "main + trend + breakdown + driver",
                "main + trend만 생성",
            ],
            "SQL-Level 예상": [0.90, 0.88, 0.91],
            "Report 품질 예상": [0.49, 0.86, 0.68],
            "선택 이유": [
                "숫자는 맞지만 설명이 얕음",
                "질문 의도에 맞는 근거가 가장 풍부함",
                "방향성은 보이나 driver 설명이 부족함",
            ],
        }
    )

    datasets = pd.DataFrame(
        {
            "Dataset": [
                "BIRD Mini-Dev V2",
                "BIRD Dev / selected split",
                "CORGI",
                "BI-Bench",
                "Spider 2.0-Lite",
                "GROVER-Bridge",
            ],
            "역할": [
                "빠른 개발 및 반복 실험",
                "SQL correctness + efficiency 검증",
                "Insight-Level 핵심 평가",
                "BI taxonomy와 framing 참고",
                "robustness stress test",
                "human alignment 검증",
            ],
            "설명": [
                "빠르게 실험 돌리기 좋은 development benchmark",
                "최종 SQL/DB-level 성능 확인용",
                "business-domain high-order query에 적합",
                "질문 유형 분류 체계를 잡을 때 유용",
                "현실 workflow 복잡도에 대한 보조 실험",
                "사람 판단과 metric 정렬을 검증하는 소규모 subset",
            ],
        }
    )

    baselines = pd.DataFrame(
        {
            "시스템": [
                "Baseline A",
                "Baseline B",
                "Baseline C",
                "Proposed: GROVER-Agent",
            ],
            "설정": [
                "One-shot NL2SQL + direct answer",
                "Retrieval-pruned single SQL",
                "Multi-candidate SQL + SQL-only selector",
                "Evidence-bundled SQL + report-aware selector",
            ],
            "검증 포인트": [
                "가장 단순한 출발점",
                "retrieval 자체의 효과",
                "candidate generation의 효과",
                "bundle + report-aware selection의 합산 효과",
            ],
        }
    )

    glossary = pd.DataFrame(
        {
            "용어": [
                "NL2SQL",
                "Evidence Bundle",
                "Support SQL",
                "Structured Report",
                "Report-aware Selector",
                "TG-F1",
                "NumAcc",
                "Coverage",
                "Intent Alignment",
                "GROVER-Bridge",
            ],
            "뜻": [
                "자연어 질문을 SQL로 바꾸는 문제 설정",
                "최종 해석에 필요한 SQL 묶음",
                "main SQL을 보조하는 추가 evidence query",
                "Direct Answer/Claims/Caveat로 분리된 보고서 형식",
                "SQL만이 아니라 보고서 품질로 후보를 고르는 선택기",
                "Table-grounded precision/recall 기반 F1",
                "숫자 claim의 정확도",
                "질문 유형별 필수 슬롯 충족도",
                "답변이 질문 의도에 맞는 정도",
                "사람이 검증한 소규모 평가 subset",
            ],
        }
    )

    return {
        "trend": trend,
        "breakdown": breakdown,
        "driver": driver,
        "claims": claims,
        "candidate_table": candidate_table,
        "datasets": datasets,
        "baselines": baselines,
        "glossary": glossary,
    }


def compute_insight_score(
    tg_f1: float,
    num_acc: float,
    cov: float,
    ia: float,
    weights: Tuple[float, float, float, float],
) -> float:
    g1, g2, g3, g4 = weights
    return g1 * tg_f1 + g2 * num_acc + g3 * cov + g4 * ia


def normalize_weights(raw_weights: List[int]) -> Tuple[float, float, float, float]:
    total = sum(raw_weights)
    if total == 0:
        return 0.35, 0.30, 0.20, 0.15
    return tuple(w / total for w in raw_weights)  # type: ignore[return-value]


TABLES = get_example_tables()
RAW_DOCUMENT = load_raw_document()


# -----------------------------
# Section renderers
# -----------------------------


def render_home() -> None:
    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">GROVER EXPLAINER</div>
            <h1>SQL을 잘 만드는지에서, 결과를 잘 설명하는지로</h1>
            <p>
                이 앱은 업로드한 GROVER 프로젝트 문서를 처음 보는 사람도 읽기 쉽도록 다시 구성한 설명 페이지입니다.
                핵심 메시지는 단순합니다. <strong>좋은 NL2SQL 시스템</strong>은 SQL만 맞히는 시스템이 아니라,
                <strong>실행 결과를 근거로 믿을 수 있는 분석 보고서를 만드는 시스템</strong>이어야 합니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    badge_row(["End-to-End", "Evidence-Bundled", "Table-Grounded", "Human-Verified"])

    st.markdown("### 이 문서가 바꾸는 질문")
    col1, col2, col3 = st.columns(3)
    with col1:
        card(
            "기존 질문",
            "<p><strong>'정답 SQL을 생성했는가?'</strong>가 중심입니다. 실행 성공, Exact Match, Test Suite 등은 중요하지만, 최종 분석의 신뢰성까지는 말해주지 못합니다.</p>",
        )
    with col2:
        card(
            "바뀐 질문",
            "<p><strong>'실행 결과를 바탕으로 유의미하고 검증 가능한 인사이트를 만들었는가?'</strong>를 함께 묻습니다. 즉 SQL correctness를 넘어 report usefulness를 봅니다.</p>",
        )
    with col3:
        card(
            "GROVER의 해답",
            "<p>SQL-Level, DB-Level, Insight-Level의 <strong>3단 평가</strong>를 두고, main SQL + support SQL bundle을 기반으로 table-grounded report를 평가합니다.</p>",
        )

    st.markdown("### 30초 요약")
    callout(
        "<strong>핵심 재정의</strong><br>NL2SQL을 <strong>q → z₀</strong> 문제로 보지 않고, <strong>q → Z → R → y</strong> 문제로 봅니다.<br><br>"
        "- q: 사용자의 자연어 질문<br>"
        "- Z: main SQL과 support SQL이 묶인 bundle<br>"
        "- R: 실제 DB 실행 결과 테이블들<br>"
        "- y: 최종 자연어 report"
    )

    st.markdown("### 한눈에 보는 6단계 파이프라인")
    row1 = st.columns(3)
    row2 = st.columns(3)
    titles = list(PIPELINE_STEPS.keys())
    descs = [
        "질문이 descriptive인지 diagnostic인지 구분",
        "관련 schema/value만 골라 context 축소",
        "main SQL + support SQL 묶음 생성",
        "실행 후 오류·빈 결과·trivial result 검증",
        "결과를 structured report로 변환",
        "보고서 품질 기준으로 최종 후보 선택",
    ]
    for idx, (col, title, desc) in enumerate(zip(row1 + row2, titles, descs), start=1):
        with col:
            step_box(idx, title.split('. ', 1)[1], desc)

    st.markdown("### 왜 특히 Methodology가 중요한가")
    left, right = st.columns([1.05, 0.95])
    with left:
        card(
            "이 연구의 실제 중심",
            "<ul>"
            "<li>새로운 SQL generator 하나를 제안하는 것이 중심이 아닙니다.</li>"
            "<li><strong>어떤 evidence를 수집할지</strong>, <strong>그 evidence를 어떻게 report로 만들지</strong>, <strong>그 report를 어떻게 검증할지</strong>가 중심입니다.</li>"
            "<li>그래서 Methodology는 알고리즘 설명이면서 동시에 평가 철학 설명이기도 합니다.</li>"
            "</ul>",
        )
    with right:
        card(
            "처음 읽는 사람이 특히 봐야 할 것",
            "<ul>"
            "<li>왜 single SQL이 아니라 SQL bundle인지</li>"
            "<li>왜 report generation이 별도 모듈인지</li>"
            "<li>왜 metric이 TG-F1 / NumAcc / Coverage / Intent Alignment로 분해되는지</li>"
            "<li>왜 human-verified subset이 필요한지</li>"
            "</ul>",
        )

    st.markdown("### GROVER를 한 장으로 보면")
    a, b, c = st.columns(3)
    with a:
        card(
            "SQL-Level",
            "<p><strong>질문:</strong> SQL이 실행적으로 맞는가?<br><strong>대표 metric:</strong> EX, Test Suite, Soft F1<br><strong>의미:</strong> '쿼리 자체'의 정확성</p>",
        )
    with b:
        card(
            "DB-Level",
            "<p><strong>질문:</strong> 얼마나 효율적으로 실행되는가?<br><strong>대표 metric:</strong> R-VES 계열, retry 수, DB call 수<br><strong>의미:</strong> '시스템 비용'과 workflow 효율</p>",
        )
    with c:
        card(
            "Insight-Level",
            "<p><strong>질문:</strong> 최종 report가 근거 있고 유용한가?<br><strong>대표 metric:</strong> TG-F1, NumAcc, Coverage, IA<br><strong>의미:</strong> '사용자에게 전달되는 분석'의 신뢰성</p>",
        )

    st.caption("모든 예시 SQL과 결과 테이블은 앱 설명을 위한 illustrative example입니다.")


def render_introduction() -> None:
    st.markdown("## 1. 연구 배경과 문제의 변화")
    callout(
        "<strong>문제의 중심 이동</strong><br>"
        "예전에는 '질문 하나에 SQL 하나를 얼마나 정확히 만들었는가'가 중심이었습니다."
        " 이제는 '실제 workflow에서 신뢰할 수 있는 분석을 끝까지 만들었는가'가 더 중요해졌습니다."
    )

    st.markdown("### 흐름이 어떻게 바뀌었나")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        mini_card("초기 NL2SQL", "자연어를 SQL로 바꾸는 semantic parsing 문제가 중심이었습니다. 핵심은 문법과 정답 SQL 매칭이었습니다.")
    with c2:
        mini_card("Large schema 시대", "BIRD류 문제 설정에서는 value grounding, large schema, execution efficiency가 중요해졌습니다.")
    with c3:
        mini_card("Workflow 확장", "Spider 2.0 계열은 multi-query workflow, enterprise metadata, 긴 문맥을 요구합니다.")
    with c4:
        mini_card("Interactive / BI 확장", "BIRD-INTERACT, BI-Bench, CORGI류는 clarification, diagnosis, insight generation까지 문제를 넓힙니다.")

    st.markdown("### 기존 접근의 세 가지 빈틈")
    v1, v2, v3 = st.columns(3)
    with v1:
        card(
            "1) SQL 자체에 머무르는 평가",
            "<p>Execution Accuracy와 Test Suite Accuracy는 매우 중요하지만, 이것만으로는 <strong>'이 쿼리 결과를 바탕으로 사용자가 납득할 만한 설명을 했는가'</strong>를 측정할 수 없습니다.</p>",
        )
    with v2:
        card(
            "2) SQL 이후 단계의 과소연구",
            "<p>실제 사용자에게 중요한 것은 결과 테이블 그 자체보다 <strong>해석된 의미</strong>입니다. 그런데 많은 시스템은 실행 결과를 그대로 보여주거나 간단한 요약만 붙입니다.</p>",
        )
    with v3:
        card(
            "3) benchmark와 evaluation noise",
            "<p>semantic equivalence, annotation ambiguity, static evaluation의 한계 때문에, leaderboard 점수 하나만으로 시스템 품질을 단정하기가 점점 어려워졌습니다.</p>",
        )

    st.markdown("### 예시 질문 하나로 직관 잡기")
    left, right = st.columns(2)
    with left:
        card(
            "기존 방식이 주는 답",
            "<p><strong>질문:</strong> '지난 분기 매출이 왜 감소했는가?'</p>"
            "<p><strong>출력:</strong> 전분기 대비 -12%라는 단일 수치와 aggregate table</p>"
            "<p><strong>문제:</strong> 감소 사실은 알 수 있어도, 어디서 줄었는지·어떤 세그먼트가 컸는지·얼마나 설명할 수 있는지까지는 알기 어렵습니다.</p>",
        )
    with right:
        card(
            "GROVER가 주는 답",
            "<p><strong>출력:</strong> direct answer + trend evidence + segment breakdown + top driver + caveat</p>"
            "<p><strong>장점:</strong> 사용자는 단순히 숫자를 보는 것이 아니라, <strong>그 숫자를 뒷받침하는 분석 구조</strong>를 함께 받게 됩니다.</p>",
        )

    st.markdown("### 문서의 세 가지 핵심 질문")
    q1, q2, q3 = st.columns(3)
    with q1:
        mini_card("Q1. SQL generation", "최종 report에 필요한 evidence를 더 잘 모으려면 single SQL 대신 어떤 generation 전략을 써야 하는가?")
    with q2:
        mini_card("Q2. Table analysis", "실행 결과를 바탕으로 LLM이 더 신뢰할 수 있는 insight를 생성하려면 어떤 intermediate representation이 필요한가?")
    with q3:
        mini_card("Q3. Evaluation", "SQL correctness를 넘어 report의 충실성·유용성·groundedness를 어떻게 정량화할 것인가?")



def render_methodology() -> None:
    st.markdown("## 2. Methodology")
    st.markdown(
        """
        <div class="hero" style="padding-top:1.6rem; padding-bottom:1.4rem;">
            <div class="eyebrow">DETAILED WALKTHROUGH</div>
            <h1 style="font-size:1.9rem;">Methodology를 처음 보는 사람도 따라가게 풀어쓴 버전</h1>
            <p>
                이 파트의 본질은 <strong>SQL을 정답 생성기</strong>가 아니라 <strong>증거 수집 도구</strong>로 재해석하는 데 있습니다.
                아래 탭에서 큰 그림, SQL bundle, table analysis, metric, human verification, end-to-end 예시를 순서대로 볼 수 있습니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    tabs = st.tabs(
        [
            "큰 그림",
            "Part I · SQL Bundle",
            "Part II · Table Analysis",
            "Part III · Metric",
            "Part IV · Human Verification",
            "End-to-End Example",
        ]
    )

    with tabs[0]:
        callout(
            "<strong>핵심 수식처럼 읽는 문장</strong><br>"
            "GROVER는 문제를 <strong>q → Z → R → y</strong> 로 정의합니다."
            " 즉 질문을 받아서 SQL 하나를 끝내는 것이 아니라, SQL 묶음을 만들고, 실제로 실행하고, 그 결과를 보고서로 바꾸는 전체 과정을 다룹니다."
        )
        st.latex(r"q \rightarrow Z \rightarrow R \rightarrow y")

        notation_df = pd.DataFrame(
            {
                "기호": ["q", "D", "S", "Z", "R", "y", "C*", "Ĉ"],
                "뜻": [
                    "자연어 질문",
                    "데이터베이스",
                    "스키마",
                    "SQL bundle",
                    "SQL 실행 결과 집합",
                    "최종 report",
                    "gold claim set",
                    "predicted claim set",
                ],
                "초심자용 해석": [
                    "사용자가 묻는 문장",
                    "실제 데이터가 들어 있는 공간",
                    "테이블/컬럼 구조",
                    "main SQL + support SQL 묶음",
                    "각 SQL이 뽑아낸 표들",
                    "최종적으로 사용자가 읽는 설명 문장",
                    "정답 측에서 꼭 말해야 하는 claim 목록",
                    "모델이 실제로 말한 claim 목록",
                ],
            }
        )
        st.dataframe(notation_df, hide_index=True, use_container_width=True)

        st.markdown("### 이 수식이 왜 중요한가")
        left, right = st.columns([1.05, 0.95])
        with left:
            card(
                "기존 q → z₀ 관점의 한계",
                "<p>질문에서 곧바로 SQL 한 개를 만드는 관점에서는 <strong>SQL 이후에 무슨 일이 벌어지는지</strong>가 잘 보이지 않습니다."
                " 결과를 해석하는 과정, 근거를 보강하는 추가 query, 불확실성을 드러내는 caveat 등이 빠지기 쉽습니다.</p>",
            )
        with right:
            card(
                "q → Z → R → y 관점의 장점",
                "<p>각 단계를 분리해서 보면 <strong>어디서 실패했는지</strong>를 더 잘 볼 수 있습니다."
                " 예를 들어 SQL은 실행됐지만 report가 unsupported claim을 말한다면, 문제는 generation이 아니라 interpretation 단계에 있습니다.</p>",
            )

        st.markdown("### 6단계를 하나씩 뜯어보기")
        selected_step = st.selectbox("보고 싶은 단계", list(PIPELINE_STEPS.keys()))
        step = PIPELINE_STEPS[selected_step]

        c1, c2 = st.columns([1, 1])
        with c1:
            card(
                f"{selected_step} · 무엇을 하나?",
                f"<p><strong>목표</strong><br>{step['goal']}</p>"
                f"<p><strong>입력</strong><br>{step['input']}</p>"
                f"<p><strong>출력</strong><br>{step['output']}</p>",
            )
            mini_card("왜 필요한가", step["why"])
            mini_card("초심자 비유", step["analogy"])
        with c2:
            card(
                "예시로 보면",
                f"<p>{step['example']}</p>",
            )
            danger_box(f"<strong>놓치기 쉬운 실패 모드</strong><br>{step['risk']}")

        st.markdown("### 질문 유형이 왜 전체 구조를 바꾸는가")
        t1, t2 = st.columns(2)
        with t1:
            card(
                "Descriptive 질문",
                "<p><strong>예:</strong> '2024년 4분기 총매출은 얼마인가?'</p>"
                "<p><strong>필수 슬롯:</strong> direct answer, key value, relevant granularity</p>"
                "<p><strong>핵심:</strong> 무엇이 얼마인지 정확히 보여주는 것이 우선입니다.</p>",
            )
        with t2:
            card(
                "Diagnostic 질문",
                "<p><strong>예:</strong> '지난 분기 매출이 왜 감소했는가?'</p>"
                "<p><strong>필수 슬롯:</strong> direct answer, trend, segment, driver, caveat</p>"
                "<p><strong>핵심:</strong> 단순 수치가 아니라 설명 구조가 필요합니다.</p>",
            )

    with tabs[1]:
        st.markdown("### 2.3 Part I: Evidence-Bundled NL2SQL")
        callout(
            "<strong>핵심 아이디어</strong><br>"
            "GROVER는 SQL을 하나만 만들지 않습니다. 질문을 설명하는 데 필요한 <strong>증거 묶음(bundle)</strong>을 함께 만듭니다."
        )

        left, right = st.columns(2)
        with left:
            card(
                "왜 single SQL로 부족한가",
                "<p>질문이 '왜 감소했는가?'라면, 전체 감소율 하나만 알아서는 부족합니다.</p>"
                "<ul>"
                "<li>시간에 따라 계속 줄었는가? (trend)</li>"
                "<li>어느 지역/세그먼트가 크게 줄었는가? (breakdown)</li>"
                "<li>가장 큰 감소 driver는 무엇인가? (driver)</li>"
                "</ul>",
            )
        with right:
            card(
                "bundle이 주는 이점",
                "<p>support SQL을 미리 확보하면, 보고서는 단순 요약이 아니라 <strong>근거가 연결된 설명</strong>이 됩니다.</p>"
                "<p>즉 SQL bundle은 '쿼리 여러 개'가 아니라 <strong>최종 해석을 위한 evidence plan</strong>입니다.</p>",
            )

        example_mode = st.radio(
            "질문 유형별 bundle 구조",
            ["Descriptive 예시", "Diagnostic 예시"],
            horizontal=True,
        )

        if example_mode == "Descriptive 예시":
            c1, c2 = st.columns([0.95, 1.05])
            with c1:
                mini_card("Main SQL", "직접 답을 주는 query. 예: 특정 분기의 총매출 계산")
                mini_card("Support SQL", "필수는 아니지만 granularity 확인이나 top-k evidence query를 붙일 수 있습니다.")
                st.code(
                    """
-- Main SQL (illustrative)
SELECT SUM(revenue) AS total_revenue
FROM sales
WHERE quarter = '2024-Q4';

-- Optional support SQL
SELECT product_name, SUM(revenue) AS product_revenue
FROM sales
WHERE quarter = '2024-Q4'
GROUP BY product_name
ORDER BY product_revenue DESC
LIMIT 5;
                    """.strip(),
                    language="sql",
                )
            with c2:
                card(
                    "이 구조가 충분한 이유",
                    "<p>Descriptive 질문은 '얼마인가'를 정확히 답하는 것이 핵심입니다. 따라서 main SQL이 질문을 직접 풀면 되고, support SQL은 answer를 더 읽기 쉽게 보조하는 역할입니다.</p>",
                )
                success_box(
                    "<strong>요점</strong><br>Descriptive에서는 support SQL이 선택적이지만, Diagnostic에서는 support SQL이 사실상 핵심 구성요소가 됩니다."
                )
        else:
            c1, c2 = st.columns([0.95, 1.05])
            with c1:
                mini_card("Main SQL", "전분기 대비 KPI 차이나 핵심 타깃 지표를 바로 계산")
                mini_card("Support SQL 1", "시간 추세를 보는 trend query")
                mini_card("Support SQL 2", "지역·제품·세그먼트별 breakdown query")
                mini_card("Support SQL 3", "상위 감소 요인을 찾는 driver query")
                st.code(
                    """
-- Main SQL: overall KPI delta
SELECT quarter, SUM(revenue) AS total_revenue
FROM sales
WHERE quarter IN ('2024-Q1', '2024-Q2')
GROUP BY quarter;

-- Support SQL 1: trend
SELECT month, SUM(revenue) AS monthly_revenue
FROM sales
WHERE month BETWEEN '2024-01' AND '2024-06'
GROUP BY month;

-- Support SQL 2: segment breakdown
SELECT region, customer_segment, SUM(revenue) AS segment_revenue
FROM sales
WHERE quarter IN ('2024-Q1', '2024-Q2')
GROUP BY region, customer_segment;

-- Support SQL 3: top driver
SELECT region, customer_segment, product_family,
       SUM(revenue_q2 - revenue_q1) AS delta
FROM segment_delta_view
GROUP BY region, customer_segment, product_family
ORDER BY delta ASC
LIMIT 5;
                    """.strip(),
                    language="sql",
                )
            with c2:
                card(
                    "왜 이 질문에는 bundle이 사실상 필수인가",
                    "<p>사용자가 '왜'를 묻는 순간, 시스템은 explanation burden을 집니다. 이 burden을 single SQL 하나에 억지로 담으려 하면 답이 얕아지거나 unsupported causal claim이 생기기 쉽습니다.</p>"
                    "<p>반대로 bundle은 explanation을 단계별로 분해합니다. 전체 변화, 추세, 세그먼트, driver가 따로 확보되므로 report도 더 안정적입니다.</p>",
                )
                danger_box(
                    "<strong>주의</strong><br>support SQL은 많을수록 무조건 좋은 것이 아닙니다. 질문 의도와 직접 관련 있는 evidence만 모으는 것이 중요합니다."
                )

        st.markdown("### Candidate generation과 selection은 어떻게 달라지나")
        c3, c4 = st.columns([0.95, 1.05])
        with c3:
            card(
                "candidate 다양성 확보",
                "<ul>"
                "<li><strong>prompt variation</strong>: 다른 지시문으로 후보 생성</li>"
                "<li><strong>decomposition variation</strong>: 질문을 분해하는 방식 변경</li>"
                "<li><strong>retrieval variation</strong>: 다른 schema/value subset 사용</li>"
                "</ul>"
                "<p>핵심은 한 질문에 대해 서로 다른 evidence plan을 가진 bundle 후보를 얻는 것입니다.</p>",
            )
        with c4:
            st.dataframe(TABLES["candidate_table"], hide_index=True, use_container_width=True)
            st.caption("예시 숫자는 설명용입니다. 여기서 GROVER는 SQL-Level만이 아니라 예상 report 품질까지 함께 보고 후보를 고릅니다.")

        success_box(
            "<strong>Part I 한 줄 요약</strong><br>"
            "GROVER의 SQL 단계는 '정답 SQL 맞히기'가 아니라 '최종 설명에 필요한 근거를 체계적으로 확보하기'로 목적이 바뀝니다."
        )

    with tabs[2]:
        st.markdown("### 2.4 Part II: SQL 이후의 Table Data Analysis")
        callout(
            "<strong>중요한 전환</strong><br>"
            "SQL 실행 뒤의 단계는 단순 post-processing이 아닙니다. 실제 사용자는 테이블 자체보다 <strong>테이블의 의미가 풀어진 설명</strong>을 원합니다."
        )

        st.markdown("### 예시 결과 테이블")
        result_tabs = st.tabs(["Trend", "Breakdown", "Driver"])
        with result_tabs[0]:
            st.dataframe(TABLES["trend"], hide_index=True, use_container_width=True)
            st.line_chart(TABLES["trend"].set_index("월"))
        with result_tabs[1]:
            st.dataframe(TABLES["breakdown"], hide_index=True, use_container_width=True)
        with result_tabs[2]:
            st.dataframe(TABLES["driver"], hide_index=True, use_container_width=True)

        st.markdown("### 왜 결과 테이블을 바로 보여주면 부족한가")
        c1, c2 = st.columns(2)
        with c1:
            card(
                "테이블만 보여줄 때의 문제",
                "<ul>"
                "<li>사용자가 어떤 숫자가 중요한지 스스로 해석해야 합니다.</li>"
                "<li>숫자와 의미의 연결이 약하면 decision-making에 바로 쓰기 어렵습니다.</li>"
                "<li>모델이 어떤 evidence를 근거로 어떤 문장을 말했는지 추적이 어렵습니다.</li>"
                "</ul>",
            )
        with c2:
            card(
                "Structured report가 주는 장점",
                "<ul>"
                "<li>답을 direct answer / supporting claims / caveat로 분리합니다.</li>"
                "<li>각 claim을 어떤 result table이 뒷받침하는지 연결하기 쉬워집니다.</li>"
                "<li>나중에 metric으로 평가할 때 claim 단위 검증이 가능합니다.</li>"
                "</ul>",
            )

        report_box(
            direct_answer="지난 분기 매출 감소의 주된 원인은 북미 지역 Enterprise 세그먼트 부진입니다.",
            claims=[
                "북미 Enterprise 매출은 전분기 대비 37.5% 감소했습니다.",
                "6개월 추세를 보면 4월 이후 월별 매출이 지속적으로 하락했습니다.",
                "북미 Enterprise 감소분이 전체 감소액의 가장 큰 비중을 차지했습니다.",
            ],
            caveat="프로모션 종료나 가격 정책 변화 같은 외부 요인은 현재 결과 테이블만으로 직접 검증되지 않습니다.",
        )

        st.markdown("### claim 단위 검증은 어떻게 하나")
        st.dataframe(TABLES["claims"], hide_index=True, use_container_width=True)

        claim_focus = st.radio(
            "claim 유형별로 직관 보기",
            ["numeric", "comparison", "ranking", "diagnostic"],
            horizontal=True,
        )
        if claim_focus == "numeric":
            success_box(
                "<strong>Numeric claim</strong><br>"
                "예: '북미 Enterprise 매출은 37.5% 감소했다.'<br>"
                "→ 표의 두 값을 꺼내 직접 계산하면 됩니다. 가장 deterministic하게 검증 가능한 claim입니다."
            )
        elif claim_focus == "comparison":
            success_box(
                "<strong>Comparison claim</strong><br>"
                "예: '북미 감소폭이 유럽보다 더 크다.'<br>"
                "→ 두 그룹의 delta를 비교하면 됩니다. 값 자체보다 관계를 검증합니다."
            )
        elif claim_focus == "ranking":
            success_box(
                "<strong>Ranking claim</strong><br>"
                "예: '가장 큰 감소 요인은 북미 Enterprise이다.'<br>"
                "→ 정렬 결과에서 top-1이 맞는지 확인합니다."
            )
        else:
            success_box(
                "<strong>Diagnostic claim</strong><br>"
                "예: '주된 원인은 북미 Enterprise 부진이다.'<br>"
                "→ 숫자 evidence는 존재하지만, '원인'이라는 해석이 섞여 있습니다. 따라서 테이블 근거 + LLM judge + human audit를 함께 쓰는 hybrid 검증이 필요합니다."
            )

        danger_box(
            "<strong>좋아 보이지만 위험한 문장 예시</strong><br>"
            "'매출 감소는 가격 정책 실패 때문입니다.'<br>"
            "현재 결과 테이블에 가격 정책 관련 컬럼이나 실험 근거가 없다면, 이 문장은 그럴듯해 보여도 table-grounded하지 않습니다. GROVER는 이런 unsupported claim을 낮게 평가하려고 합니다."
        )

        success_box(
            "<strong>Part II 한 줄 요약</strong><br>"
            "GROVER에서 report generation은 단순 요약이 아니라, <strong>검증 가능한 claim 구조를 만드는 단계</strong>입니다."
        )

    with tabs[3]:
        st.markdown("### 2.5 Part III: GROVER Metric")
        callout(
            "<strong>설계 철학</strong><br>"
            "1) SQL correctness만 보지 않는다. 2) judge-only metric에만 의존하지 않는다. 3) table-grounded verification을 우선한다. 4) 질문 유형에 따라 필요한 insight를 다르게 본다. 5) 결국 사람 판단과의 정렬을 확인한다."
        )

        level_tabs = st.tabs(["Level 1 · SQL", "Level 2 · DB", "Level 3 · Insight"])
        with level_tabs[0]:
            st.markdown("#### SQL-Level")
            st.latex(r"S_{\text{sql}} = \alpha_1 \cdot EX + \alpha_2 \cdot TS + \alpha_3 \cdot SF1")
            card(
                "초심자용 해석",
                "<p>이 score는 <strong>쿼리 자체가 얼마나 맞는가</strong>를 말합니다. Execution Accuracy는 실제 실행 결과가 맞는지, Test Suite는 semantic equivalence를 더 넓게 보는지, Soft F1은 결과 유사도를 부드럽게 재는지에 가깝습니다.</p>"
                "<p>여기서 EM은 보조 지표로 남기고 main score에서는 비중을 낮게 둡니다. 이유는 표면 형태가 달라도 의미상 같은 SQL이 많기 때문입니다.</p>",
            )

        with level_tabs[1]:
            st.markdown("#### DB-Level")
            st.latex(r"S_{\text{db}} = \beta_1 \cdot \widetilde{RVES} + \beta_2 \cdot (1-\widetilde{Retry}) + \beta_3 \cdot (1-\widetilde{Calls})")
            card(
                "초심자용 해석",
                "<p>이 score는 <strong>시스템이 얼마나 효율적으로 움직이는가</strong>를 봅니다. 같은 품질의 report를 만든다면, 더 적은 DB 호출과 더 적은 retry로 끝내는 시스템이 실무적입니다.</p>"
                "<p>즉 DB-Level은 단순 성능이 아니라, agentic workflow의 비용 구조를 보는 층입니다.</p>",
            )

        with level_tabs[2]:
            st.markdown("#### Insight-Level")
            st.markdown("##### (1) Table-Grounded Precision / Recall / F1")
            st.latex(r"TG\text{-}P = \frac{\sum_{c \in \hat{C}} \mathbb{1}[c \vdash R]}{|\hat{C}|}")
            st.latex(r"TG\text{-}R = \frac{\sum_{c^* \in C^*} \mathbb{1}[c^*\ \text{is covered by}\ y]}{|C^*|}")
            st.latex(r"TG\text{-}F1 = \frac{2 \cdot TG\text{-}P \cdot TG\text{-}R}{TG\text{-}P + TG\text{-}R}")
            mini_card("직관", "모델이 말한 claim 중 실제 표로 지지되는 비율(TG-P)과, 꼭 말했어야 하는 claim을 얼마나 빠짐없이 말했는지(TG-R)를 함께 봅니다.")

            st.markdown("##### (2) Numeric Consistency")
            st.latex(r"NumAcc = \frac{\#\ correct\ numerical\ claims}{\#\ all\ numerical\ claims}")
            mini_card("직관", "숫자 하나만 틀려도 보고서 신뢰성이 크게 떨어집니다. 그래서 numeric claim은 따로 강하게 봅니다.")

            st.markdown("##### (3) Question Coverage")
            st.latex(r"Cov = \frac{\#\ required\ slots\ addressed}{\#\ required\ slots}")
            mini_card("직관", "질문에 꼭 필요한 요소를 빠뜨리면 자연스러워 보여도 좋은 답이 아닙니다. diagnostic 질문인데 trend나 driver가 없으면 coverage가 낮아집니다.")

            st.markdown("##### (4) Intent Alignment")
            st.latex(r"IA \in [0,1]")
            mini_card("직관", "질문이 descriptive인데 과한 추천을 늘어놓거나, diagnostic인데 숫자만 던지는 식의 mismatch를 잡아냅니다.")

            st.markdown("##### (5) 종합 score")
            st.latex(r"S_{\text{insight}} = \gamma_1 \cdot TG\text{-}F1 + \gamma_2 \cdot NumAcc + \gamma_3 \cdot Cov + \gamma_4 \cdot IA")
            mini_card("문서의 기본 가중치", "γ₁=0.35, γ₂=0.30, γ₃=0.20, γ₄=0.15. 즉 groundedness와 numeric correctness를 가장 중요하게 둡니다.")

        st.markdown("### 직접 만져보는 Insight Score 샌드박스")
        preset = st.selectbox(
            "예시 시나리오",
            [
                "균형 잡힌 좋은 report",
                "숫자 실수가 있는 report",
                "핵심 슬롯을 빠뜨린 report",
                "의도와 안 맞는 report",
            ],
        )

        defaults = {
            "균형 잡힌 좋은 report": (0.84, 0.90, 0.85, 0.82),
            "숫자 실수가 있는 report": (0.78, 0.42, 0.80, 0.77),
            "핵심 슬롯을 빠뜨린 report": (0.76, 0.88, 0.45, 0.80),
            "의도와 안 맞는 report": (0.72, 0.85, 0.70, 0.35),
        }
        d_tg, d_num, d_cov, d_ia = defaults[preset]

        s1, s2, s3, s4 = st.columns(4)
        with s1:
            tg_f1 = st.slider("TG-F1", 0.0, 1.0, float(d_tg), 0.01)
        with s2:
            num_acc = st.slider("NumAcc", 0.0, 1.0, float(d_num), 0.01)
        with s3:
            cov = st.slider("Coverage", 0.0, 1.0, float(d_cov), 0.01)
        with s4:
            ia = st.slider("Intent Alignment", 0.0, 1.0, float(d_ia), 0.01)

        with st.expander("가중치 조정하기"):
            w1 = st.slider("γ₁ · TG-F1 비중", 0, 100, 35, 1)
            w2 = st.slider("γ₂ · NumAcc 비중", 0, 100, 30, 1)
            w3 = st.slider("γ₃ · Coverage 비중", 0, 100, 20, 1)
            w4 = st.slider("γ₄ · IA 비중", 0, 100, 15, 1)
            weights = normalize_weights([w1, w2, w3, w4])
        if "weights" not in locals():
            weights = (0.35, 0.30, 0.20, 0.15)

        insight_score = compute_insight_score(tg_f1, num_acc, cov, ia, weights)
        sql_score = st.slider("예시 SQL-Level score", 0.0, 1.0, 0.88, 0.01)
        db_score = st.slider("예시 DB-Level score", 0.0, 1.0, 0.74, 0.01)

        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("S_sql", f"{sql_score:.2f}")
        with m2:
            st.metric("S_db", f"{db_score:.2f}")
        with m3:
            st.metric("S_insight", f"{insight_score:.2f}")

        score_df = pd.DataFrame(
            {
                "component": ["SQL-Level", "DB-Level", "Insight-Level"],
                "score": [sql_score, db_score, insight_score],
            }
        ).set_index("component")
        st.bar_chart(score_df)

        weakest = min(
            {
                "TG-F1": tg_f1,
                "NumAcc": num_acc,
                "Coverage": cov,
                "Intent Alignment": ia,
            }.items(),
            key=lambda x: x[1],
        )[0]
        callout(
            f"<strong>현재 샌드박스 해석</strong><br>"
            f"가장 약한 요소는 <strong>{weakest}</strong>입니다. GROVER의 장점은 최종 점수만 보는 것이 아니라, 어느 축이 약한지까지 분해해서 보여준다는 점입니다."
        )

        success_box(
            "<strong>Part III 한 줄 요약</strong><br>"
            "GROVER metric은 '그럴듯함'을 재는 것이 아니라, <strong>표에 근거한 claim인가 · 숫자가 맞는가 · 중요한 요소를 빠뜨리지 않았는가 · 질문 의도에 맞는가</strong>를 따로 나눠서 봅니다."
        )

    with tabs[4]:
        st.markdown("### 2.6 Part IV: Human-verified Evaluation Protocol")
        callout(
            "<strong>왜 사람 검증이 필요한가</strong><br>"
            "benchmark에 annotation noise와 ambiguous question이 존재할 수 있기 때문에, 자동 metric만으로 논문을 밀어붙이면 설득력이 약해질 수 있습니다."
        )

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            step_box(1, "샘플링", "BIRD/CORGI에서 150~200개 정도를 골라 human-verified subset을 만듭니다.")
        with c2:
            step_box(2, "이중 annotation", "2인이 독립적으로 question type, gold support evidence, gold claim set 등을 라벨링합니다.")
        with c3:
            step_box(3, "조정(adjudication)", "불일치 사례를 합의해 최종 gold를 만듭니다.")
        with c4:
            step_box(4, "상관 분석", "GROVER-Insight가 사람의 factual correctness/usefulness/completeness와 얼마나 맞는지 봅니다.")

        annotation_df = pd.DataFrame(
            {
                "annotation 항목": [
                    "question type",
                    "acceptable SQL family",
                    "gold support evidence",
                    "gold atomic claim set",
                    "required analytical slots",
                    "ambiguity / abstention label",
                ],
                "왜 필요한가": [
                    "descriptive와 diagnostic의 요구가 다르기 때문",
                    "정답 SQL이 하나만이 아닐 수 있기 때문",
                    "어떤 evidence가 정말 필요한지 분명히 하기 위해",
                    "report를 claim 단위로 검증하기 위해",
                    "coverage를 공정하게 재기 위해",
                    "애매한 질문을 억지로 단정하지 않기 위해",
                ],
            }
        )
        st.dataframe(annotation_df, hide_index=True, use_container_width=True)

        left, right = st.columns(2)
        with left:
            card(
                "사람 평가 축",
                "<ul>"
                "<li><strong>factual correctness</strong>: 사실과 수치가 맞는가</li>"
                "<li><strong>usefulness</strong>: 실제 의사결정에 쓸 만한가</li>"
                "<li><strong>completeness</strong>: 핵심 요소를 빠뜨리지 않았는가</li>"
                "</ul>",
            )
        with right:
            card(
                "이 파트가 논문에 주는 힘",
                "<p>GROVER가 generic judge나 vanilla metric보다 사람 판단과 더 잘 맞는다는 것을 보이면, '왜 table-specific redesign이 필요한가'를 강하게 설득할 수 있습니다.</p>",
            )

        danger_box(
            "<strong>이 파트가 없으면 생길 수 있는 문제</strong><br>"
            "자동 metric이 높은 점수를 준 답변이 실제로는 사람에게 쓸모없을 수도 있습니다. 사람 정렬 검증은 이 위험을 줄여 줍니다."
        )

        success_box(
            "<strong>Part IV 한 줄 요약</strong><br>"
            "GROVER-Bridge는 자동 metric의 '현실 감각'을 점검하는 안전장치입니다."
        )

    with tabs[5]:
        st.markdown("### Diagnostic 질문 하나를 끝까지 따라가 보기")
        callout(
            "<strong>예시 질문</strong><br>지난 분기 매출이 왜 감소했는가?"
        )

        walkthrough = st.tabs(
            [
                "1) Typing",
                "2) Retrieval",
                "3) SQL Bundle",
                "4) Execution Results",
                "5) Structured Report",
                "6) Evaluation",
            ]
        )

        with walkthrough[0]:
            card(
                "질문 유형 분류",
                "<p>이 질문은 단순히 숫자를 묻는 것이 아니라 <strong>'이유'</strong>를 묻습니다. 따라서 type은 <strong>diagnostic</strong>입니다.</p>"
                "<p>이 한 번의 분류가 뒤 단계 전부를 바꿉니다. 이후 시스템은 direct answer만이 아니라 trend, segment, driver, caveat를 준비해야 합니다.</p>",
            )

        with walkthrough[1]:
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("#### 회수한 schema")
                st.code(
                    """
Tables:
- sales
- customers
- regions
- product_catalog

Relevant columns:
- order_date
- quarter
- revenue
- region
- customer_segment
- product_family
                    """.strip(),
                    language="text",
                )
            with c2:
                card(
                    "왜 이렇게 좁히는가",
                    "<p>문제와 직접 상관없는 컬럼까지 전부 넣으면 모델이 산만해집니다. retrieval은 단순 속도 개선이 아니라 <strong>정확도 개선</strong>에도 중요합니다.</p>",
                )

        with walkthrough[2]:
            st.code(
                """
Main SQL      : 분기별 총매출 차이 계산
Support SQL 1 : 최근 6개월 월별 추세 계산
Support SQL 2 : 지역 × 세그먼트별 감소폭 계산
Support SQL 3 : 감소액 기준 top driver 정렬
                """.strip(),
                language="text",
            )
            card(
                "여기서의 포인트",
                "<p>이 bundle은 각각 다른 질문에 답합니다.</p>"
                "<ul>"
                "<li>Main SQL → 정말 감소했는가?</li>"
                "<li>Trend → 일시적 하락인가 지속 하락인가?</li>"
                "<li>Breakdown → 어느 그룹에서 크게 줄었는가?</li>"
                "<li>Driver → 가장 설명력이 큰 요인은 무엇인가?</li>"
                "</ul>",
            )

        with walkthrough[3]:
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("#### Trend 결과")
                st.dataframe(TABLES["trend"], hide_index=True, use_container_width=True)
            with c2:
                st.markdown("#### Breakdown 결과")
                st.dataframe(TABLES["breakdown"], hide_index=True, use_container_width=True)
            st.markdown("#### Driver 결과")
            st.dataframe(TABLES["driver"], hide_index=True, use_container_width=True)

        with walkthrough[4]:
            report_box(
                direct_answer="지난 분기 매출 감소는 북미 Enterprise 세그먼트 부진이 가장 큰 원인으로 보입니다.",
                claims=[
                    "북미 Enterprise 매출은 전분기 대비 37.5% 감소했습니다.",
                    "전체 월별 매출은 4월 이후 지속적으로 하락했습니다.",
                    "북미 Enterprise 감소액이 다른 지역·세그먼트보다 가장 큽니다.",
                ],
                caveat="가격 정책 변화나 외부 시장 충격은 현재 결과 테이블만으로 직접 검증되지 않으므로, '원인' 해석은 이 범위 안에서만 유효합니다.",
            )
            success_box(
                "<strong>좋은 report의 특징</strong><br>"
                "답을 하나의 문장으로 끝내지 않고, 숫자 evidence와 caveat를 함께 제시합니다. 그래서 사용자는 '무슨 말인지'와 '왜 그렇게 말했는지'를 동시에 볼 수 있습니다."
            )

        with walkthrough[5]:
            eval_df = pd.DataFrame(
                {
                    "평가 항목": ["TG-F1", "NumAcc", "Coverage", "IA", "S_insight"],
                    "예시 값": [0.86, 0.92, 0.80, 0.84, 0.86 * 0.35 + 0.92 * 0.30 + 0.80 * 0.20 + 0.84 * 0.15],
                    "해석": [
                        "대부분의 claim이 table-grounded됨",
                        "수치 claim이 거의 정확함",
                        "diagnostic에 필요한 슬롯 대부분을 충족",
                        "질문 의도와 잘 맞음",
                        "최종 Insight-Level 종합 점수",
                    ],
                }
            )
            st.dataframe(eval_df, hide_index=True, use_container_width=True)
            danger_box(
                "<strong>single SQL baseline과의 차이</strong><br>"
                "single SQL baseline은 '매출이 12% 감소했다' 정도는 맞힐 수 있어도, trend·breakdown·driver를 분리해서 보여주지 못할 가능성이 큽니다. 그 결과 Coverage와 IA가 떨어질 수 있습니다."
            )

        success_box(
            "<strong>Methodology 전체 요약</strong><br>"
            "GROVER는 SQL을 더 화려하게 만드는 프레임워크가 아니라, <strong>좋은 분석 보고서를 만들기 위해 필요한 근거를 모으고, 그 근거 위에서만 말하게 만드는 프레임워크</strong>입니다."
        )



def render_experimental() -> None:
    st.markdown("## 3. Experimental")
    callout(
        "<strong>실험의 목적</strong><br>"
        "이 파트는 'GROVER가 정말 가치가 있는가?'를 보이기 위한 설계입니다. 핵심은 SQL-level 점수가 비슷해도 insight-level ranking이 달라질 수 있다는 점을 실험으로 보여주는 것입니다."
    )

    tabs = st.tabs(["연구 질문", "데이터셋 전략", "모델/환경", "Baseline & Ablation"])

    with tabs[0]:
        r1, r2, r3 = st.columns(3)
        with r1:
            card(
                "RQ1",
                "<p><strong>Evidence-bundled pipeline</strong>은 single-SQL baseline보다 Insight-Level quality를 높이는가?</p>"
                "<p><strong>가설:</strong> SQL accuracy가 비슷해도 support SQL과 report-aware selection이 insight를 개선할 것입니다.</p>",
            )
        with r2:
            card(
                "RQ2",
                "<p><strong>GROVER-Insight</strong>는 generic judge나 vanilla metric보다 사람 판단과 더 잘 정렬되는가?</p>"
                "<p><strong>가설:</strong> claim decomposition + numeric verification이 더 높은 human correlation을 보일 것입니다.</p>",
            )
        with r3:
            card(
                "RQ3",
                "<p><strong>SQL-Level ranking</strong>과 <strong>end-to-end report ranking</strong>은 일치하는가?</p>"
                "<p><strong>가설:</strong> 같은 SQL-Level score여도 Insight-Level은 크게 달라질 수 있습니다.</p>",
            )

    with tabs[1]:
        st.dataframe(TABLES["datasets"], hide_index=True, use_container_width=True)
        left, right = st.columns(2)
        with left:
            card(
                "왜 benchmark를 섞어 쓰는가",
                "<p>문서의 제안은 단일 benchmark로 모든 걸 보려 하지 않습니다. SQL correctness, business-domain insight, human alignment는 서로 다른 역할을 가지므로 benchmark를 분업적으로 씁니다.</p>",
            )
        with right:
            card(
                "실전 우선순위",
                "<p>학기 프로젝트나 빠른 프로토타입이라면 <strong>BIRD Mini-Dev V2 → CORGI subset → GROVER-Bridge</strong> 순으로 가는 것이 현실적입니다.</p>",
            )

    with tabs[2]:
        m1, m2, m3 = st.columns(3)
        with m1:
            card(
                "SQL generation용",
                "<p>문서에서는 Qwen2.5-Coder-7B-Instruct, Qwen2.5-7B-Instruct 같은 4B~8B급 open-weight 모델을 현실적인 선택지로 둡니다.</p>",
            )
        with m2:
            card(
                "Reporter / Judge용",
                "<p>Gemma 3 4B IT, Phi-4-mini-instruct처럼 결과 테이블과 긴 context를 읽을 수 있는 소형 모델을 report/judge 역할에 배치합니다.</p>",
            )
        with m3:
            card(
                "환경 세팅",
                "<p>Colab, 4-bit quantization, LoRA/QLoRA, SQLite 우선, candidate 수 3~5개, diagnostic support SQL 최대 3개 정도가 시작점으로 제안됩니다.</p>",
            )
        success_box(
            "<strong>실무적인 장점</strong><br>"
            "문서는 지나치게 큰 모델 대신 Colab에서 돌아갈 수 있는 실험 구성을 제안합니다. 즉 아이디어의 가치는 규모보다 framing과 metric 설계에 놓여 있습니다."
        )

    with tabs[3]:
        st.dataframe(TABLES["baselines"], hide_index=True, use_container_width=True)
        st.markdown("### 추천 ablation")
        a1, a2, a3 = st.columns(3)
        with a1:
            mini_card("support SQL 제거", "bundle 자체가 diagnostic question에서 얼마나 중요한지 검증합니다.")
            mini_card("report-aware selector 제거", "후보 선택 objective의 차이를 검증합니다.")
        with a2:
            mini_card("numeric checker 제거", "숫자 검증 모듈이 얼마나 신뢰성에 기여하는지 봅니다.")
            mini_card("Coverage metric 제거", "핵심 slot 개념이 왜 필요한지 확인합니다.")
        with a3:
            mini_card("diagnostic → descriptive 축소", "문제 난도가 어떻게 달라지는지 비교합니다.")
            mini_card("human subset 제거", "사람 정렬 검증 없이도 주장이 유지되는지 점검합니다.")

        danger_box(
            "<strong>중요한 해석 포인트</strong><br>"
            "논문의 승부처는 SQL score를 조금 더 올리는 데 있지 않습니다. 'SQL 점수는 비슷한데 왜 최종 분석 품질은 달라지는가'를 보여주는 것이 핵심 메시지입니다."
        )



def render_conclusion() -> None:
    st.markdown("## 4. Conclusion")
    st.markdown(
        """
        <div class="hero" style="padding-top:1.5rem; padding-bottom:1.35rem;">
            <div class="eyebrow">TAKEAWAYS</div>
            <h1 style="font-size:1.9rem;">이 문서에서 꼭 기억할 다섯 가지</h1>
            <p>연구의 중심은 새로운 SQL generator 경쟁이 아니라, NL2SQL 기반 데이터 분석 시스템을 <strong>어떻게 공정하고 유의미하게 평가할 것인가</strong>에 있습니다.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)
    with c1:
        mini_card("1. 문제 재정의", "NL2SQL은 더 이상 q → SQL 하나의 문제가 아니라, q → SQL bundle → execution result → report의 end-to-end 문제입니다.")
        mini_card("2. SQL bundle의 필요성", "특히 diagnostic 질문은 trend / breakdown / driver evidence가 필요하므로 support SQL이 중요합니다.")
        mini_card("3. report는 별도 연구 대상", "좋은 시스템은 결과 테이블을 던지는 것이 아니라, 검증 가능한 structured report를 생성해야 합니다.")
    with c2:
        mini_card("4. Insight-Level이 핵심 novelty", "TG-F1, NumAcc, Coverage, Intent Alignment를 함께 보아야 최종 분석 품질을 재볼 수 있습니다.")
        mini_card("5. 사람 정렬 검증이 중요", "GROVER-Bridge 같은 human-verified subset이 있어야 metric의 설득력이 커집니다.")

    st.markdown("### 자주 생길 오해 정리")
    faq1, faq2 = st.columns(2)
    with faq1:
        card(
            "이 연구는 새 SQL model 논문인가?",
            "<p>아니요. 문서의 framing상 중심 기여는 <strong>evaluation framework와 metric</strong>입니다. SQL bundle 시스템은 이 아이디어를 검증하기 위한 시스템 기여에 가깝습니다.</p>",
        )
    with faq2:
        card(
            "왜 scalar score 하나로 끝내지 않는가?",
            "<p>SQL, DB efficiency, Insight quality는 서로 다른 실패 양상을 가집니다. 그래서 기본 출력은 <strong>score vector</strong>로 두는 편이 분석적으로 더 유용합니다.</p>",
        )

    success_box(
        "<strong>최종 한 문장</strong><br>"
        "GROVER는 '맞는 쿼리'보다 한 단계 더 나아가, <strong>근거 있는 분석 보고서</strong>를 만드는 NL2SQL 시스템을 평가하려는 프레임워크입니다."
    )



def render_appendix() -> None:
    st.markdown("## Appendix")
    st.markdown("### 용어집")
    st.dataframe(TABLES["glossary"], hide_index=True, use_container_width=True)

    st.markdown("### 처음 구현할 때의 우선순위")
    c1, c2, c3 = st.columns(3)
    with c1:
        step_box(1, "작게 시작", "Descriptive와 diagnostic을 먼저 분리하고, diagnostic subset에 집중합니다.")
    with c2:
        step_box(2, "구조부터 만들기", "자유 생성보다 structured report 포맷을 먼저 고정합니다.")
    with c3:
        step_box(3, "평가 먼저 설계", "나중에 보겠다고 미루지 말고 TG-F1, NumAcc, Coverage 구조를 초기에 잡습니다.")

    st.markdown("### 원문 보기")
    if RAW_DOCUMENT:
        with st.expander("업로드된 원문 markdown 열기"):
            st.code(RAW_DOCUMENT, language="markdown")
    else:
        st.info("앱과 같은 폴더에서 원문 파일을 찾지 못했습니다. 그래도 이 앱은 자체 설명만으로 동작합니다.")

    st.markdown(
        '<p class="footer-note">이 앱은 업로드된 프로젝트 문서를 바탕으로, 초심자 친화적 설명과 시각적 구조를 추가한 해설 버전입니다. 예시 SQL과 표는 이해를 돕기 위한 illustrative example이며, 실제 실험 결과를 주장하지 않습니다.</p>',
        unsafe_allow_html=True,
    )


# -----------------------------
# Main app
# -----------------------------


def main() -> None:
    inject_css()

    st.sidebar.markdown(
        """
        <div class="sidebar-brand">
            <div class="sidebar-kicker">GROVER Explainer</div>
            <h2>From SQL to Reporting</h2>
            <p>문서 내용을 설명용 인터랙티브 페이지로 다시 엮었습니다. 핵심은 Methodology와 Insight-Level metric입니다.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section = st.sidebar.radio(
        "Sections",
        [
            "개요",
            "Introduction",
            "Methodology",
            "Experimental",
            "Conclusion",
        ],
    )

    st.sidebar.markdown(
        '<div class="sidebar-note"><strong>앱의 성격</strong><br>설명 목적 앱이며, 예시 수치와 SQL은 이해를 돕기 위한 illustrative content입니다.</div>',
        unsafe_allow_html=True,
    )

    if section == "개요":
        render_home()
    elif section == "Introduction":
        render_introduction()
    elif section == "Methodology":
        render_methodology()
    elif section == "Experimental":
        render_experimental()
    elif section == "Conclusion":
        render_conclusion()


if __name__ == "__main__":
    main()
