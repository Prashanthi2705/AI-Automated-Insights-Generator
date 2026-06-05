import statistics

# Sample Business Data
sales = [100, 120, 130, 125, 140, 150, 160, 300, 170, 180, 190, 200, 210, 220, 230]

print("=" * 50)
print("      AI AUTOMATED INSIGHTS GENERATOR")
print("=" * 50)

# -----------------------------
# KPI Monitoring
# -----------------------------
current_sales = sales[-1]
average_sales = statistics.mean(sales)

print("\n📊 KPI MONITORING")
print(f"Current Sales : {current_sales}")
print(f"Average Sales : {average_sales:.2f}")

# -----------------------------
# Trend Detection
# -----------------------------
first_half = statistics.mean(sales[:len(sales)//2])
second_half = statistics.mean(sales[len(sales)//2:])

print("\n📈 TREND ANALYSIS")

if second_half > first_half:
    trend = "UPWARD"
    print("Sales are showing an UPWARD trend.")
else:
    trend = "DOWNWARD"
    print("Sales are showing a DOWNWARD trend.")

# -----------------------------
# Anomaly Detection
# -----------------------------
mean = statistics.mean(sales)
stdev = statistics.stdev(sales)

anomalies = []

for value in sales:
    if abs(value - mean) > 2 * stdev:
        anomalies.append(value)

print("\n🚨 ANOMALY DETECTION")

if anomalies:
    print("Anomalies Found:", anomalies)
else:
    print("No anomalies detected.")

# -----------------------------
# Forecasting
# -----------------------------
growth = []

for i in range(1, len(sales)):
    growth.append(sales[i] - sales[i - 1])

avg_growth = statistics.mean(growth)

forecast = sales[-1] + avg_growth

print("\n🔮 PREDICTIVE FORECASTING")
print(f"Predicted Next Sales Value : {forecast:.2f}")

# -----------------------------
# Real-Time Alerts
# -----------------------------
print("\n⚠️ REAL-TIME ALERTS")

if current_sales > average_sales * 1.20:
    print("Alert: Sales significantly above average.")
elif current_sales < average_sales * 0.80:
    print("Alert: Sales significantly below average.")
else:
    print("Sales are within normal range.")

# -----------------------------
# Natural Language Insight
# -----------------------------
print("\n📝 AI GENERATED INSIGHT")

insight = f"""
Business Summary:
• Current Sales = {current_sales}
• Average Sales = {average_sales:.2f}
• Trend = {trend}
• Forecast Next Value = {forecast:.2f}

Recommendations:
• Continue KPI monitoring.
• Investigate unusual spikes or drops.
• Use forecasting results for future planning.
• Improve decision-making using automated insights.
"""

print(insight)

# -----------------------------
# Business Impact
# -----------------------------
print("🎯 BUSINESS IMPACT")
print("✔ Reduced manual analysis effort")
print("✔ Faster decision making")
print("✔ Automatic trend detection")
print("✔ Predictive business planning")
print("✔ Smart KPI monitoring")

print("\nProject Execution Successful!")
