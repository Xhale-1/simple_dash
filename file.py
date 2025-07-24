import plotly.express as px
import pandas as pd
import streamlit as st  # Добавляем Streamlit

# Заголовок дашборда
st.title("Население городов России")

# Создаем тестовый DataFrame
data = pd.DataFrame({
    "Город": ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург"],
    "Население (млн)": [12.6, 5.4, 1.6, 1.5],
    "Достопримечательность": ["Кремль", "Эрмитаж", "Академгородок", "Плотинка"]
})

# Строим интерактивный бар-чарт
fig = px.bar(
    data,
    x="Город",
    y="Население (млн)",
    color="Город",
    title="Население городов России",
    hover_data=["Достопримечательность"],
    text="Население (млн)"
)

# Настраиваем hover (подсказки)
fig.update_traces(
    hovertemplate="<b>%{x}</b><br>Население: %{y} млн<br>Достопримечательность: %{customdata[0]}"
)

# Улучшаем внешний вид
fig.update_layout(
    plot_bgcolor="rgba(240,240,240,1)",
    paper_bgcolor="white",
    font=dict(family="Arial", size=12),
    hoverlabel=dict(bgcolor="white", font_size=12)
)

# Отображаем график в Streamlit
st.plotly_chart(fig, use_container_width=True)  # Ключевая строка!
