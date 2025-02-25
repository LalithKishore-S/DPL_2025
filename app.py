import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pyvis.network import Network
import networkx as nx


driver_performance_q1 = pd.read_csv("Data_streamlit/driver_performance_q1.csv")
constructor_performance_q1 = pd.read_csv("Data_streamlit/constructor_performance_q1.csv")
latest_constructor_q1 = pd.read_csv("Data_streamlit/latest_constructor_standings_q1.csv")
top_drivers_q2 = pd.read_csv("Data_streamlit/top_drivers_positions_q2.csv")
temp_q2 = pd.read_csv("Data_streamlit/temp_q2.csv")
temp1_q3 = pd.read_csv("Data_streamlit/optimal_pits_q3.csv")
temp_q4 = pd.read_csv("Data_streamlit/toph2h_q4.csv")
temp1_q5 = pd.read_csv("Data_streamlit/dbs_q5.csv")
temp2_q5 = pd.read_csv("Data_streamlit/cbs_q5.csv")
temp3_q5 = pd.read_csv("Data_streamlit/das_q5.csv")
temp4_q5 = pd.read_csv("Data_streamlit/cas_q5.csv")
temp_q6 = pd.read_csv("Additional_data/network_teams.csv")
temp1_q8 = pd.read_csv("Data_streamlit/q8.csv")
temp1_q9 = pd.read_csv("Data_streamlit/q9_1.csv")
temp2_q9 = pd.read_csv("Data_streamlit/q9_2.csv")
temp_q10 = pd.read_csv("Data_streamlit/q10.csv")
temp1_q11 = pd.read_csv("Data_streamlit/q11_1.csv")
temp2_q11 = pd.read_csv("Data_streamlit/q11_2.csv")
temp1_q12 = pd.read_csv("Data_streamlit/q12_1.csv")
temp2_q12 = pd.read_csv("Data_streamlit/q12_2.csv")
temp1_q13 = pd.read_csv("Data_streamlit/q13_1.csv")
temp2_q13 = pd.read_csv("Data_streamlit/q13_2.csv")
temp3_q13 = pd.read_csv("Data_streamlit/q13_3.csv")
temp_q16 = pd.read_csv("Data_streamlit/q16.csv")
temp2_q16 = pd.read_csv("Data_streamlit/q16_2.csv")
# Streamlit UI
st.title("F1 Data Analysis Dashboard")

st.sidebar.title("Select Analysis")
analysis_option = st.sidebar.radio(
    "Choose an analysis:",
    [
        "Driver & Constructor Performance",
        "Qualifying vs Race Performance",
        "Pit Stop Strategies",
        "Head-to-Head Rivalries",
        "Driver Swap Impact Analysis",
        "Driver Movements & Team Networks",
        "Driver Consistency in Race Performance",
        "Lap time efficiency",
        "Best Team Lineup",
        "2025 Season Predictions",
        "Struggling Teams Analysis",
        "Driver-Specific Track Struggles",
        "Championship Retention Probability",
        "Champion Age Trends",
        "Hypothetical Driver Transfers(Bonus qn)",
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

def qualifying_race_perforance():
    st.subheader("Qualifying vs Race Performance")
    st.subheader("Correlation analysis : ")
    st.image("Data_streamlit\img1_q2.png")
    st.write("The above indicates that there does not exist much of a linear relationship b/w starting grid and finishing position.But we cant also ignore the fact that there is some(minimal) positive correlation which suggests that lower the starting position lower maybe the finishing position.")
    st.image("Data_streamlit\img2_q2.png")
    st.write("Indicates that mostly driver either gain or stay in same position.")
    st.image("Data_streamlit\img3_q2.png")
    st.write("Indictaes that drivers having smaller starting positions or grids tend to finish at the top mostly.")
    st.write(top_drivers_q2.head(10))
    st.write("This indicates that some drivers tend to do better performance at races to have maximum position change (end-start) compared to others.But we cannot say if they are best as some drivers who start and finish near the same position gets a low position change.But the above are the people who does best when it comes to making up positions.")
    st.subheader("Drivers who make up the top 3 grids most number of times")
    st.write(temp_q2['Name'].value_counts().head(10))
    st.write("The above are the list of drivers who tend to perform well at qualifications to get top 3 grid locations.")
    
def display_pit_stop_analysis():
    st.subheader("Pit Stop Strategies")
    st.subheader("Most Common Finishing Position by Pit Stop Count:")
    st.write(temp1_q3)
    st.write("The above table shows the mode position attained by the drivers for each number of total pitstops.")
    st.subheader("Correlation analysis :")
    st.image("Data_streamlit/img1_q3.png")
    st.write("No direct linear relationship between total pit stops, total pit stop time and position can be inferred from the correlation matrix.So we go for ANOVA test.")
    st.subheader("ANOVA analysis :")
    st.write("H₀ (Null Hypothesis): No difference in finishing positions across different pit stop time groups.\nH₁ (Alternative Hypothesis): At least one group has significantly different finishing positions.")
    st.write("ANOVA Test: F-statistic = 12.434, F-critical = 2.997 ")
    st.write("Reject H0: Significant difference in finishing position based on pit stop time!")
    
def display_h2h():
    st.subheader("Top 10 F1 Rivalries : ")
    st.write(temp_q4.head(10))
    st.write("We have top rivalries when even after a considerable number of matches the win ratio or probability between the drivers must be almost equal indicating an equal potential or greater competition. Thus from the above table, we can infer the top rivalries filtered by win ratio in 0.50±0.05 interval.")

def display_driver_swaps():
    driver1 = 'max verstappen'
    driver2 = 'fernando alonso'
    st.subheader("Hypothetical driver swap analysis : ")
    st.write("Understanding the result of swapping two driver’s teams in a season")
    st.write("Here we take driver1 = 'max Verstappen' driver2 = 'fernando alonso' in the year 2015")
    st.subheader("Driver Standings before Swap:")
    st.write(temp1_q5.head(10))
    st.write('max verstappen')
    st.write(temp1_q5[temp1_q5['Name']==driver1])
    st.write('fernando alonso')
    st.write(temp1_q5[temp1_q5['Name']==driver2])
    st.subheader("constructor Standings before Swap:")
    st.write(temp2_q5.head(10))
    st.subheader('toro rosso')
    st.write(temp2_q5[temp2_q5['constructor_name']=='toro rosso'])
    st.write('mclaren')
    st.write(temp2_q5[temp2_q5['constructor_name']=='mclaren'])
    
    
    st.subheader("Driver Standings after Swap:")
    st.write(temp3_q5.head(10))
    st.write('max verstappen')
    st.write(temp3_q5[temp3_q5['Name']==driver1])
    st.write('fernando alonso')
    st.write(temp3_q5[temp3_q5['Name']==driver2])
    st.subheader("constructor Standings after Swap:")
    st.write(temp4_q5.head(10))
    st.subheader('toro rosso')
    st.write(temp4_q5[temp4_q5['constructor_name']=='toro rosso'])
    st.write('mclaren')
    st.write(temp4_q5[temp4_q5['constructor_name']=='mclaren'])
    st.write("It can be seen that swapping teams of players can lead to complete change in constructor rankings if a driver being swapped is of high dominance.From the updated stats we can clearly see that the driver standings does not change as we do not affect  individuals performance by swapping teams and also assuming all other factors like pit stop strategies are almost same for the swapped teams. Also we can see that by swapping teams of a higher ranked driver like max verstappen with team of low ranked driver(comparitively) like fernandez leads to a drastic change in constructor standings.The rankings between the teams is inverted.")

    
def display_team_transitions():
    st.subheader("Driver Movements & Team Networks")
    st.write("Network Data :")
    st.write(temp_q6.head(10))
    graph = nx.from_pandas_edgelist(temp_q6,'From','To')
    nx.draw_networkx(graph)
    pyvis_graph = Network(height="700px", width="100%",directed=True)
    for node in graph.nodes():
        pyvis_graph.add_node(node, label=node,size=20, font={'size': 15})  
    for edge in graph.edges():
        pyvis_graph.add_edge(edge[0], edge[1])
    pyvis_graph.set_edge_smooth('dynamic')
    pyvis_graph.show_buttons()
    pyvis_graph.write_html("basic.html", open_browser=True)

def display_driver_consistency():
    st.subheader("Driver consistency analysis :")
    st.write("Most Consistent Drivers (Low Variance in Position):")
    st.write(temp1_q8[['forename', 'surname','avg_position', 'std_dev_position', 'total_races']].head(10))
    st.write("Least Consistent Drivers (High Variance in Position):")
    st.write(temp1_q8[['forename', 'surname','avg_position', 'std_dev_position', 'total_races']].tail(10))
    st.write("Here , Kevin is the most consistent since he has the lowest standard deviation . Gerhard is the least consistent since he has the highest standard deviation.")
    
def lap_time_eff():
    st.subheader("Lap time Efficiency : ")
    st.write("Lap Time Efficiency Across Circuits:")
    st.write(temp1_q9[['name_circuit', 'name_constructor', 'avg_lap_time', 'total_laps']])
    st.write("Rb F1 Team has the lowest average lap time of 84876.47 ms in the Albert Park Grand Prix Circuit.")
    st.write("Most Efficient Team (Lowest Average Lap Time):")
    st.write(temp2_q9)
    st.write("Overall average lap time for each constructor")
    st.image("Data_streamlit/img1_q9.png")
    st.write("This indicates that Jaguar has the lowest average lap time from which  may indicate that they have better pit stop strategies and efficient driver guiding during the races.")
    
def best_team_lineup():
    st.subheader("Best Team Lineup Based on Performance Trends:")
    st.write(temp_q10[['forename', 'surname', 'total_points', 'avg_position', 'total_wins']])
    st.write("The best line up for a constructor based on various factors like total points,average finishing position and total wins")
    st.write("From the above we can infer that the best line up possibly is a team made of")
    st.write("      Max Verstappen and Lewis Hamilton")    
    

def display_2025_predictions():
    st.subheader("Predictions for 2025 Season")
    st.write("Assuming 2024 drivers alone and that they do not change their teams for the 2025 season.Also each season has many races and we will be aggregating the points earned in each match to get the final result and assuming their performance is similar to 2024.")
    st.subheader("Predicted 2025 Driver Rankings:")
    st.write(temp1_q11.head(10))
    st.subheader("Predicted 2025 constructor Rankings:")
    st.write(temp2_q11.head(10))
    st.write("From the data, we can expect Max Verstappen to win the 2025 season")
    st.write("As of constructors, McLaren is expected to win")
    
def display_struggling_teams():
    st.subheader("Struggling Teams Analysis")
    st.subheader("Drivers Most Likely to Struggle in 2025:")
    st.write(temp1_q12.head(2))
    st.subheader("Teams Most Likely to Struggle in 2025:")
    st.write(temp2_q12.iloc[1:6,:])
    st.write("We have considered the change in performance from 2024 to 2025 to retrieve struggling teams and drivers in 2025 season. According to the data Lando Norris is expected to struggle more in 2025 season (performance compared with 2024 season).")
    st.write("Also when it comes to a team Mercedes is expected to struggle more in 2025 season (performance compared with 2024 season).")
    
    
def display_track_performance():
    st.subheader("Driver-Specific Track Struggles")
    st.subheader("General : ")
    st.write(temp1_q13.head())
    st.write("From these we can say that Adolf Brudes struggles the most in the nürburgring circuit, concluded based on large avg position ,low average position and high DNF rate.")
    st.subheader("Driver Specific : ")
    st.write("driver = 'max verstappen'")
    st.write("Circuits where max verstappen struggles")
    st.write(temp2_q13)
    st.write("Circuits where max verstappen excels")
    st.write(temp3_q13)
    st.write("From these we can conclude that max verstappen struggles most in autodromo internazionale del mugello circuit.")
    st.write("Also, he is known to excel most in circuit park Zandvoort .")
    

def display_retention_probability():
    st.subheader("Championship Retention Probability")
    st.write("Overall Championship Retention Probability: 33.78%")
    st.image("Data_streamlit/img1_q14.png")
    st.write("From these, we can say that with probability 0.34 2024 champion will retain their championship in 2025.")
    st.write("Also from the historical decade trends of championship retention, we can see that the probability of retaining championships is increasing since the 1970s")

def display_champion_age_trends():
    st.subheader("Championship Age Trends")
    st.image("Data_streamlit/img_q15.png")
    st.write("From this, we can see that drivers most frequently win championships at around 30-35 years of age followed by 25-30. On the whole, we can say that most championships are won by drivers in the age group 25-35.")

def display_hypothetical_transfers():
    st.subheader("Hypothetical Driver Transfers")
    st.write("Markov Chain-Based Predictions for Driver Team Changes")
    st.subheader("Transition matrix sample:")
    st.write(temp_q16.head(10))
    st.subheader("driver = 'max verstappen'")
    st.write("Current team : Red Bull")
    st.write(temp2_q16)
    st.write("From the probability estimate it is seen that there is a probability of 0.33 for the driver to move from red bull to toro rosso.")
    


def view_power_bi_dashboard():
    pass
"""
    st.subheader("📊 Power BI Dashboard")
    st.markdown("[🔗 Click here to open Power BI Dashboard](your_dashboard_link_here)")"""

# Display results based on selection
if analysis_option == "Driver & Constructor Performance":
    display_driver_constructor_performance()
elif analysis_option == "Qualifying vs Race Performance":
    qualifying_race_perforance()
elif analysis_option == "Pit Stop Strategies":
    display_pit_stop_analysis()
elif analysis_option == "Head-to-Head Rivalries":
    display_h2h()
elif analysis_option == "Driver Movements & Team Networks":
    display_team_transitions()
elif analysis_option == "Driver Consistency in Race Performance":
    display_driver_consistency()
elif analysis_option == "Lap time efficiency":
    lap_time_eff()
elif analysis_option == "Best Team Lineup":
    best_team_lineup()
elif analysis_option == "2025 Season Predictions":
    display_2025_predictions()
elif analysis_option == "Struggling Teams Analysis":
    display_struggling_teams()
elif analysis_option == "Driver-Specific Track Struggles":
    display_track_performance()
elif analysis_option == "Championship Retention Probability":
    display_retention_probability()
elif analysis_option == "Champion Age Trends":
    display_champion_age_trends()
elif analysis_option == "Driver Swap Impact Analysis":
    display_driver_swaps()
elif analysis_option == "Hypothetical Driver Transfers(Bonus qn)":
    display_hypothetical_transfers()
elif analysis_option == "Power BI Dashboard":
    view_power_bi_dashboard()
