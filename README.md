# AWS OpenTelemetry Python Lambda layer

Provides the [AWS Distro for OpenTelemetry Lambda layer](https://aws-otel.github.io/docs/getting-started/lambda/lambda-python) packaged as a scratch Docker image.  This is so it can be easily added to container based Lambda functions:

```dockerfile
# Add the OpenTelemetry Python Lambda layer as a build stage
FROM public.ecr.aws/cds-snc/opentelemetry-python-lambda:1.7.1 as otel

FROM public.ecr.aws/lambda/python:3.8

# Copy in the OpenTelemetry dependencies
COPY --from=otel /opt /opt
```
