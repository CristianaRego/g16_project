from flask import render_template, session
from classes.subscriptions import Subscriptions
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import io
import base64

def apps_plot():
    engine = create_engine('sqlite:///' + filename + 'G16.db')
    df = pd.read_sql('Subscriptions', con=engine)

    df['start_date'] = pd.to_datetime(df['start_date'], errors='coerce')

    df = df[(df['start_date'].dt.year == 2025) & (df['start_date'].dt.month.isin([1, 2]))]

    df['mes'] = df['start_date'].dt.month.map({1: 'Janeiro', 2: 'Fevereiro'})
    df['mes'] = pd.Categorical(df['mes'], categories=['Janeiro', 'Fevereiro'], ordered=True)

    resultado = df.groupby(['mes', 'status']).size().unstack(fill_value=0)
    
    cores_personalizadas = ['skyblue', 'salmon', 'lightgreen', 'purple']

    fig, ax = plt.subplots()
    resultado.plot(kind='bar', ax=ax, width=0.7,color=cores_personalizadas)

    plt.xlabel('Mês')
    plt.ylabel('Número de Subscrições')
    plt.title('Subscrições por Status (Jan e Fev 2025)')
    plt.xticks(rotation=0)
    plt.legend(title='Status')
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    image = base64.b64encode(buf.getvalue()).decode('utf-8')

    return render_template("plot.html", image=image, ulogin=session.get("user"))