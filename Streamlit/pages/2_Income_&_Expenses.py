import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="Income & Expenses - LINAW AIS", page_icon="📈", layout="wide")

st.title("📈 Income & Expenses Analysis")
st.markdown("Comprehensive revenue and expenditure tracking")
st.markdown("---")

# Summary Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Income", "₱850,000", "+12.3%")
with col2:
    st.metric("Total Expenses", "₱620,000", "-3.1%")
with col3:
    st.metric("Net Income", "₱230,000", "+18.5%")

st.markdown("---")

# Income and Expense Tabs
tab1, tab2, tab3 = st.tabs(["💰 Income Summary", "💸 Expense Summary", "📊 Comparative Analysis"])

# Income Summary Tab
with tab1:
    st.subheader("Income Summary")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Income by Category
        income_data = pd.DataFrame({
            'Category': ['Real Property Tax', 'Business Permits', 'Market Fees', 'Rental Income', 'Service Fees', 'Other Income'],
            'Amount': [350000, 180000, 125000, 95000, 65000, 35000],
            'Percentage': [41.2, 21.2, 14.7, 11.2, 7.6, 4.1]
        })
        
        fig_income_pie = px.pie(
            income_data, 
            values='Amount', 
            names='Category',
            title='Income Distribution by Category',
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig_income_pie, use_container_width=True)
    
    with col2:
        st.markdown("#### Income Breakdown")
        for idx, row in income_data.iterrows():
            st.write(f"**{row['Category']}**")
            st.progress(row['Percentage'] / 100)
            st.caption(f"₱{row['Amount']:,} ({row['Percentage']}%)")
            st.markdown("")
    
    st.markdown("---")
    
    # Monthly Income Trend
    st.markdown("#### Monthly Income Trend")
    monthly_income = pd.DataFrame({
        'Month': ['July', 'August', 'September', 'October', 'November'],
        'Income': [720000, 765000, 795000, 810000, 850000]
    })
    
    fig_income_trend = px.line(
        monthly_income,
        x='Month',
        y='Income',
        markers=True,
        title='Income Growth Trend (Last 5 Months)'
    )
    fig_income_trend.update_traces(line_color='#2ecc71', marker=dict(size=10))
    st.plotly_chart(fig_income_trend, use_container_width=True)
    
    # Detailed Income Table
    st.markdown("#### Detailed Income Records")
    income_detail = pd.DataFrame({
        'Date': ['2025-11-01', '2025-11-02', '2025-11-02', '2025-11-02', '2025-11-02'],
        'Category': ['Real Property Tax', 'Business Permits', 'Rental Income', 'Service Fees', 'Market Fees'],
        'Description': ['Monthly tax collection', 'New business permits', 'Barangay hall rental', 'Document processing', 'Market stall fees'],
        'Amount (₱)': ['150,000', '50,000', '25,000', '15,000', '35,000'],
        'Transaction ID': ['INC-2025-445', 'INC-2025-446', 'INC-2025-447', 'INC-2025-448', 'INC-2025-449']
    })
    st.dataframe(income_detail, use_container_width=True, hide_index=True)

# Expense Summary Tab
with tab2:
    st.subheader("Expense Summary")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Expense by Category
        expense_data = pd.DataFrame({
            'Category': ['Salaries & Wages', 'Office Supplies', 'Utilities', 'Maintenance', 'Equipment', 'Other Expenses'],
            'Amount': [285000, 95000, 78000, 65000, 75000, 22000],
            'Percentage': [46.0, 15.3, 12.6, 10.5, 12.1, 3.5]
        })
        
        fig_expense_pie = px.pie(
            expense_data,
            values='Amount',
            names='Category',
            title='Expense Distribution by Category',
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_expense_pie, use_container_width=True)
    
    with col2:
        st.markdown("#### Expense Breakdown")
        for idx, row in expense_data.iterrows():
            st.write(f"**{row['Category']}**")
            st.progress(row['Percentage'] / 100)
            st.caption(f"₱{row['Amount']:,} ({row['Percentage']}%)")
            st.markdown("")
    
    st.markdown("---")
    
    # Monthly Expense Trend
    st.markdown("#### Monthly Expense Trend")
    monthly_expense = pd.DataFrame({
        'Month': ['July', 'August', 'September', 'October', 'November'],
        'Expenses': [640000, 625000, 615000, 610000, 620000]
    })
    
    fig_expense_trend = px.line(
        monthly_expense,
        x='Month',
        y='Expenses',
        markers=True,
        title='Expense Trend (Last 5 Months)'
    )
    fig_expense_trend.update_traces(line_color='#e74c3c', marker=dict(size=10))
    st.plotly_chart(fig_expense_trend, use_container_width=True)
    
    # Detailed Expense Table
    st.markdown("#### Detailed Expense Records")
    expense_detail = pd.DataFrame({
        'Date': ['2025-11-01', '2025-11-02', '2025-11-02', '2025-11-02', '2025-11-02'],
        'Category': ['Equipment', 'Salaries & Wages', 'Office Supplies', 'Utilities', 'Maintenance'],
        'Description': ['Office equipment purchase', 'Monthly salary disbursement', 'Paper and office materials', 'Electricity and water', 'Building repairs'],
        'Amount (₱)': ['75,000', '85,000', '25,000', '18,000', '15,000'],
        'Transaction ID': ['EXP-2025-890', 'EXP-2025-891', 'EXP-2025-892', 'EXP-2025-893', 'EXP-2025-894']
    })
    st.dataframe(expense_detail, use_container_width=True, hide_index=True)

# Comparative Analysis Tab
with tab3:
    st.subheader("Comparative Analysis")
    
    # Income vs Expense Comparison
    comparison_data = pd.DataFrame({
        'Month': ['July', 'August', 'September', 'October', 'November'],
        'Income': [720000, 765000, 795000, 810000, 850000],
        'Expenses': [640000, 625000, 615000, 610000, 620000],
        'Net': [80000, 140000, 180000, 200000, 230000]
    })
    
    fig_comparison = go.Figure()
    fig_comparison.add_trace(go.Bar(
        x=comparison_data['Month'],
        y=comparison_data['Income'],
        name='Income',
        marker_color='#2ecc71'
    ))
    fig_comparison.add_trace(go.Bar(
        x=comparison_data['Month'],
        y=comparison_data['Expenses'],
        name='Expenses',
        marker_color='#e74c3c'
    ))
    fig_comparison.add_trace(go.Scatter(
        x=comparison_data['Month'],
        y=comparison_data['Net'],
        name='Net Income',
        mode='lines+markers',
        marker=dict(size=10),
        line=dict(color='#3498db', width=3)
    ))
    
    fig_comparison.update_layout(
        title='Income vs Expenses Comparison',
        barmode='group',
        xaxis_title='Month',
        yaxis_title='Amount (₱)'
    )
    st.plotly_chart(fig_comparison, use_container_width=True)
    
    st.markdown("---")
    
    # Summary Statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### Average Monthly Income")
        st.metric("", f"₱{comparison_data['Income'].mean():,.0f}")
    with col2:
        st.markdown("#### Average Monthly Expenses")
        st.metric("", f"₱{comparison_data['Expenses'].mean():,.0f}")
    with col3:
        st.markdown("#### Average Net Income")
        st.metric("", f"₱{comparison_data['Net'].mean():,.0f}")
    
    st.markdown("---")
    
    # Budget vs Actual
    st.markdown("#### Budget vs Actual Comparison")
    budget_data = pd.DataFrame({
        'Category': ['Income', 'Expenses', 'Net Income'],
        'Budget': [800000, 650000, 150000],
        'Actual': [850000, 620000, 230000],
        'Variance': [50000, -30000, 80000],
        'Variance %': [6.25, -4.62, 53.33]
    })
    st.dataframe(budget_data, use_container_width=True, hide_index=True)

st.markdown("---")
st.caption("All financial data is recorded on the LINAW blockchain for transparency and accountability")