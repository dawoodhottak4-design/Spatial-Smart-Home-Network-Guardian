import streamlit as st
import time
import random
from groq import Groq

# Page Configuration
st.set_page_config(
    page_title="Spatial Smart-Home & Network Guardian | Hybrid Command Hub",
    page_icon="📡",
    layout="wide"
)

# Custom Styling for Futuristic HUD Look
st.markdown("""
    <style>
    .main-title { font-size: 26px; font-weight: 700; color: #38bdf8; }
    .sub-title { font-size: 14px; color: #94a3b8; }
    .metric-card { background-color: #0f172a; padding: 15px; border-radius: 10px; border: 1px solid #1e293b; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Control Center
st.sidebar.markdown("### ⚙️ Guardian Control Hub")
api_key_input = st.sidebar.text_input("Enter Groq API Key", type="password", help="Required for LLM & Whisper processing")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏠 Lifestyle & Network Modes")
active_mode = st.sidebar.selectbox(
    "Select Smart-Home Routine",
    ["Balanced Mode", "Work Mode (Prioritize Zoom/Teams)", "Movie Night (4K Stream Priority)", "Deep Gaming Mode"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🤖 Multi-Agent Selector")
agent_role = st.sidebar.radio(
    "Lead AI Agent",
    ["Telecom NOC & Wi-Fi Engineer", "Smart-Home IoT Coordinator", "Cybersecurity & Parental Shield"]
)

# Main Header
st.markdown('<p class="main-title">📡 Spatial Smart-Home & Network Guardian (Hybrid Telemetry Engine)</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Meta VR Hackathon 2026 | Streamlit Control Center & Real-Time Network Engine</p>', unsafe_allow_html=True)
st.markdown("---")

# Layout Tabs: 1. Live Telemetry & Ping, 2. Voice & Text Agent, 3. Spatial AR/VR Preview
tab1, tab2, tab3 = st.tabs(["📊 Real-Time Network Telemetry & Ping", "🎙️ Groq Voice (Whisper) & Chat Agent", "🥽 Spatial WebXR / VR Bridge"])

with tab1:
    st.markdown("### 🌐 Live Device Ping Simulation & Bandwidth Telemetry")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Gateway Ping (192.168.1.1)", f"{random.randint(2, 6)} ms", "Optimal")
    with col2:
        st.metric("Cloud Latency (Groq API)", f"{random.randint(45, 80)} ms", "Connected")
    with col3:
        st.metric("Active IoT Devices", "14 Connected", "Secure")
    with col4:
        st.metric("Wi-Fi Spectrum Load", f"{random.randint(62, 85)}%", "Channel 6")

    st.markdown("---")
    
    # Real-Time Device Ping Simulation Table
    st.markdown("#### 🔍 Smart Home & Telecom Node Status")
    device_data = [
        {"Device Name": "Meta Quest 3 (VR Headset)", "IP Address": "192.168.1.105", "Status": "Online 🟢", "Ping": "3.2 ms", "Bandwidth": "45 Mbps"},
        {"Device Name": "4K Smart TV (Living Room)", "IP Address": "192.168.1.110", "Status": "Online 🟢", "Ping": "4.1 ms", "Bandwidth": "18.5 Mbps"},
        {"Device Name": "Mesh Wi-Fi Node (BedRoom)", "IP Address": "192.168.1.2", "Status": "Online 🟢", "Ping": "1.8 ms", "Bandwidth": "120 Mbps"},
        {"Device Name": "Smart Security Camera", "IP Address": "192.168.1.15", "Status": "Warning 🟡", "Ping": "28.5 ms", "Bandwidth": "4.2 Mbps"}
    ]
    st.table(device_data)

with tab2:
    st.markdown("### 🎙️ Multi-Modal Interaction (Voice Whisper + Groq LLM)")
    st.info("💡 You can type your network request or simulate voice commands processed via Groq API.")

    user_prompt = st.text_area(
        "Give a command to your Spatial Guardian:",
        placeholder="e.g., My smart security camera is lagging. Optimize the bandwidth for it and prioritize my work laptop."
    )

    # Simulated Voice-to-Text Upload Option
    audio_file = st.file_uploader("Upload Voice Command (.mp3 / .wav for Whisper simulation)", type=["mp3", "wav", "m4a"])
    
    if st.button("🚀 Execute Guardian Command", type="primary"):
        if not api_key_input:
            st.error("⚠️ Please enter your Groq API Key in the sidebar.")
        elif not user_prompt and not audio_file:
            st.warning("⚠️ Please provide a text command or upload an audio file.")
        else:
            with st.spinner(f"🔄 {agent_role} is analyzing network topology under '{active_mode}'..."):
                try:
                    client = Groq(api_key=api_key_input)
                    
                    input_text = user_prompt
                    if audio_file:
                        input_text = "[Voice Command Simulated via Whisper]: Optimize network channels and resolve latency issues."

                    system_prompt = (
                        f"You are {agent_role}, an elite AI embedded in a Meta Quest Smart-Home & Network Guardian system. "
                        f"Current active lifestyle mode is '{active_mode}'. Give precise, futuristic, technical network optimization steps "
                        f"within 70 words."
                    )

                    # Reverted back to openai/gpt-oss-120b for testing phase
                    completion = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": input_text}
                        ],
                        temperature=0.4,
                        max_tokens=150
                    )

                    reply = completion.choices[0].message.content
                    
                    st.success("### ✅ Guardian Execution Result:")
                    st.write(reply)
                    
                except Exception as e:
                    st.error(f"❌ Execution Error: {str(e)}")

with tab3:
    st.markdown("### 🥽 Spatial WebXR / AR Bridge Preview")
    st.markdown("""
    This tab connects your Streamlit Control Hub to the **Meta Quest Mixed Reality Passthrough interface**. 
    * When deployed on Streamlit Cloud or local server, the WebXR link renders 3D floating telemetry panels in your room.
    """)
    
    if st.button("🔗 Generate WebXR Simulation Link"):
        st.success("🌐 WebXR Spatial Bridge Active! You can open the immersive 3D floating dashboard in your Quest browser.")
        st.code("https://spatial-network-guardian-simulator.streamlit.app/xr-view", language="text")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>Spatial Smart-Home & Network Guardian | Hybrid Architecture for Meta VR Hackathon 2026</p>", unsafe_allow_html=True)
