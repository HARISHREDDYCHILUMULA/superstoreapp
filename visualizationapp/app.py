from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = Flask(__name__)

data = pd.read_csv('SampleSuperstore.csv')

@app.route('/')
def index():
    return render_template('index.html', columns=data.columns)

@app.route('/chart', methods=['POST'])
def create_chart():
    visualization_type = request.form['visualization_type']
    selected_attributes = request.form.getlist('selected_attributes')

    chart_div = None

    if visualization_type == 'scatter':
        if len(selected_attributes) >= 2:
            fig = px.scatter(data, x=selected_attributes[0], y=selected_attributes[1], title='Scatter Plot')
            chart_div = fig.to_html(full_html=False)
    elif visualization_type == 'pie':
        if selected_attributes:
            pie_data = data[selected_attributes[0]].value_counts()
            fig = px.pie(pie_data, values=pie_data.values, names=pie_data.index, title='Pie Chart')
            chart_div = fig.to_html(full_html=False)
    elif visualization_type == 'bar':
        if len(selected_attributes) >= 2:
            fig = px.bar(data, x=selected_attributes[0], y=selected_attributes[1], title='Bar Chart')
            chart_div = fig.to_html(full_html=False)
    elif visualization_type == 'line':
        if len(selected_attributes) >= 2:
            fig = px.line(data, x=selected_attributes[0], y=selected_attributes[1], title='Line Chart')
            chart_div = fig.to_html(full_html=False)
    elif visualization_type == 'boxplot':
        if selected_attributes:
            fig = go.Figure()
            for attribute in selected_attributes:
                fig.add_trace(go.Box(x=data[attribute], name=f'Box Plot {attribute}'))
            fig.update_layout(title='Box Plot')
            chart_div = fig.to_html(full_html=False)
    elif visualization_type == 'columnchart':
        if len(selected_attributes) >= 2:
            fig = px.bar(data, x=selected_attributes[0], y=selected_attributes[1], title='Column Chart')
            chart_div = fig.to_html(full_html=False)
        else:
            chart_div = None
    elif visualization_type == 'areachart':
        if selected_attributes:
            fig = px.area(data, x=data.index, y=selected_attributes[0], title='Area Chart')
            chart_div = fig.to_html(full_html=False)

    return render_template('index.html', chart_div=chart_div, columns=data.columns)

if __name__ == '__main__':
    app.run(debug=True)
