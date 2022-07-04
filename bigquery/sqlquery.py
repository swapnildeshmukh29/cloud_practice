from google.cloud import bigquery
if __name__ == '__main__':
    clientobj=bigquery.Client()

    query="""
    SELECT  gender,sum(salary) as salary FROM bwt_practice_bq.emp1 group by gender
    """

    query_exe=clientobj.query(query)

    for i in query_exe:
        print(i)