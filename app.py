import streamlit as st
import time

st.set_page_config(
    page_title="MIS Post-Apocalyptic Survival Hub",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme overrides using HTML injection for premium look (Light Mode)
st.markdown("""
<style>
    .reportview-container {
        background: #f8fafc;
    }
    .stApp {
        background-color: #f1f5f9;
        color: #1e293b;
    }
    h1, h2, h3 {
        color: #0f172a !important;
        font-family: 'Courier New', Courier, monospace;
        font-weight: 700;
    }
    .survival-card {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);
    }
    .alert-banner {
        background-color: #fef2f2;
        border-left: 5px solid #ef4444;
        color: #991b1b;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px 0 rgb(0 0 0 / 0.05);
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

# Main navigation aligned with the 7-week curriculum structure
tabs = st.tabs([
    "📂 Course Overview",
    "🖥️ Week 1: Virtualization", 
    "💾 Week 2: Bootable USB & Hardware", 
    "☢️ Week 3: Scenario Launch",
    "⏳ Weeks 4-7"
])

with tabs[0]:
    st.header("MIS / IT Course Portal")
    st.write("Welcome to the Management Information Systems & IT Operations Course. This portal aligns academic IT concepts with tactical, hands-on scenarios.")
    
    # Curriculum structure overview
    st.markdown("""
    ### 📅 7-Week Curriculum Outline (42 Hours Total)
    
    | Week | Topic | Practical Application |
    | :--- | :--- | :--- |
    | **Week 1** | Virtualization & Hypervisors | Creating isolated, virtualized environments |
    | **Week 2** | Bootable USBs & Computer Hardware | Bare-metal recovery & hardware assembly |
    | **Week 3** | Post-Apocalyptic Scenario Launch | Coordinating resources under grid-down constraints |
    | **Week 4** | Database Management Systems (DBMS) | Survivable registry & allocation systems |
    | **Week 5** | Decentralized Local Networks (LAN) | Salvaged router configurations & mesh networks |
    | **Week 6** | Information Security & Cryptography | Securing communication from interceptors |
    | **Week 7** | Final Integration & Disaster Recovery | Running full-scale disaster recovery simulations |
    """)

with tabs[1]:
    st.header("Week 1: Virtualization & Hypervisors")
    
    st.markdown("""
    ### 📖 What is Virtualization?
    Virtualization uses software to create an abstraction layer over computer hardware. This allows a single physical computer to be divided into multiple virtual computers—known as **Virtual Machines (VMs)**.
    
    #### Key Concepts:
    * **Host OS:** The physical machine's primary operating system.
    * **Guest OS:** The operating system running inside the virtual machine.
    * **Hypervisor:** The software that creates, runs, and manages VMs.
        * **Type 1 (Bare-Metal):** Runs directly on the physical hardware (e.g., VMware ESXi, Proxmox VE).
        * **Type 2 (Hosted):** Runs on top of a Host OS (e.g., VirtualBox, VMware Workstation).
    """)
    
    st.subheader("💡 Hypervisor Comparison Simulator")
    type_choice = st.radio(
        "Select a Hypervisor type to inspect performance characteristics:",
        ["Type 1: Bare-Metal Hypervisor", "Type 2: Hosted Hypervisor"]
    )
    
    if "Type 1" in type_choice:
        st.success("⚡ **Type 1 Selected:** Extremely low overhead, high stability, and standard for enterprise data centers. Directly communicates with physical CPUs and Memory.")
    else:
        st.info("💻 **Type 2 Selected:** Great for testing and student environments. Runs as an application inside your standard OS. Easy to configure, but incurs software translation overhead.")

with tabs[2]:
    st.header("Week 2: Bootable USBs & Computer Hardware")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 💾 How to Create a Bootable USB
        A bootable USB allows a computer to boot directly into an operating system installer or a live environment bypassing the local hard drive. This is crucial for system recovery and installing new operating systems.
        
        #### Standard Step-by-Step Procedure:
        1. **Acquire the ISO file:** Download the OS image (e.g., Ubuntu, Windows).
        2. **Choose a Flashing Utility:** Use tools like **Rufus** (Windows), **BalenaEtcher** (Cross-platform), or `dd` (Linux).
        3. **Flash the Media:** Select the target USB drive and ISO, then run the utility. *Warning: This erases all data on the USB.*
        4. **Configure UEFI/BIOS:** Boot the target computer, enter the BIOS menu (usually via `F2`, `F12`, or `Del`), change the boot order, and select the USB drive.
        """)
        
    with col2:
        st.markdown("""
        ### 🖥️ Understanding Computer Hardware
        To manage information systems, you must understand the hardware foundations:
        * **CPU (Central Processing Unit):** The brain that executes program instructions.
        * **RAM (Random Access Memory):** Volatile high-speed working memory.
        * **Storage (SSD/HDD):** Non-volatile long-term data storage.
        * **Motherboard:** The communication backbone connecting all components.
        """)
        
    st.subheader("🛠️ Bootable USB Integrity Checker Tool")
    iso_size = st.number_input("ISO File Size (GB)", min_value=0.1, max_value=64.0, value=2.4, step=0.1)
    usb_speed = st.slider("USB Write Speed (MB/s)", min_value=5, max_value=150, value=25)
    
    est_time = (iso_size * 1024) / usb_speed
    st.metric(label="Estimated Flashing Time", value=f"{int(est_time // 60)}m {int(est_time % 60)}s")

with tabs[3]:
    st.header("Week 3: Scenario Launch")
    st.markdown("""
    <div class="alert-banner">
        <strong>[ALERT LEVEL: CRITICAL]</strong> - YEAR 2028: Following 6 months of global conflict, the conventional power grid is 100% offline. 
        A cooperative group of 5.0M - 5.5M survivors has coalesced near local water basins. All communications rely on scavenged solar panels, local battery reserves, localized LANs, and low-power hardware.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### Post-Apocalyptic Survival & Resource Coordination Network
    
    #### Day 180 (Post-Grid Collapse)
    * **Population Range:** 5,000,000 - 5,500,000 individuals regrouped around essential water sources.
    * **Energy Grid:** Completely dark. Scrap solar panels and vehicle alternators are the primary power production tools.
    * **Computing Power:** Laptops, smartphones, and low-power single-board computers (Raspberry Pi style) running on battery storage.
    * **Networks:** Local isolated networks (LANs) using salvaged Wi-Fi routers. No wide-area Internet is available.
    
    ### The MIS Challenge
    How do you manage information, direct logistics, distribute resources, and establish communication systems with **zero central infrastructure**?
    *This interactive application will serve as our evolving simulator to test system designs, resource algorithms, and communication topologies.*
    """)
    
    st.subheader("🔋 Scenario Resource Simulator")
    c1, c2 = st.columns(2)
    solar_panels = c1.number_input("Solar Panels Scavenged (100W units)", min_value=0, value=2500)
    water_flow = c2.number_input("Water Purification Rate (Liters/Hour)", min_value=0, value=8500)
    
    st.metric(label="Total Continuous Power Available (Watts)", value=f"{solar_panels * 60:.1f}W (Assumed 60% Eff.)")
    st.metric(label="Survivor Support Capacity (Based on water output)", value=f"{int(water_flow / 3.0)} people/day")

with tabs[4]:
    st.header("Future Curriculum: Weeks 4-7")
    st.write("These modules will unlock dynamically as the semester progresses:")
    
    st.markdown("""
    * **Week 4:** Database Design & Survival Registry Systems
    * **Week 5:** Decentralized Networks & Routing Algorithms
    * **Week 6:** Cryptography, Authentication & Operational Security (OPSEC)
    * **Week 7:** Final Course Projects & Simulated Grid Recovery Run
    """)

