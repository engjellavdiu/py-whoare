import asyncio
import socket
import re
import aiohttp

class WhoAre:
    def __init__(self):
        self.whois_server = 'whois.verisign-grs.com'
        self.geolocation_api_url = 'http://ip-api.com/json/{}'

    @staticmethod
    def resolve_domain_to_ip(domain):
        try:
            ip_address = socket.gethostbyname(domain)
            return ip_address
        except socket.gaierror:
            return f"Domain resolution failed for {domain}"

    @staticmethod
    async def query_whois_server(domain, whois_server):
        port = 43
        try:
            reader, writer = await asyncio.open_connection(whois_server, port)
            writer.write((domain + "\r\n").encode())
            response = await reader.read(-1)
            writer.close()
            await writer.wait_closed()
            return response.decode()
        except Exception as e:
            return f"Error querying WHOIS server: {e}"

    @staticmethod
    def parse_whois_data(whois_data):
        pattern = r"(\w+.*?):\s(.*?)\r\n"
        matches = re.findall(pattern, whois_data)
        return {key.strip(): value.strip() for key, value in matches}

    async def get_ip_geolocation(self, ip_address):
        url = self.geolocation_api_url.format(ip_address)
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    response.raise_for_status()
                    return await response.json()
            except Exception as e:
                return f"Error retrieving geolocation data: {e}"

    async def handle_single_query(self, domain):
        ip_address = self.resolve_domain_to_ip(domain)
        whois_data = await self.query_whois_server(domain, self.whois_server)
        parsed_data = self.parse_whois_data(whois_data)
        geolocation_data = await self.get_ip_geolocation(ip_address)
        return {
            "domain": domain,
            "ip_address": ip_address,
            "whois_data": parsed_data,
            "geolocation_data": geolocation_data
        }

    async def handle_multiple_queries(self, domains):
        async with aiohttp.ClientSession() as session:
            tasks = [self.handle_single_query(domain) for domain in domains]
            return await asyncio.gather(*tasks)


