import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

#Function which overides the timestamps of all events in an event log.
#This is done for logs which have events without a timestamp (making them unusable as input for token-based replay)
#The timestamp does not affect anything else besides the order with which events are arranged. Hence a constantly increasing
#timestamp describes the events as occuring in the order in which they're registered.
def update_timestamp(xes_file, start_timestamp):

    tree = ET.parse(xes_file)
    root = tree.getroot()

    # Check for namespace
    namespace = root.tag.split('}')[0].strip('{') if '}' in root.tag else ''

    # Convert the start_timestamp to a datetime object
    current_timestamp = datetime.fromisoformat(start_timestamp.replace('Z', '+00:00'))

    # Find all "event" elements
    events = root.findall(".//{ns}event".format(ns=f"{{{namespace}}}" if namespace else ''))

    # Iterate over all events, replacing their original timestamp (if it exists), or adding a new one otherwise
    for event in events:
        timestamp_found = False
        for date in event.findall(".//{ns}date".format(ns=f"{{{namespace}}}" if namespace else '')):
            if date.attrib.get('key') == 'time:timestamp':
                date.attrib['value'] = current_timestamp.isoformat()
                timestamp_found = True
                break
        if not timestamp_found:
            new_date = ET.Element('date', {'key': 'time:timestamp', 'value': current_timestamp.isoformat()})
            event.append(new_date)
        # Increment the timestamp by one second
        current_timestamp += timedelta(seconds=1)

    # Write the updated tree to the original file
    tree.write(xes_file, xml_declaration=True, encoding='UTF-8')

# Input file path and new timestamp
input_file = "M16/MM16 Filtered for trace length (6-100) under 55 (0325 0325) no empty traces.xes"
new_timestamp = "2005-07-12T01:00:00.000+02:00"

# Update timestamps and overwrite the original file
update_timestamp(input_file, new_timestamp)


