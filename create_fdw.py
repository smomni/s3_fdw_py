import logging
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from sqlalchemy_fdw import ForeignDataWrapper
from s3_fdw import S3Fdw

logger = logging.getLogger('s3_fdw_py')

if __name__ == '__main__':
    url = 'postgresql://pytest:pytest@localhost:5432/pytest'
    engine = create_engine(url)
    with engine.connect() as con:
        try:
            con.execute('CREATE EXTENSION multicorn;')
        except ProgrammingError as e:
            logger.warn(e)
        con.execute(
            """
            CREATE SERVER s3_fdw_srv FOREIGN DATA WRAPPER multicorn 
            options (wrapper 's3_fdw.S3Fdw');
            """
        )
