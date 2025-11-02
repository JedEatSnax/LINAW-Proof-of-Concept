import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Blockchain Public View - LINAW AIS", page_icon="🔍", layout="wide")

st.title("🔍 Blockchain Public Document View")
st.markdown("Transparent access to verified barangay/LGU documents")
st.markdown("---")

# Search and Filter
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    search_query = st.text_input("🔎 Search documents", placeholder="Enter document title or ID...")
with col2:
    doc_type_filter = st.selectbox("Document Type", ["All", "Ordinance", "Infrastructure", "Financial Reports", "Resolution", "Procurement"])
with col3:
    date_filter = st.date_input("From Date", datetime(2025, 1, 1))

st.markdown("---")

# Sample Document Database
documents = [
    {
        'type': 'Financial Reports',
        'id': 'FR-2025-034',
        'title': 'Quarterly Financial Statement - Q3 2025',
        'date': '2025-10-15',
        'status': '✅ Verified',
        'hash': '0x7a3f8b2e4c5d6f1a9b8c7d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a',
        'details': 'Comprehensive financial statement for Q3 2025 including balance sheet, income statement, and cash flow analysis.',
        'amount': '₱850,000',
        'prepared_by': 'Maria Santos, Municipal Accountant',
        'verified_by': 'Hon. Juan dela Cruz, Barangay Captain'
    },
    {
        'type': 'Ordinance',
        'id': 'ORD-2025-012',
        'title': 'Barangay Solid Waste Management Ordinance',
        'date': '2025-09-20',
        'status': '✅ Verified',
        'hash': '0x6f1a9d4b3c2e5f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a',
        'details': 'Ordinance implementing comprehensive solid waste management program in accordance with RA 9003.',
        'amount': 'N/A',
        'prepared_by': 'Barangay Council',
        'verified_by': 'Hon. Juan dela Cruz, Barangay Captain'
    },
    {
        'type': 'Infrastructure',
        'id': 'INFRA-2025-008',
        'title': 'Multi-Purpose Hall Construction Project',
        'date': '2025-08-10',
        'status': '✅ Verified',
        'hash': '0x2e8b5c3a6d4f9a1b7c8d0e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b',
        'details': 'Construction project for a 200-capacity multi-purpose hall for community events and disaster evacuation.',
        'amount': '₱2,500,000',
        'prepared_by': 'Engineering Office',
        'verified_by': 'Hon. Juan dela Cruz, Barangay Captain'
    },
    {
        'type': 'Procurement',
        'id': 'PROC-2025-045',
        'title': 'Office Equipment and Supplies Procurement',
        'date': '2025-11-01',
        'status': '✅ Verified',
        'hash': '0x9c4d1f7a2b3e5c8d9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2',
        'details': 'Procurement of computers, printers, and office supplies for barangay hall operations.',
        'amount': '₱175,000',
        'prepared_by': 'Procurement Committee',
        'verified_by': 'Hon. Juan dela Cruz, Barangay Captain'
    },
    {
        'type': 'Resolution',
        'id': 'RES-2025-056',
        'title': 'Resolution Authorizing Budget Allocation for Health Programs',
        'date': '2025-10-28',
        'status': '✅ Verified',
        'hash': '0x1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e',
        'details': 'Resolution approving additional budget for maternal and child health programs for FY 2025.',
        'amount': '₱350,000',
        'prepared_by': 'Barangay Health Committee',
        'verified_by': 'Hon. Juan dela Cruz, Barangay Captain'
    },
    {
        'type': 'Financial Reports',
        'id': 'FR-2025-033',
        'title': 'Monthly Budget Utilization Report - October 2025',
        'date': '2025-10-31',
        'status': '✅ Verified',
        'hash': '0x3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f',
        'details': 'Detailed report on budget utilization for October 2025 showing expenditure vs approved budget.',
        'amount': '₱620,000',
        'prepared_by': 'Maria Santos, Municipal Accountant',
        'verified_by': 'Hon. Juan dela Cruz, Barangay Captain'
    }
]

# Initialize session state for document expansion
if 'expanded_docs' not in st.session_state:
    st.session_state.expanded_docs = set()

# Display Documents Table
st.subheader("📋 Public Documents Registry")

# Create DataFrame
df = pd.DataFrame(documents)

# Apply filters
if doc_type_filter != "All":
    df = df[df['type'] == doc_type_filter]

# Display table with action buttons
for idx, doc in df.iterrows():
    with st.container():
        col1, col2, col3, col4, col5 = st.columns([1.5, 1.2, 2.5, 1, 0.8])
        
        with col1:
            st.write(f"**{doc['type']}**")
        with col2:
            st.code(doc['id'], language=None)
        with col3:
            st.write(doc['title'])
        with col4:
            st.write(doc['date'])
        with col5:
            doc_key = f"{doc['id']}"
            if st.button("View", key=f"view_{idx}"):
                if doc_key in st.session_state.expanded_docs:
                    st.session_state.expanded_docs.remove(doc_key)
                else:
                    st.session_state.expanded_docs.add(doc_key)
        
        # Extended Information (shown when View is clicked)
        if doc_key in st.session_state.expanded_docs:
            with st.expander("📄 Document Details", expanded=True):
                col_a, col_b = st.columns(2)
                
                with col_a:
                    st.markdown(f"**Document ID:** `{doc['id']}`")
                    st.markdown(f"**Document Type:** {doc['type']}")
                    st.markdown(f"**Title:** {doc['title']}")
                    st.markdown(f"**Date Issued:** {doc['date']}")
                    st.markdown(f"**Status:** {doc['status']}")
                    
                with col_b:
                    st.markdown(f"**Amount:** {doc['amount']}")
                    st.markdown(f"**Prepared By:** {doc['prepared_by']}")
                    st.markdown(f"**Verified By:** {doc['verified_by']}")
                    st.markdown(f"**Blockchain Status:** 🔗 Immutable")
                
                st.markdown("---")
                st.markdown("**Description:**")
                st.info(doc['details'])
                
                st.markdown("**Blockchain Transaction Hash:**")
                st.code(doc['hash'], language=None)
                
                st.markdown("**Verification:**")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.success("✅ Document Verified")
                with col2:
                    st.success("✅ Hash Confirmed")
                with col3:
                    st.success("✅ Blockchain Synced")
                
                # Action buttons
                st.markdown("---")
                btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 3])
                with btn_col1:
                    st.button("📥 Download PDF", key=f"download_{idx}")
                with btn_col2:
                    st.button("🔍 View on Explorer", key=f"explorer_{idx}")
        
        st.markdown("---")

# Blockchain Statistics
st.markdown("### 📊 Blockchain Statistics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Documents", "6")
with col2:
    st.metric("Verified Transactions", "6")
with col3:
    st.metric("Block Height", "2,547")
with col4:
    st.metric("Network Status", "🟢 Active")

st.markdown("---")

# Recent Blockchain Activity
st.subheader("🔗 Recent Blockchain Activity")
activity_data = pd.DataFrame({
    'Block #': ['2547', '2546', '2545', '2544', '2543'],
    'Timestamp': [
        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        '2025-11-01 14:23:15',
        '2025-10-31 16:45:30',
        '2025-10-28 10:15:22',
        '2025-10-15 09:30:45'
    ],
    'Transaction Type': ['Procurement', 'Financial Report', 'Financial Report', 'Resolution', 'Financial Report'],
    'Document ID': ['PROC-2025-045', 'FR-2025-034', 'FR-2025-033', 'RES-2025-056', 'FR-2025-034'],
    'Hash': [
        '0x9c4d1f7a...',
        '0x7a3f8b2e...',
        '0x3e4f5a6b...',
        '0x1d2e3f4a...',
        '0x7a3f8b2e...'
    ],
    'Status': ['✅ Confirmed', '✅ Confirmed', '✅ Confirmed', '✅ Confirmed', '✅ Confirmed']
})

st.dataframe(activity_data, use_container_width=True, hide_index=True)

st.markdown("---")

# Information Panel
st.info("""
**🔐 About Blockchain Initiative LINAW**

The LINAW (Ledger for Integrity, Neutrality, and Accountability on the Web) blockchain ensures:
- **Immutability**: Once recorded, documents cannot be altered or deleted
- **Transparency**: All transactions are publicly verifiable
- **Security**: Cryptographic hashing protects document integrity
- **Accountability**: Complete audit trail for all government transactions
- **Trust**: Citizens can independently verify any document

All documents are timestamped and cryptographically secured on the blockchain, ensuring complete transparency and accountability in barangay/LGU operations.
""")

st.markdown("---")
st.caption("© 2025 Blockchain Initiative LINAW - Building Trust Through Transparency")