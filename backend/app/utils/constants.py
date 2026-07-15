"""
Application-wide constants for NexusFlow.
"""

# ==========================================================
# Logging
# ==========================================================

SEPARATOR = "=" * 60

# ==========================================================
# API
# ==========================================================

API_VERSION = "v1"

# ==========================================================
# Dataset Status
# ==========================================================

STATUS_ACTIVE = "ACTIVE"
STATUS_INACTIVE = "INACTIVE"
STATUS_ARCHIVED = "ARCHIVED"

# ==========================================================
# Dataset Source Types
# ==========================================================

SOURCE_POSTGRESQL = "POSTGRESQL"
SOURCE_MYSQL = "MYSQL"
SOURCE_SQLSERVER = "SQLSERVER"
SOURCE_ORACLE = "ORACLE"
SOURCE_MONGODB = "MONGODB"
SOURCE_CSV = "CSV"
SOURCE_JSON = "JSON"
SOURCE_PARQUET = "PARQUET"
SOURCE_EXCEL = "EXCEL"
SOURCE_API = "API"

# ==========================================================
# Storage Types
# ==========================================================

STORAGE_LOCAL = "LOCAL"
STORAGE_MINIO = "MINIO"
STORAGE_S3 = "S3"
STORAGE_HDFS = "HDFS"

# ==========================================================
# File Formats
# ==========================================================

FORMAT_CSV = "CSV"
FORMAT_JSON = "JSON"
FORMAT_PARQUET = "PARQUET"
FORMAT_AVRO = "AVRO"
FORMAT_ORC = "ORC"
FORMAT_EXCEL = "EXCEL"

# ==========================================================
# Default Values
# ==========================================================

DEFAULT_SCHEMA_VERSION = "1.0"