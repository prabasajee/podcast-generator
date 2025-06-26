import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

rss_element = xml_tree.Element('rss', {
    'version': '2.0',
    'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'
})

channel_element = xml_tree.SubElement(rss_element, 'channel')

link_prefix = yaml_data.get('link', '').rstrip('/')

xml_tree.SubElement(channel_element, 'title').text = yaml_data.get('title', 'Untitled')
xml_tree.SubElement(channel_element, 'format').text = yaml_data.get('format', '')
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data.get('subtitle', '')
xml_tree.SubElement(channel_element, 'itunes:author').text = yaml_data.get('author', '')
xml_tree.SubElement(channel_element, 'description').text = yaml_data.get('description', '')
xml_tree.SubElement(channel_element, 'itunes:image', {'href': link_prefix + '/' + yaml_data.get('image', '')})
xml_tree.SubElement(channel_element, 'language').text = yaml_data.get('language', '')
xml_tree.SubElement(channel_element, 'link').text = link_prefix
xml_tree.SubElement(channel_element, 'itunes:category', {'text': yaml_data.get('category', '')})

# Add items (episodes)
for item in yaml_data.get('items', []):
    item_element = xml_tree.SubElement(channel_element, 'item')
    xml_tree.SubElement(item_element, 'title').text = item.get('title', '')
    xml_tree.SubElement(item_element, 'description').text = item.get('description', '')
    xml_tree.SubElement(item_element, 'itunes:duration').text = item.get('duration', '')
    xml_tree.SubElement(item_element, 'pubDate').text = item.get('published', '')
    enclosure = xml_tree.SubElement(item_element, 'enclosure', {
        'url': link_prefix + '/' + item.get('audio', ''),
        'type': 'audio/mpeg'
    })

output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='utf-8', xml_declaration=True)
print("RSS feed generated successfully and saved to 'podcast.xml'.")
