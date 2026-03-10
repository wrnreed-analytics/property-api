from setuptools import setup, find_packages

setup(
    name="property-api",
    version="1.0.0",
    author="Wren Reed",
    description="Production REST API for property valuation and market intelligence",
    url="https://github.com/wrnreed-analytics/property-api",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "fastapi>=0.95.0",
        "uvicorn[standard]>=0.21.0",
        "sqlalchemy>=2.0.0",
        "psycopg2-binary>=2.9.0",
        "redis>=4.5.0",
        "pydantic>=1.10.0",
    ],
)
