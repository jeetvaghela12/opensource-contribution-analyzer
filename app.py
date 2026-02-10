import streamlit as st
from github import Github
import pandas as pd

# --- Page Configuration ---
st.set_page_config(page_title="OpenSource Contribution Analyzer", layout="wide", page_icon="🔍")

# --- Custom Styling ---
st.title("🔍 OpenSource Contribution Analyzer")
st.markdown("""
    ### Enhance Mentor Insights for Repository Contributors
    This tool provides a data-driven analysis of contributor activity, engagement, and pull request patterns.
""")

# --- Sidebar Configuration ---
st.sidebar.header("Configuration")
token = st.sidebar.text_input("GitHub Personal Access Token", type="password", help="Enter your GitHub PAT to fetch data.")
repo_input = st.sidebar.text_input("Repository Path", "pallets/flask", help="Format: username/repository")

# --- Logic and Analysis ---
if st.sidebar.button("Run Analysis"):
    if not token:
        st.sidebar.error("Authentication Error: Please provide a valid GitHub Token.")
    else:
        try:
            # Initialize GitHub Connection
            g = Github(token)
            repo = g.get_repo(repo_input)
            
            st.success(f"Successfully connected to: **{repo.full_name}**")
            
            # Fetching Data
            with st.spinner("Fetching latest contribution data..."):
                pulls = repo.get_pulls(state='all')[:50]
                
                data = []
                for pr in pulls:
                    data.append({
                        "Contributor": pr.user.login,
                        "PR Title": pr.title,
                        "Status": pr.state.capitalize(),
                        "Comments": pr.comments,
                        "Date Created": pr.created_at.strftime("%Y-%m-%d")
                    })
                
                df = pd.DataFrame(data)

            # --- Visualizations ---
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📊 Contributor Velocity")
                st.info("Distribution of Pull Requests by Contributor")
                pr_counts = df['Contributor'].value_counts()
                st.bar_chart(pr_counts)

            with col2:
                st.subheader("💬 Engagement Metrics")
                st.info("Discussion volume (Comments) per Contributor")
                engagement = df.groupby('Contributor')['Comments'].sum().sort_values(ascending=False)
                st.dataframe(engagement, use_container_width=True)

            # --- Activity Logs ---
            st.divider()
            st.subheader("📋 Detailed Contribution Log")
            st.dataframe(df, use_container_width=True)
            
            # Download Option
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Export Data as CSV", data=csv, file_name="contributions.csv", mime="text/csv")

        except Exception as e:
            st.error(f"Data Fetching Error: {str(e)}")

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.caption("Built for Open Source Mentors | v1.0")
