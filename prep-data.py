import csv
import json

# Open the CSV file
with open('data-raw/customer_support_tickets.csv', 'r') as f:
    # Open file to write out json file
    with open('data-raw/customer_support_tickets_desc.json', 'w') as fw:
        # Create a CSV reader object
        fw.write("[\n")
        reader = csv.reader(f)
        
        # get the header
        headers = next(reader)
        #print(headers)
        
        # count the lines
        lines = 0
        # Iterate over the rows in the CSV file
        for row in reader:
            # use the headers variable to print the CSV Row as JSON
            row_dict = dict(zip(headers, row))
            # Keep Ticket ID	Customer Name	Customer Email	Customer Age	Customer Gender	Product Purchased	Date of Purchase	Ticket Type	Ticket Subject	Ticket Description
            # and remove everything else from the row_dict
            #row_dict = {k: v for k, v in row_dict.items() if k in ['Ticket ID', 'Ticket Type', 'Ticket Subject', 'Ticket Description']}
            row_dict = {k: v for k, v in row_dict.items() if k in ['Ticket ID',  'Ticket Description']}
            # write this row to fw
            fw.write(json.dumps(row_dict) + ',\n')
            #print(row_dict)

            lines += 1
            #if lines > 10:
            #    break
        fw.write("]\n")