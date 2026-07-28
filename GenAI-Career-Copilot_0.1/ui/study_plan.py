from services.study_plan_service import generate_study_plan
import streamlit as st

def show_study_plan(index, chunks):
    """
    Display a personalized 30-day study plan
    generated from the uploaded resume.
    """
    with st.spinner("Generating your personalized 30-day study plan..."):

            try:
                result = generate_study_plan(
                    "Generate a 30-day study plan",
                    index,
                    chunks
                )
            except Exception as e:
                st.error(f"Failed to generate study plan: {e}")
                return

            # 1. Iterate through each nested week
            for week in result.weeks:
                

                week_title = f"📅 Week {week.week_number}: {week.week_goal}"
                with st.expander(week_title, expanded=(week.week_number == 1)):
                    progress = week.week_number / len(result.weeks)
                    st.progress(progress)
                    st.caption(f"Week {week.week_number} of {len(result.weeks)}")
                    st.caption(f"🎯 **Core Weekly Focus:** {week.week_goal}")
                    
                
                # 2. Iterate through each study task inside that week
                    for task in week.study_tasks:
                        task_title = f"📚 Topic: {task.topic}"
                        
                        with st.expander(task_title, expanded=False):
                            st.caption(f"⏱️ Estimated Effort: {task.estimated_hours} hours/day")
                            st.markdown(f"**Objective:** {task.goal}")
                            st.markdown(f"**🛠️ Hands-on Mini Project:** {task.mini_project}")
                                
                            # Display resources cleanly as a bulleted list
                            if task.resources:
                                st.markdown("**🔗 Free Study Resources:**")
                                for resource in task.resources:
                                    st.markdown(f"- {resource}")
                            
                            # 3. Handle the interview questions deeply nested inside each task
                            if task.interview_questions:
                                st.subheader("❓ Target Interview Questions")
                                for idx, question_text in enumerate(task.interview_questions, 1):
                                    st.markdown(f"**Q{idx}.** {question_text}")

                    st.success(f"🏁 Deliverable: {week.deliverable}")
                    
                    # Visual separator between weeks
                    st.markdown("---")
