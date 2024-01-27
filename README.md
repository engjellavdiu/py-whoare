# py-whoare

`py-whoare` is a Python library designed for performing WHOIS queries on multiple domains simultaneously. It provides an easy-to-use interface for fetching domain registration details, including registrar information, registration dates, and more, along with IP geolocation data.

## Features

-   WHOIS query execution for multiple domains.
-   IP address resolution for each domain.
-   Geolocation data retrieval for each IP address.
-   Asynchronous implementation for efficient handling of multiple requests.

## Installation

Install `py-whoare` using pip:

```bash
pip install py-whoare
```

## Usage

`py-whoare` can be used in different environments, supporting both native async environments (like Jupyter notebooks) and standard Python scripts. Here are two examples to illustrate its usage:

### Example 1: Using `asyncio.run` (Recommended for Python 3.7+)

This is the simplest way to run asynchronous code. It's suitable for scripts and environments that don't have a running event loop.

```python
import asyncio
from py-whoare import WhoAre

async def main():
    whoare_instance = WhoAre()
    results = await whoare_instance.handle_multiple_queries(["example.com", "example.org"])
    for result in results:
        # Process and print results as needed

# Run the async function
asyncio.run(main())
```

### Example 2: Manual Event Loop Management

In environments where `asyncio.run` is not suitable (like in some interactive environments or when integrating with applications that manage their own event loop), you can manually create and manage an event loop.

```python
import asyncio
from py-whoare import WhoAre

async def main():
    whoare_instance = WhoAre()
    return await whoare_instance.handle_multiple_queries(["example.com", "example.org"])

# Creating a new event loop and running the main coroutine
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    results = loop.run_until_complete(main())
    # Process and print results as needed
finally:
    loop.close()
```

## Contributing

Contributions to `py-whoare` are welcome! Please refer to the [Contributing Guidelines](CONTRIBUTING.md) for more information.

## License

`py-whoare` is available under the MIT License. See [LICENSE](LICENSE) for more details.

## Contact

For any questions or feedback, please contact me at engjellavdiu01@gmail.com.

## Acknowledgements

Thanks to all the contributors and users of `py-whoare`. Your support and feedback are greatly appreciated!
