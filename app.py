import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


driver_performance_q1 = pd.read_csv("Data_streamlit/driver_performance_q1.csv")
constructor_performance_q1 = pd.read_csv("Data_streamlit/constructor_performance_q1.csv")
latest_constructor_q1 = pd.read_csv("Data_streamlit/latest_constructor_standings_q1.csv")
# Streamlit UI
st.title("🏎️ F1 Data Analysis Dashboard")

st.sidebar.title("Select Analysis")
analysis_option = st.sidebar.radio(
    "Choose an analysis:",
    [
        "Driver & Constructor Performance",
        "Head-to-Head Rivalries",
        "Driver Movements & Team Networks",
        "Championship Retention Probability",
        "Pit Stop Strategies",
        "Champion Age Trends",
        "Grid Position vs. Race Performance",
        "Struggling Teams Analysis",
        "Driver-Specific Track Struggles",
        "Driver Swap Impact Analysis",
        "Team Transition Matrix",
        "Hypothetical Driver Transfers",
        "2025 Season Predictions",
        "Power BI Dashboard"
    ]
)

def display_driver_constructor_performance():
    st.subheader("Driver & Constructor Performance")
    st.subheader("Dominant Drivers (based on win and podium ratio alone): ")
    st.write(driver_performance_q1.head(10))
    st.write("As per the question we used the win ratio and podium finishes ratio to determine the dominant(top 10) drivers and the above are the results. But the above is sensitive to career length and thus we also include total points(career length high => total points high) to determine the dominant racers.")
    st.subheader("Dominant drivers based on win ratio,podium ratio and total points: ")
    temp = driver_performance_q1.sort_values(by=['total_pts'],ascending=[False])
    temp = set(driver_performance_q1.head(10)['name']).intersection(set(temp.head(10)['name']))
    if temp:
        for driver in temp:
            st.write(f"- {driver}")
    else:
        st.write("No common drivers found in the top 10.")
        
    st.subheader("Dominant Constructors (based on win and podium ratio alone): ")
    st.write(constructor_performance_q1.head(10))
    st.subheader("Dominant constructors based on win ratio,podium ratio and total points: ")
    temp = latest_constructor_q1
    temp = set(constructor_performance_q1.head(10)['name']).intersection(set(temp.head(10)['name']))
    if temp:
        for driver in temp:
            st.write(f"- {driver}")
    else:
        st.write("No common drivers found in the top 10.")
    st.subheader("Career longetivity vs win metrics[wins,podiums,points]")
    st.subheader("Correlation analysis")
    st.image("Data_streamlit\img1_q1.png")
    st.write("From the above heatmap (correlation matrix) we can see that there some positive correlation between career length and all win measures, which shows that a high career length corresponds to high win measures but need not be the case always as indicated by the below scatter plots.")
    st.image("Data_streamlit\img2_q1.png")
    st.image("Data_streamlit\img3_q1.png")
    

def display_h2h():
    pass
"""
    st.subheader("🤜 Head-to-Head Rivalries")
    st.write(h2h_results.head(10))
    st.image("outputs/h2h_plot.png")"""

def display_team_transitions():
    pass
"""
    st.subheader("🔗 Driver Movements & Team Networks")
    st.write(team_transitions.head(10))
    st.image("outputs/team_transitions_plot.png")
"""
def display_retention_probability():
    pass
"""
    st.subheader("🏆 Championship Retention Probability")
    st.write(retention_prob)
    st.image("outputs/championship_retention_plot.png")
    """

def display_pit_stop_analysis():
    pass
"""
    st.subheader("🛠️ Pit Stop Strategies")
    st.write(pit_stop_analysis.head(10))
    st.image("outputs/pit_stop_analysis.png")"""

def display_champion_age_trends():
    pass
"""
    st.subheader("📅 Championship Age Trends")
    st.write(champion_age_trends.head(10))
    st.image("outputs/age_trend_plot.png")
    """

def display_grid_position_analysis():
    pass
"""
    st.subheader("🏁 Grid Position vs. Race Performance")
    st.write(driver_grid_analysis.head(10))
    st.image("outputs/grid_performance.png")
    """

def display_struggling_teams():
    pass
"""
    st.subheader("📉 Struggling Teams Analysis")
    st.write(struggling_teams.head(10))
    st.image("outputs/struggling_teams_plot.png")"""

def display_track_performance():
    pass
"""
    st.subheader("🏎️ Driver-Specific Track Struggles")
    st.write(track_performance.head(10))
    st.image("outputs/track_performance_plot.png")"""

def display_driver_swaps():
    pass
"""
    st.subheader("🔄 Hypothetical Driver Swaps")
    st.write(driver_swaps.head(10))
    st.image("outputs/driver_swaps_plot.png")"""

def display_transition_matrix():
    pass
"""
    st.subheader("🔀 Team Transition Matrix")
    st.write(driver_transition_matrix.head(10))
    st.image("outputs/team_transition_matrix_plot.png")
    """

def display_hypothetical_transfers():
    pass
"""
    st.subheader("🚀 Hypothetical Driver Transfers")
    st.write("🔗 **Markov Chain-Based Predictions for Driver Team Changes**")
    st.write(driver_transition_matrix.head(10))
    st.image("outputs/hypothetical_transfers.png")
    """

def display_2025_predictions():
    pass
"""
    st.subheader("📊 Predictions for 2025 Season")
    st.write(championship_predictions.head(10))
    st.image("outputs/2025_predictions.png")"""

def view_power_bi_dashboard():
    pass
"""
    st.subheader("📊 Power BI Dashboard")
    st.markdown("[🔗 Click here to open Power BI Dashboard](your_dashboard_link_here)")"""

# Display results based on selection
if analysis_option == "Driver & Constructor Performance":
    display_driver_constructor_performance()
elif analysis_option == "Head-to-Head Rivalries":
    display_h2h()
elif analysis_option == "Driver Movements & Team Networks":
    display_team_transitions()
elif analysis_option == "Championship Retention Probability":
    display_retention_probability()
elif analysis_option == "Pit Stop Strategies":
    display_pit_stop_analysis()
elif analysis_option == "Champion Age Trends":
    display_champion_age_trends()
elif analysis_option == "Grid Position vs. Race Performance":
    display_grid_position_analysis()
elif analysis_option == "Struggling Teams Analysis":
    display_struggling_teams()
elif analysis_option == "Driver-Specific Track Struggles":
    display_track_performance()
elif analysis_option == "Driver Swap Impact Analysis":
    display_driver_swaps()
elif analysis_option == "Team Transition Matrix":
    display_transition_matrix()
elif analysis_option == "Hypothetical Driver Transfers":
    display_hypothetical_transfers()
elif analysis_option == "2025 Season Predictions":
    display_2025_predictions()
elif analysis_option == "Power BI Dashboard":
    view_power_bi_dashboard()
