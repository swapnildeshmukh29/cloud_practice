from google.cloud import bigquery
if __name__ == '__main__':
    objclient=bigquery.Client()

    view_id="fluent-anagram-351206.bwt_practice_bq.empviewbypycharm"
    source_id ="fluent-anagram-351206.bwt_practice_bq.emp1"
    view=bigquery.Table(view_id)
    view.view_query=f"select * from {source_id} where gender='M'"
    view=objclient.create_table(view)
    print(f"Created {view.table_type}: {str(view.reference)}")