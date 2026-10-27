"""
Workforce Capacity & Skill Gap Intelligence Dashboard
A deterministic, rule-based workforce analytics tool built with Streamlit and Pandas.
"""

import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# Configuration and Page Setup
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Workforce Capacity & Skill Gap Intelligence",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# Sample Data Definitions (15 Employees, 5 Projects)
# -----------------------------------------------------------------------------
def get_sample_employees():
    """Returns sample roster of 15 employees across multiple departments."""
    return [
        {
            "emp_id": "EMP001",
            "name": "Alice Chen",
            "department": "IT",
            "weekly_hours": 40,
            "allocated_hours": 20,
            "skills": {"Python": 4, "Cloud Architecture": 4, "DevOps": 3}
        },
        {
            "emp_id": "EMP002",
            "name": "Bob Smith",
            "department": "IT",
            "weekly_hours": 40,
            "allocated_hours": 30,
            "skills": {"Python": 5, "Database Design": 4, "Cybersecurity": 2}
        },
        {
            "emp_id": "EMP003",
            "name": "Charlie Patel",
            "department": "IT",
            "weekly_hours": 40,
            "allocated_hours": 15,
            "skills": {"DevOps": 4, "Kubernetes": 4, "Python": 2}
        },
        {
            "emp_id": "EMP004",
            "name": "Diana Prince",
            "department": "Analytics",
            "weekly_hours": 40,
            "allocated_hours": 25,
            "skills": {"Data Analysis": 5, "Python": 4, "Machine Learning": 3}
        },
        {
            "emp_id": "EMP005",
            "name": "Evan Wright",
            "department": "Analytics",
            "weekly_hours": 40,
            "allocated_hours": 35,
            "skills": {"Machine Learning": 4, "Deep Learning": 3, "Python": 4}
        },
        {
            "emp_id": "EMP006",
            "name": "Fiona Gallagher",
            "department": "Analytics",
            "weekly_hours": 40,
            "allocated_hours": 10,
            "skills": {"Data Analysis": 4, "SQL": 5, "Business Intelligence": 4}
        },
        {
            "emp_id": "EMP007",
            "name": "George Miller",
            "department": "Marketing",
            "weekly_hours": 40,
            "allocated_hours": 20,
            "skills": {"SEO & SEM": 5, "Content Strategy": 4, "Digital Marketing": 4}
        },
        {
            "emp_id": "EMP008",
            "name": "Hannah Abbott",
            "department": "Marketing",
            "weekly_hours": 40,
            "allocated_hours": 30,
            "skills": {"Digital Marketing": 5, "Social Media Ads": 4, "Market Research": 3}
        },
        {
            "emp_id": "EMP009",
            "name": "Ian Malcolm",
            "department": "Marketing",
            "weekly_hours": 40,
            "allocated_hours": 15,
            "skills": {"Content Strategy": 5, "Copywriting": 4, "SEO & SEM": 2}
        },
        {
            "emp_id": "EMP010",
            "name": "Julia Roberts",
            "department": "Project Management",
            "weekly_hours": 40,
            "allocated_hours": 25,
            "skills": {"Agile Management": 5, "Risk Management": 4, "Scrum": 5}
        },
        {
            "emp_id": "EMP011",
            "name": "Kevin Hart",
            "department": "Project Management",
            "weekly_hours": 40,
            "allocated_hours": 10,
            "skills": {"Agile Management": 4, "Stakeholder Management": 4, "Budgeting": 3}
        },
        {
            "emp_id": "EMP012",
            "name": "Laura Croft",
            "department": "IT",
            "weekly_hours": 40,
            "allocated_hours": 30,
            "skills": {"Cybersecurity": 5, "Cloud Architecture": 3, "Network Security": 4}
        },
        {
            "emp_id": "EMP013",
            "name": "Michael Scott",
            "department": "Marketing",
            "weekly_hours": 40,
            "allocated_hours": 20,
            "skills": {"Market Research": 4, "Public Relations": 5, "Digital Marketing": 2}
        },
        {
            "emp_id": "EMP014",
            "name": "Nina Simone",
            "department": "Analytics",
            "weekly_hours": 40,
            "allocated_hours": 40,
            "skills": {"Business Intelligence": 5, "SQL": 4, "Data Analysis": 3}
        },
        {
            "emp_id": "EMP015",
            "name": "Oscar Isaac",
            "department": "Project Management",
            "weekly_hours": 40,
            "allocated_hours": 35,
            "skills": {"Risk Management": 5, "Budgeting": 4, "Vendor Management": 4}
        }
    ]

def get_sample_projects():
    """Returns sample list of 5 projects with skill, proficiency, and hour demands."""
    return [
        {
            "project_id": "PRJ001",
            "project_name": "AI Customer Support Engine",
            "department": "IT",
            "priority": "High",
            "deadline": "2026-12-15",
            "requirements": [
                {"skill": "Machine Learning", "min_proficiency": 4, "required_hours": 30},
                {"skill": "Python", "min_proficiency": 4, "required_hours": 25},
                {"skill": "Cloud Architecture", "min_proficiency": 4, "required_hours": 20}
            ]
        },
        {
            "project_id": "PRJ002",
            "project_name": "Global Brand Expansion",
            "department": "Marketing",
            "priority": "Medium",
            "deadline": "2027-01-20",
            "requirements": [
                {"skill": "Digital Marketing", "min_proficiency": 4, "required_hours": 30},
                {"skill": "SEO & SEM", "min_proficiency": 4, "required_hours": 25},
                {"skill": "Market Research", "min_proficiency": 4, "required_hours": 20}
            ]
        },
        {
            "project_id": "PRJ003",
            "project_name": "Enterprise BI Data Warehouse",
            "department": "Analytics",
            "priority": "High",
            "deadline": "2026-11-30",
            "requirements": [
                {"skill": "Data Analysis", "min_proficiency": 4, "required_hours": 40},
                {"skill": "SQL", "min_proficiency": 4, "required_hours": 35},
                {"skill": "Data Engineering", "min_proficiency": 4, "required_hours": 30}
            ]
        },
        {
            "project_id": "PRJ004",
            "project_name": "Cloud Infrastructure Modernization",
            "department": "IT",
            "priority": "High",
            "deadline": "2026-12-31",
            "requirements": [
                {"skill": "Kubernetes", "min_proficiency": 4, "required_hours": 30},
                {"skill": "Cybersecurity", "min_proficiency": 4, "required_hours": 25},
                {"skill": "DevOps", "min_proficiency": 3, "required_hours": 20}
            ]
        },
        {
            "project_id": "PRJ005",
            "project_name": "Agile Operations Transformation",
            "department": "Project Management",
            "priority": "Low",
            "deadline": "2027-02-28",
            "requirements": [
                {"skill": "Agile Management", "min_proficiency": 4, "required_hours": 25},
                {"skill": "Risk Management", "min_proficiency": 4, "required_hours": 20}
            ]
        }
    ]

# -----------------------------------------------------------------------------
# Core Analysis Engine (Deterministic Rule-Based Logic)
# -----------------------------------------------------------------------------

def calculate_employee_capacities(employees):
    """Calculates available weekly hours for each employee."""
    for emp in employees:
        weekly = emp.get("weekly_hours", 0)
        allocated = emp.get("allocated_hours", 0)
        emp["available_hours"] = max(0, weekly - allocated)
    return employees

def run_skill_gap_analysis(projects, employees):
    """
    Analyzes aggregate skill demands vs. qualified employee capacity.
    Employees must meet or exceed minimum proficiency to be counted as qualified.
    """
    skill_demands = {}

    # Accumulate required hours and highest min_proficiency needed per skill
    for prj in projects:
        for req in prj["requirements"]:
            skill = req["skill"]
            min_prof = req["min_proficiency"]
            hours = req["required_hours"]
            if skill not in skill_demands:
                skill_demands[skill] = {
                    "skill": skill,
                    "required_hours": 0,
                    "min_proficiency": min_prof,
                    "projects": []
                }
            skill_demands[skill]["required_hours"] += hours
            skill_demands[skill]["min_proficiency"] = max(skill_demands[skill]["min_proficiency"], min_prof)
            if prj["project_name"] not in skill_demands[skill]["projects"]:
                skill_demands[skill]["projects"].append(prj["project_name"])

    # Calculate qualified available hours across employees
    results = []
    for skill, demand in skill_demands.items():
        req_hours = demand["required_hours"]
        min_prof = demand["min_proficiency"]

        # Employees meeting min proficiency and with positive available hours
        qualified_emps = [
            emp for emp in employees
            if emp.get("skills", {}).get(skill, 0) >= min_prof and emp["available_hours"] > 0
        ]
        avail_qualified_hours = sum(emp["available_hours"] for emp in qualified_emps)

        # Gap calculation
        gap_hours = max(0, req_hours - avail_qualified_hours)
        gap_percentage = round((gap_hours / req_hours) * 100, 1) if req_hours > 0 else 0.0

        results.append({
            "Skill": skill,
            "Target Proficiency": min_prof,
            "Required Hours": req_hours,
            "Qualified Available Hours": avail_qualified_hours,
            "Skill Gap (Hours)": gap_hours,
            "Gap (%)": gap_percentage,
            "Status": "Critical Gap" if gap_percentage > 50 else ("Moderate Gap" if gap_percentage > 0 else "Sufficient"),
            "Associated Projects": ", ".join(demand["projects"])
        })

    return pd.DataFrame(results)

def simulate_workforce_allocation(projects, employees):
    """
    Simulates internal employee allocation to projects.
    Prioritizes projects by priority level (High > Medium > Low).
    Allocates employees based on highest skill proficiency and highest available capacity.
    Prevents double-counting available hours.
    """
    # Priority mapping for sorting
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    sorted_projects = sorted(projects, key=lambda p: priority_order.get(p.get("priority", "Low"), 4))

    # Keep track of simulated remaining available capacity per employee
    simulated_capacity = {emp["emp_id"]: emp["available_hours"] for emp in employees}
    emp_map = {emp["emp_id"]: emp for emp in employees}

    allocation_records = []
    unfulfilled_gaps = []

    for prj in sorted_projects:
        prj_id = prj["project_id"]
        prj_name = prj["project_name"]
        priority = prj.get("priority", "Medium")

        for req in prj["requirements"]:
            skill = req["skill"]
            min_prof = req["min_proficiency"]
            needed_hours = req["required_hours"]
            initial_needed = needed_hours

            # Identify candidates: has skill, proficiency >= min_prof, has simulated capacity > 0
            candidates = []
            for emp_id, avail_hrs in simulated_capacity.items():
                if avail_hrs > 0:
                    emp = emp_map[emp_id]
                    prof = emp.get("skills", {}).get(skill, 0)
                    if prof >= min_prof:
                        candidates.append((emp, prof, avail_hrs))

            # Rank candidates by proficiency (descending), then remaining capacity (descending)
            candidates.sort(key=lambda x: (x[1], x[2]), reverse=True)

            allocated_this_req = 0

            for candidate, prof, avail_hrs in candidates:
                if needed_hours <= 0:
                    break

                hours_to_assign = min(needed_hours, simulated_capacity[candidate["emp_id"]])
                if hours_to_assign > 0:
                    simulated_capacity[candidate["emp_id"]] -= hours_to_assign
                    needed_hours -= hours_to_assign
                    allocated_this_req += hours_to_assign

                    allocation_records.append({
                        "Project ID": prj_id,
                        "Project Name": prj_name,
                        "Priority": priority,
                        "Required Skill": skill,
                        "Min Prof.": min_prof,
                        "Recommended Employee": f"{candidate['name']} ({candidate['emp_id']})",
                        "Employee Dept": candidate["department"],
                        "Employee Proficiency": prof,
                        "Suggested Allocation (Hours)": hours_to_assign,
                        "Remaining Skill Gap": needed_hours
                    })

            # If no candidates or candidates could not fulfill all required hours
            if needed_hours > 0:
                unfulfilled_gaps.append({
                    "project_id": prj_id,
                    "project_name": prj_name,
                    "priority": priority,
                    "skill": skill,
                    "min_proficiency": min_prof,
                    "unmet_hours": needed_hours,
                    "initial_needed": initial_needed
                })
                # Add record showing remaining unallocated gap
                if allocated_this_req == 0:
                    allocation_records.append({
                        "Project ID": prj_id,
                        "Project Name": prj_name,
                        "Priority": priority,
                        "Required Skill": skill,
                        "Min Prof.": min_prof,
                        "Recommended Employee": "None (No Qualified Available Staff)",
                        "Employee Dept": "-",
                        "Employee Proficiency": 0,
                        "Suggested Allocation (Hours)": 0,
                        "Remaining Skill Gap": needed_hours
                    })

    df_allocations = pd.DataFrame(allocation_records) if allocation_records else pd.DataFrame()
    return df_allocations, unfulfilled_gaps, simulated_capacity

def generate_action_recommendations(projects, employees, unfulfilled_gaps, df_allocations):
    """
    Deterministic rule-based decision engine:
    1. ALLOCATE: Qualified employees with available bandwidth matched to project requirements.
    2. TRAIN: Gaps where employees have lower proficiency (prof < min_prof) or adjacent domain experience.
    3. HIRE: Critical remaining deficits where no qualified/trainable staff are available or capacity is depleted.
    """
    recommendations = []

    # 1. Successful Allocations Summary
    if not df_allocations.empty:
        valid_allocs = df_allocations[df_allocations["Suggested Allocation (Hours)"] > 0]
        for _, row in valid_allocs.iterrows():
            recommendations.append({
                "Context": f"{row['Project Name']} ({row['Priority']})",
                "Skill / Domain": row["Required Skill"],
                "Identified Problem": "Internal staffing requirement",
                "Action": "ALLOCATE",
                "Reason & Proposed Plan": (
                    f"Assign {row['Recommended Employee']} ({row['Suggested Allocation (Hours)']} hrs/wk). "
                    f"Meets proficiency level {row['Employee Proficiency']}/5."
                )
            })

    # 2 & 3. Address Unfulfilled Gaps with TRAIN or HIRE
    # Sort unfulfilled gaps so High priority projects come first
    prio_map = {"High": 1, "Medium": 2, "Low": 3}
    sorted_gaps = sorted(unfulfilled_gaps, key=lambda g: (prio_map.get(g["priority"], 4), -g["unmet_hours"]))

    for gap in sorted_gaps:
        prj_name = gap["project_name"]
        skill = gap["skill"]
        min_prof = gap["min_proficiency"]
        unmet_hours = gap["unmet_hours"]
        priority = gap["priority"]

        # Check for trainable employees (has the skill with proficiency > 0 but < min_prof, and has capacity)
        trainable_candidates = [
            emp for emp in employees
            if 0 < emp.get("skills", {}).get(skill, 0) < min_prof and emp["available_hours"] > 0
        ]
        # Sort trainable candidates by proficiency (highest first) and available hours
        trainable_candidates.sort(
            key=lambda e: (e.get("skills", {}).get(skill, 0), e["available_hours"]),
            reverse=True
        )

        if trainable_candidates:
            cand = trainable_candidates[0]
            current_prof = cand.get("skills", {}).get(skill, 0)
            recommendations.append({
                "Context": f"{prj_name} ({priority})",
                "Skill / Domain": skill,
                "Identified Problem": f"Deficit of {unmet_hours} hrs; candidate lacks required proficiency level {min_prof}.",
                "Action": "TRAIN",
                "Reason & Proposed Plan": (
                    f"Enroll {cand['name']} ({cand['department']}, current level {current_prof}/5) "
                    f"in target training to reach level {min_prof}/5. "
                    f"Has {cand['available_hours']} hrs/wk capacity. Note: Requires management approval and timeline evaluation."
                )
            })
        else:
            # No internal candidate has this skill or bandwidth -> recommend hiring
            recommendations.append({
                "Context": f"{prj_name} ({priority})",
                "Skill / Domain": skill,
                "Identified Problem": f"Critical unfulfilled gap of {unmet_hours} hrs; zero qualified internal capacity.",
                "Action": "HIRE",
                "Reason & Proposed Plan": (
                    f"Initiate external talent acquisition for Senior {skill} Specialist (minimum proficiency {min_prof}/5). "
                    f"Critical path for {priority}-priority project deadline."
                )
            })

    return pd.DataFrame(recommendations)

# -----------------------------------------------------------------------------
# Main Application Layout & Controller
# -----------------------------------------------------------------------------
def main():
    # Load foundational data
    employees = get_sample_employees()
    projects = get_sample_projects()

    # Calculate baseline available hours
    employees = calculate_employee_capacities(employees)

    # -------------------------------------------------------------------------
    # Sidebar Controls & Filters
    # -------------------------------------------------------------------------
    st.sidebar.title("🎛️ Control Panel")
    st.sidebar.markdown("**Workforce Intelligence Prototype**  \n*Rule-based heuristic analytics engine.*")
    st.sidebar.markdown("---")

    # Project selection dropdown
    project_options = ["All Projects"] + [p["project_name"] for p in projects]
    selected_project = st.sidebar.selectbox("🎯 Filter by Project", project_options)

    # Department selection dropdown
    dept_options = ["All Departments"] + sorted(list(set(e["department"] for e in employees)))
    selected_dept = st.sidebar.selectbox("🏢 Filter by Department", dept_options)

    st.sidebar.markdown("---")
    if st.sidebar.button("🔄 Re-run Workforce Analysis", use_container_width=True):
        st.toast("Workforce analysis recalculated!", icon="✅")

    st.sidebar.info(
        "💡 **How this system works:**\n"
        "- Deterministic matching based on skill proficiency and capacity.\n"
        "- Prevents double-allocation across multiple project tasks.\n"
        "- Rules: **ALLOCATE** qualified staff, **TRAIN** near-qualified staff, or **HIRE** external talent."
    )

    # Apply filters to dataset views
    filtered_projects = projects
    if selected_project != "All Projects":
        filtered_projects = [p for p in projects if p["project_name"] == selected_project]

    filtered_employees = employees
    if selected_dept != "All Departments":
        filtered_employees = [e for e in employees if e["department"] == selected_dept]

    # Compute models
    df_skills = run_skill_gap_analysis(filtered_projects, filtered_employees)
    df_allocations, unfulfilled_gaps, simulated_capacity = simulate_workforce_allocation(filtered_projects, employees)
    df_recommendations = generate_action_recommendations(filtered_projects, employees, unfulfilled_gaps, df_allocations)

    # -------------------------------------------------------------------------
    # Header & Overview
    # -------------------------------------------------------------------------
    st.title("👥 Workforce Capacity & Skill Gap Intelligence Dashboard")
    st.caption("Heuristic Decision-Support Prototype for Workforce Allocation, Capacity Modeling & Skill Gap Resolution")

    # -------------------------------------------------------------------------
    # 1. KPI Cards
    # -------------------------------------------------------------------------
    total_employees = len(filtered_employees)
    total_available_hours = sum(e["available_hours"] for e in filtered_employees)
    
    # Critical skill gaps (gap > 0 and gap % > 40%)
    critical_skill_gaps = int((df_skills["Skill Gap (Hours)"] > 0).sum()) if not df_skills.empty else 0
    
    # Projects at risk (projects having unfulfilled gaps)
    risk_project_ids = set(g["project_id"] for g in unfulfilled_gaps)
    projects_at_risk = len(risk_project_ids)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Employees", value=total_employees)
    with col2:
        st.metric(label="Available Capacity", value=f"{total_available_hours} hrs/wk")
    with col3:
        st.metric(label="Critical Skill Gaps", value=critical_skill_gaps, delta=f"{critical_skill_gaps} deficits" if critical_skill_gaps > 0 else "0", delta_color="inverse")
    with col4:
        st.metric(label="Projects at Risk", value=projects_at_risk, delta=f"{projects_at_risk} at risk" if projects_at_risk > 0 else "0", delta_color="inverse")

    st.markdown("---")

    # -------------------------------------------------------------------------
    # 2. Skill Gap Analysis
    # -------------------------------------------------------------------------
    st.header("📊 1. Skill Gap Analysis")
    st.markdown("Comparison of project-demanded skill hours against verified qualified workforce capacity (proficiency ≥ minimum required).")

    if not df_skills.empty:
        col_table, col_chart = st.columns([1.1, 0.9])

        with col_table:
            st.subheader("Skill Demand & Capacity Matrix")
            # Format display dataframe
            display_skills = df_skills[[
                "Skill", "Required Hours", "Qualified Available Hours", "Skill Gap (Hours)", "Gap (%)", "Status"
            ]]
            st.dataframe(display_skills, use_container_width=True, hide_index=True)

        with col_chart:
            st.subheader("Demand vs. Qualified Hours")
            chart_df = df_skills.set_index("Skill")[["Required Hours", "Qualified Available Hours"]]
            st.bar_chart(chart_df)
    else:
        st.warning("No skill requirements found for the selected filter combination.")

    st.markdown("---")

    # -------------------------------------------------------------------------
    # 3. Workforce Allocation
    # -------------------------------------------------------------------------
    st.header("🎯 2. Workforce Allocation Engine (Simulation)")
    st.markdown(
        "Suggested internal staffing simulation based on priority ranking, proficiency matching, and available bandwidth. "
        "*(Note: Suggested allocations are proposed simulations, avoiding double-counting of employee hours).* "
    )

    if not df_allocations.empty:
        # Filter allocation display if department filter is active
        display_alloc = df_allocations
        if selected_dept != "All Departments":
            display_alloc = display_alloc[
                (display_alloc["Employee Dept"] == selected_dept) | 
                (display_alloc["Recommended Employee"].str.contains("None", na=False))
            ]

        st.dataframe(
            display_alloc[[
                "Project Name", "Priority", "Required Skill", "Recommended Employee",
                "Employee Dept", "Suggested Allocation (Hours)", "Remaining Skill Gap"
            ]],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No allocations generated for current filter settings.")

    st.markdown("---")

    # -------------------------------------------------------------------------
    # 4. Action Recommendations (Rule-Based Decision Engine)
    # -------------------------------------------------------------------------
    st.header("📋 3. Strategic Action Recommendations")
    st.markdown(
        "Automated rule-based recommendations prioritizing high-impact gaps:  \n"
        "- **ALLOCATE**: Direct internal assignment when qualified capacity exists.  \n"
        "- **TRAIN**: Upskill candidates with adjacent skills or lower proficiency (requires management review).  \n"
        "- **HIRE**: External recruitment when internal capacity is zero or exhausted."
    )

    if not df_recommendations.empty:
        # Category filter for recommendations
        action_filter = st.radio(
            "Filter Recommendations by Action Type:",
            ["All Actions", "ALLOCATE", "TRAIN", "HIRE"],
            horizontal=True
        )

        filtered_recs = df_recommendations
        if action_filter != "All Actions":
            filtered_recs = filtered_recs[filtered_recs["Action"] == action_filter]

        st.dataframe(
            filtered_recs[["Action", "Context", "Skill / Domain", "Identified Problem", "Reason & Proposed Plan"]],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.success("No critical actions pending. Workforce capacity fully satisfies project demands.")

    # -------------------------------------------------------------------------
    # 5. Roster & Project Reference (Collapsible Reference)
    # -------------------------------------------------------------------------
    with st.expander("🔍 View Raw Employee Roster & Project Catalog"):
        tab1, tab2 = st.tabs(["Employees Roster", "Project Catalog"])

        with tab1:
            emp_display = []
            for e in filtered_employees:
                skills_str = ", ".join([f"{k} (Lv {v})" for k, v in e["skills"].items()])
                emp_display.append({
                    "ID": e["emp_id"],
                    "Name": e["name"],
                    "Department": e["department"],
                    "Weekly Hours": e["weekly_hours"],
                    "Allocated": e["allocated_hours"],
                    "Available Capacity": e["available_hours"],
                    "Skills": skills_str
                })
            st.dataframe(pd.DataFrame(emp_display), use_container_width=True, hide_index=True)

        with tab2:
            prj_display = []
            for p in filtered_projects:
                req_str = ", ".join([f"{r['skill']} (Lv {r['min_proficiency']}+, {r['required_hours']}h)" for r in p["requirements"]])
                prj_display.append({
                    "Project ID": p["project_id"],
                    "Project Name": p["project_name"],
                    "Department": p["department"],
                    "Priority": p["priority"],
                    "Deadline": p["deadline"],
                    "Skill Demands": req_str
                })
            st.dataframe(pd.DataFrame(prj_display), use_container_width=True, hide_index=True)


if __name__ == "__main__":
    main()
