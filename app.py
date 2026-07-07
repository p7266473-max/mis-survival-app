import streamlit as st
import pandas as pd
import numpy as np

# Set up page configurations
st.set_page_config(
    page_title="MIS & IT Operations Academic Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling with Google Fonts, Glassmorphism, and Dynamic Themes
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap');
    
    html, body, .stApp {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background: radial-gradient(circle at 10% 20%, rgba(243, 246, 249, 1) 0%, rgba(234, 240, 246, 1) 90.1%);
        color: #1e293b;
    }
    
    /* Elegant Title Cards */
    .portal-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border-radius: 20px;
        padding: 3rem 2rem;
        text-align: center;
        box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
        margin-bottom: 2.5rem;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .portal-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, transparent 60%);
        pointer-events: none;
    }
    
    .portal-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.2rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    
    .portal-subtitle {
        font-size: 1.25rem;
        color: #94a3b8;
        font-weight: 400;
        max-width: 800px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    /* Academic Theme Panels based on user program */
    .academic-panel {
        background: #ffffff;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.04), 0 4px 6px -4px rgb(0 0 0 / 0.04);
        border: 1px solid #e2e8f0;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .academic-panel:hover {
        transform: translateY(-2px);
        box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.06), 0 8px 10px -6px rgb(0 0 0 / 0.06);
    }
    
    /* Alert and Scenario Banners */
    .emergency-banner {
        background: linear-gradient(135deg, #fef2f2 0%, #ffe4e6 100%);
        border-left: 6px solid #ef4444;
        color: #991b1b;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px -1px rgb(239 68 68 / 0.08);
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .badge-cs {
        background-color: #dbeafe;
        color: #1e40af;
    }
    
    .badge-accounts {
        background-color: #d1fae5;
        color: #065f46;
    }
    
    .badge-mba {
        background-color: #fef3c7;
        color: #92400e;
    }
    
    /* Metric Card Styling */
    div[data-testid="stMetricValue"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 1.85rem !important;
        font-weight: 700 !important;
    }
    
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR / CONFIGURATION
# ============================================================
st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem 0;">
    <h2 style="color: #0f172a; margin-bottom: 0.5rem; font-family: 'Playfair Display', serif;">🎓 Program Hub</h2>
    <p style="color: #64748b; font-size: 0.9rem;">Tailor your learning tracks and labs</p>
</div>
""", unsafe_allow_html=True)

program_options = {
    "🖥️ BSc Computer Science": {
        "badge": '<span class="badge badge-cs">BSc Computer Science / IT</span>',
        "color": "#1e40af",
        "desc": "Focuses on hypervisors, software sandboxing, infrastructure configurations, and localized networking."
    },
    "📊 BSc Accounts": {
        "badge": '<span class="badge badge-accounts">BSc Accounts (Accounting)</span>',
        "color": "#065f46",
        "desc": "Focuses on cost-benefit analysis, hardware asset lifecycles, internal auditing, and backup ledger integrity."
    },
    "👔 MBA (Business Administration)": {
        "badge": '<span class="badge badge-mba">Master of Business Administration</span>',
        "color": "#92400e",
        "desc": "Focuses on IT governance, strategic alignment, risk management, disaster recovery planning, and stakeholder operations."
    }
}

selected_program = st.sidebar.selectbox(
    "Select Academic Track:",
    options=list(program_options.keys())
)

# Render program info card in sidebar
st.sidebar.markdown(f"""
<div style="background-color: #ffffff; border-radius: 12px; padding: 16px; border: 1px solid #e2e8f0; margin-top: 10px;">
    {program_options[selected_program]["badge"]}
    <p style="margin-top: 10px; font-size: 0.88rem; color: #475569;">{program_options[selected_program]["desc"]}</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<small style='color:#64748b;'>MIS & IT Operations Academic Portal &bull; 2026</small>",
    unsafe_allow_html=True,
)

# ============================================================
# HEADER
# ============================================================
st.markdown("""
<div class="portal-header">
    <div class="portal-title">MIS & IT Operations Course Portal</div>
    <div class="portal-subtitle">Interactive Syllabus, Learning Modules & Lab Simulations designed for Future Engineers, Auditors, and Corporate Leaders.</div>
</div>
""", unsafe_allow_html=True)

# Main Navigation Tabs
tabs = st.tabs([
    "📂 Course Overview",
    "🖥️ Week 1: Virtualization", 
    "💾 Week 2: Infrastructure & Media", 
    "☢️ Week 3: Survival Scenario"
])

# ============================================================
# TAB 0: COURSE OVERVIEW
# ============================================================
with tabs[0]:
    st.markdown('<div class="academic-panel">', unsafe_allow_html=True)
    st.header("Course Introduction")
    st.write("Welcome to the Management Information Systems (MIS) & IT Operations Course. This web application serves as a dynamic textbook, lab manual, and sandbox simulator for your weekly assignments.")
    
    st.markdown(f"""
    ### 🎯 Tailored Track: {selected_program}
    To prepare you for real-world scenarios, the modules, toolings, and simulator assignments are automatically customized to match your discipline.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="academic-panel">
    <h3>📅 Weekly Course Architecture (7 Weeks - 42 Hours)</h3>
    <p>This semester is split into foundational IT operations (Weeks 1 & 2), followed by a simulated survival scenario (Week 3 onwards) designed to test your system design capacities under extreme real-world constraints.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 Use the navigation tabs at the top to explore lecture slides, reference guides, and interactive tools for your selected track.")

# ============================================================
# TAB 1: WEEK 1 (VIRTUALIZATION)
# ============================================================
with tabs[1]:
    st.header("Week 1: Virtualization & Resource Management")
    
    # Render customized content depending on track
    if "Computer Science" in selected_program:
        st.markdown("""
        <div class="academic-panel">
            <h3>📖 Lecture: Understanding Virtualization & Hypervisors</h3>
            <p>Virtualization is the process of creating a software-based (or virtual) representation of physical resources, such as compute, storage, and networking.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="academic-panel" style="height: 100%;">
                <h4>Why Virtualize in IT/CS?</h4>
                <ul>
                    <li><strong>Server Consolidation:</strong> Running multiple OS instances on one physical machine to maximize CPU/RAM utilization.</li>
                    <li><strong>Disaster Recovery:</strong> VMs are encapsulated in single files (like <code>.ova</code> or <code>.qcow2</code>), making backups and migrations fast.</li>
                    <li><strong>Sandbox Security:</strong> Safely run untrusted or specialized software configurations without risking the host machine.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="academic-panel" style="height: 100%;">
                <h4>Hypervisor Topologies</h4>
                <ul>
                    <li><strong>Type 1 (Bare-Metal):</strong> Runs directly on computer hardware. Examples: <strong>Proxmox VE</strong>, <strong>VMware ESXi</strong>, <strong>Hyper-V Server</strong>. Used in enterprise data centers.</li>
                    <li><strong>Type 2 (Hosted):</strong> Runs inside a Host OS (like Windows/macOS). Examples: <strong>VirtualBox</strong>, <strong>VMware Workstation Pro</strong>. Excellent for localized testing.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("""
        <div class="academic-panel">
            <h3>📦 Curated ISO File Library</h3>
            <p>To set up your virtual machines in our lab sessions, you must fetch clean bootable operating system images (<strong>ISOs</strong>). Here is our recommended reference library:</p>
            <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                <tr style="border-bottom: 2px solid #e2e8f0; text-align: left;">
                    <th style="padding: 10px;">Operating System</th>
                    <th style="padding: 10px;">Edition</th>
                    <th style="padding: 10px;">Recommended RAM</th>
                    <th style="padding: 10px;">Purpose / Lab Assignment</th>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 10px;"><strong>Ubuntu Desktop 24.04</strong></td>
                    <td style="padding: 10px;">LTS (Standard)</td>
                    <td style="padding: 10px;">4 GB</td>
                    <td style="padding: 10px;">Standard Linux CLI & GUI operations</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 10px;"><strong>Ubuntu Server 24.04</strong></td>
                    <td style="padding: 10px;">LTS (Minimal)</td>
                    <td style="padding: 10px;">2 GB</td>
                    <td style="padding: 10px;">Database hosting and minimal headless setup</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 10px;"><strong>Debian 12</strong></td>
                    <td style="padding: 10px;">Netinst (Net Installer)</td>
                    <td style="padding: 10px;">1 GB</td>
                    <td style="padding: 10px;">High-security, ultra-lightweight server sandbox</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    elif "Accounts" in selected_program:
        st.markdown("""
        <div class="academic-panel">
            <h3>📖 Lecture: Cost-Benefit Analysis & Financial Auditing of Virtualized Infrastructure</h3>
            <p>Virtualization changes the paradigm of financial asset management, shifting capital expenditures (CapEx) to operational expenditures (OpEx) while introducing new audit controls.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="academic-panel" style="height: 100%;">
                <h4>Financial Benefits & ROI</h4>
                <ul>
                    <li><strong>Hardware Consolidation:</strong> Reducing physical server footprints lowers CapEx (buying fewer servers) and OpEx (cooling/power bills).</li>
                    <li><strong>Asset Lifecycle Management:</strong> Virtualization extends the functional utility of old software applications without requiring outdated legacy hardware maintenance contracts.</li>
                    <li><strong>Resource Chargeback Models:</strong> Accounting teams can audit CPU, memory, and storage allocations to bill individual business departments directly.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="academic-panel" style="height: 100%;">
                <h4>IT Audit & Compliance Controls</h4>
                <ul>
                    <li><strong>Logical Isolation Audits:</strong> Checking that different virtual machines (e.g., payment gateways vs. public servers) are logically partitioned to maintain regulatory compliance.</li>
                    <li><strong>Virtual Asset Tracking:</strong> Ensuring "VM sprawl" (creating unchecked VMs) does not waste company financial resources.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    else:  # MBA
        st.markdown("""
        <div class="academic-panel">
            <h3>📖 Lecture: Strategic Cloud Migration & Virtualization Governance</h3>
            <p>For executive leadership, virtualization is a strategic tool to build organizational agility, improve security posturing, and ensure business continuity.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="academic-panel" style="height: 100%;">
                <h4>Strategic Alignment & Risk</h4>
                <ul>
                    <li><strong>Business Agility:</strong> Instantly provisioning VM sandboxes enables agile testing and shortens product time-to-market.</li>
                    <li><strong>Total Cost of Ownership (TCO):</strong> Comparing bare-metal on-premise hardware setups against cloud infrastructure providers (AWS, Azure) to align IT spend with corporate strategy.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="academic-panel" style="height: 100%;">
                <h4>IT Governance Frameworks</h4>
                <ul>
                    <li><strong>Governance:</strong> Aligning virtualization policies with COBIT or ITIL standards.</li>
                    <li><strong>SLA Management:</strong> Negotiating and auditing service level agreements (SLAs) with hypervisor and hardware vendors to mitigate supply-chain dependencies.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    # Common Section: Interactive Simulation tool customized per track
    st.markdown('<div class="academic-panel">', unsafe_allow_html=True)
    st.subheader("💡 Track-Specific Simulator")
    
    if "Computer Science" in selected_program:
        type_choice = st.radio(
            "Select a Hypervisor class to inspect performance trade-offs:",
            ["Type 1: Bare-Metal Hypervisor", "Type 2: Hosted Hypervisor"]
        )
        if "Type 1" in type_choice:
            st.success("⚡ **Type 1 Hypervisor:** 98-99% direct hardware access efficiency. Ideal for mission-critical IT infrastructure.")
        else:
            st.info("💻 **Type 2 Hypervisor:** 85-95% efficiency due to translation layer of host operating system. Excellent for localized testing.")
            
    elif "Accounts" in selected_program:
        st.markdown("#### Virtualization Cost-Savings Calculator")
        physical_servers = st.number_input("Number of physical servers needed WITHOUT virtualization", min_value=1, value=12)
        cost_per_server = st.number_input("Average cost per physical server ($)", min_value=500, value=3500)
        consolidation_ratio = st.slider("Consolidation Ratio (VMs per Hypervisor)", min_value=2, max_value=20, value=6)
        
        hypervisors_needed = int(np.ceil(physical_servers / consolidation_ratio))
        total_non_virtual = physical_servers * cost_per_server
        total_virtual = hypervisors_needed * cost_per_server
        savings = total_non_virtual - total_virtual
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Non-Virtualized Capital Spend", f"${total_non_virtual:,}")
        c2.metric("Virtualized Capital Spend", f"${total_virtual:,}")
        c3.metric("Estimated CapEx Savings", f"${savings:,}", delta=f"+{((savings/total_non_virtual)*100):.1f}%")
        
    else:  # MBA
        st.markdown("#### Cloud vs. On-Premises Strategic Scorecard")
        st.write("Score your organizational parameters (1 = Low, 5 = High) to find the best deployment strategy.")
        
        c1, c2 = st.columns(2)
        in_house_talent = c1.slider("In-House Technical Expertise", min_value=1, max_value=5, value=3)
        security_compliance = c2.slider("Data Compliance/Sovereignty Rigor", min_value=1, max_value=5, value=4)
        budget_flexibility = c1.slider("Budget Flexibility (OpEx Preference)", min_value=1, max_value=5, value=2)
        uptime_requirement = c2.slider("Uptime Requirements", min_value=1, max_value=5, value=4)
        
        # Calculate scorecard
        on_prem_score = (in_house_talent * 2) + (security_compliance * 2.5) - budget_flexibility
        cloud_score = (budget_flexibility * 2) + (uptime_requirement * 2) - security_compliance
        
        st.markdown("##### Strategic Recommendation:")
        if on_prem_score > cloud_score:
            st.warning(f"🔒 **Recommendation: On-Premises / Private Cloud** (Score: {on_prem_score:.1f} vs. Cloud {cloud_score:.1f}). Given strict regulatory demands or lack of alignment with cloud subscriptions, private virtualized architecture is recommended.")
        else:
            st.success(f"☁️ **Recommendation: Public / Hybrid Cloud** (Score: {cloud_score:.1f} vs. On-Prem {on_prem_score:.1f}). Elastic cloud resource consumption matches your budget model and operational scalability goals.")
            
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# TAB 2: WEEK 2 (INFRASTRUCTURE & MEDIA)
# ============================================================
with tabs[2]:
    st.header("Week 2: Physical Infrastructure & Bootable Systems")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if "Computer Science" in selected_program:
            st.markdown("""
            <div class="academic-panel" style="height: 100%;">
                <h3>💾 Lab: Bootable USB Utilities</h3>
                <p>A bootable USB allows systems administrators to install new OS distributions or run system recovery software from USB storage.</p>
                <h4>Recommended Tooling Matrix</h4>
                <ol>
                    <li><strong>Rufus:</strong> (Windows-only) High control over partition styles (<strong>GPT/MBR</strong>) and boot targets (<strong>UEFI/BIOS</strong>).</li>
                    <li><strong>BalenaEtcher:</strong> (Cross-platform) Extremely simple user interface for flash writing.</li>
                    <li><strong>Ventoy:</strong> A revolutionary tool that allows you to copy multiple ISO files directly onto a single USB and select them at boot time.</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
        elif "Accounts" in selected_program:
            st.markdown("""
            <div class="academic-panel" style="height: 100%;">
                <h3>💾 Lab: Spreadsheet Integrity & Financial Ledger Security</h3>
                <p>Accounting professionals must ensure that physical data-storage tools are cataloged, and ledger spreadsheets are locked against tampering.</p>
                <h4>Internal Accounting Controls</h4>
                <ol>
                    <li><strong>Hash Verification (SHA-256):</strong> Validating file hashes of financial ledgers to confirm data has not been modified.</li>
                    <li><strong>Physical Security Protocols:</strong> Enforcing strict access controls on system boot USB drives containing recovery programs.</li>
                    <li><strong>Audit Logs:</strong> Reviewing file metadata for unauthorized modifications to financial reporting systems.</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
        else:  # MBA
            st.markdown("""
            <div class="academic-panel" style="height: 100%;">
                <h3>💾 Lab: Business Continuity & Disaster Recovery Plans (BCP/DRP)</h3>
                <p>Management must author clear frameworks to guide technicians and accounts during unexpected system outages.</p>
                <h4>Core Executive Frameworks</h4>
                <ol>
                    <li><strong>RTO (Recovery Time Objective):</strong> The target duration of time inside which a business process must be restored.</li>
                    <li><strong>RPO (Recovery Point Objective):</strong> The maximum tolerable period in which data might be lost.</li>
                    <li><strong>Asset Ownership Mapping:</strong> Identifying stakeholders responsible for key service restoration.</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
            
    with col2:
        if "Computer Science" in selected_program:
            st.markdown("""
            <div class="academic-panel" style="height: 100%;">
                <h3>🖥️ IT Hardware Foundations</h3>
                <p>Understanding hardware specifications ensures budget-to-performance optimization.</p>
                <ul>
                    <li><strong>CPU (Central Processing Unit):</strong> Core counts vs. Clock Speed. Database servers prioritize cores, whereas single-process applications prioritize clock speed.</li>
                    <li><strong>RAM (volatile):</strong> Speed (DDR4/DDR5) and capacity. Essential for hosting multiple active VM sandboxes.</li>
                    <li><strong>Storage (non-volatile):</strong> NVMe SSDs vs. SATA HDDs. NVMe offers faster read/write speeds, reducing boot times and database lag.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        elif "Accounts" in selected_program:
            st.markdown("""
            <div class="academic-panel" style="height: 100%;">
                <h3>🖥️ Hardware Depreciation & CapEx Lifecycles</h3>
                <p>Infrastructure assets are depreciated over time, affecting corporate tax liabilities.</p>
                <ul>
                    <li><strong>Straight-Line Depreciation:</strong> Allocating the purchase cost of servers evenly over their useful lifecycle (typically 3-5 years).</li>
                    <li><strong>Hardware Lifecycle Tracking:</strong> Replacing enterprise SSDs before failure rates increase, optimizing operational costs.</li>
                    <li><strong>Residual Scrap Value:</strong> Forecasting hardware salvage value at decommissioning.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        else:  # MBA
            st.markdown("""
            <div class="academic-panel" style="height: 100%;">
                <h3>🖥️ Strategic IT Resource Procurement</h3>
                <p>Sourcing hardware involves long-term supplier relationship management and operational risk evaluation.</p>
                <ul>
                    <li><strong>Vendor Lock-in:</strong> The strategic risk of dependency on proprietary hypervisor/cloud technologies.</li>
                    <li><strong>Scalability Bottlenecks:</strong> Identifying architectural limitations in physical hardware upgrades.</li>
                    <li><strong>Green Computing (ESG):</strong> Measuring and optimizing the carbon footprint of corporate data centers.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    # Interactive Estimator Tool
    st.markdown('<div class="academic-panel">', unsafe_allow_html=True)
    if "Computer Science" in selected_program:
        st.subheader("🛠️ Flashing Estimator Utility")
        iso_size = st.number_input("ISO File Size (GB)", min_value=0.1, max_value=64.0, value=3.2, step=0.1)
        usb_speed = st.slider("USB Write Speed (MB/s)", min_value=5, max_value=150, value=20)
        
        est_time = (iso_size * 1024) / usb_speed
        st.metric(label="Estimated Write Duration", value=f"{int(est_time // 60)}m {int(est_time % 60)}s")
        
    elif "Accounts" in selected_program:
        st.subheader("📊 Asset Depreciation Simulator")
        initial_cost = st.number_input("Initial Server Asset Cost ($)", min_value=1000, value=15000, step=1000)
        years = st.slider("Useful Asset Lifecycle (Years)", min_value=3, max_value=10, value=5)
        salvage_value = st.number_input("Estimated Salvage Value ($)", min_value=0, value=1500, step=100)
        
        depreciation_per_year = (initial_cost - salvage_value) / years
        
        c1, c2 = st.columns(2)
        c1.metric(label="Annual Depreciation Expense", value=f"${depreciation_per_year:,.2f}")
        
        # Schedule table
        schedule_data = []
        book_value = initial_cost
        for y in range(1, years + 1):
            book_value -= depreciation_per_year
            schedule_data.append({"Year": y, "Depreciation": f"${depreciation_per_year:,.2f}", "Book Value": f"${book_value:,.2f}"})
        
        c2.markdown("##### Straight-Line Schedule")
        c2.table(pd.DataFrame(schedule_data))
        
    else:  # MBA
        st.subheader("📋 BCP Alignment & RTO Estimator")
        st.write("Calculate estimated business downtime losses to justify disaster recovery investments.")
        hourly_revenue_loss = st.number_input("Company Hourly Operational Revenue ($)", min_value=100, value=12500)
        rto_hours = st.slider("Target Recovery Time Objective (RTO in Hours)", min_value=1, max_value=48, value=4)
        
        est_loss = hourly_revenue_loss * rto_hours
        st.metric(label="Total Estimated Downtime Financial Risk", value=f"${est_loss:,}", delta="Reduce RTO to minimize risk")
        
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# TAB 3: WEEK 3 (SURVIVAL SCENARIO)
# ============================================================
with tabs[3]:
    st.header("Week 3: Scenario Launch")
    st.markdown("""
    <div class="emergency-banner">
        <strong>⚠️ EMERGENCY CASE SCENARIO LOADED:</strong> The year is 2028. Following 6 months of a global conflict, the conventional power grid is 100% offline. A cooperative population of 5.0M - 5.5M survivors has coalesced near local water basins. All communications rely on scavenged solar panels, local battery reserves, localized LANs, and low-power hardware.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="academic-panel">
        <h3>Post-Apocalyptic Survival & Resource Coordination Network</h3>
        <p>This scenario serves as our sandbox to test system designs, resource allocation, and operations under extreme real-world constraints.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🔋 Scenario Resource Simulator")
    
    # Custom simulation metrics and inputs per track
    if "Computer Science" in selected_program:
        c1, c2 = st.columns(2)
        solar_panels = c1.number_input("Solar Panels Scavenged (100W units)", min_value=0, value=2500)
        water_flow = c2.number_input("Water Purification Rate (Liters/Hour)", min_value=0, value=8500)
        
        st.markdown('<div class="academic-panel">', unsafe_allow_html=True)
        st.metric(label="Total Continuous Power Available (Watts)", value=f"{solar_panels * 60:.1f}W (Assumed 60% Eff.)")
        st.metric(label="Survivor Support Capacity (Based on water output)", value=f"{int(water_flow / 3.0)} people/day")
        st.markdown('</div>', unsafe_allow_html=True)
        
    elif "Accounts" in selected_program:
        st.markdown('<div class="academic-panel">', unsafe_allow_html=True)
        st.write("#### Resource Inventory Audit Simulator")
        st.write("Reconcile recorded stockpiles against audited physical amounts to prevent inventory shrinkage.")
        
        rec_water = st.number_input("Recorded Water Filters (Units)", min_value=0, value=5000)
        phys_water = st.number_input("Audited Physical Water Filters (Units)", min_value=0, value=4850)
        
        rec_grain = st.number_input("Recorded Grain Stock (Tons)", min_value=0, value=120)
        phys_grain = st.number_input("Audited Physical Grain Stock (Tons)", min_value=0, value=118)
        
        water_shrinkage = rec_water - phys_water
        grain_shrinkage = rec_grain - phys_grain
        
        c1, c2 = st.columns(2)
        c1.metric("Water Filter Shrinkage", f"{water_shrinkage} units", delta=f"-{((water_shrinkage/rec_water)*100):.1f}%", delta_color="inverse")
        c2.metric("Grain Stock Shrinkage", f"{grain_shrinkage} Tons", delta=f"-{((grain_shrinkage/rec_grain)*100):.1f}%", delta_color="inverse")
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:  # MBA
        st.markdown('<div class="academic-panel">', unsafe_allow_html=True)
        st.write("#### Executive Crisis Management Decision Panel")
        st.write("Balance critical infrastructure prioritizations. You have 100 allocation points to distribute.")
        
        p1 = st.slider("Power Grid & Comms Allocation", min_value=0, max_value=100, value=40)
        p2 = st.slider("Water Purification & Logistics Allocation", min_value=0, max_value=100 - p1, value=40)
        p3 = 100 - p1 - p2
        
        st.info(f"Points distribution: Comms: {p1}% | Water: {p2}% | Health/Security: {p3}%")
        
        # Calculate survival index
        survival_index = (p1 * 0.3) + (p2 * 0.5) + (p3 * 0.2)
        
        st.markdown("##### Strategy Outcome Assessment:")
        if p2 < 30:
            st.error(f"🚨 **Critical Alert (Survival Score: {survival_index:.1f}/100):** Water allocation is too low! High dehydration risk will lead to severe population decline within days.")
        elif p1 < 20:
            st.warning(f"⚠️ **Operational Risk (Survival Score: {survival_index:.1f}/100):** Communications breakdown. Grid coordination will fail, leading to isolated survivor camps.")
        else:
            st.success(f"✅ **Viable Allocation (Survival Score: {survival_index:.1f}/100):** Resources are balanced. Population stability is predicted for the next 90 days.")
        st.markdown('</div>', unsafe_allow_html=True)
