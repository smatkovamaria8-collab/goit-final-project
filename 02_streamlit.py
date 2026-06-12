import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from keras.models import load_model
import streamlit as st
import tensorflow as tf
import joblib

scaler = joblib.load("scaler.pkl")

loaded_model = load_model("my_best_model.keras")

st.title("Прогнозування ймовірності відтоку клієнта")

st.write("Будь ласка, введіть дані про клієнта обираючи відповідь із наявних")

is_tv_sub = st.radio("Чи має підписку на телебачення", ["Ні", "Так"])
is_movie_sub = st.radio("Чи має підписку на пакет фільмів", ["Ні", "Так"])

st.write("Будь ласка, введіть дані про клієнта використовуючи поля для вводу (просимо писати лише числа)")

sub_age = st.number_input("Вкажіть термін підписки", min_value= 0.0, value= None, step=0.01)
bill_sum = st.number_input("Вкажіть його середній рахунок", min_value= 0.0, value= None, step=0.01)
left_contract = st.number_input("Вкажіть залишковий термін дії контракту", min_value= 0.0, value= None, step=0.01)
num_errors = st.number_input("Вкажіть кількість збоїв у сервері", min_value= 0.0, value= None, step=0.01)
num_downl = st.number_input("Вкажіть середню кількість завантажень", min_value= 0.0, value= None, step=0.01)
num_upload = st.number_input("Вкажіть середню кількість вивантажень", min_value= 0.0, value= None, step=0.01)
downl_overlim = st.number_input("Вкажіть кількість скачувань понад норму", min_value= 0.0, value= None, step=0.01)

coded_words = {
    "Ні" : 0,
    "Так" : 1}

encoded_tv_sub = coded_words[is_tv_sub]
encoded_movie_sub = coded_words[is_movie_sub]

all_variables = [encoded_tv_sub, encoded_movie_sub, sub_age, bill_sum, left_contract, num_errors,
                 num_downl, num_upload, downl_overlim]

if st.button("Спрогнозувати відтік"):
    if None in all_variables:
        st.warning("Ви не вказали повністю всі змінні, будь ласка введіть пропущені")
    else:
        st.success("Всі дані були успішно внесені")
        client_array = np.array([all_variables], dtype = float)
        client_array = scaler.transform(client_array)

        prediction = loaded_model.predict(client_array)
        prediction = float(prediction[0][0])
        leave_prediction = prediction * 100
        stay_prediction = 100 - leave_prediction

        st.write(f"Результат прогнозу:\n"
                 f"{leave_prediction:.2f}% - клієнт піде;\n"
                 f"{stay_prediction:.2f}% - клієнт залишиться")

        pred_plot = [stay_prediction, leave_prediction]
        labels = ["Залишиться", "Піде"]
        
        plt.clf()
        sns.barplot(x = labels, y = pred_plot, palette = ["mediumseagreen", "crimson"])
        plt.ylim(0, 100) 
        plt.xlabel("Ймовірний статус", fontsize="medium", color="midnightblue")
        plt.ylabel("Ймовірність", fontsize="medium", color="midnightblue")
        plt.title("Результати прогнозування клієнта", fontsize="medium", color="midnightblue")
        st.pyplot(plt)
