from services.vector_store_service import build_vector_store
import streamlit as st
from helper_utils.helpers import initialize_session
from services.pdf_service import save_uploaded_file
from graph.nodes import resume_analysis_node, skill_gap_node
from ui.interview import interview_show
from ui.resume_analysis import show_resume
from ui.study_plan import show_study_plan
from ui.job_match import show_job_matcher
from ui.job_description import show_job_description_matcher
from ui.chat import show_chat



st.set_page_config(
    page_title="GenAI Career Copilot",
    page_icon="🚀",
    layout="wide"
)
st.title("GenAI Career Copilot")

# ----------------------------
# Initialize Session State
# ----------------------------
initialize_session()
if "resume_analysis_data" not in st.session_state:
    st.session_state.resume_analysis_data = None
if "interview_data" not in st.session_state:
    st.session_state.interview_data = None
if "study_plan_data" not in st.session_state:
    st.session_state.study_plan_data = None
if "job_matcher_data" not in st.session_state:
    st.session_state.job_matcher_data=None
if "job_description_matcher_data" not in st.session_state:
    st.session_state.job_description_matcher_data=None

# NEW — cached graph pre-routing results, computed once per resume upload
if "resume_analysis" not in st.session_state:
    st.session_state.resume_analysis=None
if "skill_gap_result" not in st.session_state:
    st.session_state.skill_gap_result=None


# ----------------------------
#Sidebar Configuration
# ----------------------------
with st.sidebar:
    st.title("🚀 Career Copilot")
    st.subheader("Configuration")
    
    # Keep the upload clean and tucked away in the sidebar
    uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])
    
    
if uploaded_file :
    # Save PDF
    file_path = save_uploaded_file(uploaded_file)


# Process only if a different resume is uploaded
    if st.session_state.current_resume != uploaded_file.name:
        with st.spinner("Building Vector Database..."):
            index, chunks = build_vector_store(file_path)
            st.session_state.index = index
            st.session_state.chunks = chunks
            st.session_state.current_resume = uploaded_file.name


            st.session_state.resume_analysis_data = None
            st.session_state.interview_data = None
            st.session_state.study_plan_data = None
            st.session_state.job_matcher_data = None
            st.session_state.job_description_matcher_data = None

        # NEW — run resume_analyze + skill_gap ONCE per upload, cache results
        # so every tab's graph.invoke() call reuses them instead of
        # recomputing on every single button click.

        with st.spinner("Analyzing resume and identifying skill gaps..."):
            seed_state=resume_analysis_node({
                "request":"Analyze this resume",
                "intent":"",
                "index":index,
                "chunks":chunks,
                "resume_analysis":None,
                "skill_gap_result":None,
                "interview_result": None,
                "study_plan_result": None,
                "job_match_result": None
            })
            seed_state=skill_gap_node(seed_state)
            st.session_state.resume_analysis=seed_state["resume_analysis"]
            st.session_state.skill_gap_result=seed_state["skill_gap_result"]

        st.success("✅ Resume processed successfully!")

# ----------------------------
# Main Content Area
# ----------------------------
if st.session_state.index is not None:
    # SaaS-style Tab Navigation
    tab1, tab2, tab3 ,tab4,tab5 ,tab6= st.tabs([
        "📊 Resume Analysis", 
        "🤖 Interview Questions", 
        "📅 30-Day Study Plan",
        "✅ matching jobs",
        "📋 Job Description Match",
        "💬 Chat With Resume"
    ])

    with tab1:
        # st.header("Resume Analysis")
        st.divider()
        # Pass session state down so the UI component can read/write cached data
        show_resume(st.session_state.index, st.session_state.chunks)
        
    with tab2:
        st.header("Interview Questions")
        st.divider()
        interview_show(st.session_state.index, st.session_state.chunks)
        
    with tab3:
        st.header("30-Day Study Plan")
        st.divider()
        # The study plan UI can now check if st.session_state.study_plan_data 
        # exists before invoking the Gemini API
        show_study_plan(st.session_state.index, st.session_state.chunks)

    with tab4:
        st.header("Matching Jobs")
        st.divider()
        show_job_matcher(st.session_state.index,st.session_state.chunks)

    with tab5:
        st.header("📄 Job Description Match")
        st.divider()
        show_job_description_matcher(
            st.session_state.index,
            st.session_state.chunks
        )

    with tab6:

        st.header("💬 Chat With Your Resume")

        st.divider()

        show_chat(
            st.session_state.index,
            st.session_state.chunks
        )

else:
    st.info("Please upload a resume in the sidebar to start the scanning process.")