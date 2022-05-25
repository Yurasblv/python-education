"""Module for retrieve data from s3 minio ,
refactoring by translating to english and upload in database wia docker
"""

import os
import pandas as pd
import boto3
from boto3.session import Config
from sqlalchemy import create_engine


class RefactorData:
    """Main class for working with data and connection to minio"""

    def __init__(self,
                 host_url=os.environ['host'],
                 username=os.environ['user'],
                 password=os.environ['pwd'],
                 bucket=os.environ['bucket']):
        self.host_url = host_url
        self.username = username
        self.password = password
        self.bucket = bucket

    def __iter__(self):
        return self._read_minio_data()

    def __minio_connection(self):
        """Connect minio server"""
        s3_ = boto3.resource('s3',
                            config=Config(signature_version='s3v4'),
                            endpoint_url=self.host_url,
                            aws_access_key_id=self.username,
                            aws_secret_access_key=self.password,
                            )
        return s3_

    def _read_minio_data(self):
        """Reads folder from minio server"""
        my_bucket = self.__minio_connection().Bucket(self.bucket)
        for obj in my_bucket.objects.all():
            initial_df = pd.read_csv(obj.get()['Body'])  # 'Body' is a key word
            yield initial_df


    def save_to_postgre(self):
        """Renaming headers from italian to english"""
        for table in self._read_minio_data():
            table.rename(columns={
                'data': 'Date of notification',
                'stato': 'Country of reference',
                'codice_regione': 'Code of the Region',
                'denominazione_regione': 'Name of the Region',
                'codice_provincia': 'Code of the Province',
                'denominazione_provincia': 'Name of the Provine',
                'sigla_provincia': 'Province abbreviation',
                'lat': 'Latitude',
                'long': 'Longitude',
                'totale_casi': 'Total amount of positive cases',
                'note': 'Notes in italian language'
            }, inplace=True)
            psycopg2 = create_engine(
                    f"postgresql+psycopg2://postgres:{os.environ['psycopg2_pwd']}@database/postgres"
                 ).connect()
            table.to_sql('CovidStatsItaly', con=psycopg2, if_exists='replace')


rd = RefactorData()
