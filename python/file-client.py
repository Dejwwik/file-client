#!/usr/bin/env python3

import argparse

from rest_client.rest_client import rest_read, rest_stat
from proto_client.proto_client import grpc_read, grpc_stat
from utils.utils import save_file, is_valid_url

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="File Client CLI", prog="file-client")
    parser.add_argument("action", choices=["stat", "read"], help="Action to perform")
    parser.add_argument("uuid", help="UUID of the file")
    parser.add_argument("--backend", choices=["grpc", "rest"], default="grpc", help="Which backend to use")
    parser.add_argument("--grpc-server", default="localhost:50051", help="gRPC server address") 
    parser.add_argument("--base-url", default="http://localhost:8000/", help="Base URL for REST server")
    parser.add_argument("--output", default="-", help="Output file (default is stdout)")
    return parser.parse_args()

def process_read_method(result, filename, content):
    """Process the result of read operation."""
    if result:
        if (not filename):
            # If output file not specified, print to stdout
            print("Output file was not specified. Using default value \"-\" to output content into STDOUT")
            print(result)
        elif (args.output != "-"):
            # Save to file if specified
            save_file(filename=filename, content=content)
        else:
            # Print to stdout if output is '-'
            print(result)

if __name__ == "__main__":
    args = parse_arguments()
    
    if args.backend == "grpc":
        if args.action == "stat":
            # Perform gRPC stat action
            grpc_stat(args.uuid, args.base_url) # There only print

        elif args.action == "read":
            # Perform gRPC read action
            result = grpc_read(args.uuid, args.base_url, chunk_size=0) 
            process_read_method(result, args.output, result)
    
    elif args.backend == "rest":
        
        # Check if the base URL for REST API is valid
        if not is_valid_url(args.base_url):
            raise ValueError(f"Please provide valid URL address for REST API endpoint.\n{args.base_url} is not valid address.")
    
        if args.action == "stat":
            # Perform REST stat action
            rest_stat(args.uuid, args.base_url) # There only print

        elif args.action == "read":
            # Perform REST read action
            result = rest_read(args.uuid, args.base_url) 
            process_read_method(result, args.output, result)

        # No need for else because argparse will eliminate incorrect options.
