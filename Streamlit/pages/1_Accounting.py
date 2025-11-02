import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Accounting - LINAW AIS", page_icon="📒", layout="wide")

st.title("📒 Accounting Records")
st.markdown("Comprehensive financial statements and ledger entries")
st.markdown("---")

# Tabs for different accounting views
tab1, tab2, tab3 = st.tabs(["📊 Balance Sheet", "📗 General Ledger", "📝 Journal Entries"])

# Balance Sheet Tab
with tab1:
    st.subheader("Balance Sheet")
    st.caption(f"As of {datetime.now().strftime('%B %d, %Y')}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🏦 Assets")
        assets_data = {
            'Account': [
                'Current Assets',
                '  Cash on Hand',
                '  Cash in Bank',
                '  Accounts Receivable',
                'Fixed Assets',
                '  Land',
                '  Buildings',
                '  Equipment',
                '  Less: Accumulated Depreciation',
                'TOTAL ASSETS'
            ],
            'Amount (₱)': [
                '',
                '125,000',
                '450,000',
                '85,000',
                '',
                '800,000',
                '650,000',
                '425,000',
                '(85,000)',
                '2,450,000'
            ]
        }
        assets_df = pd.DataFrame(assets_data)
        st.dataframe(assets_df, use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("#### 💼 Liabilities & Equity")
        liabilities_data = {
            'Account': [
                'Current Liabilities',
                '  Accounts Payable',
                '  Accrued Expenses',
                'Long-term Liabilities',
                '  Long-term Debt',
                'TOTAL LIABILITIES',
                '',
                "Fund Balance/Equity",
                '  Beginning Balance',
                '  Net Income (Current Period)',
                'TOTAL EQUITY',
                '',
                'TOTAL LIABILITIES & EQUITY'
            ],
            'Amount (₱)': [
                '',
                '145,000',
                '75,000',
                '',
                '500,000',
                '720,000',
                '',
                '',
                '1,500,000',
                '230,000',
                '1,730,000',
                '',
                '2,450,000'
            ]
        }
        liabilities_df = pd.DataFrame(liabilities_data)
        st.dataframe(liabilities_df, use_container_width=True, hide_index=True)

# General Ledger Tab
with tab2:
    st.subheader("General Ledger")
    st.caption("Account transaction details")
    
    # Account selector
    account = st.selectbox(
        "Select Account",
        ["Cash in Bank", "Accounts Receivable", "Revenue", "Operating Expenses"]
    )
    
    # Sample General Ledger Data
    if account == "Cash in Bank":
        gl_data = pd.DataFrame({
            'Date': ['2025-11-01', '2025-11-01', '2025-11-02', '2025-11-02'],
            'Reference': ['JE-2025-101', 'JE-2025-102', 'JE-2025-103', 'JE-2025-104'],
            'Description': ['Tax Collection', 'Equipment Purchase', 'Permit Fees', 'Salary Payment'],
            'Debit (₱)': ['150,000', '', '50,000', ''],
            'Credit (₱)': ['', '75,000', '', '85,000'],
            'Balance (₱)': ['550,000', '475,000', '525,000', '450,000']
        })
    elif account == "Revenue":
        gl_data = pd.DataFrame({
            'Date': ['2025-11-01', '2025-11-02', '2025-11-02', '2025-11-02'],
            'Reference': ['JE-2025-101', 'JE-2025-103', 'JE-2025-105', 'JE-2025-106'],
            'Description': ['Tax Collection', 'Permit Fees', 'Rental Income', 'Service Fees'],
            'Debit (₱)': ['', '', '', ''],
            'Credit (₱)': ['150,000', '50,000', '25,000', '15,000'],
            'Balance (₱)': ['150,000', '200,000', '225,000', '240,000']
        })
    else:
        gl_data = pd.DataFrame({
            'Date': ['2025-11-01', '2025-11-02'],
            'Reference': ['JE-2025-102', 'JE-2025-104'],
            'Description': ['Equipment Purchase', 'Salary Payment'],
            'Debit (₱)': ['75,000', '85,000'],
            'Credit (₱)': ['', ''],
            'Balance (₱)': ['75,000', '160,000']
        })
    
    st.dataframe(gl_data, use_container_width=True, hide_index=True)
    
    # Summary
    st.markdown("#### Account Summary")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Debits", "₱325,000")
    with col2:
        st.metric("Total Credits", "₱240,000")
    with col3:
        st.metric("Current Balance", "₱450,000")

# Journal Entries Tab
with tab3:
    st.subheader("Journal Entries")
    st.caption("Detailed transaction records")
    
    # Date filter
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("From Date", datetime(2025, 11, 1))
    with col2:
        end_date = st.date_input("To Date", datetime.now())
    
    st.markdown("---")
    
    # Sample Journal Entries
    with st.expander("📄 JE-2025-101 - Tax Collection (Nov 1, 2025)", expanded=True):
        je_data = pd.DataFrame({
            'Account': ['Cash in Bank', 'Revenue - Real Property Tax'],
            'Debit (₱)': ['150,000', ''],
            'Credit (₱)': ['', '150,000']
        })
        st.dataframe(je_data, use_container_width=True, hide_index=True)
        st.caption("**Description**: Monthly real property tax collection")
        st.caption("**Blockchain Hash**: `0x7a3f8b2e4c5d6f1a9b8c7d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a`")
    
    with st.expander("📄 JE-2025-102 - Equipment Purchase (Nov 1, 2025)"):
        je_data = pd.DataFrame({
            'Account': ['Equipment', 'Cash in Bank'],
            'Debit (₱)': ['75,000', ''],
            'Credit (₱)': ['', '75,000']
        })
        st.dataframe(je_data, use_container_width=True, hide_index=True)
        st.caption("**Description**: Purchase of office equipment")
        st.caption("**Blockchain Hash**: `0x9c4d1f7a2b3e5c8d9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2`")
    
    with st.expander("📄 JE-2025-103 - Permit Fees (Nov 2, 2025)"):
        je_data = pd.DataFrame({
            'Account': ['Cash in Bank', 'Revenue - Business Permits'],
            'Debit (₱)': ['50,000', ''],
            'Credit (₱)': ['', '50,000']
        })
        st.dataframe(je_data, use_container_width=True, hide_index=True)
        st.caption("**Description**: Business permit fee collection")
        st.caption("**Blockchain Hash**: `0x2e8b5c3a6d4f9a1b7c8d0e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b`")
    
    with st.expander("📄 JE-2025-104 - Salary Payment (Nov 2, 2025)"):
        je_data = pd.DataFrame({
            'Account': ['Salaries Expense', 'Cash in Bank'],
            'Debit (₱)': ['85,000', ''],
            'Credit (₱)': ['', '85,000']
        })
        st.dataframe(je_data, use_container_width=True, hide_index=True)
        st.caption("**Description**: Monthly salary disbursement for barangay staff")
        st.caption("**Blockchain Hash**: `0x6f1a9d4b3c2e5f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a`")

st.markdown("---")
st.caption("All accounting records are secured on the LINAW blockchain")