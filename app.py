import streamlit as st
import pandas as pd
import datetime
import os

# Page Configuration
st.set_page_config(
    page_title="Survival Kingdom Economic Portal",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme & Custom Styles
st.markdown("""
<style>
    body {
        background-color: #111111;
        color: #EEEEEE;
    }
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #E5C158;
        margin-bottom: 0.2rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    .subtitle {
        font-size: 1.1rem;
        color: #888888;
        margin-bottom: 1.5rem;
    }
    .group-card {
        background-color: #1A1A1A;
        border: 1px solid #333333;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    .group-card:hover {
        border-color: #E5C158;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(229, 193, 88, 0.25);
    }
    .lead-badge {
        background: linear-gradient(135deg, #E5C158 0%, #AA8000 100%);
        color: #111111;
        font-weight: bold;
        padding: 0.25rem 0.6rem;
        border-radius: 20px;
        font-size: 0.75rem;
        display: inline-block;
        margin-left: 0.5rem;
        vertical-align: middle;
    }
    .member-item {
        color: #CCCCCC;
        font-size: 0.95rem;
        margin-bottom: 0.3rem;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1A1A1A;
        color: #777777;
        text-align: center;
        padding: 0.5rem;
        font-size: 0.85rem;
        border-top: 1px solid #333333;
        z-index: 100;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="main-title">🛡️ Survival Kingdom Economic Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Off-Grid Ledger, Sector assignments & Gold Valuation System (2029–2035)</div>', unsafe_allow_html=True)

# Setup paths and locate CSV
filename = "global_survival_economy_2029_2035.csv"
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, filename)

# Load data helper
@st.cache_data
def load_data(path):
    if not os.path.exists(path):
        return None
    data = pd.read_csv(path)
    data["Date"] = pd.to_datetime(data["Date"])
    return data

df = load_data(csv_path)

# Group Assignments Data
group_assignments = [
    {
        "id": 1,
        "name": "Group 1: Consolidation",
        "sector": "Consolidation",
        "lead": "Thanishvel Mogam",
        "members": ["Thanishvel Mogam", "Jeremy Matthews Thomas", "Ajwaad Mahbub Karim", "Intan Syazana"],
        "icon": "💼",
        "resource": "Gold Assets"
    },
    {
        "id": 2,
        "name": "Group 2: Rice / Flour",
        "sector": "Rice / Flour",
        "lead": "Rejoice Kandemiri",
        "members": ["Dehemi Amanda", "Rejoice Kandemiri", "Darrshnee"],
        "icon": "🌾",
        "resource": "Rice & Flour"
    },
    {
        "id": 3,
        "name": "Group 3: Spices",
        "sector": "Spices",
        "lead": "Fahim Sahriar Ponno",
        "members": ["Fahim Sahriar Ponno", "Eithi Noor Jahan", "Rifat Md", "Joy Chandra Das", "Zannat Zamman"],
        "icon": "🌶️",
        "resource": "Spices"
    },
    {
        "id": 4,
        "name": "Group 4: Vegetables",
        "sector": "Vegetables",
        "lead": "Farhad Niloy",
        "members": ["Raj Malo (Himangshu)", "Farhad Niloy", "Sagor Mollah", "Shawon Sorif"],
        "icon": "🥦",
        "resource": "Vegetables"
    },
    {
        "id": 5,
        "name": "Group 5: Fruits",
        "sector": "Fruits",
        "lead": "Jishan Ahamed Himel",
        "members": ["Akter Khusbu", "Md Shahik Khan Hemel", "Md Rimon", "Jishan Ahamed Himel", "Biraj Sarker"],
        "icon": "🍎",
        "resource": "Fruits"
    },
    {
        "id": 6,
        "name": "Group 6: Electricity",
        "sector": "Electricity",
        "lead": "Arpita Roy Joya",
        "members": ["Arpita Roy Joya", "Tanvire Anwaro Ivan", "Rahi Al Md Jameal Kawsar", "Sohanur Rahman"],
        "icon": "⚡",
        "resource": "Power / Grid"
    },
    {
        "id": 7,
        "name": "Group 7: Fuel",
        "sector": "Fuel",
        "lead": "Sofiq",
        "members": ["Salam", "Utsa", "Sofiq", "Zaman Uddin Sarker", "Sayed"],
        "icon": "⛽",
        "resource": "Fuel / Biofuel"
    },
    {
        "id": 8,
        "name": "Group 8: Furniture / Utensils",
        "sector": "Furniture / Utensils",
        "lead": "Hasan Murad",
        "members": ["Abdul Azim", "Hasan Murad", "Tanjil", "Wazed", "Rabbi"],
        "icon": "🪑",
        "resource": "Utensils & Furniture"
    },
    {
        "id": 9,
        "name": "Group 9: Clothes",
        "sector": "Clothes",
        "lead": "Ishtiaq Ahamed Swapneel",
        "members": ["Afsana Akter Borsha", "Angelo Tirtho Khan", "Fatema Begum", "Ishtiaq Ahamed Swapneel"],
        "icon": "👕",
        "resource": "Apparel & Fabric"
    },
    {
        "id": 10,
        "name": "Group 10: Meat",
        "sector": "Meat",
        "lead": "Eshwary",
        "members": ["Eshwary", "Parveer"],
        "icon": "🥩",
        "resource": "Meat / Livestock"
    }
]

# Sidebar Configuration
st.sidebar.header("Navigation & Settings")
st.sidebar.info("Operational Status: OFF-GRID ECONOMY ACTIVE")

# App Mode Selection
app_mode = st.sidebar.radio(
    "Select Operational Screen",
    options=["📈 Gold Valuation Dashboard", "👥 Sector Teams & Assignments", "📦 Sector Ledger & Logs"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Ledger Parameters")

# Dynamic inputs
selected_date = st.sidebar.date_input(
    "Target Date",
    value=datetime.date(2029, 1, 1),
    min_value=datetime.date(2029, 1, 1),
    max_value=datetime.date(2035, 12, 31)
)

currencies = ["INR", "EUR", "GBP", "JPY", "CNY", "CAD", "AUD", "CHF", "SGD", "MYR", "THB", "MXN", "BRL", "KRW", "ZAR"]
selected_currency = st.sidebar.selectbox("Target Currency", options=currencies)

# Fixed peg dictionary
currency_rates = {
    "INR": 46.54,
    "EUR": 1.06,
    "GBP": 0.67,
    "JPY": 114.85,
    "CNY": 8.28,
    "CAD": 1.50,
    "AUD": 1.93,
    "CHF": 1.62,
    "SGD": 1.73,
    "MYR": 3.80,
    "THB": 43.12,
    "MXN": 9.60,
    "BRL": 1.95,
    "KRW": 1259.00,
    "ZAR": 7.57
}

# Fetch rate for current configuration
gold_rate_usd = 0.0
gold_rate_target_currency = 0.0
is_valid_date = False

if df is not None:
    target_dt = pd.to_datetime(selected_date)
    min_date = df["Date"].min()
    max_date = df["Date"].max()
    
    if min_date <= target_dt <= max_date:
        row = df[df["Date"] == target_dt]
        if not row.empty:
            gold_rate_target_currency = row[selected_currency].values[0]
            gold_rate_usd = gold_rate_target_currency / currency_rates[selected_currency]
            is_valid_date = True

# Main Logic Routing
if df is None:
    st.error(f"⚠️ Critical System File Missing: {filename} was not found in {current_dir}. Please place the CSV in the same folder as this app.")

else:
    if not is_valid_date:
        st.warning(f"⚠️ Survival Alert: Selected date {selected_date} is outside the ledger range ({df['Date'].min().strftime('%Y-%m-%d')} to {df['Date'].max().strftime('%Y-%m-%d')}).")
    
    else:
        if app_mode == "📈 Gold Valuation Dashboard":
            st.subheader("📈 Gold Standard Economic Valuation")
            
            gold_weight_oz = st.number_input("Gold Weight (Troy Ounces)", min_value=0.0, value=1.0, step=0.1)
            
            # Gold Conversion Logic
            grams = gold_weight_oz * 31.1035
            total_value = gold_rate_target_currency * gold_weight_oz
            value_per_gram = total_value / grams if grams > 0 else 0
            
            # Display Dashboard Metrics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    label=f"Total Value ({selected_currency})",
                    value=f"{total_value:,.2f} {selected_currency}"
                )
            
            with col2:
                st.metric(
                    label=f"Value per Gram ({selected_currency})",
                    value=f"{value_per_gram:,.2f} {selected_currency}/g"
                )
                
            with col3:
                st.metric(
                    label="Gold Rate (USD)",
                    value=f"${gold_rate_usd:,.2f} USD/oz"
                )
                
            st.markdown("---")
            st.subheader(f"Ledger Output for {selected_date.strftime('%B %d, %Y')}")
            st.write(f"Evaluating `{gold_weight_oz:,.4f} oz` (~`{grams:,.4f} g`) of physical assets using the established gold standard.")
            
            # Resource pegs overview
            st.markdown("### 📋 Survival Sector Base Value Pegs")
            st.caption("Baseline valuations of resources relative to 1 Troy Ounce of Gold.")
            
            pegs_col1, pegs_col2, pegs_col3 = st.columns(3)
            with pegs_col1:
                st.write("**Grain / Flour**: 0.002 oz Gold per kg")
                st.write("**Meat**: 0.004 oz Gold per kg")
                st.write("**Vegetables**: 0.001 oz Gold per kg")
            with pegs_col2:
                st.write("**Electricity**: 0.0005 oz Gold per kWh")
                st.write("**Fuel**: 0.003 oz Gold per Liter")
                st.write("**Spices**: 0.005 oz Gold per kg")
            with pegs_col3:
                st.write("**Clothes**: 0.004 oz Gold per item")
                st.write("**Furniture**: 0.01 oz Gold per item")
                st.write("**Utensils**: 0.001 oz Gold per item")

        elif app_mode == "👥 Sector Teams & Assignments":
            st.subheader("👥 Kingdom Sector Teams & Group Assignments")
            
            # Filters & Search
            col1, col2 = st.columns([2, 1])
            with col1:
                search_query = st.text_input("🔍 Search member or sector team name", "").strip().lower()
            with col2:
                filter_resource = st.selectbox("Filter by primary resource/sector", ["All"] + [g["sector"] for g in group_assignments])
            
            filtered_groups = []
            for g in group_assignments:
                # Filter criteria
                matches_search = (
                    search_query in g["name"].lower() or 
                    search_query in g["sector"].lower() or 
                    any(search_query in m.lower() for m in g["members"])
                )
                matches_resource = (filter_resource == "All" or g["sector"] == filter_resource)
                
                if matches_search and matches_resource:
                    filtered_groups.append(g)
            
            # Metrics
            met1, met2, met3 = st.columns(3)
            met1.metric("Total Sectors", len(group_assignments))
            met2.metric("Filtered Sectors", len(filtered_groups))
            met3.metric("Total Assigned Survivors", sum(len(g["members"]) for g in group_assignments))
            
            st.markdown("---")
            
            # Display Groups in Grid
            cols_per_row = 2
            for i in range(0, len(filtered_groups), cols_per_row):
                cols = st.columns(cols_per_row)
                for j in range(cols_per_row):
                    if i + j < len(filtered_groups):
                        g = filtered_groups[i + j]
                        with cols[j]:
                            # Render Group Card HTML
                            members_html = "".join([
                                f"<div class='member-item'>• {name} "
                                f"{'<span class=\'lead-badge\'>👑 Lead</span>' if name == g['lead'] else ''}</div>"
                                for name in g["members"]
                            ])
                            
                            card_content = f"""
                            <div class="group-card">
                                <h3 style="color: #E5C158; margin-top: 0; margin-bottom: 0.5rem;">
                                    {g['icon']} {g['name']}
                                </h3>
                                <p style="color: #888888; font-size: 0.9rem; margin-bottom: 0.8rem;">
                                    <b>Primary Sector Duty:</b> {g['resource']}
                                </p>
                                <div style="margin-bottom: 0.5rem;">
                                    {members_html}
                                </div>
                            </div>
                            """
                            st.markdown(card_content, unsafe_allow_html=True)

        elif app_mode == "📦 Sector Ledger & Logs":
            st.subheader("📦 Off-Grid Sector Ledger Log Simulator")
            st.write("Record inventory acquisitions or usage, and automatically compute values based on dynamic gold conversion rates on the selected date.")
            
            # Resource standard values in Gold (Oz)
            resource_gold_pegs = {
                "Gold Assets": 1.0,
                "Rice & Flour": 0.002,
                "Spices": 0.005,
                "Vegetables": 0.001,
                "Fruits": 0.0012,
                "Power / Grid": 0.0005,
                "Fuel / Biofuel": 0.003,
                "Utensils & Furniture": 0.005,
                "Apparel & Fabric": 0.004,
                "Meat / Livestock": 0.004
            }
            
            # Session state initialization for log records
            if "ledger_logs" not in st.session_state:
                st.session_state["ledger_logs"] = []
            
            # Log Input Form
            with st.form("ledger_log_form"):
                st.write("##### Add New Ledger Transaction Record")
                l_col1, l_col2, l_col3 = st.columns(3)
                
                with l_col1:
                    selected_group = st.selectbox(
                        "Sector / Logging Group",
                        options=group_assignments,
                        format_func=lambda x: f"{x['icon']} {x['name']}"
                    )
                with l_col2:
                    action_type = st.selectbox(
                        "Action Type",
                        ["Acquisition / Harvest", "Consumption", "Trade Transfer", "Audit adjustment"]
                    )
                with l_col3:
                    qty = st.number_input("Quantity of Resources", min_value=0.1, value=100.0, step=1.0)
                
                notes = st.text_input("Transaction Notes / Memo", placeholder="e.g. Scavenged 20kg of rice, or backup generator operational hours")
                
                submit_log = st.form_submit_form_button = st.form_submit_button("📁 Register Log Entry")
                
                if submit_log:
                    # Gold conversion calculation
                    item_peg = resource_gold_pegs.get(selected_group["resource"], 0.001)
                    total_gold_oz = qty * item_peg
                    value_in_target = total_gold_oz * gold_rate_target_currency
                    value_in_usd = total_gold_oz * gold_rate_usd
                    
                    new_entry = {
                        "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "Target Date": selected_date.strftime("%Y-%m-%d"),
                        "Sector": selected_group["sector"],
                        "Action": action_type,
                        "Quantity": qty,
                        "Primary Resource": selected_group["resource"],
                        "Gold Equivalent (oz)": total_gold_oz,
                        f"Value ({selected_currency})": round(value_in_target, 2),
                        "Value (USD)": round(value_in_usd, 2),
                        "Log Officer": selected_group["lead"],
                        "Notes": notes
                    }
                    st.session_state["ledger_logs"].append(new_entry)
                    st.success("Entry added to the off-grid ledger successfully.")
            
            # Display Logs
            st.write("---")
            st.write("##### 📖 Live Ledger Records")
            
            if st.session_state["ledger_logs"]:
                logs_df = pd.DataFrame(st.session_state["ledger_logs"])
                st.dataframe(logs_df, use_container_width=True)
                
                # Reset Logs Button
                if st.button("🗑️ Clear Ledger Cache"):
                    st.session_state["ledger_logs"] = []
                    st.rerun()
            else:
                st.info("No records logged in the current session yet. Use the form above to register inventory activity.")

# Persistent System Status Footer
st.markdown(
    f"""
    <div class="footer">
        System Baseline: 2001 USD/INR (Pegged at 46.54) | Current Node: Survival Kingdom Primary Core | Last Sync: 2026-06-28
    </div>
    """, 
    unsafe_allow_html=True
)
