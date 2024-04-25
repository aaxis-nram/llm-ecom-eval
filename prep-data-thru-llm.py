import csv
import json

# create an array to hold the rows
rows = []

# Open the CSV file
with open('data-raw/customer_support_tickets.csv', 'r') as f:
    # Open file to write out json file
    with open('data-raw/customer_support_tickets_cleaned.csv', 'w') as fw:
        # Create a CSV reader object
        fw.write("Ticket ID, Ticket Type, Ticket Subtype, Product, Ticket Description")
        reader = csv.reader(f)
        # get the header
        headers = next(reader)
        
        # count the lines
        lines = 0
        tlines = 0
        # Iterate over the rows in the CSV file
        for row in reader:
            # use the headers variable to print the CSV Row as JSON
            row_dict = dict(zip(headers, row))
            row_dict = {k: v for k, v in row_dict.items() if k in ['Ticket ID',  'Ticket Description']}
            # append row_dict to rows
            rows.append(row_dict)
            lines += 1
            tlines += 1
            if (lines>100):
                response_rows = getResponseFromLLM(rows)
                # iterate over response_rows array and write to fw
                for resp_row in response_rows:
                    # write to fw as CSV
                    for k, v in resp_row.items():
                        fw.write(f"\"{v}\",")
                    fw.write("\n")
                lines = 0
                rows = []
                fw.flush
            else:
                continue
            
            if (tlines>300):
                break

print("Done")



def getResponseFromLLM(rows):
    """
    This function takes in a list of rows and returns a list of responses from the LLM.

    Args:
        rows (list): A list of rows.

    Returns:
        list: A list of responses from the LLM.
    """    
    # Create a list to hold the responses
    responses = []
    prompt_data = "<data>\n"
    # convert each row into JSON and append to prompt_data
    for row in rows:
        prompt_data += json.dumps(row) + "\n"
    prompt_data += "\n</data>\n"
    # 
    # ticket types
    prompt_ticket_types = """
<ticket_types>
{
  "Billing Inquiry": [
    "Account Access",
    "Payment Issue",
    "Refund Request",
    "Cancellation Request",
    "Product Inquiry"
  ],
  "Product Inquiry": [
    "Product Recommendation",
    "Product Compatibility",
    "Peripheral Compatibility",
    "Product Setup"
  ],
  "Technical Issue": [
    "Account Access",
    "Software Bug",
    "Hardware Issue",
    "Network Problem",
    "Installation Support",
    "Data Loss",
    "Display Issue",
    "Battery Life",
    "Delivery Problem"
  ],
  "Unknown": [
    "Unknown"
  ]
}
</ticket_types> """
    
    # product types
    prompt_product_types = """<product_types>
    [   "TV",
      "Software", 
      "Gaming System", 
      "Wearable", 
      "Accessory", 
      "Smartphone", 
      "Computer",
      "Service"]
    </product_types>
    """

    prompt_text = """
In the data section is a list of tickets for customer support.
Rewrite the ticket description removing any text that appears to be from a template and is repeating in each ticket. Make the customer request sound natural.
Output the most likely ticket type and ticket subtype for each request from the ticket_types provided.
Examine the ticket description and identify which of the products in the list best fit the problem, then output the product.
Pick lines that have good enough detail to identify ticket type, subtype, and product
Replace the product_purchased in the ticket description with the product selected.
Output format CSV with columns Ticket ID, Ticket Type, Ticket Subtype, Product, Ticket Description
Enclose all columns in double-quotes.
    """
    
    request_package = { 
        "contents": {
            "role": "user",
            "parts": [
                {
                    "text": prompt_text,
                },
                {
                    "text": prompt_ticket_types,
                },
                {
                    "text": prompt_product_types,
                },
                {
                    "text": prompt_data,
                }
            ] 
        },
        "generationConfig": {
            "maxOutputTokens": 8192,
            "temperature": 1,
            "topP": 0.95,
        },
        "safetySettings": [
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            }
        ]
    }  
    
    api_endpoint = "https://us-central1-aiplatform.googleapis.com"
    project_id="lyrics-db-420116"
    location_id="us-central1"
    model_id="gemini-1.5-pro-preview-0409"

    response = requests.post(
        f"{api_endpoint}/v1/projects/{project_id}/locations/{location_id}/publishers/google/models/{model_id}:streamGenerateContent",
        json=request_package,
        headers={"Authorization": f"Bearer {get_access_token()}"},}" 