from typing import List
from xml.etree.ElementTree import Element, SubElement
from datetime import datetime
from xml.dom import minidom
from xml.etree.ElementTree import tostring


def correct_url_format(url: str):
    if url[-1] != '/':
        url = ''.join([url, '/'])
    return url


def create_url_end_points(
        url: str,
        end_points_list: List[str],
        languages: List[str] = None
):
    if not languages:
        urls = list(map(
            lambda x: f'{url}{x}',
            end_points_list
        ))
        urls = [url] + urls
    else:
        languages = map(lambda x: f'{x}/', languages)
        languages = [*languages, ""]
        end_points_list.append("")
        urls = []
        for language in languages:
            for end_point in end_points_list:
                new_url = f'{url}{language}{end_point}'
                urls.append(new_url)
    return urls


def generate_sitemap(
        landing_url: str,
        end_points_list: List[str],
        languages: List[str] = None
):
    landing_url = correct_url_format(landing_url)
    today = datetime.utcnow().strftime('%Y-%m-%d')
    urls = create_url_end_points(landing_url, end_points_list, languages)

    root = Element('urlset')
    root.set('xmlns', "http://www.sitemaps.org/schemas/sitemap/0.9")

    for url in urls:
        url_xml = SubElement(root, "url")
        below_url_loc = SubElement(url_xml, "loc")
        below_url_lastmod = SubElement(url_xml, "lastmod")
        below_url_loc.text = url
        below_url_lastmod.text = today

    return root


def main():
    root = generate_sitemap(
        'https://sample.com/',
        ['a', 'b', 'c'],
        ['cn', 'jp']
    )
    xml = tostring(root, encoding='unicode')
    xml = minidom.parseString(xml).toprettyxml(
        indent="   "
    )
    print(xml)


if __name__ == '__main__':
    main()
