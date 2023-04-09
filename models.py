from sqlalchemy import MetaData, Table, Column, Integer, String


metadata = MetaData()

records = Table(
    "records",
    metadata,
    Column("call_id", Integer, primary_key=True),
    Column("url", String, nullable=False),
)
