import pandas as pd
import pyodbc
import openpyxl
import requests
import os

from constants import connectionUser, sql_query
from constants import output_path, settlements_path

settlements = []

def get_settlements():

    for file in os.listdir(settlements_path):

        if file.endswith('.csv'):
            file_path = os.path.join(settlements_path, file)

            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path, sep=";")

            # Append the DataFrame to the combined_data DataFrame
            settlements.append(df)

            settlements_all = pd.concat(settlements, ignore_index=True)

            settlements_all = settlements_all[["MERCHANT_ACCOUNT", "BATCH_NUMBER", "ORDER_REF", "GROSS"]]

            settlements_all = settlements_all.rename(columns={"GROSS":"AMOUNT_GATEWAY"})

    return settlements_all


def get_netsuite():

    conn = pyodbc.connect(connectionUser)
    netsuite = pd.read_sql_query(sql_query, conn)

    netsuite = netsuite.groupby(["MERCHANT_ACCOUNT", "BATCH_NUMBER", "ORDER_REF"]).agg({"AMOUNT":sum}).reset_index()
    netsuite = netsuite.rename(columns={"AMOUNT": "AMOUNT_NETSUITE"})

    return netsuite

def get_data(netsuite, settlements_all):

    data = pd.merge(netsuite, settlements_all[["ORDER_REF", "AMOUNT_GATEWAY"]], on="ORDER_REF", how="outer")

    return data


if __name__ == '__main__':

    netsuite = get_netsuite()
    settlements_all = get_settlements()
    data = get_data(netsuite, settlements_all)
    data.to_excel(output_path, index=False)
    print(data.head(5))