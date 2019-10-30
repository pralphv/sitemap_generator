from typing import List
from xml.etree.ElementTree import Element, SubElement
from datetime import datetime


def correct_url_format(url: str):
    if url[-1] != '/':
        url = ''.join([url, '/'])
    return url


def generate_sitemap(landing_url: str, end_points_list: List[str]):
    landing_url = correct_url_format(landing_url)
    today = datetime.utcnow().strftime('%Y-%m-%d')
    urls = list(map(
        lambda x: f'{landing_url}{x}',
        end_points_list
    ))
    urls = [landing_url] + urls

    root = Element('urlset')
    root.set('xmlns', "http://www.sitemaps.org/schemas/sitemap/0.9")

    for url in urls:
        url_xml = SubElement(root, "url")
        below_url_loc = SubElement(url_xml, "loc")
        below_url_lastmod = SubElement(url_xml, "lastmod")
        below_url_loc.text = url
        below_url_lastmod.text = today

    return root
