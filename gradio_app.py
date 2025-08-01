import gradio as gr
import joblib
import numpy as np

# Load trained model and scaler
scaler = joblib.load("scaler.pkl")
model = joblib.load("kmeans_model.pkl")

# Segment descriptions
segment_descriptions = {
    0: "💎 **Loyal Customers**: Frequent, recent buyers with high spend.",
    1: "🧊 **At-Risk Customers**: Haven’t purchased in a while. Medium spend.",
    2: "🔥 **Potential Loyalists**: Medium recency and frequency. Growing value.",
    3: "🧪 **Recent High Spenders**: Purchased recently and spent a lot, but not frequent yet.",
    4: "😴 **Lost Customers**: Haven’t purchased for a long time. Low spend."
}

# Prediction function
def predict_segment(recency, frequency, monetary):
    input_scaled = scaler.transform([[recency, frequency, monetary]])
    cluster = model.predict(input_scaled)[0]
    description = segment_descriptions.get(cluster, "Unknown Segment")
    return f"Predicted Cluster: {cluster}\n\n{description}"

# Segment explanation markdown
info_md = """
### 📊 About Customer Segmentation
This dashboard uses **RFM Analysis (Recency, Frequency, Monetary)** to segment customers into different behavioral groups using clustering (KMeans).

**🟢 Recency**: Days since last purchase  
**🔵 Frequency**: Number of purchases  
**🟡 Monetary**: Total spending value  

### 💡 Segment Definitions
- **0 - Loyal Customers**: Frequent, recent, and high-spending customers.
- **1 - At-Risk**: Haven’t purchased recently, medium frequency and spend.
- **2 - Potential Loyalists**: Becoming regulars, decent frequency and spend.
- **3 - Recent Big Spenders**: High spenders who just started engaging.
- **4 - Lost Customers**: Inactive, low purchase behavior.

📥 Try entering sample RFM values to see the predicted segment!
"""

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Customer Segmentation using Clustering")
    gr.Markdown(info_md)

    with gr.Row():
        recency = gr.Number(label="Recency (days since last purchase)", value=90)
        frequency = gr.Number(label="Frequency (number of purchases)", value=10)
        monetary = gr.Number(label="Monetary (total spend)", value=500)

    submit_btn = gr.Button("Predict Segment")
    output = gr.Textbox(label="Segment Prediction", lines=5)

    submit_btn.click(fn=predict_segment, inputs=[recency, frequency, monetary], outputs=output)

demo.launch()
