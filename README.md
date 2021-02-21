# cloud-api-abstractor

This API abstracts the Cloud APIs for AWS and Azure, by utilising Flask. The end goal is to be able to create resources on both clouds and be able to link them together from a single entry-point, ie peer a VPC and a VNET.

## Running & Testing the cloud-api-abstractor

# Running
```bash
python3 app/api.py -fp {PARAMETER_FILE_PATH}
```

# Testing
Tests are outstanding, the below is a placeholder
```bash
pytest -q test.py
```

## Building the cloud-api-abstractor in Docker
```bash
docker build -t app .
```

## Runing the cloud-api-abstractor in Docker

```bash
docker run -p 8080:8080 app
```