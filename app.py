import streamlit as st

st.set_page_config(
    page_title="MIS / IT Operations Academic Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme overrides using HTML injection for premium look (Light Mode Academic)
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
        color: #1e3a8a !important; /* Deep academic blue */
        font-family: 'Inter', sans-serif;
        font-weight: 700;
    }
    .academic-card {
        background-color: #ffffff;
        border-left: 5px solid #1e3a8a;
        border-radius: 4px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);
    }
    .case-banner {
        background-color: #fef2f2;
        border-left: 5px solid #ef4444;
        color: #991b1b;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎓 MIS & IT Operations Course Portal")
st.subheader("Interactive Syllabus, Learning Modules & Lab Simulations")

# Main navigation aligned with the course structure
tabs = st.tabs([
    "📂 Course Overview",
    "🖥️ Week 1: Virtualization", 
    "💾 Week 2: Bootable USB & Hardware", 
    "☢️ Week 3: Survival Scenario"
])

with tabs[0]:
    st.header("Course Introduction")
    st.write("Welcome to the Management Information Systems (MIS) & IT Operations Course. This web application serves as a dynamic textbook, lab manual, and sandbox simulator for your weekly assignments.")
    
    st.markdown("""
    ### 📅 Weekly Course Architecture (7 Weeks - 42 Hours)
    This semester is split into foundational IT operations (Weeks 1 & 2), followed by a simulated survival scenario (Week 3 onwards) designed to test your system design capacities under constraints.
    """)
    
    st.info("💡 Use the navigation tabs at the top to explore lecture slides, reference guides, and interactive tools for each week.")

with tabs[1]:
    st.header("Week 1: Virtualization & Hypervisors")
    
    st.markdown("""
    ### 📖 Lecture: Understanding Virtualization
    Virtualization is the process of creating a software-based (or virtual) representation of physical resources, such as compute, storage, and networking.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        #### Why Virtualize in MIS?
        * **Server Consolidation:** Running multiple OS instances on one physical machine to maximize CPU/RAM utilization.
        * **Disaster Recovery:** VMs are encapsulated in single files (like `.ova` or `.qcow2`), making backups and migrations fast.
        * **Sandbox Security:** Safely run untrusted or specialized software configurations without risking the host machine.
        """)
    with col2:
        st.markdown("""
        #### Hypervisor Topologies
        * **Type 1 (Bare-Metal):** Runs directly on the bare-metal computer hardware. Examples: **Proxmox VE**, **VMware ESXi**, **Hyper-V Server**. Used in enterprise data centers.
        * **Type 2 (Hosted):** Runs as an application inside a Host Operating System (like Windows or macOS). Examples: **VirtualBox**, **VMware Workstation Pro**. Excellent for learning.
        """)
        
    st.markdown("""
    ---
    ### 📦 Curated ISO File Library
    To set up your virtual machines in our lab sessions, you must fetch clean bootable operating system images (**ISOs**). Here is our recommended reference library:
    """)
    
    # ISO Library Table
    st.markdown("""
    | Operating System | Edition | Recommended RAM | Purpose / Lab Assignment |
    | :--- | :--- | :--- | :--- |
    | **Ubuntu Desktop 24.04** | LTS (Standard) | 4 GB | Standard Linux CLI & GUI operations |
    | **Ubuntu Server 24.04** | LTS (Minimal) | 2 GB | Database hosting and minimal headless setup |
    | **Debian 12** | Netinst (Net Installer) | 1 GB | High-security, ultra-lightweight server sandbox |
    | **Alpine Linux** | Extended edition | 256 MB | Resource-constrained environment labs |
    """)
    
    st.subheader("💡 Hypervisor Performance Comparison Simulator")
    type_choice = st.radio(
        "Select a Hypervisor class to inspect performance trade-offs:",
        ["Type 1: Bare-Metal Hypervisor", "Type 2: Hosted Hypervisor"]
    )
    
    if "Type 1" in type_choice:
        st.success("⚡ **Type 1 Hypervisor:** 98-99% direct hardware access efficiency. Ideal for mission-critical IT infrastructure.")
    else:
        st.info("💻 **Type 2 Hypervisor:** 85-95% efficiency due to translation layer of host operating system. Excellent for localized testing.")

with tabs[2]:
    st.header("Week 2: Bootable USBs & Computer Hardware")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 💾 Lab: How to Create a Bootable USB
        A bootable USB allows systems administrators to install new OS distributions or run system recovery software from USB storage.
        
        #### Recommended Tooling Matrix
        1. **Rufus:** (Windows-only) High control over partition styles (**GPT/MBR**) and boot targets (**UEFI/BIOS**).
        2. **BalenaEtcher:** (Cross-platform) Extremely simple user interface for flash writing.
        3. **Ventoy:** A revolutionary tool that allows you to copy multiple ISO files directly onto a single USB and select them at boot time.
        
        #### BIOS / UEFI Selection Guide:
        * **UEFI (Unified Extensible Firmware Interface):** Modern boot framework, supports GPT partitions (>2TB partition size), quick boot.
        * **Legacy BIOS:** Legacy framework, limited to MBR partitions (max 4 partitions, <2TB drive size).
        """)
        
    with col2:
        st.markdown("""
        ### 🖥️ IT Hardware Foundations
        Understanding hardware specifications ensures budget-to-performance optimization.
        
        * **CPU (Central Processing Unit):** Core counts vs. Clock Speed. Database servers prioritize cores, whereas single-process applications prioritize clock speed.
        * **RAM (volatile):** Speed (DDR4/DDR5) and capacity. Essential for hosting multiple active VM sandboxes.
        * **Storage (non-volatile):** NVMe SSDs vs. SATA HDDs. NVMe offers faster read/write speeds, reducing boot times and database lag.
        """)
        
    st.subheader("🛠️ Flashing Estimator Utility")
    iso_size = st.number_input("ISO File Size (GB)", min_value=0.1, max_value=64.0, value=3.2, step=0.1)
    usb_speed = st.slider("USB Write Speed (MB/s)", min_value=5, max_value=150, value=20)
    
    est_time = (iso_size * 1024) / usb_speed
    st.metric(label="Estimated Write Duration", value=f"{int(est_time // 60)}m {int(est_time % 60)}s")

with tabs[3]:
    st.header("Week 3: Scenario Launch")
    st.markdown("""
    <div class="case-banner">
        <strong>⚠️ EMERGENCY CASE SCENARIO LOADED:</strong> The year is 2028. Following 6 months of a global conflict, the conventional power grid is 100% offline. A cooperative population of 5.0M - 5.5M survivors has coalesced near local water basins. All communications rely on scavenged solar panels, local battery reserves, localized LANs, and low-power hardware.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### Post-Apocalyptic Survival & Resource Coordination Network
    This scenario serves as our sandbox to test system designs, resource allocation algorithms, and communication topologies under extreme real-world constraints.
    """)
    
    st.subheader("🔋 Scenario Resource Simulator")
    c1, c2 = st.columns(2)
    solar_panels = c1.number_input("Solar Panels Scavenged (100W units)", min_value=0, value=2500)
    water_flow = c2.number_input("Water Purification Rate (Liters/Hour)", min_value=0, value=8500)
    
    st.metric(label="Total Continuous Power Available (Watts)", value=f"{solar_panels * 60:.1f}W (Assumed 60% Eff.)")
    st.metric(label="Survivor Support Capacity (Based on water output)", value=f"{int(water_flow / 3.0)} people/day")


