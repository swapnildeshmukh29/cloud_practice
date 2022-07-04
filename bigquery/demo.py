from pyspark.sql import SparkSession
from email import message
from email.message import EmailMessage
import smtplib

import email_sent

if __name__ == '__main__':
    spark=SparkSession.builder.master("local[*]").appName("Mail demo").getOrCreate()

    df=spark.read.csv(r"C:\Users\user\PycharmProjects\cloud_practice\emp.csv",header=True,inferSchema=True)
    df.show()
    col_count=len(df.columns)

    with open("df_metadata.txt","w") as f:
        dict={"col_count":col_count}
        f.write(str(dict))

    mydict={}
    s=""
    with open("df_metadata.txt","r") as f:
        while(True):
            s=f.read()
            if s=="":
                break

            # singleword=s.split(":")
            # mydict.update({singleword[0]:singleword[1]})

        print(s)

    if col_count>2:

        senderemail = "bhagyashrideshmukh0328@gmail.com"

        message = "this was sent by python"

        password = "agkqivwdgbcnbojf"  # tumblerpas

        contacts1 = ['pasalkarb1996@gmail.com']


        email_sent.email_send(senderemail,password,"application",message,contacts1)
    else:
        print("no change")
