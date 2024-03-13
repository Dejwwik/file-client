import grpc
import service_file_pb2
import service_file_pb2_grpc

def create_stub(grpc_server):
    """Create gRPC stub."""
    channel = grpc.insecure_channel(grpc_server)
    stub = service_file_pb2_grpc.FileStub(channel)
    return stub

def grpc_stat(uuid, grpc_server):
    """Retrieve file metadata using gRPC."""
    # Create gRPC stub
    stub = create_stub(grpc_server)
    
    # Create Uuid message
    uuid_message = service_file_pb2.Uuid(value=uuid)
    
    # Create StatRequest message
    request = service_file_pb2.StatRequest(uuid=uuid_message)

    try:
        # Make gRPC call to retrieve file metadata
        response = stub.stat(request)

        # Extract metadata from the response
        create_datetime = response.data.create_datetime
        size = response.data.size
        mimetype = response.data.mimetype
        name = response.data.name
        
        # Construct dictionary with metadata
        data = {
            "create_datetime": create_datetime,
            "size": size,
            "mimetype": mimetype,
            "name": name
        }

        # Check if all required data is present
        if create_datetime and size and mimetype and name:
            print(data)
        else:
            raise ValueError("Data was not fully received.")

    except grpc.RpcError as e:
        # Handle gRPC errors
        if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
            print("Invalid UUID provided.")
        elif e.code() == grpc.StatusCode.NOT_FOUND:
            print("File not found.")
        elif e.code() == grpc.StatusCode.FAILED_PRECONDITION:
            print("Failed to retrieve file content due to database or file system errors.")
        else:
            print(f"Error occurred: {e.details()}")

def grpc_read(uuid, grpc_server, chunk_size):
    """Retrieve file content using gRPC."""
    # Create gRPC stub
    stub = create_stub(grpc_server)
    
    # Create Uuid message
    uuid_message = service_file_pb2.Uuid(value=uuid)
    
    # Create ReadRequest message
    request = service_file_pb2.ReadRequest(uuid=uuid_message, size=chunk_size)

    try:
        # Make gRPC call to retrieve file content
        response = stub.read(request)
        
        # Read content from the response stream
        content = b""
        for reply in response:
            content += reply.data.data
        return content

    except grpc.RpcError as e:
        # Handle gRPC errors
        if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
            print("Invalid UUID provided.")
        elif e.code() == grpc.StatusCode.NOT_FOUND:
            print("File not found.")
        elif e.code() == grpc.StatusCode.FAILED_PRECONDITION:
            print("Failed to retrieve file content due to database or file system errors.")
        else:
            print(f"Error occurred: {e.details()}")
        
        return None
