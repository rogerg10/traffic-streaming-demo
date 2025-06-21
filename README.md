# Traffic Streaming Demo: AWS Kinesis & Snowflake

This repository contains example code and configuration to accompany the blog post on real-time traffic data streaming using AWS Kinesis Data Streams, Kinesis Firehose, and Snowflake.

## Structure

- `snowflake_setup`: SQL scripts for user, schema, and role setup in Snowflake.
- `send_kinesis_events`: Python script to simulate traffic sensor event streaming.

## Usage

1. Set up Snowflake objects and roles using the scripts in `snowflake/`.
2. Use the AWS CLI or `app/send_kinesis_events.py` to send test events to your Kinesis stream.

**Note:** Replace all placeholder values (passwords, emails, ARNs, keys) with your own, and never commit secrets to the repository.
