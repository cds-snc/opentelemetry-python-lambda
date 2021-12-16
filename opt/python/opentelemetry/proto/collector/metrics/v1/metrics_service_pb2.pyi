"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import opentelemetry.proto.metrics.v1.metrics_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ExportMetricsServiceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_METRICS_FIELD_NUMBER: builtins.int
    @property
    def resource_metrics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[opentelemetry.proto.metrics.v1.metrics_pb2.ResourceMetrics]:
        """An array of ResourceMetrics.
        For data coming from a single resource this array will typically contain one
        element. Intermediary nodes (such as OpenTelemetry Collector) that receive
        data from multiple origins typically batch the data before forwarding further and
        in that case this array will contain multiple elements.
        """
        pass
    def __init__(self,
        *,
        resource_metrics : typing.Optional[typing.Iterable[opentelemetry.proto.metrics.v1.metrics_pb2.ResourceMetrics]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_metrics",b"resource_metrics"]) -> None: ...
global___ExportMetricsServiceRequest = ExportMetricsServiceRequest

class ExportMetricsServiceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___ExportMetricsServiceResponse = ExportMetricsServiceResponse
