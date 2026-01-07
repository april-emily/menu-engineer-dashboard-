import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. SETUP & LAYOUT ---
st.set_page_config(
    page_title="The Menu Engineer", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Branding
with st.sidebar:
    st.header("⚙️ Configuration")
    st.write("Adjust the parameters below to simulate different market conditions.")

# Main Title Area
st.title("The Menu Engineer: Profitability & Popularity Analysis")

# Use an Expander for the explanation (Keeps the UI clean)
with st.expander("ℹ️ How to use this dashboard", expanded=True):
    st.markdown("""
    This tool helps hospitality managers optimise their menu by categorising items into the standard **Menu Engineering Matrix**:
    * **🌟 Stars (High Profit, High Popularity):** Keep these consistent and promote them.
    * **🐴 Plowhorses (Low Profit, High Popularity):** Increase price slightly or reduce portion size.
    * **🧩 Puzzles (High Profit, Low Popularity):** Rebrand, take better photos, or run a special.
    * **🐕 Dogs (Low Profit, Low Popularity):** Consider removing from the menu.
    """)

# --- 2. LOAD DATA ---
# Add a file uploader to the sidebar
st.sidebar.subheader("Upload Your Own Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    try:
        df = pd.read_csv("menu_data.csv")
    except FileNotFoundError:
        st.error("⚠️ menu_data.csv not found! Please run the data generator script first or upload your own data.")
        st.stop()

# --- 3. SIDEBAR CONTROLS ---
st.sidebar.subheader("Filtering Options")
# Get unique categories and add an "All" option
categories = ["All"] + df['Category'].unique().tolist()
selected_category = st.sidebar.selectbox("Filter by Category", categories)

st.sidebar.subheader("Scenario Planning")
inflation_rate = st.sidebar.slider("Simulate Cost Inflation (%)", 0, 50, 0, help="Increases the cost price of all items.")
price_increase = st.sidebar.slider("Simulate Price Increase (%)", 0, 50, 0, help="Increases the sales price of all items.")

# Filter DataFrame based on selection
if selected_category != "All":
    df_filtered = df[df['Category'] == selected_category].copy()
else:
    df_filtered = df.copy()

# Apply Scenario Logic
df_filtered['Simulated_Cost'] = df_filtered['Cost_Price'] * (1 + inflation_rate/100)
df_filtered['Simulated_Price'] = df_filtered['Sales_Price'] * (1 + price_increase/100)

# --- 4. CALCULATIONS ---
df_filtered['Contribution_Margin'] = df_filtered['Simulated_Price'] - df_filtered['Simulated_Cost']
df_filtered['Total_Revenue'] = df_filtered['Simulated_Price'] * df_filtered['Number_Sold']

# Averages (The Matrix Cut-offs)
avg_contribution = df_filtered['Contribution_Margin'].mean()
avg_popularity = df_filtered['Number_Sold'].mean()

# Classification Logic
def classify_item(row):
    if row['Contribution_Margin'] >= avg_contribution and row['Number_Sold'] >= avg_popularity:
        return "Star 🌟"
    elif row['Contribution_Margin'] < avg_contribution and row['Number_Sold'] >= avg_popularity:
        return "Plowhorse 🐴"
    elif row['Contribution_Margin'] >= avg_contribution and row['Number_Sold'] < avg_popularity:
        return "Puzzle 🧩"
    else:
        return "Dog 🐕"

df_filtered['Classification'] = df_filtered.apply(classify_item, axis=1)

# --- 5. KEY METRICS (New Section) ---
# Display high-level stats at the top
m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Menu Items", len(df_filtered))
m2.metric("Avg. Profit Margin", f"${avg_contribution:.2f}")
m3.metric("Total Revenue", f"${df_filtered['Total_Revenue'].sum():,.0f}")
m4.metric("Star Items", len(df_filtered[df_filtered['Classification'] == "Star 🌟"]))

st.markdown("---") # Divider line

# --- 6. VISUALS ---
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Menu Matrix Analysis")
    fig = px.scatter(
        df_filtered,
        x="Contribution_Margin",
        y="Number_Sold",
        color="Classification",
        size="Total_Revenue",
        hover_name="Item",
        text="Item",
        title="Profitability (X) vs. Popularity (Y)",
        color_discrete_map={
            "Star 🌟": "gold",
            "Plowhorse 🐴": "blue",
            "Puzzle 🧩": "green",
            "Dog 🐕": "red"
        },
        height=600
    )
    # Add quadrants
    fig.add_vline(x=avg_contribution, line_dash="dash", line_color="gray", annotation_text="Avg Margin")
    fig.add_hline(y=avg_popularity, line_dash="dash", line_color="gray", annotation_text="Avg Popularity")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Item Performance")
    # Interactive Table (Sortable)
    st.dataframe(
        df_filtered[['Item', 'Classification', 'Contribution_Margin']], 
        hide_index=True, 
        use_container_width=True,
        height=600
    )

# --- 7. DETAILED DATA ---
with st.expander("View Full Data Table"):
    st.dataframe(df_filtered)