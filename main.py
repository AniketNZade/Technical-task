import boto3
import mysql-connector-python

def read_data_from_s3(deploy15, http://deploy15.s3-website.ap-south-1.amazonaws.com):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=deploy15, Key=http://deploy15.s3-website.ap-south-1.amazonaws.com)
    data = response['Body'].read().decode('utf-8')
    return data

def push_to_rds(data):
    try:
        connection = mysql.connector.connect(
            host='database-1.c75jqxcklajk.ap-south-1.rds.amazonaws.com',
            user='admin',
            password='Password',
            database='database-1'
        )

        cursor = connection.cursor()

        query = "INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)"

        for row in data:
            cursor.execute(query, row)

        connection.commit()
        print("Data pushed to RDS successfully.")

    except Exception as e:
        print("Failed to push to RDS:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage:
data = [('value1', 'value2'), ('value3', 'value4')]  # Example data, replace it with your actual data
push_to_rds(data)


def push_to_glue(data):
    
    try:
        glue_client = boto3.client('glue')
        database_name = 'Project'
        glue_client.create_database(DatabaseInput={'Name': Project})
        print("Glue Database created successfully.")

    except Exception as e:
        print("Failed to push to Glue Database:", e)

# Example usage:
data = [('value1', 'value2'), ('value3', 'value4')]  # Example data, replace it with your actual data
push_to_glue(data)
 pass

if _name_ == "_main_":
    data = read_data_from_s3('deploy15', 'http://deploy15.s3-website.ap-south-1.amazonaws.com')
    try:
        push_to_rds(data)
    except Exception as e:
        print("Failed to push to RDS:", e)
        push_to_glue(data)
