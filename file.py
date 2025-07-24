import plotly.express as px
import pandas as pd

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
    hover_data=["Достопримечательность"],  # Доп. информация при наведении
    text="Население (млн)"  # Отображаем значения на столбцах
)

# Настраиваем hover (подсказки)
fig.update_traces(
    hovertemplate="<b>%{x}</b><br>Население: %{y} млн<br>Достопримечательность: %{customdata[0]}"
)

# Улучшаем внешний вид
fig.update_layout(
    plot_bgcolor="rgba(240,240,240,1)",  # Светло-серый фон
    paper_bgcolor="white",  # Белый фон вокруг графика
    font=dict(family="Arial", size=12),
    hoverlabel=dict(bgcolor="white", font_size=12)
)

# Сохраняем в HTML (открывается в браузере)
fig.write_html("russia_cities.html")

# Показываем график в Jupyter/Colab (если нужно)
fig.show()
