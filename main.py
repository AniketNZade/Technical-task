import boto3
import mysql.connector

def read_from_s3(bucket_name, file_name):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    data = response['Body'].read()
    return data

def push_to_rds(data, db_host, db_user, db_password, db_name):
    try:
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO your_table (data) VALUES (%s)", (data,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Data pushed to RDS successfully.")
        return True
    except Exception as e:
        print("Failed to push data to RDS:", e)
        return False

def push_to_glue_database(data):
    try:
            glue_client = boto3.client('glue')
            glue_client.put_database_records(
                DatabaseName=glue_database,
                TableName="your_table",
                Records=[{"record": data}]
            )    
            
        print("Glue Database created successfully.")
        return True
    except Exception as e:
        print("Failed to push to Glue Database:", e)    
        return False
    

if _name_ == "_main_":
    bucket_name = "your-s3-bucket"
    file_name = "your-file.csv"
    db_host = "your-rds-host"
    db_user = "your-rds-username"
    db_password = "your-rds-password"
    db_name = "your-rds-database"

    data = read_from_s3(bucket_name, file_name)

    if not push_to_rds(data, db_host, db_user, db_password, db_name):
        push_to_glue_database(data)
