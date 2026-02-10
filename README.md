# 🔍 Open Source Contribution Analyzer

An automated tool designed for **Open Source Mentors** and **Maintainers** to evaluate contributor activity and engagement metrics using the GitHub API.

## 🚀 Overview
Managing a large open-source project can be overwhelming. This tool simplifies the process by providing data-driven insights into:
- **Contributor Velocity**: Who is consistently providing PRs?
- **Engagement Metrics**: Who is actively participating in discussions?
- **Contribution History**: A detailed log of recent activities.

## ✨ Key Features
- **Real-time Data**: Fetches the latest 50 Pull Requests directly from GitHub.
- **Visual Analytics**: Interactive bar charts for PR distribution.
- **Engagement Tracking**: Summarizes comments per user to identify helpful community members.
- **Data Export**: Option to download the analyzed data as a CSV file for offline reporting.

## 🛠️ Tech Stack
- **Language**: Python 3.12
- **Framework**: Streamlit (for the UI)
- **API**: PyGithub (GitHub API v3)
- **Data Handling**: Pandas

## ⚙️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/jeetvaghela12/opensource-contribution-analyzer.git](https://github.com/jeetvaghela12/opensource-contribution-analyzer.git)
   cd opensource-contribution-analyzer
