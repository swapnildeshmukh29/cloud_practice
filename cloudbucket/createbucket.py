from google.cloud import storage
import os
os.environ["GCLOUD_PROJECT"] = "fluent-anagram-351206"
if __name__ == '__main__':
    storage_client=storage.Client()
    # bucket=storage_client.bucket("bwt-practice-createbucket1")
    # bucket.storage_class='STANDARD'
    # new_bucket=storage_client.create_bucket(bucket,location="US")
    # print("Bucket name:-"+str(new_bucket.name))
    # print("Bucket Storage class:-" + str(new_bucket.storage_class))
    # print("Bucket Location:-" + str(new_bucket.location))

    print("Bucket list")
    bucket_list=storage_client.list_buckets()

    for buc in bucket_list:
        print(buc.name)

    print("Bucket information")
    bucket_info=storage_client.get_bucket("bwt-seesion-createbucket")
    print("Bucket id=",bucket_info.id)
    print("Bucket storage class =", bucket_info.storage_class)
    print("Bucket location =", bucket_info.location)

    # #copy from one bucket to another bucket
    # source_bucket=storage_client.bucket('bwt_practice_bucket-1')
    # source_blob=source_bucket.blob('input_data/annual-enterprise-survey-financial-year-provisional_2022_05_21.csv')
    # dest_bucket=storage_client.bucket('bwt-seesion-createbucket')
    # blob_copy=source_bucket.copy_blob(source_blob,dest_bucket)
    # print("src blob name:"+str(source_blob.name))
    # print("src bucket name:" + str(source_bucket.name))
    # print("destination blob name:" + str(dest_bucket.name))
    # print("dest blob name:" + str(blob_copy.name))
    #
    # move from one bucket to another bucket
    # source_bucket = storage_client.bucket('bwt_practice_bucket-1')
    # source_blob = source_bucket.blob('input_data/annual-enterprise-survey-financial-year-provisional_2022_05_21.csv')
    # dest_bucket = storage_client.bucket('bwt-seesion-createbucket')
    # blob_copy = source_bucket.copy_blob(source_blob, dest_bucket)
    # # delete the old destination
    # source_blob.delete()
    # print("deleted")
    #
    # print("Blob info")
    # blobs=storage_client.list_blobs("bwt_practice_bucket-1")
    # for blob in blobs:
    #     print(blob.name)



    # print("delete bucket")
    # bucket_to_delete=storage_client.get_bucket("bwt_new_bucket-2")
    # #for deleting empty bucket
    # # bucket_to_delete.delete()
    # #for deleteing non empty bucket
    # # bucket_to_delete.delete(force=True)
    # # print(bucket_to_delete.name, " Deleted ")
    # #for deleting objects in bucket
    # # blob=bucket_to_delete.blob("input_data1/")
    # # blob.delete()

