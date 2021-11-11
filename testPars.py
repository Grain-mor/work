import csv
import datetime
from solana.rpc.api import Client
from solana.rpc.async_api import AsyncClient
def write_to_file():
    solana_client = Client("https://api.velas.com")
    tmp = get_transaction_count()
    count_of_transaction = tmp['result']

    with open('NativeVel.csv') as File:
        myFile = csv.DictReader(File)
        row_count = sum(1 for row in myFile)

    now = datetime.datetime.now()
    date_to_csv = now.strftime("%d-%m-%Y %H:%M")

    myData = [[row_count, date_to_csv, int(count_of_transaction)]]

    myFile = open('NativeVel.csv', 'a')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)
write_to_file()

# def write_stats_count():
#     with open('Transaction_count.csv') as File:
#         myFile = csv.DictReader(File)
#         # row_count = sum(1 for row in myFile)
#         # for i in range(row_count):
#
#     with open('Transaction_count.csv') as File:
#         myFile = csv.DictReader(File)
#         row_count = sum(1 for row in File)
#         for i in myFile:
#             print(i)
# write_stats_count()
