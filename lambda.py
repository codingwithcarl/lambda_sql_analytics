import json
import boto3
import pandas as pd
import pymysql
import xlsxwriter
import io
import time


def lambda_handler(event, context):

    # Connect to the database
    conn = pymysql.connect(

        host='hostname',

        user='admin',

        password='pass',

        database='dbname'

    )

    # Run your queries
    queries = [

        """

        SELECT * FROM example;

        """,

        "SELECT * FROM query2;"

    ]

    # Execute the queries and append to the dataframe
    dfs = []

    for query in queries:
        df = pd.read_sql(query, conn)

        dfs.append(df)

    # Write the results to an Excel file
    sheet_names = [

        'Sheet 1',

        'Sheet 2'

    ]

    s3 = boto3.client('s3')

    today = time.strftime("%Y-%m-%d-%H-%M-%S")

    file_name = today + 'query-results.xlsx'

    with io.BytesIO() as output:

        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            for sheet_name, df in zip(sheet_names, dfs):
                df.to_excel(writer, sheet_name=sheet_name[:31], index=False)

        output.seek(0)

        s3.upload_fileobj(output, 's3-bucket-name', file_name)

    return {

        'statusCode': 200,

        'body': 'Results uploaded to S3 bucket'

    }
