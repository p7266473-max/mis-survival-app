import streamlit as st
import time

st.set_page_config(
    page_title="MIS Post-Apocalyptic Survival Hub",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme overrides using HTML injection for premium look
st.markdown("""
<style>
    .reportview-container {
        background: #111216;
    }
    .stApp {
        background-color: #0f1015;
        color: #e2e8f0;
    }
    h1, h2, h3 {
        color: #00ffcc !important;
        font-family: 'Courier New', Courier, monospace;
    }
    .survival-card {
        background-color: #1a1c23;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 15px;
    }
    .alert-banner {
        background-color: #7f1d1d;
        border-left: 5px solid #ef4444;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚡ MIS SURVIVAL COMMAND CENTER")
st.subheader("Post-Apocalyptic Survival & Resource Coordination Network")

st.markdown("""
<div class="alert-banner">
    <strong>[ALERT LEVEL: CRITICAL]</strong> - YEAR 2028: Following 6 months of global conflict, the conventional power grid is 100% offline. 
    A cooperative group of 5.0M - 5.5M survivors has coalesced near local water basins. All communications rely on scavenged solar panels, local battery reserves, localized LANs, and low-power hardware.
</div>
""", unsafe_allow_html=True)

# Main Navigation
tab1, tab2, tab3, tab4 = st.tabs([
    "📖 The Case Scenario", 
    "📊 MIS Learning Modules", 
    "🔌 Scavenged Assets Tracker", 
    "📡 Group Communications"
])

with tab1:
    st.header("The WWIII Post-Apocalyptic Scenario")
    st.markdown("""
    ### Current Status: Day 180 (Post-Grid Collapse)
    * **Population Range:** 5,000,000 - 5,500,000 individuals regrouped around essential water sources.
    * **Energy Grid:** Completely dark. Scrap solar panels and vehicle alternators are the primary power production tools.
    * **Computing Power:** Laptops, smartphones, and low-power single-board computers (Raspberry Pi style) running on battery storage.
    * **Networks:** Local isolated networks (LANs) using salvaged Wi-Fi routers. No wide-area Internet is available.
    
    ### The MIS Challenge
    How do you manage information, direct logistics, distribute resources, and establish communication systems with **zero central infrastructure**?
    *This interactive application will serve as our evolving simulator to test system designs, resource algorithms, and communication topologies.*
    """)
    
    st.info("💡 As the semester progresses, this scenario will dynamically evolve, introducing resource constraints, epidemics, and communication outages.")

with tab2:
    st.header("Management Information Systems (MIS) Curriculum")
    st.markdown("""
    In a post-apocalyptic world, the core theories of MIS are not just academic—they are survival tools.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        #### 1. Databases & Resource Allocation
        * **Survival Context:** Keeping track of water distribution, medical supplies, and grain stores.
        * **MIS Concept:** Relational schemas, inventory management, transactions, and data integrity.
        """)
    with col2:
        st.markdown("""
        #### 2. Decentralized Network Architectures
        * **Survival Context:** Bridging communications between separate survivor camps without the Internet.
        * **MIS Concept:** Topologies, packet routing, peer-to-peer (P2P) systems, and security protocols.
        """)

with tab3:
    st.header("Scavenged Tech & Resource Tracker")
    st.write("Simulate your community's active resource pool:")
    
    c1, c2, c3 = st.columns(3)
    solar_panels = c1.number_input("Solar Panels Scavenged (100W units)", min_value=0, value=2500)
    laptops = c2.number_input("Functional Laptops / Mobiles", min_value=0, value=1200)
    water_flow = c3.number_input("Water Purification Rate (Liters/Hour)", min_value=0, value=8500)
    
    st.metric(label="Total Continuous Power Available (Watts)", value=f"{solar_panels * 60:.1f}W (Assumed 60% Eff.)")
    st.metric(label="Survivor Support Capacity (Based on water output)", value=f"{int(water_flow / 3.0)} people/day")

with tab4:
    st.header("📡 Local Area Network Broadcast")
    st.write("Post a broadcast message to the camp networks:")
    
    user_name = st.text_input("Sender Handle", value="Camp-3 Coordinator")
    message_text = st.text_area("Broadcast message")
    if st.button("Send Emergency Broadcast"):
        if message_text:
            st.success(f"Broadcasted to LAN: '{message_text}' from {user_name}")
            st.toast("Message sent across subnets!", icon="📡")
        else:
            st.warning("Please write a message first.")
