from urllib.parse import quote_plus


class Config:
    ODBC_CONNECTION_STRING = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        r"SERVER=localhost\SQLEXPRESS;"
        "DATABASE=CommercialVehicleHealth;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc:///?odbc_connect="
        + quote_plus(ODBC_CONNECTION_STRING)
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False