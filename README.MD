# File Client

The File Client is a simple CLI application that retrieves and prints data from either a gRPC or a REST API backend server.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dejwwik/file-client.git
   cd file-client
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Navigate into the file_client folder:
   ```bash
   cd file_client
   ```
   Yes, two times, because inside git repo, there is folder named file_client

4. Before the first run, generate gRPC Python files:
   Make sure you are in file_client folder!!!
   ```bash
   python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. service_file.proto
   ```

## Usage

The File Client provides a command-line interface with the following usage:

```vbnet
Usage: file-client [options] stat UUID
       file-client [options] read UUID
       file-client --help

Subcommands:
  stat                  Prints the file metadata in a human-readable manner.
  read                  Outputs the file content.

Options:
  --help                Show this help message and exit.
  --backend=BACKEND     Set a backend to be used, choices are grpc and rest. Default is grpc.
  --grpc-server=NETLOC  Set a host and port of the gRPC server. Default is localhost:50051.
  --base-url=URL        Set a base URL for a REST server. Default is http://localhost/.
  --output=OUTPUT       Set the file where to store the output. Default is -, i.e. the stdout.
```

## Requirements

- Use supported Python versions (3.7-3.10).
- Third-party open-source libraries are allowed.
- Linux OS support.
- Unit tests are required.
- Only one of the protocols (REST/gRPC) is required. Implementing both is a bonus.
