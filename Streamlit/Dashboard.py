import streamlit as st
import pandas as pd
from datetime import datetime

hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""

st.set_page_config(
    page_title="LINAW: Ledger for Integrity, Neutrality, and Accountability on the Web",
    page_icon="💡",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-top: 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🔗 LINAW Blockchain AIS</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Ledger for Integrity, Neutrality, and Accountability on the Web</p>', unsafe_allow_html=True)
st.markdown("---")

# Introduction
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📊 Dashboard Overview")
    st.write("""
    Welcome to the **Blockchain Initiative LINAW** - a transparent, secure, and accountable 
    financial management system for Barangay/LGU operations. This proof-of-concept demonstrates 
    how blockchain technology can revolutionize public sector accounting.
    """)
    
    st.subheader("🎯 Key Features")
    st.write("""
    - **Real-time Financial Tracking**: Monitor income, expenses, and budgets
    - **Blockchain Transparency**: All transactions recorded on immutable ledger
    - **Public Accountability**: Citizens can verify financial documents
    - **Comprehensive Reporting**: Balance sheets, ledgers, and financial statements
    """)

with col2:
    st.subheader("📅 System Information")
    st.info(f"""
    **Current Date**: {datetime.now().strftime('%B %d, %Y')}
    
    **System Status**: 🟢 Active
    
    **Blockchain Network**: LINAW Chain
    
    **Last Sync**: {datetime.now().strftime('%H:%M:%S')}
    """)

st.markdown("---")

# Quick Stats
st.subheader("💰 Financial Summary (Current Month)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Assets", value="₱2,450,000", delta="5.2%")
with col2:
    st.metric(label="Total Income", value="₱850,000", delta="12.3%")
with col3:
    st.metric(label="Total Expenses", value="₱620,000", delta="-3.1%")
with col4:
    st.metric(label="Net Position", value="₱230,000", delta="18.5%")

st.markdown("---")

# Navigation Guide
st.header("🧭 System Navigation")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📒 Accounting")
    st.write("""
    Access comprehensive financial records including:
    - Balance Sheet
    - General Ledger
    - Journal Entries
    """)
    
    st.subheader("📈 Income & Expenses")
    st.write("""
    View detailed income and expense analysis:
    - Monthly summaries
    - Category breakdowns
    - Visual charts and trends
    """)

with col2:
    st.subheader("🔍 Blockchain Public View")
    st.write("""
    Transparent access to public documents:
    - Ordinances
    - Infrastructure Projects
    - Financial Reports
    - Blockchain verification
    """)
    
    st.subheader("🔐 Security Features")
    st.write("""
    - Immutable transaction records
    - Cryptographic verification
    - Audit trails
    - Public transparency
    """)

st.markdown("---")

# Recent Activity
st.header("🕒 Recent Blockchain Activity")
recent_activity = pd.DataFrame({
    'Timestamp': [
        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        '2025-11-02 10:30:15',
        '2025-11-02 09:15:42',
        '2025-11-02 08:45:20'
    ],
    'Transaction Type': ['Financial Report', 'Expense Entry', 'Income Entry', 'Ordinance'],
    'Document ID': ['FR-2025-034', 'EXP-2025-892', 'INC-2025-445', 'ORD-2025-012'],
    'Status': ['✅ Verified', '✅ Verified', '✅ Verified', '✅ Verified'],
    'Block Hash': [
        '0x7a3f8b2e...',
        '0x9c4d1f7a...',
        '0x2e8b5c3a...',
        '0x6f1a9d4b...'
    ]
})

st.dataframe(recent_activity, use_container_width=True, hide_index=True)

st.markdown("---")
st.caption("© 2025 Blockchain Initiative LINAW - Barangay/LGU Transparency Project")